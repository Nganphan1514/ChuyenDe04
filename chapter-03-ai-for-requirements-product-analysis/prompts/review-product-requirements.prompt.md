# P3.2 — Review product requirements: SleepAlert

> - **Role:** REVIEW GATE
> - **Skills:** `$prd-generator` (required), `$brainstorm` (conditional: resolve findings)
> - **Interaction mode:** inspect-and-report
> - **Output mode:** structured findings report
> - **Approval gate:** accept, reject, or defer each finding before editing PRD
> - **Target artifact:** `chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md`
> - **Run context:** fresh session; inspect draft PRD against project brief and context.

## Use this when

A draft PRD has been generated and needs adversarial review for scope creep, unstated assumptions, ambiguous acceptance criteria, or latency violations.

## Inputs

- Draft PRD: [product-requirements.md](../docs/product-requirements.md)
- Project brief: [project-brief.md](../../chapter-01-ai-in-software-engineering/docs/project-brief.md)
- Project context: [project-context.md](../../chapter-02-prompt-engineering/docs/project-context.md)

## Task

Critique the PRD across 4 dimensions:
1. **Scope Boundary:** Did unapproved features (e.g. cloud video streaming, auto-braking) sneak into the requirements?
2. **Observability:** Can each acceptance criterion be tested objectively with camera frames and audio decibel meters?
3. **Safety & Fail-safe:** Are camera occlusion and zero-network conditions properly handled?
4. **Latency Feasibility:** Is the $\le 500$ms local response realistically achievable without blocking the vision loop?

Output a structured findings table: `ID | Category | Severity | Finding | Recommendation`.
