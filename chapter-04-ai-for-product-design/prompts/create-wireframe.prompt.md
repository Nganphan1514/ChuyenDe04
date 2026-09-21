# P4.2 — Create Wireframes: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$brainstorm` (conditional)
> - **Interaction mode:** plan-then-approve
> - **Output mode:** interactive draft → approved artifact
> - **Approval gate:** approve layout hierarchy and component structure before saving
> - **Canonical output:** `chapter-04-ai-for-product-design/docs/wireframes.md`
> - **Run context:** fresh session; use user flows and feature specifications.

## Use this when

User flows are defined and you need to lay out the information architecture, component hierarchy, visual zoning, and screen real estate for both the In-Cabin Driver HUD and the Central Fleet Management Portal.

## Inputs

- User Flows: [user-flows.md](../docs/user-flows.md)
- Feature Specification: [feature-specification.md](../../chapter-03-ai-for-requirements-product-analysis/docs/feature-specification.md)

## Task

Develop comprehensive ASCII wireframes and zoning layouts:
1. **In-Cabin Driver HUD (Touchless Glanceable Display):**
   - Header Zone: Vehicle ID, System Status (Active, Calibrating, Warning, Critical), Night Mode IR indicator.
   - Central Focal Zone: Driver face wireframe overlay / Biometric status icon (Eye Openness, Yawn indicator, Head Angle gauge).
   - Metrics Zone: Big digit EAR, PERCLOS bar gauge (Green/Amber/Red), Driving duration timer.
   - Alert Overlay Zone: High-contrast modal / banner for Level 1, Level 2 (Siren strobe), and Rest Stop suggestion.
2. **Central Fleet Safety Web Dashboard:**
   - Navigation Sidebar: Live Monitoring, Fleet Overview, Incident Logs, Vehicle Management, Reports.
   - Real-time Fleet Status Cards: Active vehicles, critical alert triggers, driver fatigue index.
   - Live Incident Feed & Interactive Map: Vehicle GPS marker, event severity badge, snapshot thumbnail modal.

## Constraints

- Strictly adhere to automotive in-cabin UX guidelines (large typography, high contrast, zero complex interaction).
- Fleet Dashboard must comply with desktop monitoring density (scannable table, real-time alert toast).
