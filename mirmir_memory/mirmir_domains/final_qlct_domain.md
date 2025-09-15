# QLCT Domain Response

## Error Code
200

## Data

### ID
af241589-f5be-4b97-8928-fe0823c8dc75

### Name
QLCT

### Description
Records number of visitors by QLCT breaky by monthly user type and day

### Instructions
(empty)

## Schema DDL

### Dataset Name
QLCT

## Table 1: SEMANTIC_QLCT_VISIT

### Table Name
`momovn-prod.MBI_DA.SEMANTIC_QLCT_VISIT`

### Table Description
Bảng dữ liệu theo dõi hoạt động và hành vi của người dùng đối với các sản phẩm TFBV, QLCT và MONI. Có thể dùng để:
- Phân tích tần suất và xu hướng sử dụng trong tháng và tuần đối với từng sản phẩm
- Xác định phân khúc người dùng dựa trên số lượng và giá trị giao dịch hàng tháng
- Đánh giá mức độ quay lại của người dùng qua các tháng và tuần.

### Columns

| Column Name | Data Type | Description | Example Data |
|-------------|-----------|-------------|--------------|
| `AGENT_ID` | STRING | ID của User | ["7717540","anh.vu2@mservice.com.vn","93408631"] |
| `MONTH` | DATE | Tháng có visit TFBV | ["2024-10-01","2025-09-01","2025-03-01"] |
| `DATE_WEEK` | DATE | Tuần có visit TFBV | ["2024-11-10","2024-11-03","2025-07-20"] |
| `DAY` | STRING | Thứ tự ngày trong tháng có visit TFBV | ["26","22","6"] |
| `PRODUCT` | STRING | Sản phẩm user dùng. Bao gồm: QLCT \| MONI | ["MONI","QLCT"] |
| `ACTION` | STRING | Hành động của user. Bao gồm: VISIT \| CHAT | ["CHAT","VISIT"] |
| `FIRST_MONTH_TFBV` | DATE | Tháng đầu tiên user visit TFBV | ["2024-10-01","2025-09-01","2025-03-01"] |
| `FIRST_MONTH_QLCT` | DATE | Tháng đầu tiên user visit QLCT | ["2024-10-01","2025-09-01","2025-03-01"] |
| `FIRST_MONTH_MONI` | DATE | Tháng đầu tiên user visit MONI | ["2024-10-01","2025-09-01","2025-03-01"] |
| `USER_TYPE_TFBV` | STRING | User type của TFBV theo tháng. Bao gồm: NEW \| RETAIN \| ACTIVE | ["REACTIVE","RETAIN","NEW"] |
| `USER_TYPE_QLCT` | STRING | User type của QLCT theo tháng. Bao gồm: NEW \| RETAIN \| ACTIVE | ["REACTIVE","RETAIN","NEW"] |
| `USER_TYPE_MONI` | STRING | User type của MONI theo tháng. Bao gồm: NEW \| RETAIN \| ACTIVE | ["REACTIVE","RETAIN","NEW"] |
| `MONTHLY_RETAIN_TFBV` | STRING | User TFBV có quay lại vào tháng tiếp theo | ["anh.vu2@mservice.com.vn","93408631","99823604"] |
| `MONTHLY_RETAIN_QLCT` | STRING | User QLCT có quay lại vào tháng tiếp theo | ["76170937","39343379","82518365"] |
| `MONTHLY_RETAIN_MONI` | STRING | User MONI có quay lại vào tháng tiếp theo | ["97859251","55523245","15910557"] |
| `WEEKLY_RETAIN_TFBV` | STRING | User TFBV có quay lại vào tuần tiếp theo | ["36687865","97859251","96458096"] |
| `WEEKLY_RETAIN_QLCT` | STRING | User QLCT có quay lại vào tuần tiếp theo | ["83840316","65454049","75707657"] |
| `WEEKLY_RETAIN_MONI` | STRING | User MONI có quay lại vào tuần tiếp theo | ["78606525","63109534","56228549"] |
| `MIN_DATE_TFBV` | DATE | Ngày đầu tiên trong tháng user có visit TFBV | ["2025-05-03","2025-05-02","2024-11-03"] |
| `MIN_DATE_QLCT` | DATE | Ngày đầu tiên trong tháng user có visit QLCT | ["2024-12-03","2025-02-15","2024-11-08"] |
| `MIN_DATE_MONI` | DATE | Ngày đầu tiên trong tháng user có visit MONI | ["2024-12-03","2024-11-10","2024-11-08"] |
| `NEW_TO_MONTH_TFBV` | STRING | User lần đầu visit TFBV trong tháng | ["27148829","44105832","30949125"] |
| `NEW_TO_MONTH_QLCT` | STRING | User lần đầu visit QLCT trong tháng | ["63027392","60434384","100198267"] |
| `NEW_TO_MONTH_MONI` | STRING | User lần đầu visit MONI trong tháng | ["27148829","30949125","52053540"] |
| `DATE` | DATE | Ngày có visit TFBV | ["2025-06-11","2025-07-20","2024-11-07"] |
| `count_week` | INTEGER | Số tuần có active TFBV trong tháng | ["1"] |
| `GENDER` | STRING | Giới tính | ["female","unknown","male"] |
| `AGE` | INTEGER | Tuổi | ["82","26","22"] |
| `AGE_GROUP` | STRING | Nhóm tuổi | ["[5]. 31 - 35 y/o","UNKNOWN","[3]. 23 - 26 y/o","[1]. <18 y/o","[6]. 36 - 40 y/o","[2]. 18 - 22 y/o","[4]. 27 - 30 y/o","[7]. >40 y/o"] |
| `IS_A30_USER` | BOOLEAN | User có giao dịch trong 30 ngày gần đây: true: có giao dịch, false: không có giao dịch | ["true","false"] |
| `CITY` | STRING | Tỉnh | ["Bến Tre","Bạc Liêu","Vĩnh Long"] |
| `REGION` | STRING | Khu vực | ["Tây Nguyên","Bắc Trung Bộ","Đồng bằng sông Cửu Long"] |
| `VIETQR_TRANS` | INTEGER | Tổng số giao dịch VIETQR trong tháng | ["82","156","165"] |
| `P2P_TRANS` | INTEGER | Tổng số giao dịch P2P trong tháng | ["22","26","57"] |
| `PAYMENT_TRANS` | INTEGER | Tổng số giao dịch Payment trong tháng | ["22","26","57"] |
| `VIETQR_AMOUNTz` | FLOAT | Tổng giá trị giao dịch VIETQR trong tháng | ["1700000","8889545","39000"] |
| `P2P_AMOUNT` | FLOAT | Tổng giá trị giao dịch P2P trong tháng | ["12333","1525000","13000"] |
| `PAYMENT_AMOUNT` | FLOAT | Tổng giá trị giao dịch Payment trong tháng | ["1635138","2265257","3831699"] |
| `TOTAL_AMOUNT` | FLOAT | Tổng giá trị giao dịch trong tháng | ["20000","66000","4000"] |
| `TOTAL_TRANS` | INTEGER | Tổng số giao dịch trong tháng | ["22","26","57"] |
| `SEGMENT` | STRING | Phân khúc dựa theo số lượng giao dịch trong tháng, bao gồm VIETQR + P2P + Payment: Light: <3, Medium: 3-14, Hardcore >15. Nếu Segment = Null => không có giao dịch trong tháng | ["2. MEDIUM","3. HARDCORE","1. LIGHT"] |
| `BUDGET` | INTEGER | User có tạo Budget trong tháng 0: Không, 1: Có | ["1","0"] |
| `INPUT_TRANSACTION` | INTEGER | User có tạo Thêm giao dịch trong tháng 0: Không, 1: Có | ["1","0"] |
| `CLASSIFY` | INTEGER | User có tạo Phân loại giao dịch trong tháng 0: Không, 1: Có | ["1","0"] |
| `USECASE` | INTEGER | Số dịch vụ User sử dụng trong tháng | ["22","6","9"] |

