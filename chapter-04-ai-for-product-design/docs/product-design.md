# SleepAlert Master Product Design Specification

> **Provenance**
> - **Source prompt:** [P4.3 — Create Prototype](../prompts/create-prototype.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Approved design system tokens, night-mode color palette, and audio-visual alert salience.
> - **Reproduction note:** Governs all visual and interaction implementation across Edge HUD and Fleet Cloud.

---

## 1. Triết lý Thiết kế Công thái học Buồng lái (Automotive In-Cabin Ergonomics)

Đối với hệ thống an toàn xe hơi và xe tải, sai lầm lớn nhất của các UI thông thường là thiết kế quá nhiều chi tiết, màu sắc sặc sỡ và hiệu ứng chuyển động liên tục gây phân tâm cho người điều khiển phương tiện. SleepAlert tuân thủ **3 nguyên tắc vàng**:

1. **Quy tắc Liếc mắt 1 giây (1-Second Glanceability Rule):** Tài xế chỉ cần liếc mắt dưới 1.0 giây là nắm được trọn vẹn trạng thái an toàn của mình. Toàn bộ thông tin chính được biểu thị qua màu sắc viền màn hình (Xanh / Hổ phách / Đỏ) và chữ số lớn.
2. **Công thái học Lái xe Ban đêm (Night-Drive Pupil Protection):**
   - Nền màn hình là màu đen tuyền (`#0A0D14` / True Black OLED) giúp hạn chế tối đa ánh sáng phát xạ vào khoang lái.
   - Tránh tuyệt đối màu xanh dương sáng (Blue Light) vì bước sóng xanh gây ức chế melatonin và làm co đồng tử, khiến mắt tài xế bị "mù tạm thời" khi nhìn ra bóng tối của mặt đường.
   - Màu cảnh báo chủ đạo là **Hổ phách (Amber `#F59E0B`)** cho mức độ chú ý và **Đỏ thẫm (Crimson `#EF4444`)** cho mức độ nguy cấp.
3. **Ưu tiên Âm thanh trước Hình ảnh (Acoustic Dominance):**
   - Khi tài xế đã nhắm mắt ngủ gật, mọi thông điệp trên màn hình đều vô nghĩa. Còi báo động âm thanh cường độ lớn (> 85dB) và giọng nói tiếng Việt phải là kênh tác động chính để đánh thức não bộ.

---

## 2. Hệ thống Định danh Màu sắc & Tokens (Design Tokens)

```text
┌──────────────────┬─────────────┬────────────────────────────────────────────────────────┐
│ Tên Token        │ Mã Hex      │ Mục đích & Ý nghĩa tâm lý                              │
├──────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ --surface-deep   │ #0B0F19     │ Nền màn hình buồng lái ban đêm, hấp thụ ánh sáng thừa  │
│ --surface-card   │ #161F30     │ Bề mặt thẻ chỉ số, có viền mảnh phân tách             │
│ --border-subtle  │ #25334D     │ Viền ngăn cách khu vực, độ tương phản vừa đủ           │
│ --status-safe    │ #10B981     │ Xanh lục bảo dịu mắt: Hệ thống hoạt động tốt, tỉnh táo │
│ --status-warn    │ #F59E0B     │ Hổ phách: Mệt mỏi tích lũy, ngáp, cần chú ý           │
│ --status-danger  │ #EF4444     │ Đỏ khẩn cấp: Ngủ gật microsleep, còi báo động          │
│ --text-primary   │ #F8FAFC     │ Trắng sáng tự nhiên, hiển thị thông số chính           │
│ --text-muted     │ #94A3B8     │ Xám trung tính, dành cho nhãn phụ và đơn vị đo         │
└──────────────────┴─────────────┴────────────────────────────────────────────────────────┘
```

---

## 3. Thang Đo Typography & Kích thước Chữ số

* **Chỉ số Trạng thái Chính (EAR / PERCLOS):** Font `Inter` / `Roboto Mono`, kích thước `36px` - `48px`, font-weight `Bold (700)`, dễ đọc ở khoảng cách 70cm - 1m từ ghế lái.
* **Tiêu đề Thông báo & Khuyến nghị:** Kích thước `20px` - `24px`, font-weight `Semi-Bold (600)`.
* **Nhãn thông số phụ:** Kích thước `14px`, text uppercase nhẹ nhàng.

---

## 4. Hệ thống Tín hiệu Âm thanh (Acoustic Cue Hierarchy)

```text
┌───────────────┬────────────────────────────┬─────────────────────────────┬─────────────┐
│ Cấp độ        │ Âm thanh kích hoạt         │ Cường độ âm thanh           │ Tần suất    │
├───────────────┼────────────────────────────┼─────────────────────────────┼─────────────┤
│ Level 0       │ Tiếng "Chime" êm dịu 0.5s  │ 55 dB (Nhẹ nhàng)           │ 1 lần khi   │
│ (Khởi động)   │ khi hiệu chuẩn xong        │                             │ nổ máy      │
├───────────────┼────────────────────────────┼─────────────────────────────┼─────────────┤
│ Level 1       │ Chuông báo 2 nhịp + Voice  │ 68 dB (Rõ ràng, không giật  │ Cách nhau   │
│ (Mệt mỏi)     │ "Vui lòng tập trung lái xe"│ mình)                       │ tối thiểu 20s│
├───────────────┼────────────────────────────┼─────────────────────────────┼─────────────┤
│ Level 2       │ Còi hú đa tần (Siren pulse)│ 85 - 90 dB (Cực lớn, kích   │ Liên tục    │
│ (Ngủ gật)     │ liên tục không ngừng       │ thích hệ thần kinh giao cảm)│ đến khi mở  │
├───────────────┼────────────────────────────┼─────────────────────────────┼─────────────┤
│ Level 3       │ Voice tiếng Việt hướng dẫn │ 72 dB (Rõ ràng, mạch lạc)   │ 1 lần khi   │
│ (Trạm nghỉ)   │ địa điểm trạm dừng gần nhất│                             │ cần nghỉ    │
└───────────────┴────────────────────────────┴─────────────────────────────┴─────────────┘
```

---

## 5. Bản quyền & Tính kế thừa
Tài liệu thiết kế này là tiêu chuẩn tương tác độc quyền cho dự án SleepAlert, đảm bảo sự nhất quán từ bản mẫu nguyên mẫu đến code triển khai thực tế trên phần cứng nhúng.
