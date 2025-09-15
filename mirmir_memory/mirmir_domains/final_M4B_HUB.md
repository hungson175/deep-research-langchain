# M4B HUB Domain

## Basic Information

- **ID**: 5d47c7cc-f998-41c5-ab4c-5caa4b441743
- **Name**: M4B HUB
- **Description**: Domain này chứa data engagement của merchant vào M4B (Sẽ bao gồm các touch point khác thuộc M4B quản lý)
- **Instructions**: (Not specified)
- **Error Code**: 200

---

## Dataset Schema Information

### Dataset Name: M4B HUB

---

## Table 1: project-5400504384186300846.MBI_DA.dim_m4b_merchant_profile

**Description**:
Bảng dimension chứa thông tin liên quan đến hồ sơ merchant trên Dịch vụ M4B của MoMo. Bảng này được sử dụng để phân tích các tiêu chí và chỉ số liên quan đến việc sử dụng và tương tác của merchant qua các loại tính năng trên hệ thống.

**Use Cases**:
- Cung cấp thông tin định danh và hồ sơ chi tiết của merchant trên nền tảng.
- Theo dõi quá trình tương tác và sử dụng các tính năng của merchant.
- Phân tích mô hình chấp nhận tính năng và chỉ số tương tác của merchant qua các lần sử dụng đầu tiên.

### Columns

| Column Name | Description |
|-------------|-------------|
| merchant_code | Mã định danh duy nhất của merchant trong hệ thống M4B. |
| id | Merchant ID. |
| merchant_size | Kích thước của merchant, có thể là nhỏ, trung bình, hoặc lớn. |
| created_date | Ngày mà merchant được tạo mới trong hệ thống. |
| created_datetime | Ngày và thời gian mà merchant được tạo mới trong hệ thống. |
| agent_id | Mã định danh cho mỗi ví MoMo của merchant. |
| brand_name | Tên thương hiệu của merchant. |
| merchant_name_m4b | Tên merchant trên dịch vụ M4B. |
| merchant_name_sl | Tên merchant trên nền tảng SL. |
| merchant_type_m4b | Loại hình merchant trong hệ thống M4B. |
| merchant_onboarding_type | Loại hình onboarding của merchant. |
| full_address | Địa chỉ đầy đủ của merchant. |
| city_name | Tên thành phố của merchant. |
| district_name | Tên quận của merchant. |
| ward_name | Tên phường của merchant. |
| street_name | Tên đường nơi merchant hoạt động. |
| house_number | Số nhà của merchant. |
| longitude | Tọa độ kinh độ của vị trí merchant. |
| latitude | Tọa độ vĩ độ của vị trí merchant. |
| category_sl_lv1 | Danh mục cấp 1 của merchant trên nền tảng SL. |
| category_sl_lv2 | Danh mục cấp 2 của merchant trên nền tảng SL. |
| category_sl_lv3 | Danh mục cấp 3 của merchant trên nền tảng SL. |
| category_sl_lv4 | Danh mục cấp 4 của merchant trên nền tảng SL. |
| payment_age_in_month | Tuổi thọ tính theo tháng của khả năng thanh toán của merchant. |
| first_transaction_date | Ngày diễn ra giao dịch đầu tiên của merchant. |
| first_engage_date | Ngày đầu tiên mà merchant có tương tác với dịch vụ M4B (có thể trước ngày tạo ra nếu merchant đã được liên kết với một agent_id có sẵn). |
| is_merchant_pinned_to_home | True: Merchant đã từng ghim M4B vào trang chủ, False: Merchant chưa từng ghim. |
| is_merchant_pinned_to_home_in_7d | True: Merchant đã ghim M4B vào trang chủ trong 7 ngày đầu tiên, False: không ghim. |
| is_merchant_still_pinned_to_home | True: Merchant vẫn còn ghim M4B vào trang chủ, False: không ghim. |
| is_merchant_turn_on_ttt | True: Merchant đã từng kích hoạt thanh toán TTT, False: chưa kích hoạt. |
| is_merchant_turn_on_ttt_in_7d | True: Merchant kích hoạt thanh toán TTT trong vòng 7 ngày đầu tiên, False: không kích hoạt. |
| first_tran_ttt_date | Ngày diễn ra giao dịch TTT đầu tiên. |
| first_tran_ttt_datetime | Ngày và thời gian diễn ra giao dịch TTT đầu tiên. |
| is_merchant_have_tran_ttt | True: Merchant đã từng thực hiện giao dịch với TTT, False: chưa thực hiện. |
| is_merchant_have_tran_ttt_in_7d | True: Merchant có giao dịch TTT trong vòng 7 ngày đầu tiên, False: không có. |
| is_merchant_have_tran_ttt_bank_cashout | True: Merchant đã từng thực hiện giao dịch rút tiền từ ngân hàng qua TTT, False: chưa thực hiện. |
| is_merchant_have_tran_ttt_bank_cashout_in_7d | True: Merchant thực hiện giao dịch rút tiền từ ngân hàng qua TTT trong 7 ngày đầu tiên, False: không có giao dịch. |
| first_auto_bank_cashout_date | Ngày diễn ra giao dịch tự động rút tiền từ ngân hàng đầu tiên của merchant. |
| first_auto_bank_cashout_datetime | Ngày và thời gian diễn ra giao dịch tự động rút tiền từ ngân hàng đầu tiên của merchant. |
| is_merchant_have_tran_auto_bank_cashout | True: Merchant đã từng thực hiện giao dịch tự động rút tiền từ ngân hàng, False: chưa thực hiện. |
| is_merchant_have_tran_auto_bank_cashout_in_7d | True: Merchant thực hiện giao dịch tự động rút tiền từ ngân hàng trong 7 ngày đầu tiên, False: không có giao dịch. |
| is_merchant_map_soundbox_in_7d | True: Merchant đã liên kết soundbox trong 7 ngày đầu tiên (có thể đã liên kết trước khi có tương tác M4B), False: chưa liên kết. |
| is_soundbox_merchant | True: Merchant đã từng liên kết soundbox, False: chưa liên kết. |
| first_map_soundbox_date | Ngày diễn ra liên kết soundbox lần đầu tiên. |
| is_merchant_have_sb_transaction_in_7d | True: Merchant có giao dịch soundbox trong vòng 7 ngày đầu tiên, False: không có giao dịch. |
| first_sb_transaction_date | Ngày diễn ra giao dịch soundbox đầu tiên. |
| is_merchant_have_sound_noti_in_7d | True: Merchant kích hoạt thông báo âm thanh trong 7 ngày đầu tiên, False: không kích hoạt. |
| first_sound_noti_date | Ngày diễn ra thông báo âm thanh lần đầu tiên. |
| is_merchant_have_staff_accept_in_7d | True: Merchant có nhân viên chấp nhận lời mời trong 7 ngày đầu tiên, False: không có. |
| first_staff_accept_date | Ngày nhân viên chấp nhận lời mời lần đầu tiên. |
| gender | Giới tính của merchant. |
| age | Tuổi của merchant. |
| age_group | Nhóm tuổi của merchant. |
| momo_age_in_month | Tuổi trên MoMo của merchant tính theo tháng. |

