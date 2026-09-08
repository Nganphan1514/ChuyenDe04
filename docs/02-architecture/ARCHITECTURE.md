# THIẾT KẾ KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

## DỰ ÁN: SLEEPALERT
### Kiến trúc Edge-to-Fleet Hybrid IoT

---

## 1. TỔNG QUAN KIẾN TRÚC VẬT LÝ & PHÂN TẦNG

Hệ thống **SleepAlert** được thiết kế theo mô hình **Edge Computing kết hợp Centralized Cloud Management**, bảo đảm tính tự chủ 100% tại buồng lái khi mất mạng và khả năng giám sát tập trung khi có kết nối.

```text
======================= KHÔNG GIAN BUỒNG LÁI (VEHICLE CABIN) =======================
  [ IR / RGB Camera ]
          │ 720p @ 30 FPS
          ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: EDGE COMPUTING UNIT (Mini PC / On-board Computer)                       │
│                                                                                 │
│   ┌────────────────────────┐         ┌────────────────────────┐                 │
│   │ Camera Capture Worker  │ ──────> │ MediaPipe Face Mesh    │                 │
│   │ (OpenCV VideoCapture)  │         │ (468 3D Landmarks)     │                 │
│   └────────────────────────┘         └───────────┬────────────┘                 │
│                                                  │                              │
│                                                  ▼                              │
│   ┌───────────────────────────────────────────────────────────┐                 │
│   │ Feature Extraction Engine (EAR, MAR, PERCLOS, Head Pose)  │                 │
│   └──────────────────────────────┬────────────────────────────┘                 │
│                                  │                                              │
│                                  ▼                                              │
│   ┌───────────────────────────────────────────────────────────┐                 │
│   │ State Evaluator & Risk Scoring (Tỉnh táo / Mệt mỏi / Ngủ) │                 │
│   └──────────────────────────────┬────────────────────────────┘                 │
│                                  │                                              │
│         ┌────────────────────────┴────────────────────────┐                     │
│         │ < 500ms Local Event                             │ Vi phạm nguy hiểm   │
│         ▼                                                 ▼                     │
│   ┌───────────────────────────┐                     ┌───────────────────────┐   │
│   │ In-Cabin Audio Engine     │                     │ Event & Snapshot      │   │
│   │ (Pygame / Audio Buzzer)   │                     │ Local SQLite & Queue  │   │
│   └───────────────────────────┘                     └───────────┬───────────┘   │
└─────────────────────────────────────────────────────────────────┼───────────────┘
                                                                  │
                                      HTTPS / WebSocket (Async)   │ Khi có 4G/WiFi
                                      (Chỉ gửi sự kiện & ảnh)     │
                                                                  ▼
=========================== TRUNG TÂM ĐIỀU HÀNH (FLEET CLOUD) =====================
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 2: CENTRAL FLEET MANAGEMENT SERVER                                         │
│                                                                                 │
│   ┌───────────────────────────┐                     ┌───────────────────────┐   │
│   │ FastAPI Gateway & Auth    │ ──────────────────> │ Fleet Database        │   │
│   │ (RESTful & WebSocket)     │                     │ (PostgreSQL / SQLite) │   │
│   └─────────────┬─────────────┘                     └───────────────────────┘   │
│                 │                                                               │
│                 ▼                                                               │
│   ┌───────────────────────────────────────────────────────────┐                 │
│   │ Web Dashboard (HTML5 / Next.js / WebSocket Live Alerts)   │                 │
│   │ Dành cho Quản lý an toàn đội xe & Điều vận                │                 │
│   └───────────────────────────────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. NGUYÊN TẮC THIẾT KẾ ĐỘC LẬP TẠI BIÊN (EDGE AUTONOMY)

1. **Non-blocking Audio Threading:**
   - Việc phát chuông cảnh báo hoặc tổng hợp giọng nói (Text-to-Speech) tốn từ vài trăm miligiây đến hàng giây. Nếu gọi đồng bộ trong luồng đọc camera thì camera sẽ bị khựng (drop FPS), dẫn tới mất dấu vết khuôn mặt.
   - SleepAlert triển khai cơ chế **Audio Event Queue**: Luồng thị giác (Vision Loop) chỉ đẩy lệnh cảnh báo (`BEEP`, `SIREN`, `VOICE_REST`) vào hàng đợi; một luồng nền riêng biệt (Audio Worker Thread) sẽ tiêu thụ và phát âm thanh.
2. **Offline-First Storage:**
   - Khi xe chạy qua đèo, đường hầm hoặc vùng không có sóng viễn thông, các sự kiện cảnh báo và ảnh chụp (snapshot) được lưu tức thì vào CSDL cục bộ (Local SQLite/CSV).
   - Một tiến trình đồng bộ nền (Sync Daemon) sẽ tự động kiểm tra kết nối Internet và gửi các sự kiện tồn đọng về Cloud ngay khi có sóng trở lại.

---

## 3. CƠ CHẾ AN TOÀN FAIL-SAFE

* **Mất dấu khuôn mặt (Face Lost Detection):** Nếu camera không tìm thấy khuôn mặt trong hơn 3 giây khi xe đang di chuyển, hệ thống kích hoạt cảnh báo nhắc nhở tài xế ngồi đúng vị trí hoặc kiểm tra lại góc đặt camera.
* **Cảnh báo ngược sáng / Thiếu sáng:** Nếu độ sáng trung bình của khung hình quá thấp ($V_{mean} < 30$), hệ thống đưa ra thông báo cần bật đèn hồng ngoại hoặc điều chỉnh góc chiếu sáng.
