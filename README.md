# SleepAlert

> **Hệ thống giám sát và cảnh báo sớm tình trạng buồn ngủ, mất tập trung cho tài xế đường dài ứng dụng Edge Computer Vision và kiến trúc Hybrid IoT.**

[![Course](https://img.shields.io/badge/Course-VKU%20CS2028%20AI%20Product%20Dev-red.svg)](docs/01-overview/PRD.md)
[![Edge-AI](https://img.shields.io/badge/AI%20Core-MediaPipe%20%7C%20PERCLOS-blue.svg)](docs/02-architecture/ARCHITECTURE.md)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-green.svg)](docs/02-architecture/ARCHITECTURE.md)
[![Latency](https://img.shields.io/badge/Latency-%3C500ms%20Local-orange.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

---

## 📌 Tổng quan dự án

**SleepAlert** là sản phẩm AI ứng dụng công nghệ Thị giác máy tính biên (Edge Computer Vision) và Hệ thống cảnh báo thông minh, được phát triển theo quy trình toàn diện (End-to-End SDLC) bám sát học phần **Chuyên đề 4 - Phát triển sản phẩm AI (CS2028)**.

Hệ thống giải quyết triệt để vấn đề mất an toàn giao thông do tài xế xe tải, xe khách đường dài ngủ gật và mệt mỏi tích lũy:
* **Phát hiện đa chỉ số sinh học (Multi-metric Fusion):** Không dựa vào 1 chỉ số đơn lẻ mà kết hợp đồng thời **EAR** (Eye Aspect Ratio - tỉ lệ mở mắt), **MAR** (Mouth Aspect Ratio - phát hiện ngáp), **PERCLOS** (Percentage of Eye Closure trong cửa sổ 300 frames - chuẩn y học giao thông), và **Head Pose Pitch/Yaw** (đo góc gục đầu hoặc mất tập trung).
* **Cảnh báo âm thanh đa cấp độ (Multi-stage Audio Alert):** Tách biệt giữa nhắc nhở nhẹ (chuông báo, rung giọng) khi mới chớm mệt mỏi và báo động khẩn cấp âm lượng lớn khi ngủ gật liên tục quá 1.5 giây.
* **Định vị trạm dừng chân thông minh:** Tích hợp dịch vụ bản đồ vị trí (Location Service) tự động tra cứu và phát giọng nói tiếng Việt hướng dẫn tài xế đến trạm nghỉ gần nhất khi mức độ mệt mỏi đạt ngưỡng nguy hiểm.
* **Edge Autonomy (Độc lập cục bộ):** Xử lý hình ảnh và kích hoạt còi/loa cảnh báo trực tiếp trên thiết bị tại cabin xe, **đáp ứng thời gian thực (< 500ms)** và vận hành liên tục ngay cả khi xe đi vào vùng mất sóng 4G/5G.
* **Đồng bộ sự kiện vi phạm an toàn:** Chỉ gửi siêu dữ liệu sự kiện (telemetry metadata, snapshot ảnh vi phạm) về máy chủ quản lý đội xe khi có kết nối mạng, bảo đảm quyền riêng tư (Zero-Leakage of raw continuous video stream).

---

## 🏛️ Kiến trúc hệ thống phân tầng (Edge-to-Fleet Architecture)

```text
[ IN-CABIN INFRARED / RGB CAMERA ]
               │ 30 FPS Video Stream
               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: EDGE AI VISION ENGINE (In-Vehicle Compute Unit)                 │
│ - MediaPipe Face Mesh (468 3D Facial Landmarks)                         │
│ - Geometric Feature Extractor: EAR, MAR, PERCLOS (300 frames), Pitch    │
│ - Rule-based & ML Classifier: Risk Scoring & Multi-state Classification │
└──────────────────────┬────────────────────────────┬─────────────────────┘
                       │                            │
      < 500ms Latency  │ Trạng thái nguy kịch        │ Khi có mạng 4G/WiFi
      (Local Trigger)  ▼                            ▼ (Async REST / WebSocket)
┌──────────────────────────────────────┐  ┌───────────────────────────────┐
│ TẦNG 2: SMART ACTIVE ALERT ENGINE    │  │ TẦNG 3: CENTRAL FLEET CLOUD   │
│ - Pygame / Text-to-Speech (Tiếng Việt│  │ - FastAPI Gateway             │
│ - Cảnh báo âm thanh đa tầng          │  │ - Real-time Fleet Dashboard   │
│ - Gợi ý trạm dừng nghỉ gần nhất (GPS)│  │ - Lịch sử vi phạm & Analytics │
│ - Snapshot lưu bằng chứng vi phạm    │  │ - Quản lý xe và tài xế        │
└──────────────────────────────────────┘  └───────────────────────────────┘
```

---

## 📚 Hệ thống hồ sơ kỹ thuật chuẩn hóa (`/docs`)

Dự án được tài liệu hóa bài bản theo các tiêu chuẩn công nghiệp (IEEE 830, SDLC):

1. **Tổng quan sản phẩm (01-overview):**
   * [PRD.md](docs/01-overview/PRD.md): Tài liệu yêu cầu sản phẩm chuẩn mực IEEE 830, User Personas, Functional Requirements (FR), Non-Functional Requirements (NFR).
   * [PROJECT_ANALYSIS.md](docs/01-overview/PROJECT_ANALYSIS.md): Phân tích bài toán, Pain Points, đối chiếu giải pháp công nghệ, User Stories và tiêu chí nghiệm thu dạng Gherkin (Given-When-Then).
2. **Kiến trúc hệ thống (02-architecture):**
   * [ARCHITECTURE.md](docs/02-architecture/ARCHITECTURE.md): Sơ đồ kiến trúc luồng dữ liệu phân tầng, cơ chế đệm bất đồng bộ (Queue Buffer) và khả năng hoạt động offline.

---

## 🛠️ Công nghệ cốt lõi

| Phân tầng | Công nghệ sử dụng | Mục đích |
| :--- | :--- | :--- |
| **Thị giác máy tính (CV)** | OpenCV, MediaPipe Face Mesh | Trích xuất 468 điểm mốc khuôn mặt, tính EAR, MAR, Head Pose |
| **Độ đo sinh học & ML** | Scikit-learn, NumPy, SciPy | Tính toán chỉ số PERCLOS, chuẩn hóa ngưỡng cá nhân hóa, phân loại trạng thái |
| **Cảnh báo âm thanh** | Pygame, pyttsx3, gTTS | Kích hoạt cảnh báo giọng nói tiếng Việt tức thì không block luồng camera |
| **Định vị & Bản đồ** | Geopy, OpenStreetMap Nominatim | Xác định tọa độ và tra cứu trạm dừng nghỉ gần nhất |
| **Backend & Quản trị** | FastAPI, Pydantic, Uvicorn | Xây dựng API phi tập trung, quản lý đội xe và nhật ký vi phạm |

---

## 🚀 Cấu trúc thư mục dự án

```text
SleepAlert/
├── .antigravity/                      # Quản trị ngữ cảnh & System Prompts cho AI
│   └── skills/
│       ├── 01_doc_architect.md       # Quy chuẩn thiết kế tài liệu & PRD
│       └── 02_edge_cv_engineer.md    # Quy chuẩn lập trình Computer Vision & Edge AI
├── docs/                              # Hồ sơ đặc tả kỹ thuật chuẩn hóa
│   ├── 01-overview/
│   │   ├── PRD.md                    # Product Requirements Document
│   │   └── PROJECT_ANALYSIS.md       # Phân tích nghiệp vụ & User Stories
│   └── 02-architecture/
│       └── ARCHITECTURE.md           # Thiết kế kiến trúc phân tầng
├── edge_core/                         # Module Edge AI chạy trên xe
│   ├── config/                       # Ngưỡng cài đặt, camera & audio settings
│   ├── detection/                    # Trích xuất đặc trưng & phân loại trạng thái
│   └── alerts/                       # Quản lý cảnh báo giọng nói & snapshot
├── backend/                           # API Gateway & Dịch vụ quản lý đội xe
├── requirements.txt                   # Danh mục thư viện phụ thuộc
└── README.md                          # Trang chủ dự án
```

---

## 📄 Bản quyền
Dự án được nghiên cứu và phát triển phục vụ học phần Chuyên đề 4 (CS2028) - Đại học Công nghệ Thông tin & Truyền thông Việt - Hàn (VKU).
