# SleepAlert Master Product Design Specification

> **Provenance**
> - **Source prompt:** [P4.3 -- Create Prototype](../prompts/create-prototype.prompt.md)
> - **Artifact status:** Accepted reviewed sample
> - **Human action:** Approved multi-space design tokens, automotive glanceability, mobile ergonomics, and acoustic warning hierarchy.
> - **Reproduction note:** Governs all visual, interaction, and component implementations across Edge HUD, Fleet Cloud Portal, and Mobile Driver App.

---

## 1. Triet ly Thiet ke 3 Khong gian Trai nghiem (Ecosystem Design Philosophy)

He thong SleepAlert ket hop hai hoa 3 moi truong su dung voi cac nguyen tac cong thai hoc dac thu ke thua tu DACN1:

1. **In-Cabin Edge Cockpit:**
   - **Quy tac Liec mat 1 giay (1-Second Glanceability Rule):** Tai xe chi can liec mat duoi 1.0 giay la nam duoc tron ven trang thai an toan cua minh. Toan bo thong tin chinh duoc bieu thi qua mau sac vien man hinh (Xanh / Ho phach / Do) va chu so lon.
   - **Bao ve Thi giac Ban dem (Night-Drive Pupil Protection):** Nen True Black (#090D16), cam anh sang xanh choi loa lam mu tam thoi mat tai xe khi nhin ra duong toi.
   - **Uu tien Am thanh truoc Hinh anh (Acoustic Dominance):** Khi tai xe nham mat ngu gat, coi bao dong Web Audio API (Sawtooth 850-1150Hz) va Voice tieng Viet la kenh tac dong chinh de cuu mang.
2. **Central Fleet Portal:**
   - Mat do thong tin cao (High Information Density), truc quan hoa du lieu tuc thi, co che loc va ghim xe nguy cap (Critical Priority Pinning).
3. **Driver Mobile App:**
   - Than thien mot tay (One-handed Ergonomics), dieu huong bang Bottom Navigation, truc quan hoa luong quet FaceID voi hieu ung laser scan va phan hoi xuc giac.

---

## 2. He thong Tokens Thiet ke (Design Tokens)

| Ten Token | Ma Hex | Muc dich va Y nghia |
| :--- | :--- | :--- |
| --surface-deep | #090D16 | Nen man hinh buong lai ban dem, hap thu anh sang thua |
| --surface-card | #101726 | Be mat the chi so, co vien manh phan tach |
| --surface-modal | #0F172A | Nen cua so pop-up xem anh vi pham Snapshot |
| --border-subtle | #1E293B | Vien ngan cach khu vuc, do tuong phan vua du |
| --status-safe | #10B981 | Xanh luc bao diu mat: He thong an toan, tinh tao |
| --status-warn | #F59E0B | Ho phach: Met moi tich luy, ngap, can chu y |
| --status-danger | #EF4444 | Do khan cap: Ngu gat microsleep, coi bao dong |
| --accent-cyan | #06B6D4 | Cyan cong nghe cao: Quet Face Mesh va Laser Mobile |
| --text-primary | #F8FAFC | Trang sang tu nhien, hien thi thong so chinh |
| --text-muted | #94A3B8 | Xam trung tinh, danh cho nhan phu va don vi do |

---

## 3. Thang Do Typography va Kich thuoc Chu so

- **Chi so Trang thai Chinh Buong lai (EAR / PERCLOS):** Font Inter / Roboto Mono, kich thuoc 36px - 48px, font-weight Bold (700), de doc o khoang cach 70cm - 1m tu ghe lai.
- **Tieu de Bao dong Do:** Kich thuoc 28px - 32px nhap nhay chu ky 0.4s (Danger Strobe).
- **Bang dieu khien Fleet va Mobile:** Font tieu chuan kich thuoc 12px - 16px, bo cuc the bo goc rounded-xl, badge trang thai voi mau sac tuong ung.

---

## 4. He thong Tin hieu Am thanh (Acoustic Cue Hierarchy)

- **Level 0 (Khoi dong):** Tieng Chime em diu 0.5s khi hieu chuan xong, 55 dB (Nhe nhang).
- **Level 1 (Met moi):** Am Ding-Dong nhac nho hoac Voice: 'Ban met roi!', 68 dB.
- **Level 2 (Ngu gat):** Coi bao dong Sawtooth coi hu 850Hz - 1150Hz, > 85 dB (Choi tai, khan cap), keo dai lien tuc den khi mo mat.
