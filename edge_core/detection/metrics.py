"""
Các hàm tính toán độ đo sinh học thuần túy: EAR, MAR, PERCLOS.
Sử dụng math.hypot chuẩn tối ưu hiệu năng cho tọa độ 2D, không phụ thuộc thư viện ngoài.
"""
import math
from typing import Sequence, Tuple

def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """Tính khoảng cách Euclidean 2D siêu nhanh bằng math.hypot."""
    return math.hypot(point1[0] - point2[0], point1[1] - point2[1])

def calculate_ear(eye_landmarks: Sequence[Tuple[float, float]]) -> float:
    """
    Tính tỉ lệ mở mắt Eye Aspect Ratio (EAR).
    Quy ước 6 điểm mí mắt theo chuẩn Soukupová và Čech (2016):
    P1: Khóe mắt ngoài, P4: Khóe mắt trong
    P2, P6: Cặp điểm mí trên - mí dưới ngoài
    P3, P5: Cặp điểm mí trên - mí dưới trong

    Công thức: EAR = (|P2 - P6| + |P3 - P5|) / (2 * |P1 - P4|)
    """
    if len(eye_landmarks) < 6:
        raise ValueError("Cần tối thiểu 6 điểm landmarks để tính EAR")

    p1, p2, p3, p4, p5, p6 = eye_landmarks[:6]

    vertical_1 = calculate_distance(p2, p6)
    vertical_2 = calculate_distance(p3, p5)
    horizontal = calculate_distance(p1, p4)

    if horizontal <= 1e-6:
        return 0.0

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return float(ear)

def calculate_mar(mouth_landmarks: Sequence[Tuple[float, float]]) -> float:
    """
    Tính tỉ lệ mở miệng Mouth Aspect Ratio (MAR) để phát hiện hành vi ngáp.
    MAR = (|Mí môi trên - Mí môi dưới|) / (|Khóe môi trái - Khóe môi phải|)
    """
    if len(mouth_landmarks) < 4:
        raise ValueError("Cần tối thiểu 4 điểm landmarks để tính MAR")

    top, bottom, left, right = mouth_landmarks[:4]

    vertical = calculate_distance(top, bottom)
    horizontal = calculate_distance(left, right)

    if horizontal <= 1e-6:
        return 0.0

    mar = vertical / horizontal
    return float(mar)

def calculate_perclos(eye_history: Sequence[bool]) -> float:
    """
    Tính chỉ số PERCLOS (Percentage of Eye Closure).
    eye_history: chuỗi các giá trị boolean (True nếu mắt nhắm, False nếu mắt mở).
    Trả về tỉ lệ phần trăm mắt nhắm trong cửa sổ (giá trị từ 0.0 đến 1.0).
    """
    total_frames = len(eye_history)
    if total_frames == 0:
        return 0.0

    closed_count = sum(1 for is_closed in eye_history if is_closed)
    return float(closed_count / total_frames)