### Smart Top Values

- **age_group**: ['7.N/A' '4.28-35' '3.23-27' '5.36-50' '6.>50' '1.<18' '2.18-22']
- **gender**: ['female' 'male' 'unknown']
- **category_sl_lv4**: ['ACCOMMODATION' 'AUTO MAINTENANCE' 'BAKERY / SWEETS' 'BAR / CLUB' 'BEVERAGE - OTHER' 'BOOKSTORE / TOYS' 'CINEMA' 'CLEANING SERVICE' 'CLINIC / SALON' 'COFFEE' 'COMFORT FOOD / STREET FOOD' 'CVS' 'DENTAL CLINIC' 'DINING' 'EDUCATION - OTHER' 'EVENT / CONFERENCE' 'EXPERIENCE' 'FASHION / ACCESSORIES' 'FAST FOOD' 'FLIGHTS' 'FOOD COURT' 'FORMAL SCHOOL / UNIVERSITY' 'GAMING' 'GYM' 'HEALTH AND BEAUTY / DRUGSTORE' 'HOME LIVING / ELECTRONICS' 'HOSPITAL' 'HOUSEHOLD MAINTENANCE' 'KARAOKE' 'LANGUAGE CENTER' 'LAUNDRY' 'LOTTERY' 'MALL / DEPARTMENT STORE' 'MILK TEA' 'MINIMART' 'MOM AND KIDS' 'NAIL' 'OTT' 'PET SERVICE' 'PHOTOCOPY / PRINTING' 'SPA / MASSAGE' 'SPORTS / RECREATION / PLAYGROUND' 'SUPERMARKET' 'TRADITIONAL MARKET / GROCERY STORE / SPECIALTY STORE' 'TRAVEL - OTHER' 'VENDING MACHINE']
- **category_sl_lv1**: ['SME OFFLINE' 'TOPBRAND OFFLINE']
- **category_sl_lv2**: ['SERVICE' 'FNB' 'RETAIL']
- **category_sl_lv3**: ['SERVICE - OTHER' 'SHOPPING' 'FOOD' 'BEVERAGE' 'HOME & MAINTENANCE' 'TRAVEL' 'ENTERTAINMENT' 'GROCERY' 'BEAUTY & SPA' 'HEALTH & MEDICAL' 'EDUCATION' 'GOOGLE']
- **merchant_type_m4b**: ['TOP_BRAND' 'BPU' 'MINI_WEB' 'SME' 'PRE_MERCHANT' 'AGENT_NETWORK' 'DONATION_MERCHANT' 'BUDDHIST_SANGHA' 'P2SU' 'MERCHANT' 'MINI_APP' 'P2M' 'OTHER']
- **merchant_onboarding_type**: ['INDIVIDUAL_NON_VERIFIED_SELF_ONBOARDING' 'INDIVIDUAL_SALE_ONBOARDING' 'INDIVIDUAL_SELF_ONBOARDING' 'ENTERPRISE_SELF_ONBOARDING']
- **brand_name**: Multiple brands including utilities companies, retail stores, restaurants, and service providers
- **merchant_size**: ['UNDEFINED' 'SME OFFLINE' 'TOPBRAND OFFLINE']

