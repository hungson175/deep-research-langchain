# Data (Non Sensitive) Dataset

## Dataset Information

- **ID**: be004a0c-5e7c-442d-ab51-a7026eed5433
- **Name**: Data (Non Sensitive)
- **Description**: All detailed transaction of service Data since 2021
- **Instructions**: (Not specified)
- **Error Code**: 200

---

## Schema Information

### Dataset Name: Data (Non Sensitive)

---

## Table 1: project-5400504384186300846.BU_UTILITIES_TELCO.DATA_DETAILS

**Description**:
Bảng chứa chi tiết dữ liệu về các giao dịch tiện ích viễn thông được thực hiện thông qua MoMo. Bảng có thể được sử dụng để phân tích các giao dịch theo thời gian, đánh giá hiệu suất kinh doanh của các dịch vụ viễn thông, và xác định một số đặc điểm khách hàng như độ tuổi, khu vực sinh sống và nhà cung cấp dịch vụ.

### Columns

| Column Name | Description |
|-------------|-------------|
| id | ID của giao dịch. |
| date | Ngày thực hiện giao dịch. |
| datetime | Thời gian chính xác thực hiện giao dịch. |
| hour | Giờ thực hiện giao dịch. |
| user_payment | ID của người dùng thực hiện giao dịch. |
| amount | Tổng số tiền của giao dịch. |
| mm_amount | Tổng số tiền dùng trong ví MoMo của giao dịch. |
| vc_amount | Tổng số tiền khuyến mãi áp dụng cho giao dịch. |
| voucher_or_not | Phân loại giao dịch có sử dụng voucher hay không. 'Voucher': giao dịch có sử dụng voucher, 'Non voucher': giao dịch không sử dụng voucher (giao dịch organic). |
| cate | Nhà mạng của người được nạp. |
| service | Dịch vụ sử dụng trong giao dịch: 'TOPUP': topup, 'MATHE': mã thẻ, 'COMBO': combo data, 'SIM': dịch vụ mua sim, 'OTHER': Dịch vụ khác. |
| subcategory |  |
| group_service |  |
| merchant | Tên dịch vụ và nhà mạng liên quan đến giao dịch, được viết dưới dạng in hoa không dấu. |
| region | Khu vực của merchant. |
| supplier | Nhà cung cấp dịch vụ liên quan đến giao dịch. |
| service_code |  |
| bonus | Số tiền bonus cho người dùng. |
| gender | Giới tính của người dùng. |
| group_age | Độ tuổi của nhóm người dùng. |
| age | Độ tuổi của người dùng. |
| statusid | Trạng thái của giao dịch. 6 = giao dịch thất bại, 2 = giao dịch thành công. |
| group_user |  |
| province | Tỉnh thành nơi người dùng sinh sống. |
| province_group | Nhóm tỉnh thành mà người dùng sinh sống. |
| Revenue | Doanh thu của giao dịch. |
| quantity | Số lượng sản phẩm mà người dùng đã mua. |
| menh_gia | Mệnh giá của sản phẩm. |
| goi_cuoc | Mã gói cước của sản phẩm. |
| dung_luong | Dung lượng data của gói cước. |
| expire | Thời gian hết hạn của gói cước. |
| month_active | Tháng người dùng active. |
| user_segment | Phân khúc của người dùng trong tháng active. 'retain_user': người dùng đã active ở tháng trước đó và tháng này tiếp tục active, 'recover_user': người dùng đã ngừng sử dụng dịch vụ hơn 1 tháng và quay lại active dịch vụ tháng này, 'new_user': người dùng chưa từng active dịch vụ Data trước đó. |
| churn_duration | Số tháng mà người dùng đã ngừng sử dụng dịch vụ. |
| money_source | Nguồn tiền mà người dùng sử dụng cho giao dịch. |
| typeid | Thẻ quà/mã nhập sử dụng cho promotion. |
| voucher_cost |  |
| telco_source | Entry point từ miniapp của giao dịch. |
| serviceid | ID của dịch vụ liên quan đến giao dịch. |
| telco_source_raw |  |
| suffix | Entry point nội bộ của giao dịch (ví dụ: button, screen,...). |
| user_raw |  |
| ttt_user_segment |  |
| voucher_type_by_gmv |  |
| voucher_type_by_trans |  |
| previous_voucher_type_by_trans |  |
| previous_voucher_type_by_gmv |  |
| acquire_user_channel |  |
| promotion_cost_type |  |
| partner |  |
| partner_type |  |
| partner_momo_user |  |

### Smart Top Values

- **partner_momo_user**: ['mathe' 'owner' 'momo user' 'partner' 'sim' 'no data' 'non momo user']
- **partner_type**: ['mathe_owner_partner' 'mathe_partner_sim' 'owner_sim' 'only_sim' 'only_mathe' 'only_partner' 'mathe_partner' 'mathe_sim' 'owner_partner_sim' 'partner_sim' 'only_owner' 'owner_partner' 'mathe_owner' 'mathe_owner_sim' 'mathe_owner_partner_sim']
- **promotion_cost_type**: ['organic' 'BU' 'other teams']
- **previous_voucher_type_by_trans**: ['GMV MORE VOUCHER' 'GMV MORE ORGANIC' 'ONLY VOUCHER' 'ONLY ORGANIC']
- **acquire_user_channel**: ['organic' 'BU' 'other teams']
- **previous_voucher_type_by_gmv**: ['GMV MORE VOUCHER' 'GMV MORE ORGANIC' 'ONLY VOUCHER' 'ONLY ORGANIC']
- **voucher_type_by_trans**: ['ONLY VOUCHER' 'ONLY ORGANIC' 'TRANS MORE ORGANIC' 'TRANS MORE VOUCHER']
- **suffix**: ['block_recommend_both' 'data_assistant' 'list_topup_combo_vina' 'promotion_detail' 'detail' 'button_vts' 'cross_sale' 'cross_sale_AI' 'flash_sale' 'block_reccomend_ai' 'manual_config_bundle' 'button_ttt' 'block_recommend' 'cross_sale_config' 'block_recomend_ai' 'cross_sale_both']
- **ttt_user_segment**: ['non_TTT' '3.Reactive' '1.New' '2.Retain' 'churn_TTT']
- **voucher_type_by_gmv**: ['GMV MORE VOUCHER' 'GMV MORE ORGANIC' 'ONLY VOUCHER' 'ONLY ORGANIC']
- Additional distinct values for serviceid, money_source, user_segment, goi_cuoc, group_user, gender, group_age, supplier, cate, subcategory, service, group_service, voucher_or_not, province_group

