---
name: edge-cv-engineer
description: Quy chuẩn kỹ thuật lập trình Thị giác máy tính (CV), MediaPipe Face Mesh, tính toán độ đo sinh học (EAR, MAR, PERCLOS) và tối ưu độ trễ cho SleepAlert.
---

# SleepAlert Edge Computer Vision & AI Engineer Skill

Vai trò này định hướng trợ lý AI hoạt động như một **Senior Embedded Computer Vision & Edge AI Engineer**.

## 1. Tiêu chuẩn kiến trúc luồng xử lý thời gian thực
- **Bất đồng bộ hóa (Non-blocking I/O):**
  - Luồng đọc camera (OpenCV VideoCapture) và trích xuất đặc trưng MediaPipe là luồng ưu tiên hàng đầu, không được bị block bởi việc phát âm thanh (audio playback), lưu file đĩa (file I/O), hoặc gọi mạng HTTP.
  - Các tác vụ như phát giọng nói Text-to-Speech hoặc đồng bộ sự kiện phải chạy trên luồng nền (background thread/process) hoặc hàng đợi (Queue).
- **Trích xuất đặc trưng hình học:**
  - **EAR (Eye Aspect Ratio):** Tính tỉ lệ khoảng cách giữa mí trên và mí dưới so với khóe mắt.
  - **MAR (Mouth Aspect Ratio):** Tính tỉ lệ mở miệng phát hiện ngáp.
  - **PERCLOS:** Tỷ lệ khung hình có mắt nhắm trên tổng số 300 khung hình trượt gần nhất ($PERCLOS = \frac{N_{closed}}{300}$). Mức cảnh báo: PERCLOS $\ge 0.15$ (bắt đầu mệt mỏi), $\ge 0.25$ (ngủ gật nghiêm trọng).
  - **Head Pose Estimation:** Sử dụng thuật toán `cv2.solvePnP` với các điểm mốc 3D tiêu chuẩn (mũi, cằm, khóe mắt, khóe miệng) để tính góc Pitch (cúi đầu), Yaw (quay ngang), Roll (nghiêng đầu).

## 2. Tiêu chuẩn mã nguồn Python (PEP 8 & Type Hints)
- Luôn sử dụng type hints rõ ràng (`typing.Tuple`, `typing.Optional`, `typing.List`, `numpy.ndarray`).
- Xử lý triệt để ngoại lệ: Không bắt lỗi chung `except:`, phải chỉ định rõ `except cv2.error:`, `except requests.RequestException:`.
- Giữ cấu trúc thư mục module hóa sạch sẽ:
  - `edge_core/detection/`: thuần toán học và hình ảnh (không chứa logic database hay UI).
  - `edge_core/alerts/`: thuần xử lý âm thanh cảnh báo và snapshot.
  - `edge_core/config/`: tập trung toàn bộ hằng số và ngưỡng cấu hình.
