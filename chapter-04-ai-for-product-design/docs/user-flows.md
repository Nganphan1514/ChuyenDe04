# SleepAlert User Flows & Interaction State Specification

> **Provenance**
> - **Source prompt:** [P4.1 — Create User Flows](../prompts/create-user-flow.prompt.md)
> - **Artifact status:** Accepted reviewed sample
> - **Human action:** Approved primary flows, multi-space alert escalation, vehicle-driver authorization matching, and mobile face enrollment journeys.
> - **Reproduction note:** Maps requirements from Chapter 3 & DACN1 codebase into observable interactive user journeys across 3 environments.

---

## 1. Tổng quan Hệ sinh thái & Tác nhân Trải nghiệm (System Actors & Multi-Platform Matrix)

Kế thừa toàn diện từ đồ án **DACN1**, SleepAlert không chỉ đơn thuần là màn hình camera buồng lái mà là một **Hệ sinh thái an toàn vận tải 3 phân hệ tương hỗ**:

1. **In-Cabin AI Edge Cockpit (Buồng lái Thông minh):**
   - Thiết bị Edge (Raspberry Pi / Jetson / Tablet công nghiệp) gắn cố định trên táp-lô hoặc kính chắn gió.
   - Trực tiếp quét camera hồng ngoại, nhận diện Face Mesh 468 điểm, đối soát người lái hợp lệ theo phân công ca xe, tự động hiệu chuẩn mắt 3s, đo EAR/MAR/PERCLOS/Pitch, phát còi hú và chụp ảnh snapshot khi có nguy hiểm.
2. **Central Fleet Safety Management Portal (Cổng Điều hành Đội xe Doanh nghiệp):**
   - Ứng dụng Web dành cho Quản lý & Điều hành viên trung tâm.
   - Bao gồm 5 phân hệ chuyên sâu:
     - *Live Fleet Dashboard:* Giám sát xe đang chạy theo thời gian thực, bản đồ GPS, Risk score, ghim xe nguy cấp lên đầu bảng.
     - *Quản lý Xe (Vehicle Registry):* Biển số, dòng xe tải/container, trạng thái bảo dưỡng, ODO.
     - *Quản lý Tài xế (Driver Registry):* Hồ sơ bằng lái, trạng thái đăng ký khuôn mặt AI FaceID, điểm an toàn tích lũy.
     - *Điều phối & Lịch chạy (Schedule Dispatcher):* Gán ca xe chạy, tuyến đường xuất bến, đối soát ca chạy với tài xế.
     - *Báo cáo & Phân tích (Analytics & Reports):* Biểu đồ vi phạm theo khung giờ (nguy cơ cao từ 0h-4h sáng), Modal xem ảnh Snapshot vi phạm kèm tọa độ GPS.
3. **Driver Mobile App (Ứng dụng Di động Dành cho Tài xế):**
   - Ứng dụng điện thoại thông minh (iOS/Android) với hệ thống Bottom Navigation (Tổng quan, Lịch chạy, Quét mặt, Vi phạm, Hồ sơ).
   - Chức năng cốt lõi: Đăng ký khuôn mặt AI (Face Register Scanner với hiệu ứng laser và hướng dẫn góc mặt), tra cứu lịch trình ca xe được phân công, xem lại lịch sử vi phạm để nâng cao ý thức lái xe an toàn.

---

## 2. Các Luồng Trải nghiệm Cốt lõi (Core User Flows)

### Flow 1: Khởi động Buồng lái, Nhận diện FaceID & Hiệu chuẩn Mắt 3 Giây (In-Cabin Ignition, Auth & Calibration)

`mermaid
stateDiagram-v2
    [*] --> SystemBoot: Bật khóa điện xe (Ignition ON)
    SystemBoot --> FaceSearching: Khởi động Camera hồng ngoại IR
    
    state FaceSearching {
        [*] --> Scanning
        Scanning --> FaceDetected: MediaPipe bắt được 468 điểm khuôn mặt
        Scanning --> Scanning: Chưa phát hiện mặt (Tiếp tục quét)
    }
    
    FaceDetected --> DriverAuth: Đối soát FaceID với Lịch phân công ca xe
    
    state DriverAuth {
        [*] --> CheckSchedule: Query CSDL Lịch chạy hiện tại của xe
        CheckSchedule --> Authorized: Khớp tài xế phân công (nguoi_lai_hop_le)
        CheckSchedule --> Unauthorized: Người lạ / Không đúng lịch chạy
        Unauthorized --> AlertUnknown: HUD cảnh báo đỏ: CẢNH BÁO TÀI XẾ KHÔNG HỢP LỆ
        AlertUnknown --> LocalLog: Ghi log vi phạm phân công ca xe
    }
    
    Authorized --> Calibrating: Chào mừng tài xế + Bắt đầu hiệu chuẩn mắt
    
    state Calibrating {
        [*] --> CollectingEAR: Lấy mẫu EAR liên tục trong 3.0s
        CollectingEAR --> ComputeMedian: Tính toán Median EAR_base
        ComputeMedian --> SetThreshold: EAR_thresh = 0.75 * EAR_base
    }
    
    SetThreshold --> ActiveMonitoring: Phát giọng nói Hiệu chuẩn thành công, chúc bạn lái xe an toàn
    ActiveMonitoring --> [*]
`

