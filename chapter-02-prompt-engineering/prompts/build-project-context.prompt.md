# P2.1 — Build reusable project context: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$brainstorm` (conditional: resolve a material ambiguity)
> - **Interaction mode:** plan-then-approve
> - **Output mode:** interactive draft → approved artifact
> - **Approval gate:** confirm unresolved decisions before saving
> - **Canonical output:** `chapter-02-prompt-engineering/docs/project-context.md`
> - **Sample correspondence:** [project-context.md](../docs/project-context.md)
> - **Run context:** fresh session; attach or provide every input below.

## Use this when

You have an approved project brief for SleepAlert and want a compact context package that another AI session can use without the original conversation.

## Inputs

- Approved project brief: [project-brief.md](../../chapter-01-ai-in-software-engineering/docs/project-brief.md)
- Any human decision newer than the brief.

If you cannot access the linked brief, ask the human to attach its content. Do not reconstruct it from memory.

## Task

Create a portable context document for SleepAlert. Extract the product boundary, safety monitoring lifecycle, approved decisions, vocabulary (EAR, MAR, PERCLOS, Pitch/Yaw, calibration), source hierarchy, excluded scope, and rules for missing or conflicting information.

Use `$brainstorm` only when an ambiguity would change the context boundary. If a decision is still open, preserve it as an open question instead of converting it into a fact. Present the context draft for review before saving.

## Constraints and source precedence

1. Newer human-approved decisions.
2. The approved project brief.
3. AI suggestions.

- Preserve the difference between a fact, a decision, and an assumption.
- Do not invent requirements or architecture outside the safety boundary.
- Keep the document compact enough to attach to another prompt.
- Explicitly exclude cloud-dependent real-time video streaming.
- Standardize biometric metrics: EAR, MAR, PERCLOS, Pitch, Yaw.
- Report conflicts or unknowns instead of silently resolving them.

## Expected output

A reusable Markdown context with product summary, approved decisions, vocabulary, artifact hierarchy, boundaries, anti-expansion rules, and unresolved questions.

## Save or update

After the human confirms the draft, write `chapter-02-prompt-engineering/docs/project-context.md`.

## Human review required

Confirm that every item labelled as a decision is actually approved and that no open question was silently closed.

## Validation checklist

- A fresh session can understand SleepAlert's edge-to-fleet boundaries without the original chat.
- Wearables and cloud video streaming are rejected.
- Authoritative artifacts are linked by role.
- Conflicts are escalated rather than silently resolved.
