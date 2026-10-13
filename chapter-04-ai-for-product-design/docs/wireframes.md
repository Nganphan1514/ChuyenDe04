# SleepAlert UI Wireframes & Layout Architecture

> **Provenance**
> - **Source prompt:** [P4.2 — Create Wireframes](../prompts/create-wireframe.prompt.md)
> - **Artifact status:** Accepted reviewed sample
> - **Human action:** Approved HUD glanceability layout, Fleet Portal 5-module hierarchy, and Driver Mobile ergonomics.
> - **Reproduction note:** Establishes comprehensive wireframes across In-Cabin HUD, Desktop Fleet Portal, and Mobile Driver App.

---

## 1. Phân hệ 1: In-Cabin Driver HUD (Buồng lái Giám sát Sinh trắc học)

Màn hình đặt ngang trên táp-lô hoặc kính lái, tỷ lệ 16:9 / 4:3, thiết kế ban đêm chống chói, chữ số cỡ lớn, không có thao tác cảm ứng khi đang di chuyển.

### 1.1. Bố cục Phân vùng Buồng lái (Zoning Matrix)

`	ext
┌───────────────────────────────────────────────────────────────────────────┐
│ [ZONE A: VEHICLE & DRIVER AUTH BAR]                                       │
│ [Xe: 43A-9999 (Xe Tải 15T)]    [Tài xế: Trần Văn Hùng (HỢP LỆ)]  [02:45 CHẠY]│
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
│ [ZONE D: SMART ACTION BANNER & LOCATION NOTIFICATION]                     │
│  [Trạm Dừng] Gợi ý: Trạm dừng chân Mai Linh cách 3.2 km phía trước (QL1A) │
└───────────────────────────────────────────────────────────────────────────┘
`

### 1.2. Trạng thái Báo động Cấp 2 (Critical Siren Strobe - RED FLASH)

`	ext
╔═══════════════════════════════════════════════════════════════════════════╗
║ 🚨🚨🚨 NGUY HIỂM! BÁO ĐỘNG NGỦ GẬT! TÀI XẾ MỞ MẮT NGAY! 🚨🚨🚨            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║                         [ ! ] MẮT ĐÃ NHẮM 1.8 GIÂY                        ║
║                         CÒI BÁO ĐỘNG ĐANG HÚ TỐI ĐA                       ║
║                                                                           ║
║                     [ ĐÃ TỰ ĐỘNG CHỤP ẢNH BẰNG CHỨNG ]                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
`

---

## 2. Phân hệ 2: Central Fleet Management Web Portal (Cổng Điều hành 5 Phân hệ)

Giao diện Web chuẩn desktop dành cho trung tâm điều hành vận tải quản lý đồng thời toàn bộ phương tiện, tài xế và lịch trình.

### 2.1. Phân hệ A: Live Fleet Dashboard & Modal Xem Bằng chứng Snapshot

`	ext
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] SLEEPALERT FLEET COMMAND CENTER        [Tìm biển số xe...]   [Admin: Bích Trâm]  │
├──────────────┬──────────────────────────────────────────────────────────────────────────┤
│ [MENU]       │ [METRIC CARDS]                                                           │
│ 📊 Tổng quan │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐  │
│ 🚛 Đội xe    │ │ Xe Đang Chạy │ │ Cảnh báo Hôm │ │ Sự Kiện Đỏ   │ │ Tỷ Lệ An Toàn    │  │
│ 👨 Tài xế    │ │     28       │ │ nay: 14      │ │     02       │ │      96.8%       │  │
│ 📅 Lịch trình│ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────────┘  │
│ 📈 Thống kê  │                                                                          │
│ 📑 Báo cáo   │ [LIVE VEHICLE MONITORING TABLE]                                          │
│              │ ┌──────────┬─────────────┬──────────────┬────────────┬─────────┬───────┐│
│              │ │ Biển số  │ Tài xế      │ Trạng thái   │ PERCLOS    │ GPS     │ Thao  ││
│              │ ├──────────┼─────────────┼──────────────┼────────────┼─────────┼───────┤│
│              │ │ 43A-9999 │ Trần V. Hùng│ 🟢 Bình thường│  6.2%      │ QL1A-ĐN │ [Xem] ││
│              │ │ 43B-5678 │ Nguyễn V. An│ 🟡 Mệt mỏi   │ 19.4%      │ Quảng Nam│[Gọi] ││
│              │ │ 92A-8888 │ Lê Quốc Huy │ 🔴 BÁO ĐỘNG  │ 28.5% (Ngủ)│ Huế     │ [SOS] ││
│              │ └──────────┴─────────────┴──────────────┴────────────┴─────────┴───────┘│
│              │                                                                          │
│              │ [MODAL XEM LẠI BẰNG CHỨNG SNAPSHOT VI PHẠM (KHI CLICK VÀO RECORD ĐỎ)]    │
│              │ ┌──────────────────────────────────────────────────────────────────────┐ │
│              │ │ Chi tiết sự kiện vi phạm: Xe 92A-8888 - Lúc 02:41:15 AM               │ │
│              │ │ ┌──────────────────────┐  Thông số đo:                               │ │
│              │ │ │                      │  • Thời gian nhắm mắt: 1.7 giây             │ │
│              │ │ │ [ẢNH CHỤP CAMERA IR] │  • EAR: 0.08  | PERCLOS: 28.5%              │ │
│              │ │ │                      │  • Tọa độ: 16.0544, 108.2022 (Đà Nẵng)      │ │
│              │ │ └──────────────────────┘  • Đã phát còi báo động: Thành công         │ │
│              │ │                            [Gửi cảnh báo phụ xe]       [Đóng]        │ │
│              │ └──────────────────────────────────────────────────────────────────────┘ │
└──────────────┴──────────────────────────────────────────────────────────────────────────┘
`

