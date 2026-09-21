# P4.1 — Create User Flows: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$brainstorm` (conditional: alternative interaction paths)
> - **Interaction mode:** plan-then-approve
> - **Output mode:** interactive draft → approved artifact
> - **Approval gate:** approve user flows and failure paths before saving
> - **Canonical output:** `chapter-04-ai-for-product-design/docs/user-flows.md`
> - **Run context:** fresh session; use PRD, Feature Spec, and Project Context.

## Use this when

Requirements and feature specs are approved, and you need to map out step-by-step user journeys, state transitions, edge cases, and recovery loops for both the in-cabin driver and the remote fleet manager.

## Inputs

- Project Context: [project-context.md](../../chapter-02-prompt-engineering/docs/project-context.md)
- Product Requirements: [product-requirements.md](../../chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md)
- Feature Specification: [feature-specification.md](../../chapter-03-ai-for-requirements-product-analysis/docs/feature-specification.md)

## Task

Map out 5 distinct user flows using clear step sequences and Mermaid state diagrams:
1. **Flow 1 (Vehicle Startup & 3-Second Eye Calibration):** Driver enters, camera acquires face, samplings baseline EAR, establishes personalized threshold.
2. **Flow 2 (Continuous Real-time Monitoring & Alert Escalation):** Normal blinking → Fatigue pre-warning (Level 1) → Critical Microsleep Alarm (Level 2) → Eye reopening recovery.
3. **Flow 3 (Distraction & Head Pose Violation):** Prolonged downward pitch angle $> 2.0$s → Head-up chime → Normal state.
4. **Flow 4 (Location-aware Rest Stop Recommendation):** Persistent fatigue → GPS query → Vietnamese speech dispatch → Safe pull-over.
5. **Flow 5 (Safety Fail-safe & Network Outage):** Face occlusion/loss $> 3$s, low light IR switch, and offline telemetry caching with auto-sync.

## Constraints

- Differentiate between in-cabin driver actions (zero touch, glance-only) and fleet manager actions (web mouse/keyboard).
- Include clear error recovery loops for each failure state.
