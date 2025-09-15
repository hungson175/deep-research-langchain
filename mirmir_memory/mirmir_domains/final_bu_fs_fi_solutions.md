# BU-FS: FI Solutions

## Error Code

200

## Data

### ID
5cd09ae2-90b8-4102-a717-0ae6f649ff69

### Name
BU-FS: FI Solutions

### Description
Data về traffic và giải ngân của sản phẩm CLO

### Instructions
(empty)

## Schema DDL

### Dataset name: BU-FS: FI Solutions

---

## Table 1: momovn-prod.BU_FI.FIS_CLO_TRAFFIC_FLOW

**Description:** Bảng lưu thông tin user truy cập vào sản phẩm CLO theo từng nguồn

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| SOURCE | STRING | nguồn dẫn user tới truy cập sản phẩm |
| VALUE | STRING | đối tác của sản phẩm |
| ETL_DATE | DATE | ngày người dùng truy cập |
| MOMO_SESSION_ID_V2 | STRING | định danh cho lượt truy cập của người dùng |
| AGENT_ID | STRING | định danh mã người dùng |

**VALUE Field Values:**
- `'clo_fecredit'`: FE CREDIT
- `'lending_mp_homecredit'`: HOME CREDIT
- `'cro_vib'`: VIB

---

## Table 2: momovn-prod.BU_FI.FIS_TCST

**Description:** Đây là bảng chứa dữ liệu của sản phẩm CLO. Trong bảng này chứa thông tin về trạng thái của ticket, số tiền giải ngân và doanh thu.

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| TICKET_ID | STRING | Mã định danh cho mỗi yêu cầu hoặc giao dịch | 116472, 116487, 116520 |
| USER | STRING | Người dùng thực hiện yêu cầu hoặc giao dịch | 25136673, 36677566, 36940788 |
| PARTNER_ID | STRING | Mã định danh của đối tác liên quan đến yêu cầu hoặc giao dịch | lending_mp_homecredit |
| FAILED_TIMES | FLOAT | Số lần yêu cầu hoặc giao dịch thất bại | nan |
| STATUS_CODE | STRING | Mã trạng thái của yêu cầu hoặc giao dịch | PRE_CHECK |
| DATE_REQUESTED | DATE | Ngày yêu cầu được thực hiện | 2022-11-24 |
| DATETIME_REQUESTED | DATETIME | Thời điểm yêu cầu được thực hiện | 2022-11-24 00:30:11, 2022-11-24 00:47:15, 2022-11-24 01:39:53 |
| DATE_MODIFIED | DATE | Ngày cập nhật trạng thái mới nhất của ticket. Nếu lấy theo trạng thái giải ngân thì dùng cột này | - |
| DATETIME_MODIFIED | DATETIME | Ngày giờ trạng thái mới nhất của ticket | - |
| DATETIME_EXPIRED | DATETIME | Thời điểm yêu cầu hoặc giao dịch được đẩy đi | - |
| DATETIME_PUSHED | DATETIME | Thời điểm yêu cầu hoặc giao dịch được đẩy đi | - |
| SCORING_CODE | STRING | Mã điểm số liên quan đến yêu cầu hoặc giao dịch | - |
| CORE_ID | STRING | Mã định danh của giao dịch, tương ứng với mã định danh của table core_trans | - |
| OFFER_ID | STRING | Mã định danh của đề nghị liên quan đến yêu cầu hoặc giao dịch | - |
| ONBOARDING_APPLICATION_ID | STRING | Mã định danh của ứng dụng onboarding liên quan đến yêu cầu hoặc giao dịch | - |
| ONBOARDING_APPLICATION_STATUS | STRING | Trạng thái của ứng dụng onboarding liên quan đến yêu cầu hoặc giao dịch | - |
| CONTRACT_ID | STRING | Mã định danh của hợp đồng liên quan đến yêu cầu hoặc giao dịch | - |
| CONTRACT_NAME | STRING | Tên của hợp đồng liên quan đến yêu cầu hoặc giao dịch | - |
| CONTRACT_AMOUNT | FLOAT | Số tiền của hợp đồng liên quan đến yêu cầu hoặc giao dịch. hãy dùng cột này để tính số giải ngân/disbursed | - |
| MINIMAL_CREDIT_AMOUNT | FLOAT | Số tiền tín dụng tối thiểu liên quan đến yêu cầu hoặc giao dịch | - |
| MAXIMAL_CREDIT_AMOUNT | FLOAT | Số tiền tín dụng tối đa liên quan đến yêu cầu hoặc giao dịch | - |
| REQUESTED_CREDIT_AMOUNT | FLOAT | Số tiền tín dụng được yêu cầu trong giao dịch | - |
| APPROVED_CREDIT_AMOUNT | FLOAT | Số tiền tín dụng được phê duyệt trong giao dịch | - |
| DISBURSED_CREDIT_AMOUNT | FLOAT | Số tiền tín dụng đã được giải ngân trong giao dịch | - |
| REVENUE_TEMP | FLOAT | Doanh thu tạm thời liên quan đến yêu cầu hoặc giao dịch | - |
| REVENUE | FLOAT | Doanh thu thực tế liên quan đến yêu cầu hoặc giao dịch | - |
| OFFER_TYPE | STRING | Để phân biệt user được giải ngân thuộc ACL hay CLX, chỉ áp dụng cho lending_mp_homecredit | - |
| SERVICE_TYPE | STRING | Để phân biệt dịch vụ CRO hoặc CLO. luôn có thêm điều kiện cột này = 'CLO' | - |

