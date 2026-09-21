# SleepAlert User Flows & Interaction State Specification

> **Provenance**
> - **Source prompt:** [P4.1 — Create User Flows](../prompts/create-user-flow.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Approved primary flows, alert escalation transitions, and fail-safe recovery paths.
> - **Reproduction note:** Maps requirements from Chapter 3 into observable interactive user journeys.

---

## 1. Overview of System Actors & Environments

SleepAlert operates across two distinct user environments:
1. **In-Cabin Driver Environment (Primary Real-time Actor):** Completely hands-free, glance-based visual feedback ($\le 1$ second glance), with primary reliance on acoustic warnings.
2. **Central Fleet Safety Management Environment (Secondary Administrative Actor):** Desktop/tablet browser interface, managing real-time vehicle fleets, monitoring incident logs, and triaging safety violations.

---

## 2. Core User Flows

### Flow 1: Khởi động Xe & Tự động Hiệu chuẩn Mắt (Ignition & 3-Second Calibration)

```mermaid
stateDiagram-v2
    [*] --> SystemBoot: Bật khóa điện xe (Ignition ON)
    SystemBoot --> FaceSearching: Khởi động Camera hồng ngoại / RGB
    
    state FaceSearching {
        [*] --> Scanning
        Scanning --> FaceDetected: MediaPipe bắt được 468 điểm khuôn mặt
        Scanning --> Scanning: Chưa thấy mặt (Quét tiếp)
    }
    
    FaceDetected --> Calibrating: Tài xế nhìn thẳng kính lái
    
    state Calibrating {
        [*] --> CollectingEAR: Lấy mẫu EAR liên tục trong 3.0s
        CollectingEAR --> ComputeMedian: Tính toán Median EAR_base
        ComputeMedian --> SetThreshold: EAR_thresh = 0.75 * EAR_base
    }
    
    SetThreshold --> ActiveMonitoring: Phát giọng nói "Hiệu chuẩn thành công"
    ActiveMonitoring --> [*]
```

* **Step-by-step Execution:**
  1. Xe nổ máy, thiết bị Edge tự động khởi động dịch vụ trong vòng 5 giây.
  2. Camera hiển thị khung ngắm khuôn mặt trên HUD với trạng thái `ĐANG TÌM KHUÔN MẶT` (Vàng nhạt).
  3. Khi tài xế ngồi vào ghế lái và nhìn về phía trước, hệ thống kích hoạt thanh tiến trình hiệu chuẩn 3.0 giây.
  4. Hệ thống thu thập chuỗi giá trị EAR, loại bỏ nhiễu ngoại lai, xác định ngưỡng mắt mở tự nhiên của riêng tài xế đó ($EAR_{base}$).
  5. Ngưỡng cảnh báo nhắm mắt $EAR_{thresh}$ được chốt tại $75\%$ của $EAR_{base}$. Loa phát âm báo ngắn xác nhận hệ thống sẵn sàng bảo vệ.

---

### Flow 2: Giám sát Trạng thái & Thang Cảnh báo Đa tầng (Continuous Monitoring & Multi-Stage Alert)

```mermaid
flowchart TD
    A[Khung hình Camera mới] --> B[Trích xuất EAR, MAR, Head Pose]
    B --> C{Mắt nhắm liên tục >= 1.5s HOẶC PERCLOS >= 0.25?}
    
    C -- CÓ (NGUY HIỂM CẤP 2) --> D[KÍCH HOẠT CÒI BÁO ĐỘNG SIREN]
    D --> E[HUD chớp đỏ toàn màn hình]
    D --> F[Chụp ảnh Snapshot + Ghi log vi phạm]
    D --> G{Tài xế mở mắt lại >= 0.5s?}
    G -- CHƯA --> D
    G -- ĐÃ MỞ MẮT --> H[Tắt còi báo động & Reset bộ đếm]
    H --> A
    
    C -- KHÔNG --> I{PERCLOS >= 0.15 HOẶC Ngáp >= 20 frames?}
    I -- CÓ (CẢNH BÁO CẤP 1) --> J[Phát âm chuông nhẹ / Voice nhắc nhở]
    J --> K[HUD hiển thị viền Hổ phách Amber]
    J --> L[Ghi nhận vào log mệt mỏi tích lũy]
    L --> A
    
    I -- KHÔNG --> M[Trạng thái TỈNH TÁO - HUD Xanh lá dịu]
    M --> A
```

* **Quy tắc chuyển trạng thái:**
  * **Xanh lá (Normal):** Tài xế tỉnh táo, mắt mở bình thường, HUD hiển thị thông số gọn gàng không gây phân tâm.
  * **Hổ phách (Level 1 Warning):** Phát hiện ngáp liên tục hoặc mệt mỏi tích lũy $\rightarrow$ Nhắc nhở âm thanh dịu để tài xế chủ động điều chỉnh.
  * **Đỏ nhấp nháy (Level 2 Critical Siren):** Mắt nhắm $\ge 1.5$s (Microsleep) $\rightarrow$ Còi hú cường độ lớn tức thì $< 500$ms, còi chỉ tắt khi tài xế mở mắt dứt khoát.

---

### Flow 3: Cảnh báo Gục đầu & Mất tập trung (Head Down & Distraction Flow)

```mermaid
sequenceDiagram
    autonumber
    participant Camera as Camera Module
    participant Pose as Head Pose Engine
    participant Alert as Audio Alert Queue
    participant HUD as In-Cabin HUD
    participant Driver as Tài xế

    Camera->>Pose: Gửi tọa độ 3D Facial Landmarks
    Pose->>Pose: Tính toán góc Pitch (Gật/Cúi)
    Note over Pose: Phát hiện Pitch < -20° (Đang cúi gục đầu)
    Pose->>Pose: Bắt đầu đếm thời gian gục đầu
    alt Gục đầu < 2.0 giây
        Pose-->>HUD: Hiển thị icon cảnh báo tư thế đầu
    else Gục đầu liên tục >= 2.0 giây
        Pose->>Alert: Đẩy sự kiện LEVEL 3 HEAD_DOWN
        Alert->>Driver: Phát âm thanh: "Vui lòng ngẩng cao đầu quan sát!"
        Pose->>HUD: Chớp viền vàng cam + Cảnh báo chú ý kính lái
        Driver->>Camera: Ngẩng đầu về vị trí bình thường (Pitch > -10°)
        Pose->>Alert: Hủy cảnh báo âm thanh
        HUD-->>Driver: Trở lại trạng thái bình thường
    end
```

---

### Flow 4: Gợi ý Trạm dừng chân Thông minh (Location-aware Rest Stop)

```mermaid
flowchart TD
    A[Phát hiện 2 lần cảnh báo Mệt mỏi/Buồn ngủ trong 15 phút] --> B[Kích hoạt Location Service]
    B --> C{Có tín hiệu GPS / Bản đồ?}
    
    C -- CÓ --> D[Tìm kiếm trạm dừng nghỉ / cây xăng gần nhất <= 50km]
    D --> E[Lấy tên trạm & khoảng cách km]
    E --> F[Loa phát giọng nói tiếng Việt:]
    F --> G["Gợi ý: Trạm dừng [Tên trạm] cách [X] km phía trước, bạn nên ghé nghỉ ngơi"]
    G --> H[HUD hiển thị thẻ hướng dẫn trạm dừng kèm khoảng cách]
    
    C -- MẤT SÓNG / KHÔNG TÌM THẤY --> I[Phát nhắc nhở an toàn cơ bản:]
    I --> J["Bạn đã lái xe mệt mỏi, vui lòng tấp vào lề an toàn để nghỉ ngơi"]
```

---

### Flow 5: Xử lý Sự cố & Hoạt động Ngoại tuyến (Fail-Safe & Offline Recovery Flow)

```mermaid
stateDiagram-v2
    [*] --> Tracking: Đang giám sát bình thường
    
    Tracking --> FaceLost: Không tìm thấy mặt > 3.0s (Che camera / Rời ghế)
    state FaceLost {
        [*] --> AudioPing: Kêu chuông "Ping Ping" nhắc nhở
        AudioPing --> DisplayWarning: HUD hiện "KHÔNG TÌM THẤY KHUÔN MẶT"
        DisplayWarning --> AutoRecover: Tài xế ngồi lại đúng vị trí
    }
    FaceLost --> Tracking: Khôi phục khuôn mặt (< 1 giây)
    
    Tracking --> OfflineMode: Xe đi vào vùng mất sóng 4G/WiFi
    state OfflineMode {
        [*] --> LocalQueue: Lưu sự kiện & Snapshot vào SQLite cục bộ
        LocalQueue --> NetworkPolling: Kiểm tra kết nối định kỳ 30s
    }
    OfflineMode --> SyncCompleted: Có sóng 4G/WiFi trở lại
    SyncCompleted --> Tracking: Đồng bộ toàn bộ sự kiện tồn đọng lên Fleet Server
```
