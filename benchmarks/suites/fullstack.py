"""Full-Stack Feature Requests — 40 prompts for Organisation Mode benchmarking.

Each prompt is a multi-faceted feature request that naturally exercises
multiple departments. Includes expected department mappings and
completeness checklists for rubric scoring.

Used for Axis 2: Organisation Mode vs single-model baseline.
"""

from __future__ import annotations

SUITE_NAME = "fullstack"
SCORE_TYPE = "rubric"

QUESTIONS: list[dict] = [
    # ── Web Applications (1-10) ──────────────────────────────────────
    {
        "id": "fs-01",
        "question": (
            "Build a REST API for a task management app with JWT authentication, "
            "a React frontend with dark mode support, and a Docker Compose "
            "setup for local development. Include proper error handling and input validation."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design"],
        "checklist": [
            "REST API endpoints defined (CRUD for tasks)",
            "JWT auth flow implemented (register, login, token refresh)",
            "React frontend with component structure",
            "Dark mode toggle with CSS variables or theme provider",
            "Docker Compose with API + DB services",
            "Input validation on API endpoints",
            "Error handling with proper HTTP status codes",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-02",
        "question": (
            "Create a landing page for a B2B SaaS analytics product. It should have a "
            "hero section with animated gradient, feature cards with hover effects, "
            "pricing table with 3 tiers, and an FAQ accordion. Include SEO meta tags."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design", "Content"],
        "checklist": [
            "Hero section with headline and CTA",
            "Animated gradient background",
            "Feature cards with hover effects",
            "3-tier pricing table",
            "FAQ accordion component",
            "SEO meta tags (title, description, OG tags)",
            "Responsive design considerations",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-03",
        "question": (
            "Build a real-time chat application backend using WebSockets. Users should be "
            "able to create rooms, join rooms, send messages, and see who is currently online. "
            "Include a database schema and API documentation."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Content"],
        "checklist": [
            "WebSocket connection handling",
            "Room creation and joining logic",
            "Message broadcast within rooms",
            "Online user tracking",
            "Database schema for messages and rooms",
            "API documentation for endpoints",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-04",
        "question": (
            "Design and implement a notification system for a mobile app. "
            "Cover push notifications, in-app notifications, email digests, "
            "and user preference settings. Include the database schema and API endpoints."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design", "Product"],
        "checklist": [
            "Push notification service integration",
            "In-app notification UI component",
            "Email digest template",
            "User notification preferences API",
            "Database schema for notifications",
            "Notification grouping/batching strategy",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-05",
        "question": (
            "Build a file upload service that supports drag-and-drop, progress bars, "
            "file type validation, image thumbnail generation, and S3 storage. "
            "Include both the frontend component and backend API."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design"],
        "checklist": [
            "Drag-and-drop upload area",
            "Upload progress bar",
            "File type and size validation",
            "Image thumbnail generation",
            "S3 storage integration",
            "Backend upload API with multipart handling",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-06",
        "question": (
            "Create a dashboard for monitoring application health. Include server uptime "
            "charts, error rate graphs, response time percentiles, and alerting thresholds. "
            "Design the data model and API layer."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design", "Data Science"],
        "checklist": [
            "Uptime chart component",
            "Error rate graph",
            "Response time percentile display",
            "Alert threshold configuration",
            "Data model for metrics storage",
            "API endpoints for metric retrieval",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-07",
        "question": (
            "Build an e-commerce product page with image carousel, size/color selectors, "
            "reviews section, 'add to cart' functionality, and related products. "
            "Ensure accessibility compliance (WCAG 2.2 AA)."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design"],
        "checklist": [
            "Image carousel with thumbnails",
            "Size and color variant selectors",
            "Reviews section with ratings",
            "Add-to-cart button with quantity",
            "Related products grid",
            "WCAG 2.2 AA compliance",
            "Responsive layout",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-08",
        "question": (
            "Implement a search feature with autocomplete, faceted filtering (category, "
            "price range, rating), pagination, and search result highlighting. "
            "Include the backend search logic and frontend components."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design"],
        "checklist": [
            "Autocomplete dropdown",
            "Faceted filter UI (category, price, rating)",
            "Pagination controls",
            "Search result highlighting",
            "Backend search query handling",
            "Debounced search input",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-09",
        "question": (
            "Create a multi-step onboarding wizard for a SaaS app. Steps: "
            "account creation, team setup, integration selection, workspace configuration. "
            "Include progress indicator, validation, and skip/back navigation."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design", "Product"],
        "checklist": [
            "Multi-step form with state management",
            "Progress indicator",
            "Per-step validation",
            "Skip and back navigation",
            "Account creation form",
            "Team setup UI",
            "Integration selection interface",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-10",
        "question": (
            "Build a blog platform backend with Markdown support, categories, tags, "
            "draft/publish workflow, and RSS feed generation. Include the API, "
            "database schema, and deployment configuration."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Content"],
        "checklist": [
            "Blog post CRUD API",
            "Markdown rendering",
            "Category and tag system",
            "Draft/publish workflow",
            "RSS feed generation",
            "Database schema",
            "Deployment configuration",
        ],
        "complexity": "medium",
    },

    # ── Security & QA focused (11-18) ────────────────────────────────
    {
        "id": "fs-11",
        "question": (
            "Conduct a security audit of a typical Express.js REST API that handles "
            "user registration, login, and profile management. Identify the top 5 "
            "vulnerabilities (OWASP Top 10), provide specific code fixes, and write "
            "a report with severity ratings."
        ),
        "expected": "rubric",
        "expected_departments": ["QA", "Engineering"],
        "checklist": [
            "Input validation vulnerabilities identified",
            "Authentication/authorization issues found",
            "SQL injection or NoSQL injection risks",
            "XSS prevention measures",
            "Rate limiting recommendations",
            "Severity ratings for each finding",
            "Specific code fix provided for each vulnerability",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-12",
        "question": (
            "Write a comprehensive test suite for an authentication API. Cover unit tests "
            "for password hashing and token generation, integration tests for the login/register "
            "flow, and edge cases like expired tokens, rate limiting, and concurrent sessions."
        ),
        "expected": "rubric",
        "expected_departments": ["QA", "Engineering"],
        "checklist": [
            "Unit tests for password hashing",
            "Unit tests for JWT generation/verification",
            "Integration tests for login flow",
            "Integration tests for registration flow",
            "Edge case: expired token handling",
            "Edge case: rate limiting test",
            "Edge case: concurrent session test",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-13",
        "question": (
            "Set up a CI/CD pipeline for a Node.js monorepo with 3 packages. Include "
            "linting, unit tests, integration tests, Docker image building, and "
            "deployment to staging/production with manual approval gates."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering"],
        "checklist": [
            "GitHub Actions or CI config file",
            "Linting step",
            "Unit test step",
            "Integration test step",
            "Docker build step",
            "Staging deployment",
            "Production deployment with approval gate",
            "Monorepo-aware caching",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-14",
        "question": (
            "Create a Terraform configuration for deploying a web application to AWS. "
            "Include: VPC, ECS Fargate cluster, ALB, RDS PostgreSQL, S3 bucket, "
            "and IAM roles with least-privilege policies."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering"],
        "checklist": [
            "VPC with subnets",
            "ECS Fargate task/service definition",
            "ALB with target groups",
            "RDS PostgreSQL instance",
            "S3 bucket with policy",
            "IAM roles with least-privilege",
            "Security groups",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-15",
        "question": (
            "Design a database migration strategy for splitting a monolithic PostgreSQL "
            "database into two separate databases: one for users/auth and one for "
            "product/orders. Include migration scripts, data sync strategy, and rollback plan."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "QA"],
        "checklist": [
            "Migration scripts for schema split",
            "Data sync/copy strategy",
            "API changes to route to correct DB",
            "Zero-downtime migration approach",
            "Rollback plan",
            "Data integrity verification queries",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-16",
        "question": (
            "Review this API design for rate limiting issues and implement a proper "
            "rate limiting solution using Redis. Include sliding window and token bucket "
            "algorithms, per-user and per-IP limits, and proper 429 response headers."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "QA"],
        "checklist": [
            "Sliding window algorithm implementation",
            "Token bucket algorithm implementation",
            "Per-user rate limits",
            "Per-IP rate limits",
            "429 response with Retry-After header",
            "Redis integration",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-17",
        "question": (
            "Implement GDPR compliance features for a user data platform. Include: "
            "data export (right to portability), data deletion (right to erasure), "
            "consent management, audit logging, and a privacy policy page."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "QA", "Content"],
        "checklist": [
            "Data export endpoint (JSON/CSV)",
            "Data deletion endpoint with cascade",
            "Consent management API",
            "Audit log implementation",
            "Privacy policy content",
            "Cookie consent banner",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-18",
        "question": (
            "Perform a load testing analysis for an API that needs to handle 10,000 "
            "concurrent users. Design the test plan, identify bottlenecks, and "
            "recommend infrastructure scaling strategies."
        ),
        "expected": "rubric",
        "expected_departments": ["QA", "Engineering"],
        "checklist": [
            "Load test plan with scenarios",
            "Tool selection (k6, Locust, etc.)",
            "Bottleneck identification methodology",
            "Database optimization recommendations",
            "Caching strategy",
            "Horizontal scaling approach",
            "Auto-scaling configuration",
        ],
        "complexity": "medium",
    },

    # ── Product & Data focused (19-28) ───────────────────────────────
    {
        "id": "fs-19",
        "question": (
            "Analyze the user funnel for a SaaS product: signup → onboarding → "
            "first value action → conversion to paid. Identify the biggest drop-off, "
            "propose 3 experiments to improve it, and write the PRD for the best one."
        ),
        "expected": "rubric",
        "expected_departments": ["Product", "Data Science"],
        "checklist": [
            "Funnel stages clearly defined",
            "Drop-off rates per stage",
            "Root cause analysis for biggest drop-off",
            "3 experiment proposals with hypotheses",
            "PRD for winning experiment",
            "Success metrics defined",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-20",
        "question": (
            "Design an A/B testing framework for a web application. Include: "
            "experiment configuration, random assignment, feature flagging, "
            "statistical analysis (sample size, p-values, confidence intervals), "
            "and a dashboard for results."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Data Science", "Product"],
        "checklist": [
            "Experiment configuration schema",
            "Random assignment logic",
            "Feature flag integration",
            "Statistical analysis module",
            "Sample size calculator",
            "Results dashboard design",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-21",
        "question": (
            "Build a recommendation engine for an e-commerce platform. "
            "Implement collaborative filtering and content-based filtering, "
            "create the data pipeline, and design the API for serving recommendations."
        ),
        "expected": "rubric",
        "expected_departments": ["Data Science", "Engineering"],
        "checklist": [
            "Collaborative filtering algorithm",
            "Content-based filtering algorithm",
            "Data pipeline for training data",
            "Model serving API",
            "Cold-start handling",
            "Evaluation metrics (precision, recall, NDCG)",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-22",
        "question": (
            "Create a customer segmentation analysis using RFM (Recency, Frequency, "
            "Monetary) analysis. Include SQL queries for data extraction, Python code "
            "for clustering, visualizations, and actionable recommendations per segment."
        ),
        "expected": "rubric",
        "expected_departments": ["Data Science", "Product"],
        "checklist": [
            "SQL queries for RFM metrics",
            "Clustering implementation (K-means or similar)",
            "Segment visualizations",
            "Segment profiles",
            "Actionable recommendations per segment",
            "Data quality considerations",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-23",
        "question": (
            "Write a product requirements document (PRD) for adding a team collaboration "
            "feature to a project management tool. Include user stories, wireframes "
            "description, API requirements, and a phased rollout plan."
        ),
        "expected": "rubric",
        "expected_departments": ["Product", "Design"],
        "checklist": [
            "Problem statement",
            "User stories with acceptance criteria",
            "Wireframe or UI descriptions",
            "API requirements",
            "Non-functional requirements",
            "Phased rollout plan",
            "Success metrics",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-24",
        "question": (
            "Design a pricing page for a SaaS product with 3 tiers (Starter, Pro, Enterprise). "
            "Include feature comparison, pricing psychology (anchoring, decoy), "
            "FAQ section, and a conversion-optimized CTA strategy."
        ),
        "expected": "rubric",
        "expected_departments": ["Design", "Product", "Content"],
        "checklist": [
            "3-tier pricing table",
            "Feature comparison matrix",
            "Pricing psychology applied (anchoring/decoy)",
            "FAQ section",
            "CTA strategy per tier",
            "Annual vs monthly toggle",
            "Mobile responsive design",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-25",
        "question": (
            "Create a data dashboard for a marketing team showing: campaign performance, "
            "conversion rates by channel, customer acquisition cost, and lifetime value. "
            "Include SQL queries and chart specifications."
        ),
        "expected": "rubric",
        "expected_departments": ["Data Science", "Design"],
        "checklist": [
            "Campaign performance metrics",
            "Conversion rate by channel chart",
            "CAC calculation logic",
            "LTV calculation logic",
            "SQL queries for data extraction",
            "Dashboard layout design",
            "Date range filtering",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-26",
        "question": (
            "Develop a competitive analysis framework for a fintech startup entering "
            "the payment processing space. Include market sizing (TAM/SAM/SOM), "
            "competitor feature matrix, and positioning strategy."
        ),
        "expected": "rubric",
        "expected_departments": ["Research", "Product"],
        "checklist": [
            "TAM/SAM/SOM calculations",
            "Competitor identification (5+ competitors)",
            "Feature comparison matrix",
            "Pricing comparison",
            "Positioning strategy",
            "SWOT analysis",
        ],
        "complexity": "medium",
    },
    {
        "id": "fs-27",
        "question": (
            "Build an ML pipeline for detecting fraudulent transactions. Include "
            "feature engineering, model selection (compare at least 2 models), "
            "evaluation metrics, and a FastAPI serving endpoint."
        ),
        "expected": "rubric",
        "expected_departments": ["Data Science", "Engineering"],
        "checklist": [
            "Feature engineering pipeline",
            "At least 2 model comparisons",
            "Evaluation metrics (precision, recall, F1, AUC)",
            "Class imbalance handling",
            "FastAPI serving endpoint",
            "Model monitoring considerations",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-28",
        "question": (
            "Write a go-to-market strategy for launching a developer tool. Cover: "
            "target personas, distribution channels, content strategy (blog, docs, "
            "tutorials), community building, and first 90-day plan."
        ),
        "expected": "rubric",
        "expected_departments": ["Product", "Content", "Research"],
        "checklist": [
            "Target developer personas",
            "Distribution channel strategy",
            "Content calendar (blog, tutorials)",
            "Documentation plan",
            "Community building strategy",
            "90-day launch timeline",
            "Success metrics",
        ],
        "complexity": "medium",
    },

    # ── Cross-functional complex (29-40) ─────────────────────────────
    {
        "id": "fs-29",
        "question": (
            "Redesign a legacy monolith into a microservices architecture. "
            "Identify service boundaries, design the API gateway, create the "
            "event-driven communication layer, and plan the migration strategy."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "QA"],
        "checklist": [
            "Service boundary identification",
            "API gateway design",
            "Event-driven communication (message broker)",
            "Service discovery mechanism",
            "Migration strategy (strangler fig or big bang)",
            "Testing strategy for microservices",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-30",
        "question": (
            "Create an internal developer portal with API catalog, documentation hub, "
            "service health dashboard, and developer onboarding guide. Include both "
            "the technical architecture and content."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Content", "Design"],
        "checklist": [
            "API catalog with search",
            "Documentation hub structure",
            "Service health dashboard",
            "Developer onboarding guide",
            "Authentication/authorization for portal",
            "Content management approach",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-31",
        "question": (
            "Build a webhook delivery system that handles: webhook registration, "
            "payload signing, retry with exponential backoff, delivery logging, "
            "and a developer dashboard for monitoring webhook health."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design"],
        "checklist": [
            "Webhook registration API",
            "Payload signing (HMAC)",
            "Retry with exponential backoff",
            "Delivery logging and status tracking",
            "Developer dashboard UI",
            "Dead letter queue for failed deliveries",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-32",
        "question": (
            "Design a multi-tenant SaaS platform architecture. Cover: tenant isolation "
            "strategies, database per tenant vs shared schema, per-tenant billing, "
            "custom domain support, and tenant admin panel."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Product"],
        "checklist": [
            "Tenant isolation strategy",
            "Database architecture decision",
            "Per-tenant billing integration",
            "Custom domain support",
            "Tenant admin panel features",
            "Scalability considerations",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-33",
        "question": (
            "Create a technical blog post about building a real-time collaborative "
            "text editor using CRDTs. Include architecture diagrams, code examples, "
            "performance benchmarks, and SEO optimization."
        ),
        "expected": "rubric",
        "expected_departments": ["Content", "Engineering", "Design"],
        "checklist": [
            "CRDT explanation with examples",
            "Architecture diagram",
            "Working code examples",
            "Performance comparison (OT vs CRDT)",
            "SEO meta tags and structure",
            "Technical accuracy",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-34",
        "question": (
            "Implement an OAuth 2.0 / OIDC provider from scratch. Support authorization "
            "code flow, PKCE, refresh tokens, and scope management. Include security "
            "hardening and compliance documentation."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "QA", "Content"],
        "checklist": [
            "Authorization code flow",
            "PKCE implementation",
            "Refresh token rotation",
            "Scope management",
            "Token endpoint security",
            "Compliance documentation",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-35",
        "question": (
            "Build a feature flag management system. Support: boolean and percentage "
            "rollout flags, user targeting rules, environment separation, audit log, "
            "and a management UI."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Design", "Product"],
        "checklist": [
            "Boolean flag support",
            "Percentage rollout mechanism",
            "User targeting rules",
            "Environment separation",
            "Audit log for flag changes",
            "Management UI",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-36",
        "question": (
            "Design a data lake architecture for a company processing 10TB of daily "
            "event data. Cover ingestion, storage layers (raw/curated/analytics), "
            "catalog, governance, and query performance."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Data Science"],
        "checklist": [
            "Data ingestion pipeline",
            "Storage layer architecture (bronze/silver/gold)",
            "Data catalog implementation",
            "Data governance policies",
            "Query optimization",
            "Cost management strategy",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-37",
        "question": (
            "Create a developer SDK (Python) for a REST API. Include typed client, "
            "pagination helpers, rate limit handling, retry logic, error types, "
            "comprehensive tests, and documentation with usage examples."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Content", "QA"],
        "checklist": [
            "Typed client class",
            "Pagination handling",
            "Rate limit handling",
            "Retry logic with backoff",
            "Custom error types",
            "Unit tests",
            "Documentation with examples",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-38",
        "question": (
            "Build an observability stack for a Kubernetes cluster. Include: "
            "metrics collection (Prometheus), log aggregation (Loki/EFK), "
            "distributed tracing (Jaeger), alerting rules, and Grafana dashboards."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering"],
        "checklist": [
            "Prometheus metrics configuration",
            "Log aggregation setup",
            "Distributed tracing integration",
            "Alerting rules with escalation",
            "Grafana dashboard definitions",
            "Kubernetes manifests",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-39",
        "question": (
            "Design and implement a content moderation pipeline for user-generated content. "
            "Include: text classification (toxicity, spam), image moderation, "
            "human review queue, appeal workflow, and moderation dashboard."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Data Science", "Design", "Product"],
        "checklist": [
            "Text toxicity classification",
            "Spam detection",
            "Image moderation approach",
            "Human review queue",
            "Appeal workflow",
            "Moderation dashboard",
        ],
        "complexity": "complex",
    },
    {
        "id": "fs-40",
        "question": (
            "Create a complete API monetization system. Include: API key management, "
            "usage tracking and metering, tiered rate limits, billing integration "
            "(Stripe), usage dashboard for customers, and admin analytics."
        ),
        "expected": "rubric",
        "expected_departments": ["Engineering", "Product", "Design"],
        "checklist": [
            "API key generation and management",
            "Usage tracking/metering",
            "Tiered rate limits",
            "Stripe billing integration",
            "Customer usage dashboard",
            "Admin analytics view",
        ],
        "complexity": "complex",
    },
]
