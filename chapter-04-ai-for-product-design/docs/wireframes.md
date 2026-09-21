# SleepAlert UI Wireframes & Layout Architecture

> **Provenance**
> - **Source prompt:** [P4.2 — Create Wireframes](../prompts/create-wireframe.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Approved HUD glanceability layout, typography scales, and Fleet portal density.
> - **Reproduction note:** Establishes structural wireframes prior to visual styling and interactive prototyping.

---

## 1. Không gian 1: In-Cabin Driver HUD (Màn hình Buồng lái Xe)

Màn hình đặt trên táp-lô hoặc tích hợp kính lái, tỷ lệ 16:9 hoặc 4:3, thiết kế chuẩn công thái học ban đêm (chống lóa mắt, chữ số siêu lớn, không có menu hay nút bấm phức tạp khi xe chạy).

### 1.1. Bố cục Tổng thể & Phân vùng (Zoning Matrix)

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ [ZONE A: HEADER STATUS]                                                   │
│ [Xe: VN-43A-9999]           [Trạng thái: BÌNH THƯỜNG]         [02:45 CHẠY]│
├───────────────────────────────────────────────────────────────────────────┤
│                                     │                                     │
│ [ZONE B: BIOMETRIC VISION FOCUS]    │ [ZONE C: REAL-TIME SAFETY GAUGES]   │
│                                     │                                     │
│         ┌─────────────────┐         │ TỈ LỆ MỞ MẮT (EAR):                 │
│         │   (O)     (O)   │         │ [████████████████░░░░] 0.32 (Mắt mở)│
│         │        |        │         │                                     │
│         │      \___/      │         │ MỆT MỎI TÍCH LŨY (PERCLOS 300f):    │
│         └─────────────────┘         │ [████░░░░░░░░░░░░░░░░] 8.5% (Tốt)   │
│       [KHUÔN MẶT ĐÃ KHÓA]           │                                     │
│                                     │ TƯ THẾ ĐẦU (PITCH):                 │
│                                     │ [-2.4° CHÍNH DIỆN]  [YAW: 0.8°]     │
│                                     │                                     │
├───────────────────────────────────────────────────────────────────────────┤
│ [ZONE D: SMART ACTION BANNER & NOTIFICATION]                              │
│  ⛽ Gợi ý: Trạm dừng chân Mai Linh cách 3.2 km phía trước (QL1A)          │
└───────────────────────────────────────────────────────────────────────────┘
```

---

### 1.2. Các trạng thái trực quan khẩn cấp của HUD

#### A. Trạng thái Hiệu chuẩn Mắt (Calibration State - 3.0 giây đầu)
```text
┌───────────────────────────────────────────────────────────────────────────┐
│                       ĐANG HIỆU CHUẨN KHUÔN MẶT                           │
│                   Vui lòng nhìn thẳng về phía trước                       │
│                                                                           │
│                      [██████████████░░░░░░] 2.1s / 3.0s                   │
│                                                                           │
│                 Đang xác lập ngưỡng mở mắt tự nhiên của bạn...            │
└───────────────────────────────────────────────────────────────────────────┘
```

#### B. Trạng thái Mệt mỏi / Cảnh báo Cấp 1 (Amber Warning State)
```text
┌───────────────────────────────────────────────────────────────────────────┐
│ ⚠️ CẢNH BÁO: PHÁT HIỆN DẤU HIỆU MỆT MỎI TÍCH LŨY (NGÁP LIÊN TỤC)          │
├───────────────────────────────────────────────────────────────────────────┤
│    [!] PERCLOS: 18.5% (Vượt ngưỡng an toàn 15%)                           │
│    Khuyến nghị: Mở hé cửa kính lấy gió tươi hoặc giảm tốc độ an toàn!     │
└───────────────────────────────────────────────────────────────────────────┘
```

#### C. Trạng thái Ngủ gật Nguy kịch / Báo động Cấp 2 (Critical Siren Strobe - RED FLASH)
```text
╔═══════════════════════════════════════════════════════════════════════════╗
║ 🚨🚨🚨 NGUY HIỂM! BÁO ĐỘNG NGỦ GẬT! TÀI XẾ MỞ MẮT NGAY! 🚨🚨🚨            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║                         [ ! ] MẮT ĐÃ NHẮM 1.8 GIÂY                        ║
║                         CÒI BÁO ĐỘNG ĐANG HÚ TỐI ĐA                       ║
║                                                                           ║
║                     [ ĐÃ TỰ ĐỘNG CHỤP ẢNH BẰNG CHỨNG ]                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Không gian 2: Central Fleet Safety Web Dashboard (Cổng Quản lý Đội xe)

Giao diện Web chuẩn desktop dành cho trung tâm điều hành vận tải quản lý đồng thời nhiều đầu xe.

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] SLEEPALERT FLEET COMMAND CENTER        [Tìm biển số xe...]   [Admin: Bích Trâm]  │
├──────────────┬──────────────────────────────────────────────────────────────────────────┤
│ [MENU]       │ [METRIC CARDS]                                                           │
│ 📊 Tổng quan │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐  │
│ 🚛 Đội xe    │ │ Xe Đang Chạy │ │ Cảnh báo Hôm │ │ Sự Kiện Đỏ   │ │ Tỷ Lệ An Toàn    │  │
│ 🚨 Vi phạm   │ │     28       │ │ nay: 14      │ │     02       │ │      96.8%       │  │
│ 🗺️ Bản đồ    │ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────────┘  │
│ 📑 Báo cáo   │                                                                          │
│ ⚙️ Cài đặt   │ [LIVE VEHICLE MONITORING TABLE]                                          │
│              │ ┌──────────┬─────────────┬──────────────┬────────────┬─────────┬───────┐│
│              │ │ Biển số  │ Tài xế      │ Trạng thái   │ PERCLOS    │ GPS     │ Thao  ││
│              │ ├──────────┼─────────────┼──────────────┼────────────┼─────────┼───────┤│
│              │ │ 43A-9999 │ Trần V. Hùng│ 🟢 Bình thường│  6.2%      │ QL1A-ĐN │ [Xem] ││
│              │ │ 43B-5678 │ Nguyễn V. An│ 🟡 Mệt mỏi   │ 19.4%      │ Quảng Nam│[Gọi] ││
│              │ │ 92A-8888 │ Lê Quốc Huy │ 🔴 BÁO ĐỘNG  │ 28.5% (Ngủ)│ Huế     │ [SOS] ││
│              │ │ 29B-1234 │ Hoàng G. Bảo│ ⚪ Mất sóng  │   --       │ Đèo Hải │[Check]││
│              │ └──────────┴─────────────┴──────────────┴────────────┴─────────┴───────┘│
│              │                                                                          │
│              │ [MODAL XEM LẠI BẰNG CHỨNG SNAPSHOT VI PHẠM (KHI CLICK)]                  │
│              │ ┌──────────────────────────────────────────────────────────────────────┐ │
│              │ │ Chi tiết sự kiện vi phạm: Xe 92A-8888 - Lúc 02:41:15 AM               │ │
│              │ │ ┌──────────────────────┐  Thông số đo:                               │ │
│              │ │ │                      │  • Thời gian nhắm mắt: 1.7 giây             │ │
│              │ │ │ [ẢNH CHỤP CAMERA IR] │  • EAR: 0.08  | PERCLOS: 28.5%              │ │
│              │ │ │                      │  • Tọa độ: 16.0544, 108.2022 (Đà Nẵng)      │ │
│              │ │ └──────────────────────┘  • Đã phát còi báo động: Thành công         │ │
│              │ │                            [Gửi cảnh báo tới phụ xe]   [Đóng]        │ │
│              │ └──────────────────────────────────────────────────────────────────────┘ │
└──────────────┴──────────────────────────────────────────────────────────────────────────┘
```
