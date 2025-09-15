# Telco Funnel Domain Response

## Error Code
200

## Data

### ID
fdc4e81a-0f8e-4412-b5b4-1602705daae6

### Name
Telco Funnel

### Description
Funnel cơ bản của user Airtime và Data

### Instructions
(empty)

## Schema DDL

### Dataset Name
Telco Funnel

### Table Name
`momovn-prod.BU_UTILITIES_TELCO.FULL_FUNNEL_TELCO_OPTIMIZE`

### Table Description
Bảng ghi nhận các giao dịch và hành động của người dùng liên quan đến dịch vụ viễn thông qua ứng dụng MoMo. Đây là bảng phân tích đầy đủ hành vi của người dùng từ khi tiếp cận dịch vụ cho đến lúc thực hiện thanh toán.

**Thông tin có thể được lấy từ bảng này:**
- Phân loại người dùng theo các dịch vụ và hành động mà họ thực hiện: như việc xem màn hình dịch vụ, click nút xác nhận, hay tham gia mua hàng.
- Đo lường số lượng giao dịch và lưu lượng truy cập dựa trên từng bước trong hành trình người dùng.
- Phân tích phân khúc người dùng dựa trên dịch vụ Airtime và Data để tối ưu hóa hoạt động tiếp thị và cải thiện trải nghiệm người dùng.

### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `date_partition` | DATE | Ngày thực hiện hành động của user. |
| `user_id` | STRING | Người dùng ở dạng mã hóa. |
| `step` | STRING | Các bước thực hiện hành động của người dùng với dịch vụ viễn thông: screen_service: xem màn hình dịch vụ; trans_confirmation: nhấn nút xác nhận giao dịch TTAT; is_payment_by_core_trans: giao dịch thanh toán; MHTTAT: xem MHTTAT; load_KQGD: tải thành công MHKQGD; CTA: click Mua hàng ở màn hình dịch vụ. |
| `service_name` | STRING | Tên dịch vụ viễn thông: mobilebuycard (Airtime), mobiletopup (Airtime), mobilecombo (Data), mobiletopupdata (Data). |
| `service` | STRING | Loại dịch vụ viễn thông: topup_new, topup, topup_revamp (Topup Airtime), buycard_new, buycard (thẻ Airtime), data_topup, data_topup_new, data_topup_revamp (topup data), data_buycard, data_buycard_new (thẻ Data), data_combo, data_combo_revamp (combo data). |
| `number_event` | INTEGER | Số lượng traffic/số lượng giao dịch, đặc biệt khi bước thực hiện là 'is_payment_by_core_trans'. |
| `airtime_segment_user` | STRING | Phân khúc người dùng của dịch vụ Airtime: new_user (người dùng mới), retain_user (người dùng tiếp tục sử dụng từ tháng trước), recover_user (người dùng quay lại sau khi không sử dụng từ tháng T-2). |
| `data_segment_user` | STRING | Phân khúc người dùng của dịch vụ Data: new_user (người dùng mới), retain_user (người dùng tiếp tục sử dụng từ tháng trước), recover_user (người dùng quay lại sau khi không sử dụng từ tháng T-2). |

### Smart Top Values

#### Distinct values for `service`:
['topup' 'data_topup_revamp' 'data_topup' 'data_buycard' 'Topup_new' 'data_combo' 'buycard_new' 'Topup_revamp' 'data_topup_new' 'topup_new' 'topup_postpaid' 'topup_revamp' 'Topup' 'travelsim_number' 'sim' 'data_combo_revamp' 'simcenter' 'data_buycard_new' 'buycard']

#### Distinct values for `service_name`:
['sim_phone' 'folder_tra_sau' 'mobilecombo' 'mobilebuycard' 'mobiletopupcombo' 'travelsim' 'data' 'sim' 'mobiletopupdata' 'mobiletopup' 'airtime']

#### Distinct values for `step`:
['trans_confirmation' 'CTA' 'contact_field' 'Load_KQGD' 'product_clicked' 'screen_service' 'back_to_home' 'MHTTAT' 'is_payment_by_core_trans' 'click_tab']

#### Distinct values for `data_segment_user`:
['recover_user' 'retain_user' 'new_user']

#### Distinct values for `airtime_segment_user`:
['recover_user' 'retain_user' 'new_user']

## Knowledgebase
(empty)

## Memory
(empty)

## Error Message
(empty)