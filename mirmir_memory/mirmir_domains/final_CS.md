# CS Dataset

## Dataset Information

- **ID**: 63409031-024f-465a-8ac7-da361d19f5f4
- **Name**: CS
- **Description**: The dataset records information about user suggestions received through custommer service and chatbot
- **Instructions**:
- **Error Code**: 200

---

## Schema Information

### Dataset Name: CS

---

### Table: momovn-prod.CS.CRM_TICKET

**Description**: Table to store detailed records of customer service tickets, capturing various aspects of the service process and customer interactions. Information that could be obtained from this table includes:

- Tracking and managing customer service requests and their statuses
- Analyzing customer feedback and satisfaction metrics
- Monitor service level agreements (SLA) and processing times for efficiency improvements.

### Columns

| Column Name | Description |
|------------|-------------|
| TICKET_ID | Mã định danh duy nhất cho mỗi vé khách hàng. |
| STATUS | Trạng thái hiện tại của vé khách hàng. |
| CALL_BY_PHONE | Số điện thoại được dùng để gọi dịch vụ khách hàng. |
| CREATED_DATE | Ngày tạo vé khách hàng. |
| HOUR_CREATED_DATE | Giờ trong ngày khi vé khách hàng được tạo. |
| CREATED_TIME | Thời điểm tạo vé khách hàng. |
| PROCESS_DATE | Ngày xử lý vé khách hàng. |
| CLOSE_DATE | Ngày đóng vé khách hàng. |
| CLOSE_TIME | Thời điểm vé khách hàng được đóng. |
| RATING_DATE | Ngày khách hàng đánh giá dịch vụ sau khi kết thúc. |
| RATING_TIME | Thời điểm khách hàng đánh giá dịch vụ. |
| TICKET_TYPE | Loại vé khách hàng, chỉ định loại yêu cầu hoặc vấn đề. |
| SOURCE_REQUEST | Nguồn yêu cầu ban đầu của vé khách hàng. |
| BU | Đơn vị kinh doanh liên quan đến việc xử lý vé khách hàng. |
| Level0 | Cấp độ 0 của vấn đề trong vé khách hàng. |
| Level1 | Cấp độ 1 của vấn đề trong vé khách hàng. |
| Level2 | Cấp độ 2 của vấn đề trong vé khách hàng. |
| Level3 | Cấp độ 3 của vấn đề trong vé khách hàng. |
| Level4 | Cấp độ 4 của vấn đề trong vé khách hàng. |
| Quy_trinh | Tên quy trình liên quan đến việc xử lý vé khách hàng. |
| ALL_SLA_TIME | Tổng thời gian cam kết cho tất cả các quy trình xử lý. |
| EXPECTED_TIME | Thời gian dự kiến để xử lý vé khách hàng. |
| SLA_TIME | Thời gian thực tế thực hiện theo cam kết SLA. |
| SLA_TIME_RECEIVE | Thời gian SLA nhận yêu cầu từ khách hàng. |
| STATUS_PROCESS | Trạng thái xử lý hiện tại của vé khách hàng. |
| CONTENTS | Nội dung chi tiết của vé khách hàng. |
| PROCESS_NOTE | Ghi chú quá trình xử lý, có thể bao gồm dữ liệu cá nhân. |
| PROCESS_HISTORY | Lịch sử xử lý vé khách hàng, có thể bao gồm dữ liệu cá nhân. |
| TICKET_DA_TIEP_NHAN | Dấu hiệu cho biết vé đã tiếp nhận. |
| SUPPORT_ATTITUDE | Thái độ hỗ trợ từ nhân viên. |
| SPEED_FEEDBACK | Đánh giá tốc độ phản hồi dịch vụ. |
| SATISFACTION_LEVEL | Mức độ hài lòng của khách hàng. |
| comment_after_rating | Bình luận của khách hàng sau khi đánh giá. |
| Q_01 | Câu hỏi 01 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt01 | Điểm số đánh giá cho câu hỏi 01. |
| Q_02 | Câu hỏi 02 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt0s | Điểm số đánh giá cho câu hỏi 02. |
| Q_03 | Câu hỏi 03 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt03 | Điểm số đánh giá cho câu hỏi 03. |
| Q_04 | Câu hỏi 04 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt04 | Điểm số đánh giá cho câu hỏi 04. |
| Q_05 | Câu hỏi 05 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt05 | Điểm số đánh giá cho câu hỏi 05. |
| Q_06 | Câu hỏi 06 liên quan đến đánh giá dịch vụ của khách hàng. |
| vt06 | Điểm số đánh giá cho câu hỏi 06. |
| TRANS_NAME | Tên giao dịch liên quan đến vé khách hàng. |
| TRANS_TAG | Thẻ giao dịch liên quan đến vé khách hàng. |
| GROUP_XU_LY | Nhóm thực hiện xử lý công việc cho vé khách hàng. |
| GROUP_CLOSE_TICKET | Nhóm thực hiện đóng vé khách hàng. |
| TIME_THUC_TE_TIEPNHAN | Thời gian thực tế tiếp nhận vé khách hàng. |
| TIME_THUC_TE_XULY | Thời gian thực tế xử lý vé khách hàng. |
| ASSIGN_BY | Người thực hiện gán nhiệm vụ xử lý cho vé khách hàng. |
| TID | TID liên quan đến vé khách hàng. |
| PARENT_ID | ID cha liên quan đến vé khách hàng, có thể dùng để liên kết. |
| Is_last_ticket | Là vé cuối cùng xử lý (True) hoặc không phải vé cuối cùng (False). |
| merge_ticket | Thông tin gộp vé khách hàng. |
| ALLOW_COMMENT | Cho phép bình luận trên vé khách hàng. |
| CUSTOMER_CLAIM | Số điện thoại của khách hàng liên quan đến khiếu nại. |
| CUS_COMMENT | Mức độ bình luận của khách hàng. |
| IS_AUTO | Vé khách hàng được xử lý tự động. |
| ERR_ID | ID lỗi liên quan đến vé khách hàng. |
| ERR_MSG | Nội dung lỗi liên quan, có thể bao gồm dữ liệu cá nhân. |
| UPDATE_LEVEL | Mức độ cập nhật cho vé khách hàng. |
| CSKH_STATUS | Trạng thái chăm sóc khách hàng liên quan đến vé. |
| STAGE_TICKET | Giai đoạn của vé khách hàng hiện tại. |
| PROCESS_TICKET | Quá trình xử lý vé khách hàng. |
| IS_PROD_ISSUE | Có vấn đề sản phẩm (1) hoặc không (0). |
| SOURCE_REQUEST_1 | Nguồn yêu cầu lần thứ nhất của vé khách hàng. |
| CALL_CENTER_ID | ID trung tâm gọi điện liên quan đến vé khách hàng. |
| CONVERSATIONID | ID cuộc hội thoại liên quan đến vé khách hàng. |
| PROCESS_TYPE | Loại quá trình xử lý của vé khách hàng. |
| CT3 | CT3 liên quan đến vé khách hàng. |
| attach_file | Tệp đính kèm liên quan, có thể bao gồm dữ liệu cá nhân. |
| EXTRA_QUESTIONS | Các câu hỏi thêm từ khách hàng, có thể bao gồm dữ liệu cá nhân. |
| CLOSE_BY | Người đóng vé khách hàng. |
| PROCESS_BY | Người xử lý vé khách hàng. |
| CLAIM_DATE | Ngày khách hàng làm đơn khiếu nại. |
| AUTO_PROCESS | Quá trình tự động xử lý vé khách hàng. |
| FIRST_REPLY_DATE | Ngày trả lời đầu tiên cho vé khách hàng. |
| LAST_REPLY_DATE | Ngày trả lời cuối cùng cho vé khách hàng. |
| CHUYEN_BPLQ_1 | Ngày chuyển bộ phận liên quan lần thứ nhất của vé. |
| BPLQ_PHANHOI_1 | Ngày bộ phận liên quan phản hồi lần thứ nhất. |
| BPLQ_1 | Thông tin bộ phận liên quan lần thứ nhất. |
| SLA_CAMKET_BPLQ_1 | Thời gian SLA cam kết cho bộ phận liên quan lần thứ nhất. |
| SLA_THUCTE_BPLQ_1 | Thời gian SLA thực tế cho bộ phận liên quan lần thứ nhất. |
| CHUYEN_BPLQ_2 | Ngày chuyển bộ phận liên quan lần thứ hai của vé. |
| BPLQ_PHANHOI_2 | Ngày bộ phận liên quan phản hồi lần thứ hai. |
| BPLQ_2 | Thông tin bộ phận liên quan lần thứ hai. |
| SLA_CAMKET_BPLQ_2 | Thời gian SLA cam kết cho bộ phận liên quan lần thứ hai. |
| SLA_THUCTE_BPLQ_2 | Thời gian SLA thực tế cho bộ phận liên quan lần thứ hai. |
| CHUYEN_BPLQ_3 | Ngày chuyển bộ phận liên quan lần thứ ba của vé. |
| BPLQ_PHANHOI_3 | Ngày bộ phận liên quan phản hồi lần thứ ba. |
| BPLQ_3 | Thông tin bộ phận liên quan lần thứ ba. |
| SLA_CAMKET_BPLQ_3 | Thời gian SLA cam kết cho bộ phận liên quan lần thứ ba. |
| SLA_THUCTE_BPLQ_3 | Thời gian SLA thực tế cho bộ phận liên quan lần thứ ba. |
| SLA_CAMKET_TICKET | Thời gian SLA cam kết cho xử lý vé khách hàng tổng thể. |
| SLA_THUCTE_TICKET | Thời gian SLA thực tế cho xử lý vé khách hàng tổng thể. |
| SLA_CAMKET_TIEPNHAN | Thời gian SLA cam kết cho việc tiếp nhận vé khách hàng. |
| SLA_THUCTE_TIEPNHAN | Thời gian SLA thực tế cho việc tiếp nhận vé khách hàng. |
| AGENT_PHANLOAI_1 | Thông tin về agent phân loại lần thứ nhất của vé. |
| SLA_CAMKET_PHANLOAI_1 | Thời gian SLA cam kết cho phân loại lần thứ nhất. |
| SLA_THUCTE_PHANLOAI_1 | Thời gian SLA thực tế cho phân loại lần thứ nhất. |
| AGENT_PHANLOAI_2 | Thông tin về agent phân loại lần thứ hai của vé. |
| SLA_CAMKET_PHANLOAI_2 | Thời gian SLA cam kết cho phân loại lần thứ hai. |
| SLA_THUCTE_PHANLOAI_2 | Thời gian SLA thực tế cho phân loại lần thứ hai. |
| AGENT_PHANLOAI_3 | Thông tin về agent phân loại lần thứ ba của vé. |
| SLA_CAMKET_PHANLOAI_3 | Thời gian SLA cam kết cho phân loại lần thứ ba. |
| SLA_THUCTE_PHANLOAI_3 | Thời gian SLA thực tế cho phân loại lần thứ ba. |
| AGENT_PHANLOAI_4 | Thông tin về agent phân loại lần thứ tư của vé. |
| SLA_CAMKET_PHANLOAI_4 | Thời gian SLA cam kết cho phân loại lần thứ tư. |
| SLA_THUCTE_PHANLOAI_4 | Thời gian SLA thực tế cho phân loại lần thứ tư. |
| AGENT_CHUYEN_XL_VE_TN | Thông tin về agent chuyển xử lý về tiếp nhận của vé. |
| SLA_CAMKET_CHUYEN_XL_VE_TN | Thời gian SLA cam kết cho chuyển xử lý về tiếp nhận. |
| SLA_THUCTE_CHUYEN_XL_VE_TN | Thời gian SLA thực tế cho chuyển xử lý về tiếp nhận. |
| AGENT_PHANHOI_VA_TIEPNHAN_1 | Thông tin về agent phản hồi và tiếp nhận lần thứ nhất của vé. |
| SLA_CAMKET_PHANHOI_VA_TIEPNHAN_1 | Thời gian SLA cam kết cho phản hồi và tiếp nhận lần thứ nhất. |
| SLA_THUCTE_PHANHOI_VA_TIEPNHAN_1 | Thời gian SLA thực tế cho phản hồi và tiếp nhận lần thứ nhất. |
| AGENT_PHANHOI_VA_TIEPNHAN_2 | Thông tin về agent phản hồi và tiếp nhận lần thứ hai của vé. |
| SLA_CAMKET_PHANHOI_VA_TIEPNHAN_2 | Thời gian SLA cam kết cho phản hồi và tiếp nhận lần thứ hai. |
| SLA_THUCTE_PHANHOI_VA_TIEPNHAN_2 | Thời gian SLA thực tế cho phản hồi và tiếp nhận lần thứ hai. |
| AGENT_PHANHOI_VA_TIEPNHAN_3 | Thông tin về agent phản hồi và tiếp nhận lần thứ ba của vé. |
| SLA_CAMKET_PHANHOI_VA_TIEPNHAN_3 | Thời gian SLA cam kết cho phản hồi và tiếp nhận lần thứ ba. |
| SLA_THUCTE_PHANHOI_VA_TIEPNHAN_3 | Thời gian SLA thực tế cho phản hồi và tiếp nhận lần thứ ba. |
| AGENT_PHANHOI_VA_TIEPNHAN_4 | Thông tin về agent phản hồi và tiếp nhận lần thứ bốn của vé. |
| SLA_CAMKET_PHANHOI_VA_TIEPNHAN_4 | Thời gian SLA cam kết cho phản hồi và tiếp nhận lần thứ bốn. |
| SLA_THUCTE_PHANHOI_VA_TIEPNHAN_4 | Thời gian SLA thực tế cho phản hồi và tiếp nhận lần thứ bốn. |
| AGENT_XULY | Thông tin về agent xử lý vé khách hàng. |
| PROCESS_BY_TOOL | Quá trình xử lý vé khách hàng bằng công cụ. |
| SLA_CAMKET_XULY | Thời gian SLA cam kết xử lý. |
| SLA_THUCTE_XULY | Thời gian SLA thực tế xử lý. |
| UPDATE_LEVEL_INDEX | Chỉ số mức độ cập nhật cho vé khách hàng. |
| NULL_LEVEL_CREATED | Mức độ tạo mới khi cấp độ bị null. |
| RECEIVE_TIME_INT | Thời gian tiếp nhận yêu cầu khách hàng dưới dạng integer. |
| RECEIVE_TIME | Thời gian tiếp nhận yêu cầu từ khách hàng. |
| PARENT_ID_AUTO | ID cha tự động liên quan đến vé khách hàng. |
| PHONE_NUMBER | Số điện thoại liên quan đến vé khách hàng. |
| PARENT_PHONE_NUMBER | Số điện thoại của vé cha liên quan. |
| Rating | Điểm đánh giá từ khách hàng. |
| solved | Số vé đã được giải quyết. |
| WorkingDays | Số ngày làm việc xử lý vé. |
| CASE_NAME | Tên case liên quan đến vé khách hàng. |
| STATUS_CASE_ID | Trạng thái của case liên quan đến vé khách hàng. |
| CASE_ID_REVAMP | ID trường hợp được sửa đổi liên quan đến vé khách hàng. |
| MOMO_WALLET | Ví MoMo liên quan đến vé khách hàng. |
| SOURCE | Nguồn yêu cầu hoặc thông tin ban đầu của vé khách hàng. |
| END_DATE_CASE_ID | Ngày kết thúc liên quan đến case ID. |
| CREATED_DATE_CASE_ID | Ngày tạo liên quan đến case ID. |
| IS_CASE_ID | ID của trường hợp xử lý vấn đề. |

