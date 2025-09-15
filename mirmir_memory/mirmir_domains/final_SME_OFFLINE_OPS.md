# Domain: SME OFFLINE OPS

## Domain Information
- **ID**: 4ece5632-02ec-4d9d-9ea9-70ed5d6cc1ed
- **Name**: SME OFFLINE OPS
- **Description**: Domain này để tạo các product AI cho 1 số task adhoc offline
- **Instructions**: (Empty)
- **Knowledgebase**: (Empty)
- **Memory**: (Empty)

---

## Table 1: adhoc_m4b_service_list_replicate

**Full Table Name**: `project-5400504384186300846.MBI_DA.adhoc_m4b_service_list_replicate`

**Description**: Bảng replicate này lưu thông tin của dịch vụ trong danh sách để đội ngũ vận hành SME OFFLINE kiểm tra chất lượng nhập liệu trong service_list. Ngoài ra, bảng này được thiết kế để hỗ trợ đội ngũ BO OFFLINE sử dụng MiMir. Có thể ngừng hoạt động nếu không cần sử dụng nữa.

Thông tin có thể lấy từ bảng này bao gồm:
- Danh sách các dịch vụ và mã định danh của chúng
- Tên của merchant và các thông tin liên quan
- Dữ liệu về thời gian và người tạo, cập nhật hoặc xóa thông tin

### Columns (25 total)

| Column Name | Description |
|-------------|-------------|
| `id` | Mã định danh cho từng dịch vụ trong danh sách |
| `service_code` | Mã dịch vụ để nhận dạng và phân loại dịch vụ |
| `service_description` | Mô tả chi tiết về dịch vụ, cung cấp thông tin về chức năng và ưu điểm |
| `bu_name` | Tên đơn vị kinh doanh liên quan đến dịch vụ |
| `bu_group_code_l1` | Mã nhóm cấp 1 của đơn vị kinh doanh |
| `bu_group_code_l2` | Mã nhóm cấp 2 của đơn vị kinh doanh |
| `bu_group_code_l3` | Mã nhóm cấp 3 của đơn vị kinh doanh |
| `bu_group_code_l4` | Mã nhóm cấp 4 của đơn vị kinh doanh |
| `bu_group_code_l5` | Mã nhóm cấp 5 của đơn vị kinh doanh |
| `bu_group_code_l6` | Mã nhóm cấp 6 của đơn vị kinh doanh |
| `group_code_l1` | Mã nhóm cấp 1 không thuộc đơn vị kinh doanh |
| `merchant` | Tên của merchant cung cấp dịch vụ |
| `key_merchant` | Thông tin chính của merchant liên quan đến dịch vụ |
| `key_merchant_2` | Thông tin bổ sung của merchant liên quan đến dịch vụ |
| `key_merchant_3` | Thông tin bổ sung thứ ba của merchant liên quan đến dịch vụ |
| `newvertical` | Ngành dọc mới của dịch vụ |
| `newvertical_merchant` | Ngành dọc của merchant mới liên quan dịch vụ |
| `specialproject` | Dự án đặc biệt liên quan đến dịch vụ |
| `valid_status` | Trạng thái hợp lệ của dịch vụ |
| `created_by` | Email của nhân viên MoMo tạo thông tin dịch vụ |
| `created_time` | Thời gian tạo thông tin dịch vụ |
| `updated_by` | Email của nhân viên MoMo cập nhật thông tin dịch vụ |
| `updated_time` | Thời gian cập nhật thông tin dịch vụ |
| `deleted_by` | Email của nhân viên MoMo xóa thông tin dịch vụ |
| `deleted_time` | Thời gian xóa thông tin dịch vụ |
| `end_time` | Thời gian kết thúc liên quan đến dịch vụ |

**Data Example**: Empty DataFrame - no sample data available

---

## Table 2: DM_OFF_STORE_PROFILE

**Full Table Name**: `project-5400504384186300846.MBI_DA.DM_OFF_STORE_PROFILE`

**Description**: Profile của các store trong hệ thống M4B. Primary key: store_id. Trong bảng có các cột có prefix "merchant_" là những cột thông tin ở level merchant, sẽ lặp lại giữa các store có cùng merchant_id. Các cột không có prefix merchant thì được hiểu là thông tin của store, ví dụ cột city_name được hiểu là city của store nhưng merchant_city_name được hiểu là city của merchant.

Thông tin có thể lấy từ bảng này bao gồm:
- Phân loại dịch vụ và trạng thái hoạt động của các cửa hàng qua các cột như active_status và category_sl_lv1
- Theo dõi thời gian QA và tạo các store/merchant qua các cột như qa_approved_datetime và merchant_created_datetime
- Đánh giá hoạt động kinh doanh với GMV tích lũy và số lượng giao dịch qua các cột như accum_gmv và accum_trans

