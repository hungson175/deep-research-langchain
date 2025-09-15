# Data Dataset

## Dataset Information

- **ID**: c210420f-d014-4463-bcb9-c9e4a38c0963
- **Name**: Data
- **Description**: All detailed transaction of service Data since 2021
- **Instructions**:
- **Error Code**: 200

## Schema Information

### Dataset Name: Data

---

### Table: project-5400504384186300846.BU_UTILITIES_TELCO.DATA_DETAILS

**Description**: Bảng này lưu trữ thông tin chi tiết về các giao dịch liên quan đến tiện ích viễn thông thông qua MoMo. Bảng cung cấp thông tin cho việc phân tích giao dịch với các dịch vụ từ nhà mạng, sử dụng tiền từ ví MOMO hoặc voucher khuyến mãi. Dữ liệu này có thể được sử dụng để đánh giá doanh thu từ các giao dịch viễn thông, xác định xu hướng sử dụng dịch vụ viễn thông, và phân tích hành vi người dùng trong các giao dịch.

### Columns

| Column Name | Description |
|-------------|-------------|
| id | ID cho giao dịch. |
| date | Ngày thực hiện giao dịch. |
| datetime | Thời gian thực hiện giao dịch. |
| hour | Giờ thực hiện giao dịch. |
| user_payment | Số tiền người dùng thanh toán cho giao dịch. |
| amount | Tổng số tiền của giao dịch. |
| mm_amount | Tổng số tiền dùng trong ví MoMo của giao dịch. |
| vc_amount | Tổng số tiền khuyến mãi của giao dịch. |
| voucher_or_not | Phân loại giao dịch có sử dụng voucher hay không. |
| cate | Nhà mạng của người được nạp. |
| service | Dịch vụ sử dụng: TOPUP: topup, MATHE: mã thẻ, COMBO: combo data, SIM: dịch vụ mua sim, OTHER: Dịch vụ khác. |
| subcategory | Không có mô tả. |
| group_service | Không có mô tả. |
| merchant | Tên dịch vụ và nhà mạng của giao dịch. |
| region | Khu vực của nhà cung cấp dịch vụ. |
| supplier | Nhà cung cấp của giao dịch. |
| service_code | Không có mô tả. |
| bonus | Số tiền thưởng cho người dùng. |
| gender | Giới tính của người dùng. |
| group_age | Nhóm độ tuổi của người dùng. |
| age | Độ tuổi của người dùng. |
| statusid | Trạng thái giao dịch: 6 = giao dịch thất bại, 2 = giao dịch thành công. |
| group_user | Không có mô tả. |
| province | Tỉnh thành nơi người dùng hiện tại đang ở. |
| province_group | Nhóm tỉnh thành nơi người dùng hiện tại đang ở. |
| Revenue | Doanh thu của giao dịch. |
| quantity | Số lượng sản phẩm người dùng mua. |
| menh_gia | Mệnh giá của sản phẩm. |
| goi_cuoc | Mã gói cước của sản phẩm. |
| dung_luong | Dung lượng data của gói cước. |
| expire | Thời gian hết hạn của gói cước. |
| month_active | Tháng người dùng active dịch vụ. |
| user_segment | Phân khúc người dùng trong tháng kích hoạt. |
| churn_duration | Số tháng người dùng rời bỏ dịch vụ. |
| money_source | Nguồn tiền người dùng sử dụng cho giao dịch. |
| typeid | Mã thẻ quà/mã nhập sử dụng cho promotion. |
| voucher_cost | Không có mô tả. |
| telco_source | Entry point từ miniapp của giao dịch. |
| serviceid | ID dịch vụ. |
| telco_source_raw | Không có mô tả. |
| suffix | Entry point nội bộ của giao dịch (ví dụ: nút màn hình, ...). |
| user_raw | Không có mô tả. |
| ttt_user_segment | Không có mô tả. |
| voucher_type_by_gmv | Không có mô tả. |
| voucher_type_by_trans | Không có mô tả. |
| previous_voucher_type_by_trans | Không có mô tả. |
| previous_voucher_type_by_gmv | Không có mô tả. |
| acquire_user_channel | Không có mô tả. |
| promotion_cost_type | Không có mô tả. |
| partner | Không có mô tả. |
| partner_type | Không có mô tả. |
| partner_momo_user | Không có mô tả. |

