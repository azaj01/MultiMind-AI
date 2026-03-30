"""Council QA — 40 questions for Agent Council benchmarking.

Questions designed to benefit from multi-perspective analysis:
ambiguous problems, trade-off decisions, controversial technical
topics, and questions where different expertise brings value.

Each includes expected key points that a strong answer should cover.

Used for Axis 3: Council Mode vs single-model baseline.
"""

from __future__ import annotations

SUITE_NAME = "council_qa"
SCORE_TYPE = "rubric"

QUESTIONS: list[dict] = [
    # ── Technical Trade-offs (1-10) ──────────────────────────────────
    {
        "id": "cqa-01",
        "question": (
            "Should a startup with 5 engineers build with a monolith or microservices "
            "architecture? The product is a B2B SaaS platform for inventory management "
            "expecting 100 customers in year one."
        ),
        "expected": "rubric",
        "key_points": [
            "Monolith recommended for small team and early stage",
            "Microservices add operational complexity",
            "Consider modular monolith as middle ground",
            "Team size matters more than technology choice",
            "Acknowledge when microservices become necessary",
        ],
    },
    {
        "id": "cqa-02",
        "question": (
            "Compare REST, GraphQL, and gRPC for a new API that will serve both a "
            "web frontend, a mobile app, and internal microservices. Which would you "
            "recommend and why?"
        ),
        "expected": "rubric",
        "key_points": [
            "REST for simplicity and broad tooling",
            "GraphQL for flexible frontend queries",
            "gRPC for internal service-to-service",
            "Hybrid approach is often best",
            "Consider team expertise and client needs",
            "Performance characteristics of each",
        ],
    },
    {
        "id": "cqa-03",
        "question": (
            "What are the trade-offs between using a relational database (PostgreSQL) "
            "versus a document database (MongoDB) for a social media platform with "
            "complex relationships between users, posts, comments, and likes?"
        ),
        "expected": "rubric",
        "key_points": [
            "Relational: strong for complex joins and relationships",
            "Document: flexible schema for varied post types",
            "Consider graph database for social connections",
            "Transaction support differences",
            "Scaling approaches differ (vertical vs horizontal)",
            "Query pattern analysis matters",
        ],
    },
    {
        "id": "cqa-04",
        "question": (
            "A team is debating whether to adopt TypeScript for an existing large "
            "JavaScript project (200K+ lines). What are the arguments for and against, "
            "and what migration strategy would you recommend?"
        ),
        "expected": "rubric",
        "key_points": [
            "Type safety catches bugs at compile time",
            "Migration cost for large codebase",
            "Gradual adoption strategy (allowJs, strict incremental)",
            "Developer productivity vs learning curve",
            "Tooling improvements (IDE support, refactoring)",
            "Third-party type definitions may be incomplete",
        ],
    },
    {
        "id": "cqa-05",
        "question": (
            "Explain the CAP theorem and how it applies to choosing between Cassandra, "
            "DynamoDB, and CockroachDB for a globally distributed e-commerce platform."
        ),
        "expected": "rubric",
        "key_points": [
            "CAP theorem correctly explained",
            "Cassandra: AP system, eventual consistency",
            "DynamoDB: configurable consistency",
            "CockroachDB: CP system, serializable transactions",
            "Trade-offs for e-commerce (consistency vs availability)",
            "Practical implications for shopping cart and checkout",
        ],
    },
    {
        "id": "cqa-06",
        "question": (
            "When should you use server-side rendering (SSR) vs static site generation "
            "(SSG) vs client-side rendering (CSR) for a web application? Give concrete "
            "examples of applications best suited for each approach."
        ),
        "expected": "rubric",
        "key_points": [
            "SSR: dynamic content, SEO-critical, personalized pages",
            "SSG: blog, marketing pages, documentation",
            "CSR: dashboards, admin panels, real-time apps",
            "Hybrid approaches (ISR, streaming SSR)",
            "Performance implications (TTFB, LCP)",
            "Infrastructure and hosting differences",
        ],
    },
    {
        "id": "cqa-07",
        "question": (
            "Compare Kubernetes, Docker Swarm, and serverless (AWS Lambda/Cloud Run) "
            "for deploying a set of 15 microservices with varying traffic patterns. "
            "Consider cost, complexity, and team capabilities."
        ),
        "expected": "rubric",
        "key_points": [
            "Kubernetes: powerful but operationally complex",
            "Docker Swarm: simpler but limited ecosystem",
            "Serverless: cost-efficient for variable traffic",
            "Consider managed Kubernetes (EKS/GKE)",
            "Cold start issues with serverless",
            "Team learning curve and hiring implications",
        ],
    },
    {
        "id": "cqa-08",
        "question": (
            "What is the best strategy for handling database migrations in a "
            "continuous deployment environment with zero downtime requirements? "
            "Consider schema changes, data migrations, and rollback scenarios."
        ),
        "expected": "rubric",
        "key_points": [
            "Expand-and-contract pattern",
            "Forward-only migrations preferred",
            "Separate deployment from migration",
            "Shadow columns for schema changes",
            "Feature flags for code/schema coordination",
            "Testing migrations in staging",
            "Monitoring after migration",
        ],
    },
    {
        "id": "cqa-09",
        "question": (
            "How should a company handle secrets management across development, "
            "staging, and production environments? Compare approaches: env vars, "
            "Vault, AWS Secrets Manager, and SOPS."
        ),
        "expected": "rubric",
        "key_points": [
            "Environment variables: simple but insecure for production",
            "Vault: enterprise-grade, complex to operate",
            "AWS Secrets Manager: cloud-native, integrated",
            "SOPS: encrypted files in git, good for GitOps",
            "Rotation and auditing requirements",
            "Developer experience considerations",
        ],
    },
    {
        "id": "cqa-10",
        "question": (
            "Debate the use of ORM (like SQLAlchemy or Prisma) vs raw SQL for a "
            "high-performance data processing application that runs complex analytics "
            "queries on 100M+ row tables."
        ),
        "expected": "rubric",
        "key_points": [
            "ORMs add abstraction overhead",
            "Raw SQL gives full control over query optimization",
            "Hybrid approach: ORM for CRUD, raw SQL for analytics",
            "Query builder as middle ground",
            "N+1 query problem with ORMs",
            "Maintainability vs performance trade-off",
        ],
    },

    # ── Ambiguous Design Decisions (11-20) ───────────────────────────
    {
        "id": "cqa-11",
        "question": (
            "A team needs to choose a state management solution for a large React "
            "application (50+ components, complex forms, real-time data). Compare "
            "Redux Toolkit, Zustand, Jotai, and React Context. Which combination "
            "would you recommend and why?"
        ),
        "expected": "rubric",
        "key_points": [
            "Redux Toolkit: predictable, good DevTools, boilerplate",
            "Zustand: lightweight, minimal API",
            "Jotai: atomic, bottom-up approach",
            "React Context: not ideal for frequent updates",
            "Mix: server state (TanStack Query) + client state",
            "Avoid over-engineering for the problem size",
        ],
    },
    {
        "id": "cqa-12",
        "question": (
            "How should error handling be designed in a distributed microservices "
            "system? Cover: error propagation, timeouts, circuit breakers, retry "
            "strategies, dead letter queues, and user-facing error messages."
        ),
        "expected": "rubric",
        "key_points": [
            "Circuit breaker pattern (Resilience4j, Polly)",
            "Retry with exponential backoff and jitter",
            "Timeout cascading prevention",
            "Dead letter queues for async failures",
            "Structured error codes (not just HTTP status)",
            "Error correlation with trace IDs",
            "Graceful degradation strategies",
        ],
    },
    {
        "id": "cqa-13",
        "question": (
            "Is it better to use a managed database service (RDS, Cloud SQL) or "
            "self-host PostgreSQL on Kubernetes for a growing startup? Current "
            "DB size is 50GB, growing 5GB/month, with 1000 QPS peak."
        ),
        "expected": "rubric",
        "key_points": [
            "Managed: less operational burden, automatic backups",
            "Self-hosted: more control, potential cost savings at scale",
            "50GB is well within managed service comfort zone",
            "1000 QPS is moderate — managed handles easily",
            "Startup should focus on product, not DB ops",
            "When self-hosting becomes worthwhile (scale/cost)",
        ],
    },
    {
        "id": "cqa-14",
        "question": (
            "What are the security trade-offs between JWT tokens and session-based "
            "authentication? When should you use each? Consider: token theft, "
            "rotation, revocation, scalability, and mobile clients."
        ),
        "expected": "rubric",
        "key_points": [
            "JWT: stateless, scalable, hard to revoke",
            "Sessions: stateful, easy to invalidate, server affinity",
            "Token theft: JWT more dangerous (no server-side control)",
            "Short-lived JWTs + refresh tokens as mitigation",
            "Mobile clients prefer token-based",
            "Consider Redis-backed sessions for hybrid approach",
        ],
    },
    {
        "id": "cqa-15",
        "question": (
            "A company is considering moving from a weekly release cycle to "
            "continuous deployment. What are the prerequisites, risks, and "
            "benefits? How should they approach the transition?"
        ),
        "expected": "rubric",
        "key_points": [
            "Prerequisites: automated tests, CI/CD pipeline, monitoring",
            "Feature flags for incomplete features",
            "Canary/blue-green deployments",
            "Rollback strategies",
            "Cultural change management",
            "Incremental transition (not big bang)",
        ],
    },
    {
        "id": "cqa-16",
        "question": (
            "How should you design a caching strategy for an e-commerce site? "
            "Cover: what to cache (product pages, sessions, API responses), "
            "cache invalidation, cache warming, and CDN vs application-level caching."
        ),
        "expected": "rubric",
        "key_points": [
            "CDN for static assets and product images",
            "Application cache (Redis) for sessions and cart",
            "Cache-aside pattern for API responses",
            "Cache invalidation strategies (TTL, event-based)",
            "Cache stampede prevention",
            "Stale-while-revalidate pattern",
        ],
    },
    {
        "id": "cqa-17",
        "question": (
            "Should API versioning use URL paths (/v1/users), query parameters "
            "(?version=1), or custom headers (Accept: application/vnd.api+json;version=1)? "
            "Discuss trade-offs for each with a public API used by 500+ integrations."
        ),
        "expected": "rubric",
        "key_points": [
            "URL versioning: most visible, easiest to understand",
            "Header versioning: cleaner URLs, harder to discover",
            "Query parameter: simple but pollutes URL",
            "For public API: URL versioning recommended",
            "Backward compatibility is more important than technique",
            "Deprecation and sunset headers",
        ],
    },
    {
        "id": "cqa-18",
        "question": (
            "Compare event sourcing vs traditional CRUD for an insurance claims "
            "processing system that requires complete audit trails and the ability "
            "to reconstruct system state at any point in time."
        ),
        "expected": "rubric",
        "key_points": [
            "Event sourcing: natural fit for audit trails",
            "CRUD: simpler to query current state",
            "Event sourcing complexity (projections, snapshots)",
            "Insurance domain benefits from event history",
            "CQRS as complementary pattern",
            "Testing and debugging challenges with events",
        ],
    },
    {
        "id": "cqa-19",
        "question": (
            "A mobile app team is deciding between React Native, Flutter, and native "
            "development (Swift/Kotlin) for a banking app that needs biometric auth, "
            "push notifications, and offline mode. What should they choose?"
        ),
        "expected": "rubric",
        "key_points": [
            "Native: best performance, full API access, higher cost",
            "Flutter: good performance, single codebase, growing ecosystem",
            "React Native: large ecosystem, JavaScript talent available",
            "Banking apps need high security (native APIs)",
            "Biometric auth: native provides best support",
            "Offline mode: all three can handle, native easiest",
            "Regulatory and compliance considerations",
        ],
    },
    {
        "id": "cqa-20",
        "question": (
            "What is the ideal logging strategy for a production web application? "
            "Cover: structured vs unstructured logging, log levels, PII handling, "
            "log aggregation, alerting, and cost management at scale."
        ),
        "expected": "rubric",
        "key_points": [
            "Structured logging (JSON) for machine parsing",
            "Appropriate log levels (ERROR, WARN, INFO, DEBUG)",
            "PII scrubbing before logging",
            "Correlation IDs across services",
            "Centralized aggregation (ELK, Loki, Datadog)",
            "Log retention policies for cost control",
            "Alert on patterns, not individual log lines",
        ],
    },

    # ── Multi-perspective Problems (21-30) ───────────────────────────
    {
        "id": "cqa-21",
        "question": (
            "A SaaS company's largest customer is requesting a custom feature that "
            "doesn't align with the product roadmap. The customer accounts for 30% "
            "of revenue. How should the company handle this?"
        ),
        "expected": "rubric",
        "key_points": [
            "Revenue concentration risk",
            "Custom development vs product-led growth",
            "Negotiate to find alignment with roadmap",
            "Consider feature flags or plugin architecture",
            "Long-term product strategy implications",
            "Alternative: professional services engagement",
        ],
    },
    {
        "id": "cqa-22",
        "question": (
            "How should AI-generated code be treated in code reviews? Should it be "
            "held to the same standards? What additional checks are needed? "
            "How does this affect team dynamics and code ownership?"
        ),
        "expected": "rubric",
        "key_points": [
            "Same quality standards regardless of source",
            "Additional security review for AI-generated code",
            "Risk of hallucinated dependencies",
            "Code ownership and accountability",
            "Team skill development concerns",
            "Advantages: speed, boilerplate reduction",
        ],
    },
    {
        "id": "cqa-23",
        "question": (
            "Is it better to optimize developer experience (DX) or system performance "
            "when they conflict? For example: using an ORM that's slower but easier "
            "to use, or choosing a simpler architecture that's less scalable."
        ),
        "expected": "rubric",
        "key_points": [
            "Depends on current scale and constraints",
            "Premature optimization is the root of all evil",
            "Good DX leads to faster feature development",
            "Performance matters when it impacts users",
            "Profile before optimizing",
            "Escape hatches: use ORM + raw SQL for hot paths",
        ],
    },
    {
        "id": "cqa-24",
        "question": (
            "A startup has the choice between building on open-source tools (self-hosted) "
            "or using commercial SaaS solutions (managed). They need: analytics, "
            "error tracking, CI/CD, and monitoring. Budget is limited. Advise them."
        ),
        "expected": "rubric",
        "key_points": [
            "Total cost of ownership (infra + time + maintenance)",
            "SaaS: faster to set up, less maintenance",
            "Open-source: lower cost, more control, more work",
            "Hybrid approach: commercial for critical, OSS for nice-to-have",
            "Consider free tiers of SaaS products",
            "Team bandwidth is the real constraint",
        ],
    },
    {
        "id": "cqa-25",
        "question": (
            "What are the ethical considerations of implementing a recommendation "
            "algorithm that maximizes user engagement? The algorithm is effective "
            "but may create filter bubbles and addiction patterns."
        ),
        "expected": "rubric",
        "key_points": [
            "Engagement optimization vs user well-being",
            "Filter bubble and echo chamber risks",
            "Addictive design patterns (infinite scroll, notifications)",
            "Regulatory landscape (DSA, GDPR)",
            "Diversity injection in recommendations",
            "Transparency and user control",
            "Business incentives vs ethical responsibility",
        ],
    },
    {
        "id": "cqa-26",
        "question": (
            "How should a company approach technical debt? When should it be "
            "prioritized over new features? How do you measure and communicate "
            "technical debt to non-technical stakeholders?"
        ),
        "expected": "rubric",
        "key_points": [
            "Not all tech debt is bad (strategic vs accidental)",
            "Measure: velocity decrease, bug rate, incident frequency",
            "Communicate in business terms (delivery speed, risk)",
            "Allocate % of sprint capacity (e.g., 20%)",
            "Pay interest metaphor for stakeholders",
            "Prioritize by impact on user experience and delivery",
        ],
    },
    {
        "id": "cqa-27",
        "question": (
            "Compare monorepo (Turborepo/Nx) vs multi-repo for a team of 30 engineers "
            "working on a platform with a shared component library, 3 web apps, "
            "2 mobile apps, and 5 backend services."
        ),
        "expected": "rubric",
        "key_points": [
            "Monorepo: atomic changes, shared tooling, code reuse",
            "Multi-repo: team autonomy, independent deployment",
            "Build performance at scale (caching, affected detection)",
            "Code ownership and review boundaries",
            "CI/CD complexity differences",
            "Google/Meta use monorepos; many OSS projects use multi",
        ],
    },
    {
        "id": "cqa-28",
        "question": (
            "What are the best practices for designing idempotent APIs? Why does "
            "idempotency matter for payment systems? Provide concrete implementation "
            "patterns with examples."
        ),
        "expected": "rubric",
        "key_points": [
            "Idempotency key header pattern",
            "Safe retries without duplicate side effects",
            "Critical for payments (double-charge prevention)",
            "Database-level uniqueness constraints",
            "Idempotency store (Redis or DB)",
            "GET is naturally idempotent; POST needs explicit handling",
            "Timeout and response caching for retried requests",
        ],
    },
    {
        "id": "cqa-29",
        "question": (
            "A development team is split on whether to use end-to-end encryption "
            "for all user messages in a messaging app. This would prevent the company "
            "from content moderation. What should they do?"
        ),
        "expected": "rubric",
        "key_points": [
            "Privacy vs safety trade-off",
            "E2E encryption protects user privacy",
            "Content moderation becomes difficult/impossible",
            "Regulatory requirements (CSAM, terrorism)",
            "Client-side scanning as compromise (controversial)",
            "Transparency report obligations",
            "Competitive pressure (Signal, WhatsApp)",
        ],
    },
    {
        "id": "cqa-30",
        "question": (
            "Should a startup buy or build an internal admin panel? They currently "
            "use direct database queries for customer support operations. Options: "
            "Retool, custom React admin, or Directus. Evaluate each."
        ),
        "expected": "rubric",
        "key_points": [
            "Retool: fast to build, monthly cost, vendor lock-in",
            "Custom React: full control, expensive to build/maintain",
            "Directus: open-source, self-hosted, database-centric",
            "Current state (direct DB queries) is a security risk",
            "Consider team size and admin panel complexity",
            "Start with low-code, migrate when needs grow",
        ],
    },

    # ── Complex Reasoning (31-40) ────────────────────────────────────
    {
        "id": "cqa-31",
        "question": (
            "Explain how you would design a distributed rate limiter that works "
            "across multiple server instances. Compare sliding window, token bucket, "
            "and leaky bucket algorithms in this context."
        ),
        "expected": "rubric",
        "key_points": [
            "Centralized store (Redis) for distributed state",
            "Sliding window: accurate but memory-intensive",
            "Token bucket: burst-friendly, simple",
            "Leaky bucket: smooth output rate",
            "Race conditions with distributed counters",
            "Lua scripts for atomic Redis operations",
            "Local + global hybrid for performance",
        ],
    },
    {
        "id": "cqa-32",
        "question": (
            "How should a company handle data consistency in a system where orders, "
            "inventory, and payments are managed by separate microservices? "
            "Compare saga pattern, two-phase commit, and eventual consistency."
        ),
        "expected": "rubric",
        "key_points": [
            "2PC: strong consistency, performance bottleneck",
            "Saga: compensation-based, better availability",
            "Choreography vs orchestration sagas",
            "Eventual consistency: most scalable, hardest to reason about",
            "Outbox pattern for reliable event publishing",
            "Idempotency is critical for all approaches",
        ],
    },
    {
        "id": "cqa-33",
        "question": (
            "What is the best way to handle file uploads in a web application? "
            "Compare: direct upload to S3 (pre-signed URLs), server-side proxy, "
            "and multipart upload via API. Consider security, performance, and cost."
        ),
        "expected": "rubric",
        "key_points": [
            "Pre-signed URLs: best performance, reduced server load",
            "Server proxy: more control, server bandwidth cost",
            "Content type validation (don't trust client)",
            "File size limits and chunked uploads",
            "Virus scanning workflow",
            "CDN integration for serving",
        ],
    },
    {
        "id": "cqa-34",
        "question": (
            "How would you debug a production memory leak in a Node.js application "
            "that only appears under sustained high load (5000+ req/s)? Walk through "
            "your debugging methodology step by step."
        ),
        "expected": "rubric",
        "key_points": [
            "Heap snapshots and comparison",
            "Heap dump analysis with Chrome DevTools",
            "Common leak sources (closures, event listeners, timers)",
            "Load testing to reproduce",
            "Memory profiling in production (heapdump)",
            "Garbage collection analysis (--expose-gc)",
            "Monitoring heap growth over time",
        ],
    },
    {
        "id": "cqa-35",
        "question": (
            "Design a notification system that handles 10 million push notifications "
            "per day with delivery guarantees. Cover: queuing, batching, "
            "provider failover (APNS, FCM), and delivery tracking."
        ),
        "expected": "rubric",
        "key_points": [
            "Message queue for reliable delivery (Kafka, SQS)",
            "Batching for provider efficiency",
            "Provider failover and circuit breaking",
            "Device token management",
            "Delivery receipt tracking",
            "Rate limiting per device and per user",
            "Priority queues for urgent vs marketing",
        ],
    },
    {
        "id": "cqa-36",
        "question": (
            "What are the performance implications of using JSON vs Protocol Buffers "
            "vs MessagePack for API serialization? When would you choose each? "
            "Consider both latency and developer experience."
        ),
        "expected": "rubric",
        "key_points": [
            "JSON: human-readable, universal, larger payloads",
            "Protobuf: compact, fast, schema-enforced",
            "MessagePack: compact JSON alternative, schema-free",
            "Benchmarks: protobuf 5-10x faster than JSON",
            "JSON for public APIs, protobuf for internal services",
            "Schema evolution differences",
            "Debugging difficulty with binary formats",
        ],
    },
    {
        "id": "cqa-37",
        "question": (
            "How should database indexing be approached for a multi-tenant SaaS "
            "application? Cover: tenant ID in indexes, composite indexes, "
            "partial indexes, and index bloat management."
        ),
        "expected": "rubric",
        "key_points": [
            "Tenant ID as leading column in composite indexes",
            "Partial indexes for active tenants",
            "Index bloat from frequent updates",
            "Covering indexes for common queries",
            "pg_stat_user_indexes for monitoring",
            "Re-indexing strategy (REINDEX CONCURRENTLY)",
            "Index-only scans optimization",
        ],
    },
    {
        "id": "cqa-38",
        "question": (
            "Compare approaches to implementing real-time features: WebSockets, "
            "Server-Sent Events, long polling, and WebTransport. For each, describe "
            "the ideal use case and scaling characteristics."
        ),
        "expected": "rubric",
        "key_points": [
            "WebSockets: bidirectional, complex to scale",
            "SSE: server-push only, simpler, HTTP/2 friendly",
            "Long polling: simplest, highest overhead",
            "WebTransport: emerging, UDP-based, low latency",
            "Load balancer considerations (sticky sessions)",
            "Connection state management at scale",
        ],
    },
    {
        "id": "cqa-39",
        "question": (
            "How should an engineering team approach system design for a URL "
            "shortener that needs to handle 100M URLs and 10B redirects per month? "
            "Cover: hash generation, storage, caching, and analytics."
        ),
        "expected": "rubric",
        "key_points": [
            "Base62 encoding or hash-based short codes",
            "Collision handling strategy",
            "Read-heavy workload → heavy caching (Redis/Memcached)",
            "Database partitioning/sharding by short code",
            "301 vs 302 redirect implications",
            "Analytics pipeline (click tracking, geo, referrer)",
            "Expiration and cleanup strategy",
        ],
    },
    {
        "id": "cqa-40",
        "question": (
            "What are the best practices for implementing blue-green deployments "
            "with database schema changes? How do you handle the database "
            "being shared between old and new versions simultaneously?"
        ),
        "expected": "rubric",
        "key_points": [
            "Forward-compatible schema changes",
            "Expand-contract migration pattern",
            "Both versions must work with same schema",
            "Add columns nullable, backfill, then enforce",
            "Never rename columns during blue-green",
            "Database migration before code deployment",
            "Health checks and traffic shifting",
        ],
    },
]