---

## Table 2: QLCT_CHATBOT_CONVERSATION_LOG

### Table Name
`momovn-prod.MBI_DA.QLCT_CHATBOT_CONVERSATION_LOG`

### Table Description
Bảng này ghi lại nhật ký các cuộc hội thoại giữa người dùng và chatbot Moni trên ứng dụng, bao gồm thông tin về đoạn hội thoại, tin nhắn của người dùng và Moni, thời gian bắt đầu và kết thúc cuộc trò chuyện, loại người dùng theo tháng, và thông tin nhân khẩu học của người dùng.

**Các mục đích sử dụng có thể bao gồm:**
- Phân tích hành vi người dùng và cải thiện trải nghiệm khách hàng trên ứng dụng.
- Đánh giá hiệu suất phản hồi của chatbot Moni.
- Xác định xu hướng và vấn đề thường gặp của người dùng thông qua các hội thoại.

### Columns

| Column Name | Data Type | Description | Example Data |
|-------------|-----------|-------------|--------------|
| `user_id` | STRING | ID của user | ["17628945","95991884","65698902"] |
| `conversation_id` | STRING | ID đoạn hội thoại | ["botQlct.81073133.3cbb3e23612e48f4b186a35d1a6c8981","botQlct.95713120.c5815619ee7b4ae89d077bcb0c2971de","botQlct.51010209.b6f426325e9841e5a623e489c206bd2d"] |
| `event_id` | STRING | ID event | ["botQlct.ba230f29a8cf4227878ee804c76ff1ba","botQlct.5fb0994bdb45439ca378336e6a80ab73","botQlct.b013c6245c414d84827ebfa7b4875db5"] |
| `user_message` | STRING | Tin nhắn của user | ["Tạo thói quen tài chính sớm như nào?","Đúng rồi. hay thiết kế chọn từ ngày nào đến ngày nào chi tiêu","Học chi tiêu trong 30s"] |
| `response_message` | STRING | Tin nhắn Moni trả lời | |
| `state` | STRING | Trạng thái hiện tại của đoạn hội thoại | [Multiple state values listed] |
| `state2` | STRING | Trạng thái phụ của đoạn hội thoại | [Multiple state2 values listed] |
| `start_time` | TIMESTAMP | Thời gian bắt đầu chat | ["2025-04-05 00:24:10+00","2025-04-05 12:13:45+00","2025-04-05 14:49:36+00"] |
| `end_time` | TIMESTAMP | Thời gian kết thúc chat | ["2025-04-05 14:49:36+00","2025-04-05 19:40:55+00","2025-04-05 20:18:16+00"] |
| `event_date` | DATE | Ngày vào Moni chat | ["2024-10-29","2024-06-23","2025-07-20"] |
| `request_flow` | STRING | Luồng yêu cầu của đoạn hội thoại | ["INSIGHT1","GUIDELINE","TUTORIAL","NEXT_INSIGHT1","INSIGHT2","NEXT_INSIGHT4","HOME","NEXT_INSIGHT2","INSIGHT3","NEXT_INSIGHT5","DYNAMIC_FLOW_HIEU_QUA_CHI_TIEU","GUIDELINE_KIEM_SOAT_AN_NGOAI","","GUIDELINE_BITESIZE_TEST","INSIGHT4","NEXT_INSIGHT3","FREE TEXT","INSIGHT5"] |
| `response_flow` | STRING | Luồng phản hồi của đoạn hội thoại | ["GREETING CARD "] |
| `duration` | FLOAT | Khoảng thời gian chat | ["2.491","4.425","5.247"] |
| `topic` | STRING | Chủ đề của đoạn chat | ["Theo dõi & phân tích chi tiêu","Khác","Mẹo tài chính & tiết kiệm","Giải trí nói chuyện phím","Quản lý ngân sách","Ghi chép giao dịch"] |
| `monthly_user_type` | STRING | User type của MONI theo tháng. Bao gồm: NEW, RETAIN, ACTIVE | ["new","retain","reactivate"] |
| `gender` | STRING | Giới tính của người dùng | ["male","female","unknown"] |
| `age` | INTEGER | Tuổi của người dùng | ["99","38","34"] |
| `age_group` | STRING | Nhóm tuổi của người dùng | ["[4]. 27 - 30 y/o","[5]. 31 - 35 y/o","UNKNOWN","[3]. 23 - 26 y/o","[7]. >40 y/o","[1]. <18 y/o","[6]. 36 - 40 y/o","[2]. 18 - 22 y/o"] |
| `region` | STRING | Khu vực của người dùng | ["Đồng bằng sông Hồng","Tây Bắc Bộ","Đồng bằng sông Cửu Long","Tây Nguyên","Bắc Trung Bộ","Đông Bắc Bộ","Nam Trung Bộ","Đông Nam Bộ"] |
| `city` | STRING | Tỉnh của người dùng | ["Lạng Sơn","Điện Biên","Hoà Bình"] |
| `is_a30_user` | BOOLEAN | User có giao dịch trong 30 ngày gần đây. true: có giao dịch; false: không có giao dịch | ["false","true"] |

