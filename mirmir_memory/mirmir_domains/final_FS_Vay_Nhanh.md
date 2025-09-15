# FS Vay Nhanh Dataset

## Dataset Information

- **ID**: bb231763-b11c-45c6-9b0d-eb6d24588e3d
- **Name**: FS Vay Nhanh
- **Description**: Data liên quan đến giải ngân, traffic Vaynhanh
- **Instructions**: (Not specified)
- **Error Code**: 200

---

## Schema Information

### Dataset Name: FS Vay Nhanh

---

## Table 1: momovn-prod.BU_FI.BAOTU_VAYNHANH_LOAN_INFO

**Description**:
Bảng này lưu trữ thông tin chi tiết về các khoản vay nhanh trong hệ thống MoMo. Bảng chứa thông tin về người cho vay, mã khoản vay, số tiền được vay, trạng thái của khoản vay, và các thời điểm quan trọng trong quá trình xử lý khoản vay.

**Use Cases**:
- Theo dõi và quản lý quá trình cho vay nhanh của hệ thống.
- Phân tích và đánh giá điểm tín dụng của khách hàng.
- Tối ưu hóa quá trình xử lý các khoản vay theo từng phân khúc khách hàng.

### Columns

| Column Name | Description |
|-------------|-------------|
| AGENT_ID | Mã định danh cho mỗi ví MoMo, liên kết với người nhận khoản vay. |
| LENDER_ID | Mã định danh của người cho vay khoản vay. |
| LOAN_ID | Mã định danh cho mỗi khoản vay trong hệ thống. |
| CREATED_TIME | Thời gian tạo khoản vay trong hệ thống. |
| CREATED_DATE | Ngày tạo khoản vay trong hệ thống. |
| SUBMITTED_TIME | Thời gian nộp hồ sơ vay. |
| SUBMITTED_DATE | Ngày nộp hồ sơ vay. |
| DISBURSED_TIME | Thời gian khoản vay được giải ngân. |
| DISBURSED_DATE | Ngày khoản vay được giải ngân. |
| LIQUIDATED_TIME | Thời gian khoản vay được thanh lý. |
| LIQUIDATED_DATE | Ngày khoản vay được thanh lý. |
| MOMO_CREDIT_SCORE | Điểm tín dụng MoMo của người vay, đánh giá khả năng trả nợ. |
| STATUS | Trạng thái hiện tại của khoản vay (ví dụ: đang chờ xử lý, đã giải ngân, bị từ chối). |
| REJECTED_REASON | Lý do khoản vay bị từ chối. |
| LOAN_AMOUNT | Số tiền mà khách hàng đã vay trong khoản vay. |
| TENOR | Thời hạn khoản vay, thường được tính bằng tháng. |
| DISBURSED_AMOUNT | Số tiền thực tế đã được giải ngân cho khoản vay. |
| FIRST_DUE_DATE | Ngày đến hạn thanh toán đầu tiên cho khoản vay. |
| EMI | Số tiền phải trả định kỳ cho khoản vay. |
| PROCESS_TYPE | Loại hình xử lý của khoản vay (có thể là tự động hoặc thủ công). |
| PROCESS_TYPE_BY_LENDER | Loại hình xử lý cụ thể theo mỗi người cho vay. |
| DISBURSED_COUNT_TIME | Số lần khoản vay được giải ngân. |
| DISBURSED_COUNT_TIME_BY_LENDER | Số lần khoản vay được giải ngân theo từng người cho vay. |
| SEGMENT_USER | Phân khúc khách hàng dựa trên phân tích dữ liệu hiện tại. |
| FINAL_SEGMENT_USER | Phân khúc khách hàng cuối cùng để xác định xử lý khoản vay. |

### Data Example