---

## Table 2: project-5400504384186300846.MBI_DA.fact_m4b_event

**Description**:
Fact table chứa dữ liệu event của Momo for Business (M4B). Dùng để theo dõi và phân tích các sự kiện của merchant trong hệ thống M4B.

**Information Available**:
- Phân tích dữ liệu sự kiện của merchant trong M4B
- Xác định các màn hình và trigger liên quan đến từng sự kiện
- Kiểm tra và tối ưu phiên bản và hệ điều hành của ứng dụng M4B

### Columns

| Column Name | Description |
|-------------|-------------|
| date | Ngày diễn ra event |
| datetime | Thời điểm của sự kiện |
| event_id | Mã định danh duy nhất của sự kiện |
| momo_session_id_v2 | ID session của MoMo v2 |
| agent_id | Mã định danh của agent. Join với bảng dim_m4b_user để lấy merchant_code |
| m4b_screen_id | Mã màn hình M4B nơi xảy ra sự kiện. Map với bảng dm_m4b_screen để lấy mô tả |
| non_defined_screen_name | Tên màn hình chưa được xác định trong dim_m4b_screen |
| global_trigger_id | Global trigger_id. Dùng để xác định sự kiện. Mapping với bảng dim_m4b_global_trigger để lấy thông tin |
| device_os | Hệ điều hành của thiết bị |
| app_version | Phiên bản ứng dụng của M4B |
| service_name | Tên dịch vụ |
| screen_name | Tên màn hình |
| event_name | Tên sự kiện |
| block_name | Tên block |
| button_name | Tên nút |
| component_name | Tên thành phần |
| tab_name | Tên tab |
| icon_name | Tên icon |
| api | API |
| status | Trạng thái |
| error_code | Mã lỗi |
| error_reason | Lý do lỗi |
| login_account | Tài khoản đăng nhập |
| raw_merchant_code | Raw merchant_code được truyền từ hệ thống M4B. Chưa được xác minh |

### Smart Top Values

- **status**: ['on' 'FAIL' 'success' 'failed' 'SUCCESS' 'fail' 'deactive' 'off' 'active']
- **device_os**: ['Android' 'iOS' 'ANDROID' 'IOS']

---

## Table 3: project-5400504384186300846.MBI_DA.dim_m4b_trigger

**Description**:
Bảng dimension này lưu trữ thông tin về các trigger trong hệ thống M4B của MoMo. Những thông tin này bao gồm mã định danh toàn cầu của trigger, tên và chức năng của màn hình, và các mô tả liên quan đến trigger. Bảng này có thể được sử dụng để quản lý và theo dõi các trigger trong ứng dụng M4B, hỗ trợ trong việc kiểm tra và điều chỉnh các hành động tự động trong hệ thống, và phục vụ việc phân tích các sự kiện đã xảy ra trong ứng dụng.

