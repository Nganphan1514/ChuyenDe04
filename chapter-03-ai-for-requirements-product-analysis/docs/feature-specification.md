# SleepAlert In-Cabin Detection and Safety Alert Feature Specification

> **Provenance**
> - **Source prompt:** [P3.3 — Create feature specification](../prompts/create-feature-specification.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Approved calibration, biometric calculation, audio queueing, and fail-safe recovery behavior.
> - **Reproduction note:** This artifact is finalized after passing the PRD review gate.

## 1. Calibration and Detection Lifecycle

Upon system start, the camera worker opens the driver-facing feed at 720p/30 FPS.
- **Phase 1 (Face Acquisition):** MediaPipe Face Mesh scans incoming frames. If no face is detected, the status remains `FACE_SEARCHING`.
- **Phase 2 (Dynamic Calibration):** Once a stable face is detected for 3.0 continuous seconds (`CALIBRATION_DURATION_SECONDS = 3.0`), the system collects all valid EAR samples while the driver looks naturally forward. The median value becomes $EAR_{base}$. The closed-eye threshold is automatically set to $EAR_{thresh} = 0.75 \times EAR_{base}$.
- **Phase 3 (Active Monitoring):** On every frame, EAR, MAR, and Head Pose (Pitch, Yaw) are extracted. Each frame appends an eye-closed boolean (`EAR < EAR_thresh`) to the `eye_window` sliding buffer (size = 300).

## 2. Alert Escalation & Acoustic Queueing

Audio output is strictly decoupled from video capture via `AsyncAudioEngine`:
- **Pre-warning (Level 1):** If `PERCLOS >= 0.15` or `yawn_frames >= 20`, an audio event `("WARNING", message)` is pushed to the worker queue. Cooldown between fatigue warnings is 20 seconds.
- **Critical Siren (Level 2):** If `drowsy_frames >= 45` (~1.5s at 30 FPS) or `PERCLOS >= 0.25`, an urgent event `("SIREN", None)` is pushed immediately. The siren repeats continuously until eye reopening is confirmed across at least 15 consecutive frames.
- **Distraction Alert (Level 3):** If `pitch < -20.0` degrees for $> 2.0$ seconds, a voice event prompts the driver to raise their head.

## 3. Location-aware Rest Stop Lifecycle

When two Level 1 or Level 2 warnings occur within 15 minutes:
1. The system invokes `services.location_service.find_nearest_rest_stop()` using cached GPS coordinates.
2. If a valid stop is found within 50 km, an audio message is synthesized in Vietnamese: `"Gợi ý trạm dừng nghỉ [Tên trạm], cách khoảng [X] km phía trước"`.
3. If no GPS signal or network is available, the system falls back to a generic reminder: `"Bạn đã lái xe liên tục khi mệt mỏi, vui lòng tấp vào lề an toàn để nghỉ ngơi"`.

## 4. Fail-Safe Recovery and Offline Persistence

- **Face Occlusion / Loss:** If facial landmarks vanish for $> 3.0$ seconds while the vehicle is in motion, a `FACE_LOST` chime sounds, reminding the driver to adjust posture or clear obstructions.
- **Snapshot Capture:** Every Level 2 trigger captures the un-annotated source frame, encodes it as JPEG into `snapshots/` with the filename `snap_{timestamp}_{vehicle_id}.jpg`, and appends an entry to `logs/detection_log.csv`.
- **Network Resiliency:** The telemetry payload is placed in a local SQLite dispatch queue. If the vehicle is in a cellular dead zone, events accumulate safely on disk and sync asynchronously once 4G/WiFi is restored.