Empty DataFrame
Columns: [AGENT_ID, LENDER_ID, LOAN_ID, CREATED_TIME, CREATED_DATE, SUBMITTED_TIME, SUBMITTED_DATE, DISBURSED_TIME, DISBURSED_DATE, LIQUIDATED_TIME, LIQUIDATED_DATE, MOMO_CREDIT_SCORE, STATUS, REJECTED_REASON, LOAN_AMOUNT, TENOR, DISBURSED_AMOUNT, FIRST_DUE_DATE, EMI, PROCESS_TYPE, PROCESS_TYPE_BY_LENDER, DISBURSED_COUNT_TIME, DISBURSED_COUNT_TIME_BY_LENDER, SEGMENT_USER, FINAL_SEGMENT_USER]
Index: []

---

## Table 2: momovn-prod.BU_FI.BAOTU_VAYNHANH_ENTRY_POINT

**Description**:
Bảng này chứa thông tin về điểm truy cập nhanh dịch vụ vay Baotu thông qua MoMo. Người dùng có thể lấy thông tin về sự kiện truy cập dịch vụ vay, xác định nguồn truy cập và loại người dùng. Ngoài ra, bảng cung cấp thông tin về điểm tín dụng của người dùng thông qua phạm vi điểm và phiên bản chấm điểm. Các trường thông tin có thể được sử dụng để phân tích hành vi khách hàng, phát triển mô hình phân tích điểm tín dụng và tối ưu hóa dịch vụ chăm sóc khách hàng.

### Columns

| Column Name | Description |
|-------------|-------------|
| ETL_DATE | Ngày dữ liệu được trích xuất ETL. |
| EVENT_TIME | Thời điểm xảy ra sự kiện truy cập dịch vụ vay Baotu. |
| AGENT_ID | Mã định danh cho mỗi ví MoMo. |
| ACCESSED_SOURCE | Nguồn truy cập vào dịch vụ vay Baotu. |
| momo_session_id_v2 | ID phiên sử dụng MoMo cho lần truy cập. |
| WHITELIST_CHECK | Kiểm tra danh sách trắng cho người dùng hoặc dịch vụ. |
| USER_TYPE | Phân loại người dùng dựa trên hành vi sử dụng. |
| SCORE_VERSION | Phiên bản của hệ thống chấm điểm tín dụng. |
| CREDIT_SCORE_RANGE | Phạm vi điểm tín dụng của người dùng. |

### Data Example

| ETL_DATE | EVENT_TIME | AGENT_ID | ACCESSED_SOURCE | momo_session_id_v2 | WHITELIST_CHECK | USER_TYPE | SCORE_VERSION | CREDIT_SCORE_RANGE |
|----------|------------|----------|-----------------|-------------------|-----------------|-----------|---------------|-------------------|
| 2025-07-15 | 2025-07-15 18:25:14.119000+00:00 | 100194197 | app_all_service_top | E64C59C1-CAF1-4D5C-8172-E3D219E560B7 | 1 IN WHITELIST | 2 Re-loan | MOMO_CREDIT_SCORE_FMPL_V7 | 01 585 - 589 |
| 2025-07-15 | 2025-07-15 22:03:23.193000+00:00 | 100218188 | app_all_service_top | 424221B9-3040-4578-A25B-06A7712CA763 | 1 IN WHITELIST | 2 Re-loan | MOMO_CREDIT_SCORE_FMPL_V7 | 01 585 - 589 |
| 2025-07-15 | 2025-07-15 22:03:14.576000+00:00 | 100218188 | app_all_service_top | 424221B9-3040-4578-A25B-06A7712CA763 | 1 IN WHITELIST | 2 Re-loan | MOMO_CREDIT_SCORE_FMPL_V7 | 01 585 - 589 |
| 2025-07-15 | 2025-07-15 01:21:09.086000+00:00 | 100437191 | app_all_service_top | 56BE5307-833F-41C5-9955-059EDB35F1E1 | 1 IN WHITELIST | 2 Re-loan | MOMO_CREDIT_SCORE_FMPL_V7 | 01 585 - 589 |
| 2025-07-15 | 2025-07-15 01:20:57.679000+00:00 | 100437191 | app_all_service_top | 56BE5307-833F-41C5-9955-059EDB35F1E1 | 1 IN WHITELIST | 2 Re-loan | MOMO_CREDIT_SCORE_FMPL_V7 | 01 585 - 589 |