* **Quy trình chi tiết:**
  1. Xe nổ máy, thiết bị Edge tự động khởi động dịch vụ trong vòng 5 giây.
  2. Camera tìm kiếm khuôn mặt. Khi nhận diện được, hệ thống đối soát vector khuôn mặt với danh sách tài xế được phân công chạy xe này trong ca hiện tại (kế thừa logic 
guoi_lai_hop_le từ DACN1).
  3. Nếu là người lạ hoặc không đúng phân công -> Cảnh báo tài xế lạ (unknown_driver_warning) và gửi cảnh báo về tổng đài.
  4. Nếu hợp lệ -> Kích hoạt thanh tiến trình hiệu chuẩn 3.0 giây (eye_calibrator.reset()). Hệ thống tính toán ngưỡng mắt mở tự nhiên riêng biệt ({thresh} = 0.75 \times EAR_{base}$) trước khi chuyển sang trạng thái giám sát chủ động.

---

### Flow 2: Giám sát Trạng thái & Thang Cảnh báo Đa tầng (Continuous Biometric Triage & Alert Escalation)

`mermaid
flowchart TD
    A[Khung hình Camera mới] --> B[Trích xuất EAR, MAR, Head Pose]
    B --> C{Mắt nhắm liên tục >= 1.5s HOẶC PERCLOS >= 0.25?}
    
    C -- CÓ (NGUY HIỂM CẤP 2) --> D[KÍCH HOẠT CÒI BÁO ĐỘNG SIREN 85dB]
    D --> E[HUD chớp đỏ toàn màn hình (Danger Strobe)]
    D --> F[Chụp ảnh Snapshot vi phạm + Lưu đệm Offline SQLite]
    D --> G{Tài xế mở mắt lại >= 0.5s?}
    G -- CHƯA --> D
    G -- ĐÃ MỞ MẮT --> H[Tắt còi báo động & Reset bộ đếm vi giấc ngủ]
    H --> A
    
    C -- KHÔNG --> I{PERCLOS >= 0.15 HOẶC Ngáp >= 20 frames?}
    I -- CÓ (CẢNH BÁO CẤP 1) --> J[Phát âm chuông nhẹ / Voice nhắc nhở]
    J --> K[HUD hiển thị viền Hổ phách Amber]
    J --> L[Ghi nhận vào log mệt mỏi tích lũy]
    L --> A
    
    I -- KHÔNG --> M[Trạng thái TỈNH TÁO - HUD Xanh lục bảo dịu mắt]
    M --> A
`

---

### Flow 3: Đăng ký Khuôn mặt Tài xế trên Driver Mobile App (Face Registration Flow)

`mermaid
sequenceDiagram
    autonumber
    participant Driver as Tài xế (Mobile App)
    participant Camera as Camera điện thoại
    participant AI as Face Embedding Engine
    participant Cloud as Fleet Backend API

    Driver->>Camera: Mở tab Quét Khuôn Mặt (Register Face)
    Camera-->>Driver: Hiển thị khung ngắm Oval + Hiệu ứng Laser quét
    Driver->>Camera: Căn chỉnh khuôn mặt chính diện góc 0°
    Camera->>AI: Trích xuất khuôn mặt chuẩn (đủ sáng, rõ nét)
    AI-->>Driver: Đếm mẫu 1/3 (Chính diện hoàn tất)
    Driver->>Camera: Xoay nhẹ sang trái/phải theo hướng dẫn
    AI-->>Driver: Đếm mẫu 3/3 (Đủ vector nhận diện)
    AI->>Cloud: POST /api/driver/register-face (128D Embeddings)
    Cloud-->>Driver: Thông báo Đăng ký FaceID thành công
`

---

### Flow 4: Điều phối Lịch chạy & Đồng bộ Kiểm soát Xe (Dispatcher & Fleet Assignment Flow)

`mermaid
flowchart LR
    A[Điều hành viên mở Tab Lịch Trình] --> B[Chọn Xe + Chọn Tuyến + Chọn Giờ]
    B --> C[Gán Tài xế đã đăng ký FaceID]
    C --> D[Lưu Lịch phân công vào Fleet DB]
    D --> E[Đồng bộ sang Driver Mobile App: 'Lịch Chạy Của Tôi']
    D --> F[Đồng bộ xuống In-Cabin Edge: Xác thực khi nổ máy]
`

---

### Flow 5: Gợi ý Trạm dừng chân & Xử lý Ngoại tuyến (Rest Stop & Offline Recovery Flow)

`mermaid
stateDiagram-v2
    [*] --> SafeRunning: Giám sát bình thường
    
    SafeRunning --> HighFatigue: Phát hiện 2 lần cảnh báo buồn ngủ trong 15 phút
    state HighFatigue {
        [*] --> QueryGPS: Lấy tọa độ GPS hiện tại
        QueryGPS --> NearestRestStop: Tìm trạm dừng/cây xăng gần nhất <= 50km
        NearestRestStop --> AudioVoiceGuidance: Loa phát: Gợi ý: Trạm dừng phía trước cách X km, bạn nên nghỉ ngơi
        AudioVoiceGuidance --> HUDStationBanner: HUD hiện thẻ chỉ dẫn trạm dừng
    }
    HighFatigue --> SafeRunning: Đã dừng xe nghỉ ngơi / Tài xế xác nhận
    
    SafeRunning --> OfflineNetwork: Mất kết nối 4G/WiFi vùng đèo núi
    state OfflineNetwork {
        [*] --> SQLiteBuffer: Lưu Snapshot + Toạ độ + Dữ liệu sự kiện cục bộ
        SQLiteBuffer --> AutoRetry: Kiểm tra kết nối định kỳ 30s
    }
    OfflineNetwork --> CloudSynced: Khôi phục kết nối mạng
    CloudSynced --> SafeRunning: Tự động đồng bộ toàn bộ sự kiện về Fleet Portal
`
