# P2P AIO_QR

## Dataset Information

**ID:** 05cf9a74-c3c0-4b95-923c-71c8d42ed8aa
**Name:** P2P AIO_QR
**Description:** records all transaction of P2P AIO_QR
**Instructions:** (No specific instructions provided)
**Error Code:** 200

## Schema Information

### Table 1: momovn-prod.MBI_DA.HOANG_P2P_AIO_QR_ORIGINAL_TABLE

**Description:** Bảng momovn-prod.MBI_DA.HOANG_P2P_AIO_QR_ORIGINAL_TABLE lưu trữ thông tin chi tiết về các giao dịch P2P (chuyển-nhận tiền) thực hiện qua AIO-QR. Bảng này có thể được sử dụng để phân tích xu hướng giao dịch P2P, xác định nhóm tuổi và khu vực của người nhận tiền, và theo dõi trạng thái thành công hoặc thất bại của các giao dịch.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| serviceid | Serviceid của giao dịch (luồng product user thực hiện chuyển-nhận tiền qua AIO-QR) | transfer_myqr_upload, transfer_split_bill_lixi, transfer_myqr, transfer_aioqr_p2m, transfer_split_bill_myqr, transfer_split_bill_aioqr, transfer_myqr_p2m, transfer_aioqr |
| tid | TID của giao dịch qua AIO QR | 34321694116, 34314749726, 34311251716 |
| datetime | Thời gian giao dịch AIO-QR | 2025-01-07 19:45:16, 2025-01-07 14:48:02, 2023-01-07 17:05:43 |
| date | Ngày giao dịch qua AIO-QR | 2024-09-28, 2024-01-26, 2025-03-13 |
| month | Tháng giao dịch qua AIO-QR | 2022-11-01, 2023-11-01, 2024-08-01 |
| amount | Giá trị giao dịch qua AIO-QR | 120000, 191000, 510000 |
| statusid | Trạng thái giao dịch: GD thành công nếu statusid = 2, thất bại nếu statusid = 6 | 6, 2 |
| fee | Phí giao dịch qua AIO-QR | 12000, 0 |
| receiver_id | User ID của user nhận tiền về MoMo | 7672784, 25550315, 31542472 |
| user_id | User ID của user gửi tiền (có thể là user_id MoMo nếu internal trans (W2W), bank account nếu là giao dịch B2W) | 33478953, 63051124, 61123508 |
| age | Tuổi của user nhận tiền | 34, 63, 64 |
| age_group | Nhóm tuổi của user nhận tiền | [4].28-35, [2].18-22, others, [6].>50, [5].36-50, [1].<18, [3].23-27 |
| city | Thành phố sinh sống của user nhận tiền | Hoà Bình, Yên Bái, Thái Nguyên |
| city_group | Khu vực sinh sống của user nhận tiền | Hà Nội, TP Du lịch, Hồ Chí Minh, Tỉnh khác, KCN Miền Bắc, TP Lớn, KCN Miền Nam |
| cheat_type | Loại user nhận tiền có phải cheat không (thông thường không tính đến feature cheat này) | [2]. Not cheat, [1]. Cheat |

### Table 2: momovn-prod.MBI_DA.HOANG_P2P_AIO_QR_ACQUISITION_BY_SOURCE_TABLE

