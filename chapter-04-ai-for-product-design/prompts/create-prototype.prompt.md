# P4.3 — Create Interactive Prototype: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$brainstorm` (conditional)
> - **Interaction mode:** plan-then-approve
> - **Output mode:** runnable HTML5/Tailwind prototype
> - **Approval gate:** test real-time state changes and alert behaviors before saving
> - **Canonical output:** `chapter-04-ai-for-product-design/prototype/index.html`
> - **Run context:** fresh session; use wireframes and user flows.

## Use this when

Wireframes and interaction flows are established, and you need a high-fidelity interactive web prototype to test, demonstrate, and validate UX behaviors before building backend integrations.

## Inputs

- Wireframes: [wireframes.md](../docs/wireframes.md)
- User Flows: [user-flows.md](../docs/user-flows.md)
- Feature Specification: [feature-specification.md](../../chapter-03-ai-for-requirements-product-analysis/docs/feature-specification.md)

## Task

Construct a standalone single-file interactive prototype (`prototype/index.html`) using HTML5, Tailwind CSS, and Vanilla JavaScript.

The prototype must support:
1. **Dual Workspace Tabs:** Switch seamlessly between **In-Cabin Driver HUD** and **Central Fleet Management Dashboard**.
2. **In-Cabin Simulation Controls:**
   - State Toggle Buttons: `Tỉnh táo (Normal)`, `Ngáp (Yawn)`, `Mệt mỏi (Fatigue L1)`, `Ngủ gật khẩn cấp (Critical L2 - Microsleep)`, `Gục đầu (Head Down L3)`, `Mất mặt (Face Lost)`.
   - Real-time Sliders: EAR, PERCLOS, Pitch angle.
   - Dynamic Visual Effects: Calibrating progress bar, Amber warning pulse, Red emergency flashing strobe with simulated siren sound.
3. **Fleet Dashboard Live Interactions:**
   - Real-time stat counters updating with simulated vehicle fleet.
   - Live Incident Table receiving events from the cabin simulator.
   - Snapshot preview modal popping up on clicking violation records.
