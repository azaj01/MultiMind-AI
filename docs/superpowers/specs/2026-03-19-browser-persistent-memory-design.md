# Browser-Based Persistent Memory for MultiMind

**Date:** 2026-03-19
**Status:** Approved
**Scope:** Chat history + settings persistence in the browser (no database, no multi-turn LLM context)

## Problem

MultiMind AI is currently fully ephemeral. Chat messages vanish on page refresh, settings reset on server restart, and there is no browser-side storage of any kind. Users lose all work when they reload the page.

## Goals

- Persist chat conversations in the browser across page refreshes
- Persist user settings (provider, models, mode) in the browser
- Provide a sidebar to browse, load, and delete saved conversations
- Zero backend changes — purely client-side persistence

## Non-Goals

- Multi-turn LLM context (sending conversation history to the model)
- Cross-device sync
- User accounts or authentication
- Server-side storage of any kind

## Storage Mechanism

**localStorage** — synchronous key-value store, ~5-10MB per origin.

**Rationale:** The data volumes (settings object ~1KB, conversations ~100-200KB each) are well within localStorage limits. The synchronous API keeps the vanilla JS codebase simple. IndexedDB is unnecessary for this scale.

## Data Model

### Key: `multimind_settings`

Single JSON object mirroring the existing `SettingsPayload`:

```json
{
  "provider_name": "",
  "provider_kind": "ollama",
  "base_url": "http://127.0.0.1:11434",
  "ollama_think": false,
  "model_map": { "plan": "", "execute": "", "critique": "" },
  "council_models": [],
  "judge_model": "",
  "org_model": ""
}
```

### Key: `multimind_conversations`

JSON array of conversation objects, sorted by `updated_at` descending:

```json
[
  {
    "id": "uuid-string",
    "title": "First 50 chars of first user message...",
    "created_at": 1710800000000,
    "updated_at": 1710800300000,
    "mode": "thinking",
    "messages": [
      { "role": "user", "content": "...", "timestamp": 1710800000000 },
      { "role": "assistant", "content": "...", "timestamp": 1710800060000 }
    ]
  }
]
```

### Key: `multimind_active_conversation`

String — the `id` of the currently active conversation, or `null` for a new chat.

### Key: `multimind_sidebar_open`

Boolean — whether the sidebar is expanded or collapsed.

## Storage Manager Module

New functions added to `app.js` (or a separate `storage.js`):

| Function | Returns | Description |
|----------|---------|-------------|
| `getConversations()` | `Conversation[]` | Parse and return all saved conversations, sorted by `updated_at` desc |
| `saveConversation(conv)` | `void` | Upsert a conversation (match by `id`). Save to localStorage. |
| `deleteConversation(id)` | `void` | Remove conversation by `id` from the array. |
| `getConversation(id)` | `Conversation \| null` | Get a single conversation by `id`. |
| `getSettings()` | `SettingsPayload` | Return saved settings, or defaults if none exist. |
| `saveSettings(settings)` | `void` | Save settings to localStorage. |
| `generateId()` | `string` | Generate a UUID using `crypto.randomUUID()`. |

All functions use `JSON.parse(localStorage.getItem(...))` / `localStorage.setItem(..., JSON.stringify(...))` wrapped in try/catch for quota exceeded errors.

## UI: Collapsible Sidebar

### Layout

A collapsible sidebar on the left side of the chat area. When open (~240px wide), the chat area shrinks. When collapsed, chat takes full width.

### Components

1. **Toggle button** — hamburger icon (`☰`) in the chat header bar. Toggles sidebar open/closed. State persisted to `multimind_sidebar_open`.

2. **"+ New Chat" button** — at the top of the sidebar. Creates a new conversation object, clears the chat log, sets it as active.

3. **Conversation list** — scrollable list below the "+ New Chat" button. Each item shows:
   - Title (auto-generated, truncated with ellipsis)
   - Message count
   - Active conversation highlighted with left border accent
   - Hover reveals a trash icon on the right side for deletion

4. **Conversation titles** — auto-generated from the first 50 characters of the user's first message. Truncated with `...` if longer.

### States

- **Default:** Sidebar starts collapsed on first visit. Subsequent visits restore last state.
- **Active conversation:** Highlighted in sidebar. Loading a conversation clears the DOM and replays messages.
- **New chat:** No conversation selected. Chat log is empty. First message creates the conversation.
- **Delete:** Clicking the trash icon removes the conversation from localStorage and the sidebar. If the deleted conversation was active, a new empty chat starts.

## Settings Persistence

### Auto-save on change

Every settings UI change (dropdown selection, toggle flip, URL edit) immediately saves to localStorage via `saveSettings()`. The existing POST to `/api/settings` remains to keep the server in sync.

### Load priority

On page load:
1. Check localStorage for `multimind_settings`
2. If found, use it and send to server via POST `/api/settings`
3. If not found, fetch from server via GET `/api/settings` (existing behavior)

### Settings panel cleanup

The "Save" button in settings becomes redundant. It can be removed or converted to a visual "Saved" indicator.

## Chat History Flow

### Saving messages

1. User sends a message → append `{role: "user", content, timestamp}` to active conversation's `messages` array. Call `saveConversation()`.
2. Assistant response completes → append `{role: "assistant", content, timestamp}` to `messages` array. Call `saveConversation()`.
3. On first user message in a new conversation → set `title` to first 50 chars. Update `updated_at`.

### Loading a conversation

1. User clicks a conversation in the sidebar.
2. Set `activeConversationId` to the selected conversation's `id`.
3. Clear the chat log DOM.
4. For each message in the conversation, render it in the chat log (replay as DOM nodes using existing message templates).
5. Scroll to bottom.

### New conversation

1. User clicks "+ New Chat".
2. Generate a new UUID. Create conversation object with empty `messages`, `title: "New Chat"`.
3. Call `saveConversation()`. Set as active. Clear chat log DOM.

## Files Changed

| File | Changes |
|------|---------|
| `multimind/static/app.js` | Add storage manager functions (~60 lines). Add `activeConversationId` to state. Add sidebar rendering and interaction logic. Modify `streamStandardChat` and `streamOrgChat` to save messages. Modify `loadSettings` to read from localStorage first. |
| `multimind/templates/index.html` | Add `<aside id="sidebar">` element before main chat area. Add sidebar toggle button in header. Add "+ New Chat" button markup. |
| `multimind/static/styles.css` | Add sidebar styles (~80 lines): width, transitions, conversation list items, active highlight, hover-to-delete reveal, collapsed/expanded states. |

**No backend changes.**

## Error Handling

- **localStorage quota exceeded:** Catch `QuotaExceededError`. Show a non-blocking toast: "Storage full. Delete some conversations." Do not crash.
- **Corrupt JSON in localStorage:** Catch parse errors. Reset the affected key to default. Log a console warning.
- **Missing conversation on load:** If `activeConversationId` references a deleted conversation, start a new chat.

## Testing

- **Manual:** Create conversations, refresh page, verify they persist. Delete conversations. Toggle sidebar. Change settings, refresh, verify persistence.
- **Edge cases:** Delete active conversation. Fill localStorage quota (create many large conversations). Clear localStorage manually (should fall back to server defaults).
- **No automated tests** — the storage layer is a thin wrapper around browser APIs. Manual verification is sufficient for this scope.
