# TÀI LIỆU YÊU CẦU SẢN PHẨM (PRODUCT REQUIREMENTS DOCUMENT - PRD)

## DỰ ÁN: SLEEPALERT
### Hệ thống giám sát và cảnh báo sớm tình trạng buồn ngủ, mất tập trung cho tài xế đường dài
**Mã học phần:** CS2028 - Chuyên đề 4: Phát triển sản phẩm AI từ đầu đến cuối  
**Phiên bản:** 1.0.0  
**Trạng thái:** Approved / Baseline Architecture  
**Ngày phê duyệt:** 08/09/2026  

---

## 1. TỔNG QUAN SẢN PHẨM & TẦM NHÌN (PRODUCT OVERVIEW & VISION)

### 1.1. Bối cảnh & Tầm nhìn sản phẩm (Vision Statement)
Theo số liệu của Ủy ban An toàn Giao thông Quốc gia và Tổ chức Y tế Thế giới (WHO), mệt mỏi và ngủ gật khi lái xe (đặc biệt là tài xế xe tải hạng nặng, xe container và xe khách chạy tuyến đêm) là một trong những nguyên nhân hàng đầu gây ra các vụ tai nạn thảm khốc với thiệt hại nghiêm trọng về người và tài sản. Hiện tượng này thường diễn ra âm thầm thông qua các vi giấc ngủ (microsleeps - những khoảng thời gian nhắm mắt từ 1 đến 3 giây) mà chính tài xế cũng không nhận biết kịp thời.

**SleepAlert** được định vị là **hệ thống an toàn chủ động (Active Safety System)** kết hợp Thị giác máy tính biên (Edge Computer Vision), đo lường chỉ số sinh học đa kênh (Multi-metric Biological Fusion) và Hệ thống cảnh báo âm thanh thích ứng (Adaptive Audio Warning). Mục tiêu tối thượng của SleepAlert là:
1. **Phát hiện trước khi quá muộn:** Nhận diện các dấu hiệu mệt mỏi sớm (ngáp, chớp mắt chậm, gục đầu nhẹ, PERCLOS tăng) trước khi tài xế rơi vào trạng thái ngủ sâu mất kiểm soát.
2. **Cảnh báo tức thời tại chỗ (< 500ms):** Kích hoạt âm thanh/giọng nói cảnh báo ngay lập tức trong cabin, hoàn toàn độc lập với kết nối Internet.
3. **Bảo vệ toàn vẹn dữ liệu cá nhân (Privacy-by-Design):** Xử lý luồng hình ảnh tại biên (In-cabin Edge Unit), tuyệt đối không truyền video trực tiếp lên máy chủ đám mây, chỉ gửi siêu dữ liệu sự kiện cảnh báo và ảnh chụp bằng chứng khi xảy ra vi phạm nguy hiểm.

### 1.2. Mục tiêu chiến lược (Strategic Goals)
* **Chính xác & Khách quan:** Giảm thiểu tỷ lệ cảnh báo sai (False Positives) thông qua thuật toán chuẩn hóa ngưỡng mở mắt thích ứng theo từng cá nhân (Dynamic Calibration) và chỉ số PERCLOS 300 frames.
* **Hoạt động liên tục:** Duy trì khả năng phát hiện ổn định trong điều kiện ánh sáng thay đổi (ban ngày ngược sáng, ban đêm dùng camera hồng ngoại IR).
* **Quản trị an toàn đội xe:** Cung cấp thông tin cảnh báo sớm cho trung tâm điều hành vận tải để có biện pháp can thiệp, điều chuyển tài xế khi cần thiết.

---

## 2. ĐỐI TƯỢNG NGƯỜI DÙNG & USER PERSONAS

### 2.1. Persona 1: Tài xế xe khách đường dài (Primary End-User)
* **Họ tên:** Trần Văn Hùng (42 tuổi)
* **Nghề nghiệp:** Tài xế xe khách giường nằm tuyến Bắc - Nam (Hà Nội - Đà Nẵng).
* **Đặc điểm & Thói quen:** Thường xuyên lái xe vào khung giờ nguy hiểm (23h00 - 04h00 sáng), mắt dễ mỏi khi nhìn đèn pha đối diện, có thói quen uống cà phê hoặc tăng lực nhưng vẫn có nguy cơ bị rơi vào trạng thái vi giấc ngủ (microsleep).
* **Kỳ vọng:** Cần một thiết bị cảnh báo nhanh, âm thanh đủ lớn để tỉnh táo ngay khi vừa nhắm mắt quá lâu, nhưng không kêu inh ỏi gây ức chế khi chỉ chớp mắt bình thường. Hệ thống có thể nhắc nhở trạm dừng chân gần nhất để nghỉ ngơi hợp lý.

