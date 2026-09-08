# SleepAlert Product Requirements

> **Provenance**
> - **Source prompts:** [P3.1 — Create product requirements](../prompts/create-product-requirements.prompt.md) and [P3.2 — Review product requirements](../prompts/review-product-requirements.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Approved scope, accepted requirement corrections, confirmed offline-first latency boundary.
> - **Reproduction note:** P3.2 produced findings; only accepted findings are reflected in this baseline.

## Goal

Provide commercial vehicle drivers with real-time, non-intrusive in-cabin active safety monitoring that detects drowsiness and distraction within 500ms and escalates local acoustic warnings without requiring cloud connectivity.

## Functional Requirements

1. **FR-01 (Dynamic Eye Calibration):** Upon vehicle ignition and driver detection, the system must sample eye landmarks for 3.0 seconds to establish an individualized baseline EAR ($EAR_{base}$) and calculate $EAR_{thresh} = 0.75 \times EAR_{base}$.
2. **FR-02 (Biometric Feature Extraction):** The system must compute EAR, MAR, and Head Pose (Pitch/Yaw) on every video frame at $\ge 25$ FPS under daytime RGB and night IR lighting.
3. **FR-03 (PERCLOS Metric Calculation):** The system must maintain a sliding history of the last 300 frames and compute PERCLOS ($N_{closed} / 300$) on every frame once $\ge 120$ frames are populated.
4. **FR-04 (Level 1 Fatigue Pre-warning):** When $0.15 \le \text{PERCLOS} < 0.25$ or when MAR exceeds 0.60 for $\ge 20$ consecutive frames (yawn), the system dispatches a gentle acoustic reminder.
5. **FR-05 (Level 2 Critical Microsleep Alarm):** When EAR remains below $EAR_{thresh}$ continuously for $\ge 1.5$ seconds or when $\text{PERCLOS} \ge 0.25$, the system immediately triggers a maximum-volume siren alarm until eyes reopen for $\ge 0.5$ seconds.
6. **FR-06 (Level 3 Head Down & Distraction Warning):** When Pitch angle $< -20^{\circ}$ (head drooping downward toward steering wheel) persists for $\ge 2.0$ seconds, the system sounds a directional alert prompting the driver to look up.
7. **FR-07 (Location-aware Rest Stop Recommendation):** When consecutive fatigue warnings occur within 15 minutes, the system queries cached/nearby geographic rest-stops and announces the nearest safe stop via Vietnamese speech.
8. **FR-08 (Event Snapshot & Local Persistence):** Upon every Level 2 critical alarm, the system captures a single-frame violation snapshot, records telemetry (timestamp, EAR, PERCLOS, Pitch, GPS) to local storage, and enqueues it for asynchronous fleet synchronization.

## Non-Goals & Exclusions

No automatic emergency braking (AEB), no steering wheel takeover, no continuous cloud video streaming, no multi-passenger detection, and no driver wage/timesheet calculation in this release.

## Acceptance Signals

The primary verification loop is: boot camera → calibrate in 3s → normal eye blinking (no alarm) → close eyes for 1.5s (immediate siren triggered in $\le 500$ms) → reopen eyes (siren stops in $\le 500$ms) → event snapshot and telemetry logged locally.