---

## Table 3: QLCT_EVENT_TRACKING_VER2

### Table Name
`momovn-prod.MBI_DA.QLCT_EVENT_TRACKING_VER2`

### Table Description
Bảng này theo dõi các sự kiện liên quan đến dịch vụ quản lí chi tiêu (QLCT) trên MoMo. Các thông tin trong bảng bao gồm thời gian, sự kiện và chi tiết hành động của người dùng trong ứng dụng.

**Bảng này có thể được sử dụng cho các mục đích sau:**
- Theo dõi hành vi người dùng trên dịch vụ QLCT.
- Phân tích xu hướng sử dụng và tối ưu hóa ứng dụng.
- Đánh giá hiệu quả của các thành phần giao diện.

### Columns

| Column Name | Data Type | Description | Example Data |
|-------------|-----------|-------------|--------------|
| `event_id` | STRING | Mã định danh duy nhất cho mỗi sự kiện | ["Vm2swMlghnXhcbMpyG82M","a8_3DbBMaVyTF8-bC7Bgf","RsCKBAKUNHdSu1zSzvEX6"] |
| `user_id` | STRING | Mã định danh của người dùng thực hiện hành động | ["64170971","63413332","47742111"] |
| `date` | DATE | Ngày xảy ra sự kiện | ["2025-08-31","2025-09-03","2025-07-30"] |
| `week` | DATE | Tuần xảy ra sự kiện | ["2025-06-22","2025-03-30","2025-04-20"] |
| `month` | DATE | Tháng xảy ra sự kiện | ["2025-08-01","2025-06-01","2025-03-01"] |
| `datetime` | TIMESTAMP | Ngày giờ cụ thể khi sự kiện diễn ra | ["2025-06-22 10:21:19.304","2025-06-22 01:36:20.199","2025-06-22 19:54:35.345"] |
| `trigger_id` | STRING | Mã định danh cho sự kiện khởi tạo | |
| `action_event` | STRING | Tên sự kiện hành động của người dùng | ["Swiped","Interacted","Displayed","Clicked","Selected","Inputed","Viewed"] |
| `block_event` | STRING | Tên sự kiện bị chặn hoặc ngăn cản | ["Chi tiết cate","Quản lý recurring","Phân loại giao dịch","Báo cáo tháng","Top nav LSGD","Home Page","Báo cáo tuần","Widget","PLGD ở LSGD","Chọn GD từ quá khứ","Tạo ngân sách","Setting","Onboarding","Thêm giao dịch","Sổ giao dịch","Biến động thu chi"] |
| `description` | STRING | Mô tả chi tiết về sự kiện | ["Homepage - Hiển thị Block rating","User swipe block calendar để đổi qua tháng khác thành công","Homepage - Hiển thị Block tình hình thu chi - Column Chart"] |
| `screen_name` | STRING | Tên màn hình liên quan đến sự kiện | [Multiple screen name values] |
| `event_name` | STRING | Tên của sự kiện được ghi nhận | [Multiple event name values] |
| `component_name` | STRING | Tên của thành phần giao diện liên quan đến sự kiện | [Multiple component name values] |
| `component_type` | STRING | Loại của thành phần giao diện liên quan đến sự kiện | [Multiple component type values] |
| `button_name` | STRING | Tên nút bấm liên quan đến sự kiện | [Multiple button name values] |
| `icon_name` | STRING | Tên biểu tượng liên quan đến sự kiện | ["change_chart","[4, 2, 1, 5, 7, 8, 9, 3]","[4, 2, 1, 0]"] |
| `block_name` | STRING | Tên khối giao diện liên quan đến sự kiện | [Multiple block name values] |
| `status` | STRING | Trạng thái của sự kiện | ["suggest_classify","off","selected","normal_widget","on","unselected","success"] |
| `page` | STRING | Tên trang liên quan đến sự kiện | [Multiple page values] |
| `popup_name` | STRING | Tên popup liên quan đến sự kiện | |
| `checkbox_name` | STRING | Tên của ô chọn liên quan đến sự kiện | ["count_expense_to_report"] |
| `action` | STRING | Hành động người dùng thực hiện liên quan đến sự kiện | ["click","submit","click_placeholder","close","pin"] |
| `tab_name` | STRING | Tên của tab liên quan đến sự kiện | [Multiple tab name values] |
| `type` | STRING | Loại của sự kiện | [Multiple type values] |
| `content_category` | STRING | Danh mục nội dung liên quan đến sự kiện | ["11","1","8"] |