### 2.2. Persona 2: Người quản lý an toàn đội xe (Fleet Safety Manager)
* **Họ tên:** Lê Thị Bích Trâm (35 tuổi)
* **Nghề nghiệp:** Trưởng phòng Điều hành An toàn tại Hãng xe liên tỉnh.
* **Đặc điểm & Nhu cầu:** Cần giám sát trạng thái an toàn của 30 đầu xe chạy ban đêm trên cả nước; muốn biết tài xế nào thường xuyên có dấu hiệu buồn ngủ để nhắc nhở, đổi ca hoặc bố trí thời gian nghỉ ngơi khoa học.
* **Kỳ vọng:** Bảng điều khiển (Dashboard) thời gian thực hiển thị danh sách xe đang chạy, số lần cảnh báo trong ca, xem được ảnh bằng chứng chụp lại khoảnh khắc tài xế ngủ gật, và xuất báo cáo thống kê định kỳ.

---

## 3. YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - FR)

Hệ thống SleepAlert bao gồm 5 nhóm yêu cầu chức năng cốt lõi:

### FR-01: Phát hiện trạng thái khuôn mặt & Đo lường chỉ số sinh học thời gian thực
* **FR-01.1 (Tỉ lệ mở mắt - EAR):** Hệ thống phải liên tục trích xuất 6 điểm mốc mí mắt trái và 6 điểm mốc mí mắt phải từ MediaPipe Face Mesh, tính toán chỉ số EAR cho từng khung hình.
* **FR-01.2 (Tỉ lệ mở miệng - MAR):** Tính toán khoảng cách giữa các điểm mốc môi trong và môi ngoài để phát hiện tần suất và thời lượng ngáp.
* **FR-01.3 (Chỉ số PERCLOS):** Duy trì cửa sổ trượt 300 khung hình (~10 giây ở 30 FPS). Hệ thống phải tính tỷ lệ phần trăm khung hình mà mắt nhắm ($EAR < EAR_{threshold}$) trên tổng số 300 khung hình.
* **FR-01.4 (Tư thế đầu - Head Pose):** Áp dụng thuật toán PnP để tính góc cúi đầu (Pitch) và quay đầu (Yaw), xác định xem tài xế có đang gục đầu xuống vô lăng hoặc quay đầu không chú ý mặt đường hay không.
* **FR-01.5 (Tự động hiệu chuẩn - Calibration):** Trong 3 giây đầu tiên khi nhận diện khuôn mặt tài xế, hệ thống tự động đo EAR trung bình khi mắt mở bình thường để thiết lập ngưỡng cá nhân hóa.

### FR-02: Cơ chế cảnh báo âm thanh đa cấp độ (Multi-stage Active Alert)
* **FR-02.1 (Cấp độ 1 - Nhắc nhở mệt mỏi sớm):** Khi tài xế ngáp liên tục hoặc $0.15 \le PERCLOS < 0.25$, hệ thống phát chuông thông báo nhẹ hoặc giọng nói tiếng Việt ngắn nhắc nhở tài xế tập trung.
* **FR-02.2 (Cấp độ 2 - Báo động ngủ gật nguy kịch):** Khi mắt nhắm liên tục quá 1.5 giây ($EAR < Threshold$) hoặc $PERCLOS \ge 0.25$, hệ thống ngay lập tức kích hoạt còi báo động âm lượng cao (siren alarm) kéo dài đến khi tài xế mở mắt.
* **FR-02.3 (Cấp độ 3 - Cảnh báo gục đầu / Mất tập trung):** Khi góc cúi đầu $Pitch < -20^{\circ}$ kéo dài quá 2 giây, phát âm thanh cảnh báo ngẩng cao đầu quan sát.

