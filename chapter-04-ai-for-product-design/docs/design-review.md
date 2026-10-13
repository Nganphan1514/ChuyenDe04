# SleepAlert AI Design Review & Ergonomic Assessment Report

> **Provenance**
> - **Source prompt:** [P4.4 -- AI Design Review](../prompts/review-design.prompt.md)
> - **Artifact status:** Accepted reviewed sample
> - **Human action:** Evaluated critique findings, prioritized ergonomic fixes, and confirmed automotive safety and fleet management standards.
> - **Reproduction note:** Structured heuristic review conducted prior to code implementation and synced with DACN1 architecture.

---

## 1. Phuong phap Danh gia va Tieu chuan So chieu

Doi ngu phat trien da su dung cac tieu chuan quoc te ve cong thai hoc phuong tien giao thong va quan ly doi xe de tham dinh:
- **NHTSA Visual-Manual Driver Distraction Guidelines:** Quy dinh tai xe khong duoc roi mat khoi mat duong qua 2.0 giay cho mot tac vu, va moi lan liec nhin khong qua 1.0 giay.
- **ISO 15008:** Yeu cau ve do tuong phan, kich thuoc ky tu va goc nhin cua man hinh hien thi trong xe co gioi ban ngay lan ban dem.
- **WCAG 2.1 AAA:** Do tuong phan mau sac cho cac trang thai nguy hiem toi thieu dat ty le 7:1.

---

## 2. Bang Tham dinh Chi tiet (Findings & Prioritized Actions)

| ID | Linh vuc | Muc do | Van de nhan dien tu DACN1 goc | Co so cong thai hoc | Hanh dong khac phuc da ap dung |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **F1** | Glanceability | CRITICAL | DACN1 goc chi co bang HTML admin, chua co HUD ban dem toi uu cho tai xe. | Doc bang so lieu ton > 3s gay xao nhang nghiem trong khi lai xe. | Thiet ke HUD chuyen biet voi 3 trang thai mau toan man hinh (Normal, Warn, Danger Strobe) va chu so lon. |
| **F2** | Night-Vision | HIGH | Giao dien sang mau gay choi mat ban dem. | Anh sang nen lam co dong tu mat tai xe, giam tam nhin ngoai xe. | Doi sang nen True Black (#090D16), hap thu anh sang thua, bao ve thi luc ban dem. |
| **F3** | Audio Bias | HIGH | Chi bao dong tren man hinh khi ngu gat. | Khi ngu gat mat dang nham, khong the doc man hinh. | Tich hop Web Audio API phat coi hu Sawtooth 850-1150Hz tuc thi (< 500ms) kem Voice tieng Viet. |
| **F4** | Driver Auth | HIGH | Chua truc quan hoa viec doi soat nguoi lai hop le tren xe. | Nguy co tai xe khong du dieu kien hoac chua gan ca tu y dieu khien xe. | Bo sung the xac thuc khuon mat FaceID ngay tren thanh Header buong lai va canh bao tai xe la. |
| **F5** | Mobile Usability | MEDIUM | Dang ky khuon mat chua co huong dan truc quan. | Nguoi dung boi roi khong biet da quet du goc khuon mat hay chua. | Thiet ke Mobile Face Register voi vong oval cong nghe, hieu ung laser quet va chi bao mau (1/3, 2/3, 3/3). |
| **F6** | Fleet Triage | MEDIUM | Bang danh sach xe khong lam noi bat xe dang ngu gat. | Quan ly doi xe kho phat hien kip thoi xe dang gap nan giua hang chuc xe. | Tu dong phan loai va ghim xe BAO DONG DO len dau bang, kem nut mo Snapshot bang chung tuc thi. |

---

## 3. Ket luan cua Phien Review

1. **Phe duyet He sinh thai Toan dien:** Ca 3 khong gian trai nghiem (In-Cabin Cockpit, Central Fleet Management Portal, Driver Mobile App) dap ung day du yeu cau hoc phan va ke thua tron ven suc manh tu DACN1.
2. **San sang Trien khai:** Ban mau tuong tac (prototype/index.html) hoat dong muot ma va hoan toan doc lap, san sang buoc sang Chapter 5 (Thiet ke Kien truc Phan mem).