---

## Table 2: project-5400504384186300846.BU_UTILITIES_TELCO.DATA_SEGMENT_USER

**Description**:
Bảng quản lý và phân loại người dùng MSM dựa theo dữ liệu hoạt động và churn. Sử dụng để phân tích các phân khúc người dùng, xác định người dùng rời bỏ và đánh giá hiệu quả chiến lược khuyến mãi. Bảng này hữu ích để theo dõi và cải thiện retention rate của người dùng dịch vụ viễn thông.

### Columns

| Column Name | Description |
|-------------|-------------|
| month_active | Ngày tháng người dùng bắt đầu hoạt động. |
| reference | Tham chiếu liên quan tới người dùng. |
| month_lead | Thời điểm tháng dẫn đầu của người dùng. |
| retain | Ngày tháng người dùng được giữ lại. |
| month_churn | Tháng mà người dùng có dấu hiệu churn. |
| user_segment | Phân khúc người dùng. |
| churn_user | Thể hiện người dùng có churn hay không. |
| churn_duration | Thời gian duy trì trạng thái churn tính bằng ngày. |
| FIRST_DATE | Ngày đầu tiên dữ liệu của người dùng được ghi nhận. |
| LAST_DATE | Ngày gần nhất dữ liệu của người dùng được ghi nhận. |
| CHURN_DURATION_DAY | Số ngày mà người dùng duy trì trạng thái churn. |
| TRANS | Số lượng giao dịch hiện tại của người dùng. |
| PREVIOUS_TRANS | Số lượng giao dịch trước đó của người dùng. |
| GMV | Tổng giá trị hàng hóa hiện tại của người dùng. |
| PREVIOUS_GMV | Tổng giá trị hàng hóa trước đó của người dùng. |
| PROMOTION_COST | Chi phí liên quan đến chiến lược khuyến mãi. |
| PREVIOUS_VC_AMOUNT | Giá trị voucher sử dụng trước đó. |
| VOUCHER_TYPE_BY_GMV | Loại voucher được sử dụng theo GMV hiện tại. |
| PREVIOUS_VOUCHER_TYPE_BY_GMV | Loại voucher sử dụng trước theo GMV. |
| VOUCHER_TYPE_BY_TRANS | Loại voucher sử dụng theo số lượng giao dịch hiện tại. |
| PREVIOUS_VOUCHER_TYPE_BY_TRANS | Loại voucher sử dụng trước theo số lượng giao dịch. |
| GMV_TYPE | Loại GMV hiện tại của người dùng. |
| PREVIOUS_GMV_TYPE | Loại GMV trước đó của người dùng. |
| first_tid | Mã giao dịch đầu tiên của người dùng. |

### Smart Top Values (Table 2)

- **VOUCHER_TYPE_BY_GMV**: ['GMV MORE ORGANIC' 'ONLY ORGANIC' 'ONLY VOUCHER' 'GMV MORE VOUCHER']
- **PREVIOUS_VOUCHER_TYPE_BY_GMV**: ['GMV MORE ORGANIC' 'ONLY ORGANIC' 'ONLY VOUCHER' 'GMV MORE VOUCHER']
- **VOUCHER_TYPE_BY_TRANS**: ['ONLY ORGANIC' 'ONLY VOUCHER' 'TRANS MORE ORGANIC' 'TRANS MORE VOUCHER']
- **PREVIOUS_VOUCHER_TYPE_BY_TRANS**: ['GMV MORE ORGANIC' 'ONLY ORGANIC' 'ONLY VOUCHER' 'GMV MORE VOUCHER']
- **GMV_TYPE**: ['7. 200k - 250k' '2. 15K - 35K' '4. 70K - 120K' '3. 35K - 70K' '1. 0 - 15K' '6. 150k - 200k' '5. 120k - 150K' '9. 250k+']
- **PREVIOUS_GMV_TYPE**: ['7. 200k - 250k' '2. 15K - 35K' '4. 70K - 120K' '3. 35K - 70K' '6. 150k - 200k' '1. 0 - 15K' '5. 120k - 150K' '9. 250k+']
- **churn_user**: ['churn' 'retain']
- **user_segment**: ['retain_user' 'recover_user' 'new_user']

---

## Knowledge Base

(Empty)

---

## Memory

- giao dịch thành công: statusid = 2 (2025-05-13T14:20:21.616227)
- MAU: phải thêm điều kiện statusid = 2 (2025-05-13T14:20:25.623500)
- giftid: typeid (2025-05-13T14:20:32.762014)
- giao dịch thành công: statusid = 2 (2025-05-13T14:19:10.055815)
- TTT: Túi Thần Tài (2025-05-13T14:20:43.240149)

---

## Error Message

(Empty)