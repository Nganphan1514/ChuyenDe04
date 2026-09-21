# P4.4 — AI Design Review: SleepAlert

> - **Role:** REVIEW GATE
> - **Skills:** `$brainstorm` (conditional)
> - **Interaction mode:** inspect-and-report
> - **Output mode:** structured findings and design critique
> - **Approval gate:** accept or address each ergonomic and accessibility finding
> - **Canonical output:** `chapter-04-ai-for-product-design/docs/design-review.md`
> - **Run context:** fresh session; inspect prototype, wireframes, and flows against automotive UX standards.

## Use this when

The prototype, wireframes, and user flows are implemented and require adversarial review for safety, glanceability, cognitive load, night-driving contrast (WCAG 2.1 AAA), and fail-safe recovery.

## Inputs

- Prototype: [prototype/index.html](../prototype/index.html)
- Wireframes: [wireframes.md](../docs/wireframes.md)
- User Flows: [user-flows.md](../docs/user-flows.md)
- Product Requirements: [product-requirements.md](../../chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md)

## Task

Critique the UX/UI design across 5 critical dimensions:
1. **In-Cabin Glanceability (< 1.0s rule):** Can the driver grasp their safety state without taking their eyes off the road for more than 1 second?
2. **Night Driving Ergonomics:** Are display colors predominantly dark with amber/red accents to avoid pupil constriction and road blindness?
3. **Cognitive Load & Distraction:** Are animations and visual updates restrained so they do not startle or distract the driver during normal conditions?
4. **Alarm Salience & Haptic/Acoustic Dominance:** When a critical microsleep occurs, does the acoustic alarm take precedence over visual cues?
5. **Fleet Portal Information Density:** Is the dispatcher able to triage 50+ vehicles simultaneously without alert fatigue?

Output a structured findings matrix: `ID | Category | Severity | Issue Observed | Ergonomic Rationale | Corrective Action`.
