# P1.1 — Clarify the project idea: SleepAlert

> - **Role:** PRIMARY
> - **Skills:** `$brainstorm` (required)
> - **Interaction mode:** multi-turn conversation
> - **Output mode:** interactive draft → approved artifact
> - **Approval gate:** wait for explicit human approval before saving
> - **Canonical output:** `chapter-01-ai-in-software-engineering/docs/project-brief.md`
> - **Run context:** fresh session; use only the input in this prompt and the human's answers.

## Use this when

You have a rough, customer-style product idea for an AI Driver Drowsiness Monitoring System and need an agreed project brief before writing requirements, design, architecture, or code.

## Inputs

- Raw idea: Một hệ thống giám sát và cảnh báo sớm buồn ngủ, mất tập trung cho tài xế xe tải/xe khách đường dài bằng camera trong cabin, nhận diện khuôn mặt, đo đạc chỉ số mắt/miệng/đầu và phát âm thanh cảnh báo tức thì.
- Initial boundary: Cảnh báo tại chỗ thời gian thực (< 500ms), không phụ thuộc mạng; đồng bộ dữ liệu sự kiện về quản lý đội xe khi có kết nối.
- Any explicit human decisions made before this session.

If an input is unavailable, ask the human to provide it. Do not infer a missing business decision.

## Task

Use `$brainstorm` to turn the raw idea into an agreed brief.

1. Restate the raw idea as a problem hypothesis; separate stated facts from assumptions.
2. Ask focused clarification questions in small rounds: primary user persona, in-cabin environment, latency limit, false positive tolerance, offline capability, privacy requirements.
3. Do not assume hardware constraints, alert escalation policy, or cloud dependency without confirmation.
4. Keep a compact decision log as answers arrive.
5. When enough decisions are explicit, draft a one- to two-page project brief.
6. Ask the human to approve the draft or request revisions. Do not treat the draft as canonical before approval.

## Constraints and source precedence

1. Human answers and approvals in this conversation.
2. The raw idea above.
3. AI suggestions.

- Keep the product focused on driver safety and edge autonomy.
- Do not create full requirements, architecture, tasks, or code in this chapter.
- Exclude mechanical vehicle control (e.g. auto-braking, steering wheel takeover) and continuous raw video cloud streaming.
- Use precise biometric terms: EAR (Eye Aspect Ratio), MAR (Mouth Aspect Ratio), PERCLOS, Head Pose.
- Report conflicts or unknowns instead of silently resolving them.

## Expected output

Before approval, provide a draft brief with: problem hypothesis, primary user, desired outcome, in-scope behavior, exclusions, constraints, AI working rules, decision log, and open assumptions.

## Save or update

After explicit approval, write the approved Markdown to `chapter-01-ai-in-software-engineering/docs/project-brief.md`.

## Human review required

The human must approve the brief and resolve or accept every remaining assumption.

## Validation checklist

- The in-cabin detection → local alert escalation → event snapshot journey is clear.
- Every retained feature follows from an approved decision.
- Vehicle mechanical intervention and continuous raw video streaming are explicitly excluded.
- Unknowns remain labelled as assumptions.
- The approved brief can be attached to a fresh session.
