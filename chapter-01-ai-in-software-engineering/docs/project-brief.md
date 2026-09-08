# SleepAlert Project Brief

> **Provenance**
> - **Source prompt:** [P1.1 — Clarify project idea](../prompts/clarify-project-idea.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Answered clarification questions and approved scope, exclusions, and assumptions.
> - **Reproduction note:** This reflects the agreed baseline for SleepAlert; a different conversation can produce a different approved brief.

## Problem Statement

Long-haul truck and bus drivers face severe fatigue and microsleep risks during extended night shifts (22:00–05:00). Existing market solutions either rely on intrusive wearables (smartwatches causing discomfort and delayed alerts), post-accident lane departure sensors, or high-latency cloud streaming cameras that breach driver privacy and fail in zero-connectivity areas (mountain passes, tunnels).

## Product Vision & Core Job

**SleepAlert** is an in-cabin active safety monitoring system that detects early drowsiness and critical sleep onset using non-intrusive edge computer vision.

The core job of SleepAlert is to:
1. Continuously monitor driver facial landmarks in real time (30 FPS) without requiring wearables.
2. Quantify fatigue using multi-metric biometric indicators: EAR (Eye Aspect Ratio), MAR (Mouth Aspect Ratio), PERCLOS (Percentage of Eye Closure over 300 frames), and Head Pose (Pitch/Yaw).
3. Trigger immediate, multi-stage local acoustic alerts (< 500ms latency) inside the cabin to wake the driver before vehicle control is lost.
4. Provide location-aware rest-stop recommendations when fatigue accumulates.
5. Capture lightweight event telemetry and violation snapshots for fleet safety management when connectivity is available.

## Exclusions & Non-Goals

The first release deliberately excludes:
- Automatic emergency braking (AEB) or physical vehicle mechanical takeover.
- Continuous 24/7 raw video streaming to the cloud (Zero-SaaS-Leakage privacy guarantee).
- Complex in-cabin multi-passenger surveillance (strictly focused on the driver's seat).
- Commercial driver wage calculation, telematics payroll, or route optimization.

## Success Signals & Journey

Success is a robust and trustworthy safety loop:
- **Startup:** Driver enters vehicle → system boots with ignition → completes 3-second dynamic eye calibration.
- **Monitoring:** System runs locally at $\ge 25$ FPS under both daylight and infrared night illumination.
- **Pre-warning:** When yawn frequency increases or PERCLOS exceeds 0.15, a polite Vietnamese voice reminder prompts alertness.
- **Critical Alarm:** When eyes remain closed $\ge 1.5$ seconds or head tilts down $> 20^{\circ}$ for 2 seconds, an immediate high-volume siren fires until eyes open.
- **Auditability:** Event snapshot and telemetry are recorded locally and synced asynchronously to the fleet dashboard upon network availability.

## Open Assumptions

Hardware assumptions (camera focal length, IR illuminator wavelength, and on-board compute specifications) remain open until reviewed during architecture design.
