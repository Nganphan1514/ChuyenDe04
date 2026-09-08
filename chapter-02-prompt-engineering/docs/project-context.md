# SleepAlert Project Context

> **Provenance**
> - **Source prompt:** [P2.1 — Build reusable project context](../prompts/build-project-context.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Confirmed which statements are decisions and which remain assumptions.
> - **Reproduction note:** The package reflects the approved brief and decisions supplied to that run.

## Product Boundary

SleepAlert is an in-cabin active safety edge computing system designed for commercial transportation (freight trucks, long-distance sleeper buses). The system operates on a dedicated in-vehicle compute unit equipped with an infrared/RGB driver-facing camera and in-cabin speakers. It performs non-intrusive driver state analysis using facial landmark geometry and triggers graduated acoustic warnings.

## Approved Decisions & Constraints

- **Edge Autonomy:** All facial detection, metric calculation (EAR, MAR, PERCLOS, Head Pose), and alarm triggering must run 100% locally in real time ($\ge 25$ FPS, latency $\le 500$ms).
- **Non-blocking Architecture:** Audio warning synthesis and disk I/O (snapshots, logs) must never block the real-time video capture loop.
- **Privacy & Compliance:** Continuous video streaming to the cloud is strictly forbidden (Zero-SaaS-Leakage). Only discrete safety violation events and single-frame snapshots are transmitted.
- **Biometric Vocabulary:**
  - `EAR (Eye Aspect Ratio)`: Ratio of eye height to eye width; baseline calibrated per driver.
  - `MAR (Mouth Aspect Ratio)`: Ratio of vertical mouth opening to horizontal width (yawn detection).
  - `PERCLOS`: Percentage of eye closure over a sliding window of 300 frames (~10 seconds).
  - `Head Pose (Pitch/Yaw)`: 3D head orientation angles calculated via PnP; pitch $< -20^{\circ}$ indicates downward nodding.
- **Graduated Alerts:**
  - Level 1 (Fatigue pre-warning): Gentle Vietnamese chime / voice reminder when PERCLOS $\ge 0.15$ or frequent yawning.
  - Level 2 (Critical microsleep): Maximum volume siren when eyes closed $\ge 1.5$s or PERCLOS $\ge 0.25$.
  - Level 3 (Distraction / Head down): Warning when pitch $< -20^{\circ}$ persists for $> 2.0$s.

## Source Precedence

1. Human-approved decisions and the current context artifact.
2. The approved [project brief](../../chapter-01-ai-in-software-engineering/docs/project-brief.md).
3. The accepted [product requirements](../../chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md).
4. The future architecture package for API and edge-to-cloud schemas.
5. Current codebase, tests, and configuration.

When sources conflict, escalate the conflict immediately. Do not invent requirements or re-introduce cloud video streaming.

## Current Boundary

The product safety boundary is locked; specific hardware mounting brackets, CAN bus integration, and multi-camera driver blind-spot monitoring remain open and out-of-scope for the MVP.
