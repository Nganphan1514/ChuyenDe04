# Chapter 1 — AI in Software Engineering

> [!IMPORTANT]
> ⚠️ **Không thể tái lập kết quả chỉ bằng cách sao chép prompt.** Model, system instruction, skill, input đính kèm, repository state, nghiên cứu và quyết định của người học đều làm thay đổi kết quả. Hãy xem AI output là bản nháp cần kiểm tra, không phải đáp án mẫu cần sao chép.

> [!TIP]
> 🧭 **Bắt đầu bằng vấn đề, không phải danh sách tính năng.** `$brainstorm` sẽ hỏi nhiều câu và đưa ra options. Cách bạn trả lời, chọn hoặc tự viết phương án khác sẽ quyết định project brief cuối cùng.

## Start here

Bạn có một ý tưởng thô, giống yêu cầu sơ bộ từ khách hàng. Mục tiêu là chốt một project brief đã được bạn phê duyệt; chưa viết PRD, thiết kế hay code.

## Recommended path

1. **PRIMARY — P1.1:** copy [clarify-project-idea.prompt.md](prompts/clarify-project-idea.prompt.md) vào một fresh session.
2. Trả lời các câu hỏi làm rõ. Bạn có thể chọn option của agent hoặc tự viết câu trả lời.
3. Đọc decision log và draft project brief. Yêu cầu sửa nếu có điều chưa đúng.
4. **REVIEW GATE:** chỉ approve khi scope, exclusions và assumptions phản ánh đúng ý bạn.
5. Sau approval, lưu [project-brief.md](docs/project-brief.md).

## Input package

- Raw idea theo ngôn ngữ của khách hàng.
- Những giới hạn bạn đã biết: người dùng, thời gian, công nghệ, phạm vi.
- Những quyết định bạn muốn giữ nguyên.

Không cần biến ý tưởng thành tài liệu hoàn chỉnh trước khi chạy prompt.

## Review gate

Đi tiếp khi bạn có thể giải thích: sản phẩm giúp ai, giải quyết việc gì, journey nhỏ nhất là gì, điều gì không làm, và assumption nào còn mở. Nếu chưa trả lời được, quay lại vòng hỏi đáp của P1.1.

## Handoff

Giữ [project-brief.md](docs/project-brief.md) với trạng thái `Accepted`. Stage kế tiếp phải attach chính file này, không dựa vào chat cũ.

## Prompt reference

### P1.1 — PRIMARY — Clarify project idea

- Skills: `$brainstorm` (required)
- Interaction: multi-turn conversation
- Input: raw customer-style idea
- Output: approved project brief
- Approval gate: approve trước khi lưu