---

## Table 3: momovn-prod.BU_FI.BAOTU_VAYNHANH_USER_ACCESSED

**Description**:
Bảng này lưu trữ thông tin về việc truy cập của người dùng liên quan đến dịch vụ cho vay nhanh của BAOTU.

**Information Available**:
- Xác định mã định danh của ví MoMo liên quan đến mỗi lần truy cập thông qua cột AGENT_ID.
- Phân tích thời gian truy cập của người dùng thông qua cột EVENT_TIME.
- Phân loại người dùng và loại người dùng đang tương tác với dịch vụ cho vay của BAOTU thông qua cột USER_TYPE và USER_TYPE_BY_LENDER.

### Columns

| Column Name | Description |
|-------------|-------------|
| ETL_DATE | Ngày thực hiện ETL trên dữ liệu. |
| EVENT_TIME | Thời gian xảy ra sự kiện truy cập. |
| momo_session_id_v2 | ID phiên MoMo được cập nhật dùng để theo dõi hoạt động của người dùng. |
| AGENT_ID | Mã định danh cho mỗi ví MoMo. |
| WHITELIST_CHECK | Trạng thái kiểm tra người dùng có nằm trong danh sách whitelist hay không. |
| SCORE_VERSION | Phiên bản của hệ thống tính điểm tín dụng được sử dụng khi truy cập. |
| CREDIT_SCORE_RANGE | Phạm vi điểm tín dụng của người dùng, thường được dùng để đánh giá mức độ tín dụng. |
| ROUTING_LENDER | Người cho vay được định tuyến khi người dùng truy cập vào dịch vụ BAOTU. |
| USER_TYPE | Phân loại người dùng như user thường, merchant, v.v. |
| USER_TYPE_BY_LENDER | Loại người dùng theo phân loại của người cho vay. |

### Data Example

| ETL_DATE | EVENT_TIME | momo_session_id_v2 | AGENT_ID | WHITELIST_CHECK | SCORE_VERSION | CREDIT_SCORE_RANGE | ROUTING_LENDER | USER_TYPE | USER_TYPE_BY_LENDER |
|----------|------------|-------------------|----------|-----------------|---------------|-------------------|----------------|-----------|-------------------|
| 2024-06-05 | 2024-06-04 23:41:13.818012+00:00 | B94EA076-75F2-48B7-9FD4-55A9F194770D | 15079427 | 2 NOT IN WHITELIST | MOMO_CREDIT_SCORE_FMPL_V5 | 01 < 710 |  | First loan | First loan |
| 2024-06-05 | 2024-06-05 01:38:18.451000+00:00 | b2865132-061f-4e44-93e9-52249c111d8a | 25633628 | 2 NOT IN WHITELIST | MOMO_CREDIT_SCORE_FMPL_V5 | 01 < 710 |  | First loan | First loan |
| 2024-06-05 | 2024-06-05 09:00:19.752000+00:00 | C1F9096E-3667-4728-93B7-A6DBA81B2A58 | 15671081 | 2 NOT IN WHITELIST | MOMO_CREDIT_SCORE_FMPL_V5 | 01 < 710 |  | First loan | First loan |
| 2024-06-05 | 2024-06-04 18:18:43.833012+00:00 | 8DEC08FC-1CBE-4101-8DA8-14138EFE0CA8 | 21237495 | 2 NOT IN WHITELIST | MOMO_CREDIT_SCORE_FMPL_V5 | 01 < 710 |  | First loan | First loan |
| 2024-06-05 | 2024-06-05 12:12:48.270000+00:00 | 28134092-3834-4A32-8578-21C805FEA920 | 17901551 | 2 NOT IN WHITELIST | MOMO_CREDIT_SCORE_FMPL_V5 | 01 < 710 |  | First loan | First loan |

---

## Knowledge Base

(Empty)

---

## Memory

(Empty)

---

## Error Message

(Empty)