**PARTNER_ID Definitions:**
- `lending_mp_homecredit`: Home Credit
- `cro_vib`: VIB
- `clo_fecredit`: FE CREDIT
- `clo_mcredit`: MCREDIT

## Knowledgebase

(empty)

## Memory

- **ID:** de7d37a3-ebb2-4854-ba80-8dd8479b54f9
  **Content:** Số giải ngân (disbursed amount) được tính bằng cột CONTRACT_AMOUNT trong bảng momovn-prod.BU_FI.FIS_TCST.
  **User:** BU-FS: FI Solutions
  **Created:** 2025-08-13T15:14:14.923219

- **ID:** aa3934a1-82a9-4ac4-9194-bdc7530adcb7
  **Content:** Khi người dùng hỏi về 'home', 'FE', 'CRO', hoặc 'VIB', hãy sử dụng PARTNER_ID tương ứng: 'home' -> 'lending_mp_homecredit', 'FE' -> 'clo_fecredit', 'CRO' -> 'cro_vib', 'VIB' -> 'cro_vib'
  **User:** FS - FI Solutions
  **Created:** 2025-08-13T13:51:41.179744

- **ID:** a6b5c47d-3ed1-4898-9a3f-076e2af01d01
  **Content:** Khi so sánh lượng application submitted, cần sử dụng status_code bao gồm: 'APPLICATION_CANCELED', 'APPLICATION_REJECTED', 'APPLICATION_APPROVED', 'APPLICATION_RESUBMIT', 'APPLICATION_SUBMITTED', 'DISBURSED', 'CONTRACT_SIGNED', 'RESET'
  **Hash:** d8ec3d6d7430746dceebf77c671c7b3c
  **Created:** 2025-08-20T21:00:03.328674-07:00

- **ID:** 8750751c-8f7d-4e8f-9dcb-6405cca1062a
  **Content:** Không có dữ liệu người dùng vào màn hình onboarding sản phẩm CLO Mcredit với trạng thái INITIATED trong ngày 14/8/2025 và 15/8/2025
  **Hash:** 8823cdfee13e8824cceb3e01854f8e08
  **User:** BU-FS: FI Solutions
  **Created:** 2025-08-15T03:46:08.671335-07:00

- **ID:** ee00e738-ebb0-4f95-8c13-f223e7345035
  **Content:** Để tính tổng số tiền giải ngân cho dịch vụ CLO, sử dụng CONTRACT_AMOUNT thay vì DISBURSED_CREDIT_AMOUNT
  **Hash:** 66044916d6832df2d230cead986f36b2
  **User:** FS - FI Solutions
  **Created:** 2025-07-17T03:46:01.633709-07:00

- **ID:** 5887dd30-695c-4f1c-b5e8-9e14a62c0261
  **Content:** Khoảng thời gian lọc là DATE_MODIFIED BETWEEN '2025-06-01' AND '2025-06-30' cho dịch vụ CLO
  **Hash:** a77e69ad41801409246ccf28cb928114
  **User:** FS - FI Solutions
  **Created:** 2025-07-17T03:46:01.688043-07:00

- **ID:** 06fa2286-e639-4ace-8428-7e7084fbbf75
  **Content:** Khi truy vấn số liệu giải ngân, luôn thêm điều kiện service_type = 'CLO'
  **User:** FS - FI Solutions
  **Created:** 2025-08-13T13:45:32.474427

- **ID:** e844ee65-187f-4133-973a-96d4b3a02106
  **Content:** official_account: Kênh hoặc nguồn mà người dùng truy cập sản phẩm thông qua các tài khoản chính thức của đối tác hoặc của MoMo.
  **User:** BU-FS: FI Solutions
  **Created:** 2025-08-14T21:50:27.076587

## Error Message

(empty)