### Smart Top Values

```json
{
  "partner_type": ["only_sim", "mathe_partner", "only_owner", "mathe_owner_partner_sim", "owner_partner", "owner_partner_sim", "owner_sim", "mathe_partner_sim", "only_mathe", "only_partner", "partner_sim", "mathe_sim", "mathe_owner", "mathe_owner_sim", "mathe_owner_partner"],
  "partner": ["61132747", "54839853", "1443525"],
  "partner_momo_user": ["mathe", "partner", "sim", "momo user", "non momo user", "no data", "owner"],
  "promotion_cost_type": ["BU", "other teams", "organic"],
  "acquire_user_channel": ["BU", "other teams", "organic"],
  "previous_voucher_type_by_gmv": ["ONLY ORGANIC", "GMV MORE ORGANIC", "ONLY VOUCHER", "GMV MORE VOUCHER"],
  "previous_voucher_type_by_trans": ["ONLY ORGANIC", "GMV MORE ORGANIC", "ONLY VOUCHER", "GMV MORE VOUCHER"],
  "voucher_type_by_trans": ["ONLY ORGANIC", "TRANS MORE VOUCHER", "ONLY VOUCHER", "TRANS MORE ORGANIC"],
  "voucher_type_by_gmv": ["ONLY ORGANIC", "GMV MORE ORGANIC", "ONLY VOUCHER", "GMV MORE VOUCHER"],
  "ttt_user_segment": ["1.New", "2.Retain", "non_TTT", "churn_TTT", "3.Reactive"],
  "user_raw": ["68596690", "89290850", "67345391"],
  "serviceid": ["MOMOGGLP20230803", "MOMOIYHA20210714", "MOMOQKAP20211130"],
  "telco_source_raw": ["credit_paylater_new_revamp_block_recommend_payX", "tabbar_home_revamp_promotion_button_ttt", "mobilecenter_revamp_details"],
  "telco_source": ["shake_nearby_home", "funds_manager_byphone", "credit_paylater_new_invoice_list_data_assistant"],
  "voucher_cost": ["109125", "30250", "44800"],
  "typeid": ["Rewards_data_giam10k_bill50k240329_discount_100pt10k_33825273", "growtht7_hm1_500k_3g4g_10k_2", "230511_pc_data_50pt_15k_churn"],
  "user_segment": ["retain_user", "recover_user", "new_user"],
  "money_source": ["direct debit", "group fund", "visa debit", "momo", "others", "pay_later", "bank_link", "napas", "visa ao ccm", "TTT", "visa credit"],
  "month_active": ["2018-05-01", "2019-06-01", "2023-07-01"],
  "churn_duration": ["1", "3", "45"],
  "suffix": ["block_recommend_both", "block_recomend_ai", "list_topup_combo_vina"],
  "dung_luong": ["1 GB", "3", "500 MB/mỗi ngày"],
  "menh_gia": ["740000", "1344000", "87891"],
  "goi_cuoc": ["EJPNKDPYUNLI15D", "5G480B", "D24_DC"],
  "expire": ["1", "3", "30"],
  "quantity": ["1", "3", "4"],
  "province_group": ["Others", "Hà Nội", "Tỉnh khác", "KCN Miền Bắc", "Hồ Chí Minh", "Unknown", "TP Lớn", "TP Du lịch", "KCN Miền Nam"],
  "Revenue": ["8720.3999999999778", "3204.5454545454545", "54574.999999999993"],
  "province": ["Long An", "Hậu Giang", "Nghệ An"],
  "age": ["1", "3", "45"],
  "group_user": ["other", "New User", "Current"],
  "statusid": ["6", "2"],
  "gender": ["unknown", "MALE", "UNKNOWN", "female", "FEMALE", "male"],
  "supplier": ["MobiPlus", "Mobifone", "GOHUB"],
  "region": ["Mien Bac"],
  "service_code": ["mathe_epay06.buycard_data_mobifone", "vttimathe_imedia.buycard_data_vinaphone", "m4bvttilocal_web"],
  "bonus": ["510", "4560", "21600"],
  "group_service": ["3G/4G"],
  "cate": ["Viettel", "Vnsky", "Mobifone", "itel", "Gohub", "Local", "Vietnamobile", "Wintel", "Saymee", "Vinaphone", "Xplori"],
  "subcategory": ["Viettel", "MobiPlus", "GOHUB", "Mobifone", "WINTEL", "VIETTEL", "Mservice", "VIEN PHUONG NAM", "VIETTEL DIRECT", "Mobifoneplus", "Vietnamobile", "EWAVE", "EPAY", "My data", "MOBICAST", "VNSKY", "XPLORI", "VIETNAMOBILE", "IMD", "PHUONG QUAN", "Vinaphone", "ASIM", "VMG/IMEDIA"],
  "group_age": ["28_to_32", "[5]. 31 - 35 y/o", "[6]. 36 - 40 y/o", "33_to_37", "UNKNOWN", "[1]. <18 y/o", ">37", "18_to_22", "[7]. >40 y/o", "[4]. 27 - 30 y/o", "[3]. 23 - 26 y/o", "[2]. 18 - 22 y/o", "23_to_27"],
  "user_payment": ["57196028", "53494787", "55943641"],
  "vc_amount": ["67000", "30250", "44800"],
  "mm_amount": ["740000", "87891", "358400"],
  "hour": ["1", "3", "17"],
  "datetime": ["2021-08-14 14:30:50", "2021-08-14 15:08:04", "2021-08-14 07:04:24"],
  "voucher_or_not": ["Voucher", "Non voucher", "Non_voucher"],
  "amount": ["740000", "1344000", "87891"],
  "date": ["2024-08-08", "2020-05-24", "2019-05-20"],
  "service": ["MATHE", "TOPUP", "COMBO", "OTHERS", "SIM"],
  "id": ["15448651961", "15469160272", "15444085835"]
}
```