### 2.2. Phân hệ B, C, D: Quản lý Xe, Quản lý Tài xế, Lịch trình & Thống kê Giờ Đỏ (0h - 4h)

`	ext
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ TAB ĐIỀU PHỐI LỊCH CHẠY (SCHEDULER):                                                    │
│ [Tạo Ca Mới] [Chọn Xe: 43A-9999] [Chọn Tài Xế: Trần Văn Hùng] [Tuyến: ĐN -> SG] [LƯU]  │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ TAB PHÂN TÍCH TẬP TRUNG VI PHẠM THEO KHUNG GIỜ (0h - 4h sáng):                          │
│ 00h-02h: [██████████████████████] 42% (Khung giờ đỉnh điểm tài xế sụp mí)               │
│ 02h-04h: [██████████████████]     35% (Nguy cơ vi giấc ngủ sâu microsleep)              │
│ 04h-06h: [██████]                 12%                                                   │
└─────────────────────────────────────────────────────────────────────────────────────────┘
`

---

## 3. Phân hệ 3: Driver Mobile App (Ứng dụng Di động Dành cho Tài xế)

Bố cục Smartphone chiều dọc (Mobile Native 9:16), điều hướng bằng **Bottom Navigation Bar** 5 biểu tượng:

`	ext
┌────────────────────────────────────────┐
│ [STATUS BAR: 09:41  |  LTE  |  100%]   │
├────────────────────────────────────────┤
│ XIN CHÀO TÀI XẾ: TRẦN VĂN HÙNG         │
│ Bằng lái: Hạng FC | Điểm an toàn: 94/100│
├────────────────────────────────────────┤
│                                        │
│ [TAB REGISTER FACE: QUÉT KHUÔN MẶT AI] │
│                                        │
│         ┌────────────────────┐         │
│         │   \     O    O   / │         │
│         │    |       |    |  │         │
│         │====|=====[LASER]=|==│ (Quét)  │
│         │    |     \___/  |  │         │
│         │   /              \ │         │
│         └────────────────────┘         │
│     [Trạng thái: Thu thập mẫu 3/3]     │
│  [Xoay nhẹ khuôn mặt sang trái/phải]   │
│                                        │
├────────────────────────────────────────┤
│ [TAB LỊCH CHẠY: MY UPCOMING SCHEDULES] │
│ • Ca hôm nay: 22:00 - Đà Nẵng -> TP.HCM│
│ • Xe phân công: 43A-9999 (Container)   │
│ • Trạng thái: ĐÃ KHỚP FACEID TRÊN XE   │
├────────────────────────────────────────┤
│ [TAB VI PHẠM: MY INCIDENT HISTORY]     │
│ • 02:15 - Cảnh báo ngáp (Mức 1)        │
│ • 23:40 - Ngắt quãng tư thế cúi đầu    │
├────────────────────────────────────────┤
│ [BOTTOM NAVIGATION]                    │
│ [📊 Home] [📅 Lịch] [👤 Scan Mặt] [🚨 Log]│
└────────────────────────────────────────┘
`
