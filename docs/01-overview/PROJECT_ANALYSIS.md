# PHÂN TÍCH DỰ ÁN & ĐẶC TẢ CHI TIẾT (PROJECT ANALYSIS)

## DỰ ÁN: SLEEPALERT
### Hệ thống giám sát và cảnh báo sớm tình trạng buồn ngủ, mất tập trung cho tài xế đường dài

---

## 1. PHÂN TÍCH PAIN POINTS & ĐỐI CHIẾU GIẢI PHÁP

### 1.1. Những hạn chế của các giải pháp hiện nay
Trên thị trường hiện có một số giải pháp cảnh báo buồn ngủ, tuy nhiên còn bộc lộ nhiều nhược điểm lớn:

| Phương pháp | Ưu điểm | Nhược điểm chí mạng (Pain Points) |
| :--- | :--- | :--- |
| **Thiết bị đeo (Smartwatch / Vòng đeo tay)** | Đo được nhịp tim, nhiệt độ cơ thể | Gây khó chịu khi đeo lái xe liên tục 8-10 tiếng; độ trễ cảnh báo lớn (nhịp tim chỉ biến đổi sau khi tài xế đã thực sự ngủ gật); dễ bị tháo bỏ. |
| **Cảm biến vô lăng / Lệch làn (ADAS)** | Đã được trang bị trên một số dòng xe sang | Chỉ kích hoạt khi xe đã chệch hướng hoặc bánh xe cán vạch $\rightarrow$ lúc này xe đã mất lái và có thể đâm vào dải phân cách hoặc xe ngược chiều. |
| **Camera AI dựa trên Cloud Streaming** | Lưu trữ toàn bộ video | Đòi hỏi băng thông 4G liên tục, chi phí truyền tải cao, **độ trễ lớn (> 2 - 3 giây)** không kịp cứu mạng tài xế; vi phạm nghiêm trọng quyền riêng tư của tài xế. |

### 1.2. Hướng tiếp cận vượt trội của SleepAlert
SleepAlert lựa chọn kiến trúc **In-Cabin Edge Computer Vision**:
1. **Phản xạ tức thời:** Phân tích trực tiếp chuyển động vi mô của mắt và góc nghiêng đầu tại chỗ $\rightarrow$ độ trễ phát hiện và cảnh báo $< 500$ms.
2. **Không xâm lấn (Non-intrusive):** Tài xế chỉ cần ngồi vào ghế lái bình thường, không cần đeo bất kỳ cảm biến nào trên cơ thể.
3. **Kết hợp chỉ số sinh học đa tầng:**
   $$\text{Mức độ rủi ro (Risk Score)} = f(\text{EAR}, \text{MAR}, \text{PERCLOS}, \text{Head Pose})$$
   Việc kết hợp này loại bỏ hiện tượng cảnh báo giả khi tài xế chỉ chớp mắt tự nhiên hoặc nói chuyện.

---

## 2. MA TRẬN USER STORIES & TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA)

Các User Stories được chuẩn hóa theo chuẩn Agile và diễn giải tiêu chí nghiệm thu bằng cú pháp **Gherkin (Given - When - Then)**.

### US-01: Tự động hiệu chuẩn ngưỡng mở mắt (Dynamic Eye Calibration)
* **Là một:** Tài xế xe khách bắt đầu ca làm việc,
* **Tôi muốn:** Hệ thống tự động quét và đo đạc kích thước mắt mở bình thường của tôi trong 3 giây đầu tiên,
* **Để:** Thiết lập ngưỡng cảnh báo cá nhân hóa chính xác, không bị cảnh báo nhầm nếu tôi có mắt một mí hoặc mắt nhỏ tự nhiên.

```gherkin
Scenario: Hiệu chuẩn thành công khi tài xế vào buồng lái
  Given Xe đã nổ máy và camera phát hiện rõ khuôn mặt tài xế
  When Tài xế nhìn thẳng vào kính lái trong 3 giây đầu tiên
  Then Hệ thống tính toán chỉ số EAR cơ sở (Baseline EAR) trung bình
  And Thiết lập ngưỡng nhắm mắt EAR_threshold = 0.75 * Baseline_EAR
  And Phát âm thanh thông báo "Đã hiệu chuẩn xong, chúc bạn thượng lộ bình an"
```