### FR-03: Gợi ý trạm dừng chân an toàn theo vị trí (Location-aware Rest Stop)
* **FR-03.1:** Khi phát hiện tài xế liên tục có dấu hiệu buồn ngủ vượt ngưỡng an toàn trong vòng 15 phút, hệ thống tự động kích hoạt dịch vụ định vị (Location Service).
* **FR-03.2:** Tra cứu trạm dừng chân, cây xăng hoặc bãi đỗ xe an toàn gần nhất trên tuyến đường và phát thông báo giọng nói tiếng Việt (ví dụ: *"Đã phát hiện trạm dừng nghỉ Mai Linh cách 2.5 km, bạn nên giảm tốc độ và ghé vào nghỉ ngơi"*).

### FR-04: Lưu trữ bằng chứng vi phạm an toàn (Automated Snapshot & Logging)
* **FR-04.1:** Khi xảy ra sự kiện Báo động cấp độ 2 (ngủ gật), hệ thống tự động cắt khung hình camera (Snapshot) và lưu trữ cục bộ kèm tem thời gian (Timestamp), giá trị EAR, PERCLOS và tọa độ GPS.
* **FR-04.2:** Lưu nhật ký sự kiện vào file CSV hoặc SQLite cục bộ để bảo đảm dữ liệu không bị thất thoát kể cả khi xe mất nguồn đột ngột.

### FR-05: Đồng bộ dữ liệu & Cổng quản trị đội xe (Fleet Management Sync)
* **FR-05.1:** Thiết bị trên xe tự động đồng bộ nhật ký vi phạm và ảnh snapshot về máy chủ quản trị trung tâm thông qua API RESTful an toàn khi có kết nối 4G/WiFi.
* **FR-05.2:** Bảng điều khiển quản lý (Web Dashboard) hiển thị danh sách các xe đang lưu thông, trạng thái sức khỏe tài xế, biểu đồ cảnh báo theo thời gian và xuất báo cáo thống kê PDF.

---

## 4. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - NFR)

| Mã NFR | Phân loại | Tiêu chí kỹ thuật bắt buộc |
| :--- | :--- | :--- |
| **NFR-01** | **Hiệu năng & Độ trễ** | Thời gian trễ từ khi tài xế nhắm mắt quá ngưỡng đến khi còi cảnh báo phát ra **$\le 500$ miligiây**. Tốc độ xử lý hình ảnh duy trì **$\ge 25$ FPS** trên camera độ phân giải HD 720p. |
| **NFR-02** | **Độ tin cậy & Sẵn sàng** | Hệ thống Edge trên xe phải có tính năng **Edge Autonomy 100%**: toàn bộ logic nhận diện, tính toán và phát cảnh báo chạy hoàn toàn offline không phụ thuộc vào Internet. |
| **NFR-03** | **Bảo mật & Riêng tư** | **Zero Unauthorized Streaming:** Không truyền video trực tiếp (raw video stream) lên Internet để bảo đảm quyền riêng tư của tài xế và hành khách. Chỉ gửi dữ liệu khi xảy ra sự kiện vi phạm an toàn. |
| **NFR-04** | **Tính thích ứng môi trường** | Tương thích tốt với cả camera RGB và camera hồng ngoại IR (cho phép giám sát trong khoang lái xe ban đêm hoàn toàn tối). |
| **NFR-05** | **Khả năng mở rộng** | Backend kiến trúc Microservice / FastAPI hỗ trợ kết nối đồng thời từ ít nhất 100 phương tiện vận tải mà không suy giảm hiệu năng. |

---

## 5. RÀNG BUỘC KỸ THUẬT & PHẠM VI (SCOPE & CONSTRAINTS)

### 5.1. Trong phạm vi dự án (In-Scope)
* Phát triển trọn vẹn mô-đun phát hiện thời gian thực tại biên (Edge AI) chạy trên máy tính hoặc máy tính nhúng (PC/Laptop/Mini PC).
* Bộ thư viện tính toán: OpenCV 4.x, MediaPipe 0.10.x, Scikit-learn, NumPy, Pygame/pyttsx3.
* API Gateway và Web Portal quản trị đội xe xây dựng bằng FastAPI.
* Tài liệu kỹ thuật, kế hoạch kiểm thử và báo cáo nghiệm thu sản phẩm.

### 5.2. Ngoài phạm vi hiện tại (Out-of-Scope)
* Tích hợp trực tiếp vào hệ thống phanh tự động (AEB) của xe (chỉ cảnh báo âm thanh và thị giác, không can thiệp vào cơ cấu chấp hành cơ khí).
