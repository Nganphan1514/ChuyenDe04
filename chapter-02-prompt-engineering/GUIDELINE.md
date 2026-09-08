# Chapter 2 — Prompt Engineering

> [!IMPORTANT]
> ⚠️ **Prompt tốt vẫn cần context thật.** Kết quả thay đổi khi brief, human decision, model, skill và repository state khác nhau. Prompt mẫu chỉ cho bạn cấu trúc làm việc, không đảm bảo tạo ra cùng một tài liệu.

> [!TIP]
> 🧠 **Context phải di động.** Hãy thử mở một fresh session và chỉ attach context package. Nếu agent vẫn phải hỏi lại sản phẩm là gì hoặc đoán scope, context chưa đủ dùng.

## Start here

Bạn đã có project brief được phê duyệt. Mục tiêu là tạo context package ngắn để một agent mới hiểu đúng sản phẩm mà không cần thấy cuộc trò chuyện cũ.

## Recommended path

1. **PRIMARY — P2.1:** chạy [build-project-context.prompt.md](prompts/build-project-context.prompt.md) cùng project brief.
2. Kiểm tra các mục `fact`, `decision`, `assumption` và `open question`.
3. **REVIEW GATE:** xác nhận mọi decision trong context thật sự đã được bạn chốt.
4. Lưu [project-context.md](docs/project-context.md) khi bạn approve.

## Input package

- [Project brief](../../chapter-01-ai-in-software-engineering/docs/project-brief.md).
- Human decisions mới hơn brief.

## Review gate

Context đạt khi fresh session có thể mô tả product boundary, vocabulary, source precedence và exclusions mà không thêm feature. Nếu agent phải đoán một quyết định, bổ sung decision hoặc giữ nó là open question.

## Handoff

Giữ [project-context.md](docs/project-context.md) với trạng thái `Accepted`. Attach brief và context khi tạo requirements, không dùng câu “như đã nói ở chapter trước”.

## Prompt reference

### P2.1 — PRIMARY — Build reusable project context

- Skills: `$brainstorm` (conditional)
- Interaction: plan-then-approve
- Input: approved brief và human decisions mới
- Output: approved context package
- Approval gate: xác nhận các decision trước khi lưu