**Primary Key**: `store_id`

### Columns (84 total)

| Column Name | Description |
|-------------|-------------|
| `store_id` | ID của store, dạng số, khác với mã store_code |
| `store_code` | Mã số của cửa hàng dưới dạng chuỗi ký tự như 'Xzyuabc...', dùng để phân biệt với store_id |
| `merchant_code` | Mã định danh của merchant dưới dạng ký tự, tương tự như MID |
| `merchant_id` | Mã định danh duy nhất của merchant dưới dạng số |
| `latest_state_code` | State code (snapshot) của store |
| `latest_state_name` | Mô tả trạng thái của store dựa vào latest_state_code (ví dụ: đã duyệt, chưa QA, đã thanh lý,...) |
| `brand_name` | Tên thương hiệu trên M4B, có thể giống nhau giữa nhiều merchant_id khác nhau |
| `merchant_name_m4b` | Tên merchant được hiển thị trên M4B, có thể khác với tên trên service list hoặc brand name |
| `merchant_name_sl` | Tên merchant trên danh sách dịch vụ, có thể có nhiều agent dẫn đến nhiều phân loại |
| `store_name` | Tên cửa hàng trên hệ thống M4B |
| `representative_name` | Tên người đại diện của merchant |
| `merchant_created_date` | Ngày merchant được tạo trên hệ thống m4b |
| `merchant_created_datetime` | Thời điểm merchant được tạo ra trên hệ thống m4b |
| `merchant_qa_approved_datetime` | Thời điểm merchant được QA approve, nếu trạng thái hiện tại là QA Đã Duyệt |
| `merchant_qa_approved_date` | Ngày mà merchant được QA approve, nếu trạng thái hiện tại là QA Đã Duyệt |
| `created_datetime` | Thời điểm tạo store trên M4B |
| `created_date` | Ngày tạo store trên M4B |
| `qa_approved_datetime` | Thời điểm store được QA approve, nếu trạng thái hiện tại là QA Đã Duyệt |
| `qa_approved_date` | Ngày mà store được QA approve, nếu trạng thái hiện tại là QA Đã Duyệt |
| `qr_activated_datetime` | Thời điểm store lần đầu được gán với mã QR code tĩnh |
| `qr_activated_date` | Ngày store lần đầu được gán với mã QR code tĩnh |
| `dynamic_qr_datetime` | Thời điểm store lần đầu phát sinh giao dịch qua QR động hoặc scanner POS |
| `dynamic_qr_date` | Ngày store lần đầu phát sinh giao dịch qua QR động hoặc scanner POS |
| `acquired_datetime` | Thời điểm store được acquired, được hiểu là thời điểm thanh toán được |
| `acquired_date` | Ngày store được acquired, được tính vào KPI của sale |
| `first_trans_date` | Ngày đầu tiên phát sinh giao dịch |
| `last_trans_date` | Ngày cuối cùng phát sinh giao dịch cho đến hiện tại |
| `f30_gmv` | GMV trong 30 ngày đầu kể từ ngày acquired |
| `f30_trans` | Tổng số giao dịch trong 30 ngày đầu kể từ ngày acquired |
| `f30_user` | Tổng số user duy nhất trong 30 ngày đầu kể từ ngày acquired |
| `f60_gmv` | GMV trong 60 ngày đầu kể từ ngày acquired |
| `f60_trans` | Tổng số giao dịch trong 60 ngày đầu kể từ ngày acquired |
| `f90_gmv` | GMV trong 90 ngày đầu kể từ ngày acquired |
| `f90_trans` | Tổng số giao dịch trong 90 ngày đầu kể từ ngày được kích hoạt thanh toán |
| `accum_gmv` | Tổng GMV lifetime tới ngày hiện tại |
| `accum_trans` | Tổng số giao dịch lifetime tới ngày hiện tại |
| `num_month_active_from_acquisition` | Số tháng từ ngày acquired đến khi có giao dịch đầu tiên |
| `merchant_size_sl` | Phân loại SME OFFLINE/TOPBRAND OFFLINE theo service list |
| `merchant_type_m4b` | Loại hình M4B của merchant (BPU, SME) |
| `merchant_onboarding_type` | Luồng onboard merchant qua sale team hoặc tự onboard |
| `merchant_size` | Phân loại merchant trong dự án Offline merchant với mục đích tính KPI |
| `full_address` | Địa chỉ đầy đủ của store |
| `city_name` | Tên thành phố nơi store tọa lạc |
| `district_name` | Tên quận nơi store tọa lạc |
| `ward_name` | Tên phường nơi store tọa lạc |
| `street_name` | Tên đường nơi store tọa lạc |
| `house_number` | Số nhà nơi store tọa lạc |
| `longitude` | Kinh độ của store |
| `latitude` | Vĩ độ của store |
| `active_status` | Trạng thái hoạt động của store; 1 - đang hoạt động, 0 - không còn hoạt động |
| `merchant_register_dynamic_qr` | Xác định merchant có đăng ký thanh toán động không (1 = có, 0 = không) |
| `sale_username` | Tên miền, email của sale người tạo ra merchant trên M4B |
| `asm` | Quản lý sale cấp vùng |
| `rsm` | Quản lý sale cấp miền |
| `sale_team_m4b` | Nguồn sale, là telesale hoặc directsale hoặc không có |
| `sale_note` | Ghi chú của salesman, thường ghi thời gian hoạt động và thông tin khác |
| `email` | Email của chủ merchant |
| `operating_time` | Thời gian hoạt động của store, dạng free text |
| `store_phone` | Số điện thoại của store |
| `category_m4b` | Lĩnh vực của merchant đã được điền trên M4B |
| `sub_category_m4b` | Lĩnh vực phụ của merchant đã được điền trên M4B |
| `category_sl_lv1` | Phân loại dịch vụ offline theo cấp độ 1 trên service list |
| `category_sl_lv2` | Phân loại dịch vụ offline theo cấp độ 2 trên service list |
| `category_sl_lv3` | Phân loại dịch vụ offline theo cấp độ 3 trên service list |
| `category_sl_lv4` | Phân loại dịch vụ offline theo cấp độ 4 trên service list |
| `merchant_bank_account_number` | Số tài khoản ngân hàng của merchant nhận tiền payout |
| `merchant_bank_name` | Tên ngân hàng của merchant nhận tiền payout |
| `merchant_payout_phone` | Số điện thoại của merchant là chủ ví payout |
| `fee` | Phí hiện tại thu của merchant |
| `payout_method` | Phương thức payout của merchant |
| `sale_team_pic` | Sale team được tính KPI cho số active store |
| `master_merchant_label` | Tên của master merchant nếu merchant thuộc một master merchant cụ thể |
| `merchant_type_master_merchant` | Phân loại merchant thuộc master merchant, giá trị 'online' hoặc 'offline' |
| `ipos_creation_source` | Nguồn tạo store bên IPOS (MoMo tạo, IPOS tạo hoặc migrate) |
| `ipos_store_ref_id` | Reference ID dùng để map với data phía iPOS |
| `is_bo_merchant` | 1: BO đã note trạng thái, 0: chưa có BO action |
| `num_day_qa_from_creation` | Số ngày từ lúc store được tạo đến khi được QA duyệt |
| `merchant_num_day_qa_from_creation` | Số ngày từ lúc merchant được tạo đến khi được QA duyệt |
| `dynamic_integration_datetime` | Thời điểm đầu tiên tích hợp phương thức thanh toán động cho store |
| `dynamic_integration_date` | Ngày đầu tiên tích hợp phương thức thanh toán động cho store |
| `primary_service_code` | Service_code ứng với merchant_code, dùng để map với service list |
| `sale_parent_username` | Username của người thuê salesman |
| `sale_type` | Phân loại salesman vào các nhóm như 'ctv', 'non_ctv', 'master merchant' |
| `sale_parent_type` | Phân loại của người thuê salesman |
| `paylater_config_type` | Phân loại merchant chấp nhận thanh toán nguồn ví trả sau |
| `min_aio_qr_datetime` | Thời điểm đầu tiên store được trang bị QR tĩnh |
| `is_store_aio_qr` | Phân biệt store có được trang bị QR tĩnh không; 1: có, 0: không |
| `system_fo_status` | Nội dung "Hệ thống xét duyệt" trên M4B |
| `status_fo_qc_m4b` | Trạng thái QC trên M4B cuối cùng của FO |
| `aio_dynamic_api_date` | Ngày đầu tiên có trạng thái API dynamic call, giúp phát hiện AIO Dynamic QR |
| `merchant_latest_state_code` | N/A |
| `contract_group_agg` | Phân loại hợp đồng theo sản phẩm tổng hợp |
| `min_sign_contract_datetime` | N/A |
| `max_sign_contract_datetime` | N/A |
| `f30_date_payout_ttt` | Đếm số ngày bật payout TTT trong 30 ngày đầu từ ngày acquired |
| `sb_1st_install_date` | N/A |
| `sb_serial` | N/A |

**Data Example**: Empty DataFrame - no sample data available

---

*This document was generated from raw JSON API response data for quality assurance and hallucination prevention.*