## Knowledge Base

(Empty)

## Memory

- giao dịch thành công: statusid = 2 (2025-05-13T14:20:25.903653)
- TTT: Túi Thần Tài (2025-05-13T14:20:47.215151)
- Khi xử lý vấn đề liên quan tới MAU, dùng COUNT(DISTINCT user_payment) thay vì COUNT(DISTINCT user_raw) (2025-07-30T23:29:12.950802)
- Khi xử lý cột 'expire', sử dụng safe_cast(t1.expire as float64) để tránh lỗi kiểu dữ liệu (2025-07-28T23:59:22.308527)
- Gói 30 ngày: expire = 30 (2025-08-12T00:52:31.173329)
- Khi user sử dụng agent, thì thay bằng cột service_code (2025-09-11T16:13:31.825248)
- Các gói cước 5G bao gồm: 5G135, 5G150, 5G160B, 5G180B, 5G230B, 5G280B, 5G330B, 5G380B, 5G480B, 5GLQ190, 5GLQ210, TET5G, 5GMXH200, 5GMXH230, 3T5G135, 3T5G150, 3T5G160B, 3T5G180B, 3T5G480B, 3T5GLQ190, 3T5GLQ210, 5G135N, 3T5G135N, 5G150N, 3T5G150N, 5G13KS, 5G36KS, 5G85KS, 5GMAX (2025-09-11T15:53:49.789176)
- Cột `statusid` là một số nguyên, không phải chuỗi (2025-07-30T19:42:53.269714)
- Additional detailed memory entries related to calculations, revenue, user segments, etc.

## Error Message

(Empty)