"""
Cấu hình thông số hệ thống SleepAlert
Sử dụng dataclasses từ thư viện chuẩn Python (Zero Dependency).
"""
import os
from dataclasses import dataclass

@dataclass
class SystemSettings:
    # Camera settings
    CAMERA_INDEX: int = 0
    FRAME_WIDTH: int = 1280
    FRAME_HEIGHT: int = 720
    FPS_TARGET: int = 30

    # Calibration & Detection Thresholds
    CALIBRATION_DURATION_SECONDS: float = 3.0
    DEFAULT_EAR_THRESHOLD: float = 0.22
    DEFAULT_MAR_THRESHOLD: float = 0.60
    PERCLOS_WINDOW_SIZE: int = 300
    PERCLOS_WARNING_THRESHOLD: float = 0.15
    PERCLOS_CRITICAL_THRESHOLD: float = 0.25

    # Head Pose Pitch Thresholds (degrees)
    PITCH_HEAD_DOWN_THRESHOLD: float = -20.0

    # Alert Cooldowns (seconds)
    DROWSY_TIME_THRESHOLD: float = 1.5   # Thời gian nhắm mắt liên tục kích hoạt báo động đỏ
    YAWN_CONSECUTIVE_FRAMES: int = 20
    AUDIO_COOLDOWN_SECONDS: float = 3.0

    # Fleet & Vehicle Info
    VEHICLE_ID: str = "VN-43A-9999"
    CENTRAL_SERVER_URL: str = "http://127.0.0.1:8000"

settings = SystemSettings()