---

### US-02: Cảnh báo ngủ gật tức thời bằng còi báo động (Critical Drowsiness Alarm)
* **Là một:** Tài xế đang lái xe ban đêm,
* **Tôi muốn:** Nhận được còi báo động âm lượng lớn ngay khi mắt tôi nhắm liên tục quá 1.5 giây,
* **Để:** Tôi giật mình tỉnh táo ngay lập tức và mở mắt điều khiển xe an toàn.

```gherkin
Scenario: Kích hoạt báo động khẩn cấp khi mắt nhắm quá 1.5 giây
  Given Tài xế đang điều khiển phương tiện trên đường
  When Tỉ lệ mở mắt EAR < EAR_threshold kéo dài liên tục >= 1.5 giây
  Then Hệ thống kích hoạt còi báo động khẩn cấp (Siren Sound) với âm lượng tối đa
  And Chụp lại ảnh vi phạm lưu vào thư mục snapshots kèm thông số EAR và thời gian
  And Còi chỉ ngắt khi tài xế mở mắt trở lại trong ít nhất 0.5 giây
```

---

### US-03: Nhắc nhở mệt mỏi sớm dựa trên PERCLOS và Ngáp (Fatigue Pre-warning)
* **Là một:** Tài xế chạy đường dài,
* **Tôi muốn:** Hệ thống phát lời nhắc nhở nhẹ nhàng khi tôi ngáp nhiều hoặc tần suất nhắm mắt tăng cao (PERCLOS $\ge 0.18$),
* **Để:** Tôi nhận thức được thể trạng của mình và chủ động điều chỉnh tốc độ hoặc bật nhạc/mở cửa sổ.

```gherkin
Scenario: Nhắc nhở khi ngáp liên tục hoặc mệt mỏi tích lũy
  Given Tài xế đã lái xe liên tục hơn 2 tiếng
  When Chỉ số PERCLOS trong 300 frames vượt ngưỡng 0.18 hoặc MAR > 0.6 liên tục trong 3 lần
  Then Hệ thống phát âm thanh nhắc nhở bằng giọng nói tiếng Việt nhẹ nhàng
  And Ghi nhận trạng thái "Mệt mỏi tích lũy" vào nhật ký hành trình
```

---

### US-04: Gợi ý trạm dừng chân gần nhất theo tọa độ thực tế (Smart Rest-stop Recommendation)
* **Là một:** Tài xế đang cảm thấy kiệt sức,
* **Tôi muốn:** Hệ thống tự động tra cứu và đọc tên trạm dừng nghỉ an toàn gần nhất,
* **Để:** Tôi biết chính xác còn bao xa nữa thì có chỗ dừng đỗ nghỉ ngơi hợp pháp.

```gherkin
Scenario: Tra cứu và phát âm thanh trạm dừng chân
  Given Mức độ mệt mỏi của tài xế đạt cấp độ cần dừng nghỉ
  When Dịch vụ định vị xác định được tọa độ GPS hiện tại của xe
  Then Hệ thống tìm kiếm trạm dừng nghỉ / cây xăng gần nhất trên bản đồ
  And Phát giọng nói: "Gợi ý: Trạm dừng chân [Tên trạm] cách khoảng [X] km phía trước"
```

---

### US-05: Quản trị viên theo dõi trạng thái đội xe từ xa (Fleet Monitoring Portal)
* **Là một:** Người quản lý điều hành đội xe,
* **Tôi muốn:** Theo dõi trực quan danh sách các xe đang chạy và các sự kiện cảnh báo buồn ngủ trong ca,
* **Để:** Kịp thời liên hệ nhắc nhở tài xế hoặc bố trí phụ xe đổi lái nếu cần thiết.

```gherkin
Scenario: Đồng bộ và hiển thị sự kiện vi phạm trên Web Dashboard
  Given Thiết bị Edge trên xe có kết nối mạng Internet (4G/WiFi)
  When Một sự kiện cảnh báo cấp độ 2 (ngủ gật) được ghi nhận trên xe
  Then Dữ liệu sự kiện kèm ảnh snapshot được gửi bất đồng bộ qua API về Central Server
  And Dashboard của Quản trị viên cập nhật trạng thái xe và phát chuông cảnh báo đỏ
```