### Columns

| Column Name | Description |
|-------------|-------------|
| Stt | Số thứ tự của trigger trong danh sách. |
| global_trigger_id | Mã định danh toàn cầu cho trigger. |
| function | Chức năng của trigger. |
| screen_name | Tên của màn hình liên quan đến trigger. |
| description | Mô tả về trigger. |
| old_description | Mô tả cũ về trigger. |
| description_trackify | Mô tả sử dụng để trackify trigger. |
| link | Link liên kết với thông tin chi tiết của trigger. |
| po_pic | Hình ảnh liên quan đến Product Owner của trigger. |
| note | Ghi chú thêm về trigger. |

### Smart Top Values

- **function**: ['5. Sự cố và hỗ trợ' '1. Vận hành căn bản' '3. Trợ thủ tài chính' '7. Khám phá' '6. Soundbox và cross sale ipos' '4. Dòng tiền và tác vụ liên quan ']
- **screen_name**: ['account_info' 'add_revenue' 'financial_assistant' 'home' 'login' 'notification_setting' 'order_soundbox_detail' 'payout_history' 'qr_detail' 'soundbox_home' 'staff_account_management' 'staff_invite' 'staff_invite_detail' 'start_app' 'store_management' 'tabbar' 'trans_detail' 'trans_history' 'transaction_detail' 'trending_aggregation' 'trending_detail']

---

## Table 4: project-5400504384186300846.MBI_DA.dim_m4b_screen

**Description**:
Bảng dimension chứa thông tin chi tiết về các màn hình trong hệ thống M4B (Momo for Business).

**Use Cases**:
- Theo dõi và quản lý các màn hình trong hệ thống M4B.
- Kiểm tra và cải thiện tính năng engagement của các màn hình.
- Phân tích mối liên hệ giữa màn hình và chức năng của chúng.

### Columns

| Column Name | Description |
|-------------|-------------|
| id | Mã định danh duy nhất cho mỗi màn hình trong hệ thống M4B. |
| screen_name | Tên của màn hình trong hệ thống M4B. |
| function | Chức năng của màn hình trong hệ thống M4B. |
| description | Mô tả chi tiết về màn hình trong hệ thống M4B. |
| old_description | Mô tả cũ của màn hình, trước khi được cập nhật trong hệ thống M4B. |
| is_engagement | Giá trị boolean cho biết liệu màn hình có thuộc dạng engagement hay không (true: là màn hình engagement, false: không phải). |
| link | Đường dẫn liên kết tới nội dung hoặc tài liệu liên quan đến màn hình. |
| po_pic | Thông tin về người sở hữu hoặc chịu trách nhiệm về màn hình trong hệ thống M4B. |
| note | Ghi chú phụ thêm liên quan đến màn hình. |

### Smart Top Values

- **function**: ['3. Trợ thủ tài chính']
- **screen_name**: ['(Không điền screen name vào đây)' 'home' 'trans_history' 'tabbar' 'start_app' 'login' 'store_management' 'account_info' 'order_soundbox_detail' 'payout_history' 'staff_account_management' 'qr_detail' 'notification_setting' 'staff_invite' 'financial_assistant' 'staff_invite_detail' 'soundbox_home' 'add_revenue' 'trans_reconcile_detail' 'trending_aggregation' 'nfc_owner' 'trending_detail' 'nfc_staff' 'intro' 'news_feed' 'trans_detail' 'receiving_money_config' 'soundbox_management' 'mapping_soundbox' 'soundbox_order_confirm' 'ec_benefit' 'paylater_setting' 'scan_qr_payment' 'scan_qr_soundbox' 'sb_address_book' 'ec_detail' 'staff_info' 'welcome_new_ec' 'unregistered_nike' 'soundbox_order_detail' 'registered_nike' 'Đối tác MoMo' 'orders_history']

---

## Table 5: project-5400504384186300846.MBI_DA.dim_m4b_user

**Description**:
Bảng dimension lưu thông tin tất cả các agent_id được định nghĩa là merchant owner trên hệ thống phân quyền. Mỗi agent_id có thể liên kết với một hoặc nhiều mã merchant.

**Information Available**:
- Mã định danh duy nhất của agent_id
- Số điện thoại liên quan đến agent_id
- Mã merchant và số lượng mã merchant liên kết với agent_id