## Knowledgebase
(empty)

## Memory

### 1. Default message exclusion
Exclude messages where user_message = 'default_start_message' from all future queries related to conversations or messages.

### 2. USER_TYPE column
The column named `USER_TYPE` in the provided schema for `momovn-prod.MBI_DA.SEMANTIC_QLCT_VISIT` should be treated as `USER_TYPE_TFBV` based on successful query executions. The `USER_TYPE` column does not exist in the actual table.

### 3. Create budget event
Khi xử lý sự kiện Click tạo ngân sách, sử dụng SCREEN_NAME = 'expense_budget_category_information' và EVENT_NAME = 'service_button_clicked'

### 4. Menu icon click
Khi xử lý sự kiện click vào icon thuộc block menu, sử dụng lower(DESCRIPTION) LIKE 'Homepage - Click vào icon thuộc block Menu%' thay vì lower(block_name) LIKE '%menu%'

### 5. Visit counting
Nếu hỏi về số visit hoặc số lượng user thì phải count (distinct agent_id)

### 6. Retention calculation
Khi tính toán retention từ tháng trước đến ngày 25 của tháng sau, cần sử dụng điều kiện JOIN với T2.MONTH = DATE_ADD(T1.MONTH, INTERVAL 1 MONTH)

### 7. MEU QLCT definition
MEU QLCT = user has PRODUCT = 'QLCT' in that month.

## Error Message
(empty)