**Description:** Bảng ghi nhận thông tin về người dùng nhận tiền qua mô hình thanh toán AIO-QR trong tháng. Thông tin từ bảng này có thể được sử dụng để:
- Phân tích hành vi người dùng qua AIO-QR theo từng tháng, ngày và thời gian cụ thể.
- Đánh giá giá trị giao dịch theo từng loại active của người dùng (New/Retain, Reactive) và loại promotion.
- Phân tích nhân khẩu học người dùng gồm tuổi, nhóm tuổi và khu vực sinh sống.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng user active nhận tiền | 2025-09-01, 2023-01-01, 2024-06-01 |
| date | Ngày user active nhận tiền | 2023-02-27, 2023-12-09, 2022-12-08 |
| datetime | Thời gian user active nhận tiền | 2023-05-01 00:04:18, 2023-05-01 20:41:35, 2023-05-01 00:22:04 |
| receiver_id | UserID người dùng nhận tiền qua AIO-QR | 81905936, 77339942, 83645363 |
| tid | TID 1st active đầu tiên của tháng | 39342582682, 39344917508, 39345158458 |
| amount | Giá trị giao dịch | 350000, 152401, 446000 |
| serviceid | ServiceID 1st active đầu tiên trong tháng | transfer_aioqr_p2m, transfer_myqr_p2m, transfer_myqr_upload, transfer_split_bill_lixi, transfer_myqr, transfer_aioqr, transfer_split_bill_aioqr, transfer_split_bill_myqr |
| user_type | Loại active của user (New/Retain, Reactive) | [3]. Reactivation, [2]. Retention, [1]. New to service |
| city | Thành phố nơi người nhận tiền sinh sống | Bắc Ninh, Tiền Giang, Hải Dương |
| city_group | Khu vực quận/huyện nơi người nhận tiền sinh sống | TP Lớn, TP Du lịch, Hà Nội, KCN Miền Bắc, Hồ Chí Minh, Tỉnh khác, KCN Miền Nam |
| age_group | Độ tuổi của người nhận tiền | [3].23-27, [5].36-50, [6].>50, [2].18-22, [4].28-35, [1].<18, others |
| age | Tuổi của người nhận tiền | 19, 30, 45 |
| promotion_lv1 | Người dùng 1st active trong tháng là Promo/Organic | [2]. Promotion, [1]. Organic |
| promotion_lv2 | Loại Promotion (cấp độ 2) - được định nghĩa bởi đơn vị kinh doanh | [2]. Mission, [5]. Other Scheme, [5]. Comm, [1]. Scheme W2W, [2]. Scheme by amount, [4]. Game, [3]. Voucher, [1]. CRM, [3]. Scheme sender QR, [6]. Journey |
| promotion_lv3 | Loại Promotion (cấp độ 3) - được định nghĩa bởi đơn vị kinh doanh | Scheme 2222đ, 250707_aioqr_qr_user_acquisition_retargeting_journey_open_app_1k_2751, rw_stp_qr_ua_250728_cbttt_100pt500d_lbzkc |
| source | Nguồn phát sinh hoạt động | noti, banner |

### Table 3: momovn-prod.MBI_DA.LOAN_P2P_RECEIVER_SEGMENT_ALL

**Description:** Bảng này quản lý thông tin về các phân đoạn người nhận khoản vay P2P trong hệ thống Momo cho tất cả các tháng. Từ bảng này, người dùng có thể lấy thông tin về phân đoạn của người nhận khoản vay, theo dõi các thay đổi theo từng tháng, phân tích dữ liệu về người dùng nhận khoản vay và kiểm tra các yếu tố ảnh hưởng đến việc nhận khoản vay.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng nhận khoản vay được theo dõi. | 2024-10-01, 2025-03-01, 2024-01-01 |
| user_id | ID của người dùng nhận khoản vay từ hệ thống P2P. | 14338208, 1522640, 15698528 |
| segment | Phân đoạn của người nhận khoản vay, thể hiện thuộc tính hoặc loại người dùng trong hệ thống. | [2]. Lookalike seller, [8]. Micro Seller, [1]. SME merchant, [4]. Driver, [7]. Hardcore Upload, [3]. Social seller, [6]. Hardcore Payment Link, [5]. Driver phonebook |
| df | Yếu tố định danh (descriptor factor) của người nhận khoản vay trong quá trình phân tích. | P2M, P2P |

## Memory

The following memory entries contain business rules and query guidelines for this dataset:

1. **Query Rule for 2025đ QR Transfers (June 2025):** Không cần filter serviceid và statusid khi truy vấn số user nhận 2025đ qua QR nhận tiền MoMo trong tháng 6/2025
   - Created: 2025-07-28T20:07:02.563109-07:00

2. **2025Đ Scheme Promotion Filter:** Scheme nhận tiền 2025Đ là một promotion, cần filter promotion_lv1 = '[2]. Promotion'
   - Created: 2025-08-11T02:19:02.158285-07:00

3. **Successful Transaction Definition:** For metrics like MAU, DAU, TPV, user defines successful transactions as those with statusid = 2. This applies when using the statusid column, for example, from the momovn-prod.MBI_DA.HOANG_P2P_AIO_QR_GENERAL_BEHAVIOR_TABLE.
   - Created: 2025-06-20T11:49:54.851943

4. **QR Scan Feature Filter:** Để lấy tính năng quét mã QR thì lấy serviceid NOT LIKE '%upload%'
   - Created: 2025-07-28T19:59:22.790419-07:00