### Columns

| Column Name | Description |
|-------------|-------------|
| agent_id | Mã định danh duy nhất của tất cả agent_id được định nghĩa là merchant owner. |
| phone | Số điện thoại liên quan đến agent_id. |
| merchant_code | Mã định danh merchant của agent. Hiện tại chỉ lấy merchant code cho những agent có 1 merchant code duy nhất. |
| merchant_code_count | Số lượng mã merchant liên kết với agent. |
| secondary_merchant_code | Mã định danh merchant của agent có nhiều hơn 1 merchant. Lấy tạm merchant tạo gần nhất. |
| merchant_owner | Hiện tại chỉ có giá trị 'YES', xác nhận có phải merchant_owner hay không. |
| is_merchant_owner | Hiện tại chỉ có giá trị 'YES', xác nhận có phải merchant_owner hay không. |

---

## Table 6: project-5400504384186300846.MBI_DA.fact_m4b_engage_merchant_weekly

**Description**:
Bảng fact theo dõi hoạt động hàng tuần của đối tác MoMo.

**Objectives**:
- Theo dõi số ngày engage và số session engage trong tuần của merchant.
- Xác định trạng thái của merchant trong tuần với các loại engage: new_engage, retain_merchant, reactivate_merchant.
- Phân tích khả năng quay lại và hoạt động tiếp theo của merchant dựa trên tuần trước và tuần tiếp theo.

### Columns

| Column Name | Description |
|-------------|-------------|
| merchant_code | Mã định danh của đối tác MoMo. |
| days_engaged | Số ngày đối tác MoMo engage trong tuần. |
| sessions | Tổng số phiên engage của đối tác MoMo trong tuần. |
| merchant_size | Quy mô của đối tác MoMo. |
| is_soundbox_merchant | Đối tác MoMo có đang được map với Soundbox trong tuần engagement. |
| engage_week | Tuần bắt đầu engage của đối tác MoMo, bắt đầu từ thứ 2. |
| retain_week | Tuần nếu đối tác MoMo quay lại, NULL nếu không quay lại. |
| next_week | Tuần tiếp theo sau tuần engage. |
| retain_merchant_code | Mã đối tác MoMo nếu quay lại trong tuần tiếp theo, NULL nếu không quay lại. |
| retain_merchant_code_wtd | (Chỉ tính tới D-1 của mỗi tuần) Mã đối tác MoMo nếu quay lại trong tuần tiếp theo, NULL nếu không quay lại. |
| engaged_week_type | Phân loại hoạt động của đối tác MoMo trong tuần: 1. new_engage, 2. retain_merchant, 3. reactivate_merchant, 4. Error. |
| previous_engage_week | Tuần engage trước đó của đối tác MoMo, NULL cho merchant mới. |
| onboarding_week | Tuần đầu tiên đối tác MoMo bắt đầu hoạt động. |
| is_merchant_pinned_to_home | True: Đối tác MoMo được pin vào HOME trong tuần engagement, False: không được pin vào home. |
| last_event_time | Thời gian cuối cùng có event của đối tác MoMo trong tuần engagement. |

### Smart Top Values

- **engaged_week_type**: ['1.new_engage' '2.retain_merchant' '3.reactivate_merchant']
- **days_engaged**: ['1' '2' '3' '7' '4' '6' '5']
- **is_soundbox_merchant**: ['NO' 'YES']
- **merchant_size**: ['SME OFFLINE' 'UNDEFINED' 'TOPBRAND OFFLINE']

---

## Additional Tables Summary

### Table 7: fact_m4b_session
**Description**: Bảng fact thông tin sessions của merchant vào M4B.

### Table 8: fact_m4b_active_merchant_monthly
**Description**: Bảng fact để tính toán các đặc điểm sử dụng của merchant trong một tháng, tập trung vào merchant đang hoạt động.

### Table 9: natra_m4b_metric_weekly
**Description**: Bảng lưu weekly metric của M4B SME OFFLINE merchants, base là merchant active payment.

### Table 10: fact_m4b_lsgd_event
**Description**: Bảng này lưu event trong màn hình lịch sử giao dịch của những user được define là merchant.

### Table 11: dim_m4b_all_trigger
**Description**: Bảng dimension lưu toàn bộ global_trigger_id hiện tại từ ứng dụng M4B.

---

## Knowledge Base

(Empty)

---

## Memory

(Empty)