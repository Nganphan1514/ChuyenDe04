# P3.1 — Create product requirements: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$prd-generator` (required), `$brainstorm` (conditional: scope or success criteria remain unclear)
> - **Interaction mode:** plan-then-approve
> - **Output mode:** interactive draft → approved artifact
> - **Approval gate:** approve the PRD before saving
> - **Canonical output:** `chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md`
> - **Sample correspondence:** [product-requirements.md](../docs/product-requirements.md)
> - **Run context:** fresh session; attach or provide every input below.

## Use this when

The project brief and portable context are approved, and you need a small, testable product boundary for the SleepAlert system.

## Inputs

- Project brief: [project-brief.md](../../chapter-01-ai-in-software-engineering/docs/project-brief.md)
- Project context: [project-context.md](../../chapter-02-prompt-engineering/docs/project-context.md)
- Any newer human-approved product decision.

If a linked artifact is unavailable, ask for it. Do not infer product scope from the filename.

## Task

Use `$prd-generator` to draft a focused PRD for SleepAlert. Include product goal, users, detection & calibration lifecycle, success signals, functional requirements (FR-01 to FR-08), observable acceptance criteria, non-functional expectations, and exclusions.

Use `$brainstorm` before drafting only when an unresolved choice materially changes scope. Present the PRD as a draft and wait for human approval; do not save a canonical PRD during the first response.

## Constraints and source precedence

1. Newer human-approved decisions.
2. Project context.
3. Project brief.
4. AI suggestions.

- Describe product behavior, not implementation tasks.
- Keep latency requirements ($\le 500$ms) and edge autonomy verifiable.
- Exclude mechanical vehicle control and continuous cloud video streaming.
- Report missing or conflicting source information instead of inventing it.

## Expected output

A concise draft PRD that product, design, engineering, and testing can review.

## Save or update

After human approval, write `chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md`.
