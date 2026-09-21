# Chapter 4 — AI for Product Design

> [!IMPORTANT]
> ⚠️ **Thiết kế không chỉ là giao diện đẹp mà là trải nghiệm an toàn.** Đối với hệ thống cảnh báo lái xe như SleepAlert, giao diện buồng lái (In-Cabin Display) phải đảm bảo tiêu chuẩn **Glanceability (quan sát dưới 1 giây)** và không làm chói mắt tài xế ban đêm. AI có thể đề xuất nhiều layout, nhưng con người phải chốt tiêu chuẩn công thái học (Ergonomics).

> [!TIP]
> 🧭 **Đi từ luồng nghiệp vụ (Flow) → Bố cục khung (Wireframe) → Bản mẫu tương tác (Prototype) → Đánh giá phản biện (Design Review).** Đừng vội tạo giao diện chi tiết khi chưa chốt được thứ bậc nhiệm vụ (Task Hierarchy) và các kịch bản lỗi (Failure Paths).

## Start here

Bạn đã có PRD và Feature Specification được phê duyệt ở Chapter 3. Mục tiêu của Chapter 4 là chuyển hóa các yêu cầu kỹ thuật thành hệ thống luồng người dùng (User Flows), bố cục khung (Wireframes), bản mẫu tương tác chạy được (Interactive Prototype) và biên bản đánh giá thiết kế bằng AI (AI Design Review).

## Recommended path

1. **PRIMARY — P4.1 (User Flow):** Chạy [create-user-flow.prompt.md](prompts/create-user-flow.prompt.md) để xây dựng luồng chính (Happy path) và các nhánh rẽ (Edge cases: mất dấu khuôn mặt, mất sóng GPS, cảnh báo khẩn cấp). Lưu vào [docs/user-flows.md](docs/user-flows.md).
2. **PRIMARY — P4.2 (Wireframing):** Chạy [create-wireframe.prompt.md](prompts/create-wireframe.prompt.md) để phác thảo cấu trúc khung cho 2 không gian: Màn hình buồng lái (HUD) và Cổng quản lý đội xe (Fleet Dashboard). Lưu vào [docs/wireframes.md](docs/wireframes.md).
3. **PRIMARY — P4.3 (Prototyping):** Chạy [create-prototype.prompt.md](prompts/create-prototype.prompt.md) để xây dựng bản mẫu tương tác thực tế (HTML5/Tailwind CSS/JS) cho phép mô phỏng các trạng thái tài xế và cảnh báo còi hú thời gian thực tại [prototype/index.html](prototype/index.html).
4. **REVIEW GATE — P4.4 (AI Design Review):** Chạy [review-design.prompt.md](prompts/review-design.prompt.md) để kiểm tra công thái học, độ tương phản ban đêm (WCAG), độ trễ nhận thức và giảm tải thần kinh cho tài xế. Lưu vào [docs/design-review.md](docs/design-review.md).
5. Tổng hợp toàn bộ hồ sơ thiết kế chính thức vào [docs/product-design.md](docs/product-design.md).

## Input package

- [Project context](../../chapter-02-prompt-engineering/docs/project-context.md).
- [Product requirements](../../chapter-03-ai-for-requirements-product-analysis/docs/product-requirements.md).
- [Feature specification](../../chapter-03-ai-for-requirements-product-analysis/docs/feature-specification.md).

## Review gate

Thiết kế đạt chuẩn khi:
- Mọi trạng thái hệ thống (Hiệu chuẩn, Tỉnh táo, Mệt mỏi, Buồn ngủ khẩn cấp, Mất khuôn mặt, Mất mạng) đều có phản hồi trực quan và âm thanh tương ứng.
- Màn hình buồng lái không chứa văn bản thừa, không làm phân tâm người lái.
- Bản mẫu tương tác (Prototype) kiểm chứng được việc chuyển đổi trạng thái tức thời.

## Handoff

Giữ [docs/product-design.md](docs/product-design.md) ở trạng thái `Accepted`. Đây là căn cứ thẩm mỹ và trải nghiệm bắt buộc trước khi chuyển sang Chapter 5 (Kiến trúc & Thiết kế phần mềm).