---

### Data Example

Empty DataFrame
Columns: [TICKET_ID, STATUS, CREATED_DATE, HOUR_CREATED_DATE, CREATED_TIME, PROCESS_DATE, CLOSE_DATE, CLOSE_TIME, RATING_DATE, RATING_TIME, TICKET_TYPE, SOURCE_REQUEST, BU, Level0, Level1, Level2, Level3, Level4, Quy_trinh, ALL_SLA_TIME, EXPECTED_TIME, SLA_TIME, SLA_TIME_RECEIVE, STATUS_PROCESS, CONTENTS, TICKET_DA_TIEP_NHAN, SUPPORT_ATTITUDE, SPEED_FEEDBACK, SATISFACTION_LEVEL, comment_after_rating, Q_01, vt01, Q_02, vt0s, Q_03, vt03, Q_04, vt04, Q_05, vt05, Q_06, vt06, TRANS_NAME, TRANS_TAG, GROUP_XU_LY, GROUP_CLOSE_TICKET, TIME_THUC_TE_TIEPNHAN, TIME_THUC_TE_XULY, ASSIGN_BY, TID, PARENT_ID, Is_last_ticket, merge_ticket, ALLOW_COMMENT, CUS_COMMENT, IS_AUTO, ERR_ID, UPDATE_LEVEL, CSKH_STATUS, STAGE_TICKET, PROCESS_TICKET, IS_PROD_ISSUE, SOURCE_REQUEST_1, CALL_CENTER_ID, CONVERSATIONID, PROCESS_TYPE, CT3, CLOSE_BY, PROCESS_BY, CLAIM_DATE, AUTO_PROCESS, FIRST_REPLY_DATE, LAST_REPLY_DATE, CHUYEN_BPLQ_1, BPLQ_PHANHOI_1, BPLQ_1, SLA_CAMKET_BPLQ_1, SLA_THUCTE_BPLQ_1, CHUYEN_BPLQ_2, BPLQ_PHANHOI_2, BPLQ_2, SLA_CAMKET_BPLQ_2, SLA_THUCTE_BPLQ_2, CHUYEN_BPLQ_3, BPLQ_PHANHOI_3, BPLQ_3, SLA_CAMKET_BPLQ_3, SLA_THUCTE_BPLQ_3, SLA_CAMKET_TICKET, SLA_THUCTE_TICKET, SLA_CAMKET_TIEPNHAN, SLA_THUCTE_TIEPNHAN, AGENT_PHANLOAI_1, SLA_CAMKET_PHANLOAI_1, SLA_THUCTE_PHANLOAI_1, AGENT_PHANLOAI_2, SLA_CAMKET_PHANLOAI_2, SLA_THUCTE_PHANLOAI_2, AGENT_PHANLOAI_3, SLA_CAMKET_PHANLOAI_3, ...]
Index: []

---

## Knowledge Base

(Empty)

---

## Memory

(Empty)

---

## Error Message

(Empty)