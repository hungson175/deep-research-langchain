# SME OFFLINE PAYMENT

## Overview
- **Domain ID**: 03f0b56d-7b56-49d8-9073-6bb94e564fe2
- **Domain Name**: SME OFFLINE PAYMENT
- **Description**: A DATASET containing processed information about merchant payment and merchant profile

## Tables

### project-5400504384186300846.MBI_DA.DM_OFF_TRANSACTION

**Description**: Tổng hợp transaction offline payment, gồm các giao dịch payment thành công, có agent nhận tiền thỏa mã 1 trong 2 điều kiện: (1) được define là dịch vụ offline trên service list, (2) là agent của merchant_id được xác định thuộc offline trên hệ thống M4B. Do đó tùy từng mục đích sử dụng và mục đích phân loại khác nhau mà cần lọc lại data. Primary key: tid. Với dự án offline merchant, cần lọc ra các giao dịch valid (tại tháng 11/2023, rule là amount>=10k), thì sử dụng cột is_valid_trans để lọc.

Thông tin có thể lấy từ table này gồm:
- Thông tin về giao dịch offline và phân loại theo mã dịch vụ
- Phân loại merchant theo các tiêu chí khác nhau như size, type, loại hình thanh toán
- Phân tích mức độ active của store và thông tin quản lý sale team

Contact: cong.tran1@mservice.com.vn
Maintained by: team CDO-K khai.do@mservice.com.vn

#### Columns

| Column Name | Description |
|-------------|-------------|
| date | Ngày diễn ra giao dịch |
| date_time | Thời điểm diễn ra giao dịch |
| month | Tháng diễn ra giao dịch |
| tid | ID của giao dịch trong hệ thống core, được gọi là TID (transaction ID) |
| service_code | Service_code của giao dịch thanh toán, dùng để lấy thông tin từ Service List |
| agent_id | Agent id của user |
| amount | Số tiền của giao dịch thanh toán, trước khi trừ promotion |
| fund_id | Id của nguồn tiền user dùng thanh toán nếu thanh toán bằng MoMo |
| money_source | Nguồn tiền thanh toán nếu user thanh toán bằng app MoMo (MoMo, NHLK, TTT, VTS,...) |
| payment_type | Phân loại hình thức thanh toán dựa vào payment_method và payment_channel như QR tĩnh, QR động, scanner pos |
| payment_type_group | Phân loại app thanh toán của user, gồm "MoMo" và "Bank" |
| merchant_code | Mã định danh merchant (MID), unique cho mỗi merchant |
| store_id | ID số của store, unique trên M4B. Store có thể được gán là -1 |
| store_code | Mã store bằng chữ, cần check giá trị bên trong cột là store_code hay store_id khi join |
| store_code_unique | Concat merchant code & store code để đếm active store |
| merchant_name_m4b | Tên của merchant theo M4B |
| store_name | Tên store trên M4B |
| merchant_type_m4b | Type M4B của merchant (BPU, SME) |
| merchant_onboarding_type | Luồng onboard merchant do sale team hoặc tự onboard |
| merchant_size | Phân loại merchant theo size và offline/online, bao gồm SME OFFLINE, TOPBRAND OFFLINE, UNDEFINED, PRE - SME OFFLINE |
| store_city | Thành phố của cửa hàng |
| store_district | Quận của cửa hàng |
| store_ward | Phường của cửa hàng |
| bu_category_sl | Phân loại dịch vụ offline hiện tại của BU Offline, gồm: Retail, FnB, SME |
| category_sl_lv1 | Phân loại dịch vụ offline trên Service List, tương đương BU_GROUP_CODE_L1 |
| category_sl_lv2 | Phân loại dịch vụ offline trên Service List, tương đương BU_GROUP_CODE_L2 |
| category_sl_lv3 | Phân loại dịch vụ offline trên Service List, tương đương BU_GROUP_CODE_L3 |
| category_sl_lv4 | Phân loại dịch vụ offline trên Service List, tương đương BU_GROUP_CODE_L4 |
| merchant_name_sl | Tên của merchant theo Service List |
| sale_team_m4b | Sale_team mà tạo ra cửa hàng phát sinh giao dịch |
| rsm | Người quản lý đội sale theo miền |
| asm | Người quản lý đội sale theo vùng |
| sale_username | Email, tên miền của sale tạo merchant trên m4b |
| sale_team_pic | Sale team được tính KPI cho số active store |
| store_monthly_active_type | Active_type của store theo level tháng, gồm các giá trị new active, retention, reactive, inactive |
| store_monthly_trans_segment | Segment của store theo số lượng transaction trong tháng, gồm light (1-6), medium (7-30), heavy (31+) |
| master_merchant_label | Tên của master merchant nếu thuộc master merchant, ví dụ IPOS, NHANH, HARAVAN |
| merchant_type_master_merchant | "online" hoặc "offline" nếu merchant thuộc master merchant |
| ipos_creation_source | Nguồn tạo store cho IPOS: MoMo, IPOS tạo hay migrate sang IPOS |
| is_bo_merchant | 1: BO đã note trạng thái trên merchant; 0: chưa có BO action |
| num_day_qa_from_creation | Thời gian từ store được tạo đến lúc BO duyệt |
| merchant_num_day_qa_from_creation | Thời gian từ merchant được tạo đến lúc BO duyệt |
| store_dynamic_integration_datetime | Ngày tích hợp/ mở mới dynamic qr |
| store_qa_approved_datetime | Thời điểm được QC duyệt của store |
| store_acquired_datetime | Thời điểm store được acquired, ngày store có thể thanh toán được |
| store_acquired_date | Ngày store được acquired, ngày store có thể thanh toán được |
| merchant_qa_approved_datetime | Thời điểm được duyệt QA của Merchant |
| is_valid_transaction | Transaction có được tính là valid không |
| merchant_paylater_config_type | Phân biệt merchant được chấp nhận thanh toán bằng nguồn tiền ví trả sau |
| sale_parent_username | Username của ngừoi thuê salesman, thường bằng với sale_username nếu là sale inhouse |
| sale_type | Phân loại salesman vào các nhóm |
| sale_parent_type | Phân loại của ngừoi thuê salesman |
| rank_tid | None |
| soundbox_tran_type_id | type = 1 là transaction soundbox |
| sb_1st_install_date | Ngày đầu tiên soundbox được gắn vào store này |

#### Sample Data

```
         date           date_time      month          tid           service_code  agent_id   amount  fund_id money_source           payment_type payment_type_group     merchant_code  store_id        store_code                  store_code_unique merchant_name_m4b                      store_name merchant_type_m4b    merchant_onboarding_type merchant_size       store_city store_district   store_ward bu_category_sl category_sl_lv1 category_sl_lv2 category_sl_lv3                                       category_sl_lv4                merchant_name_sl sale_team_m4b            rsm           asm sale_team_pic store_monthly_active_type store_monthly_trans_segment master_merchant_label merchant_type_master_merchant ipos_creation_source  is_bo_merchant  num_day_qa_from_creation  merchant_num_day_qa_from_creation store_dynamic_integration_datetime store_qa_approved_datetime store_acquired_datetime store_acquired_date merchant_qa_approved_datetime  is_valid_transaction merchant_paylater_config_type sale_type sale_parent_type  rank_tid  soundbox_tran_type_id sb_1st_install_date
0  2024-10-09 2024-10-09 22:48:27 2024-10-01  68647470326        m4b1ynt20240301  18333324  50000.0        1         MOMO   static aio qr - momo               MoMo  MOMO1YNT20240301   1654364  3KTLI9XBuhaPInXA  MOMO1YNT20240301_3KTLI9XBuhaPInXA    TRẦN TIẾN THÂN                    THREEMART.VN               BPU  INDIVIDUAL_SALE_ONBOARDING   SME OFFLINE       Bình Phước      Đồng Xoài      Tân Phú            SME     SME OFFLINE          RETAIL         GROCERY  TRADITIONAL MARKET / GROCERY STORE / SPECIALTY STORE                    THREEMART.VN    directsale  dung.nguyen16  nhien.nguyen    directsale              2. RETENTION                     3.HEAVY                  SAPO                       OFFLINE     Không thuộc iPOS               1                         7                                 17                         2024-03-07        2024-03-18 16:41:06     2024-03-07 23:21:35          2024-03-07           2024-03-18 16:41:10                  True               enable paylater       ctv          inhouse         1                      0          2025-03-14
1  2024-10-09 2024-10-09 16:30:38 2024-10-01  68619529731  m4b5jb020240810_42497  89904447  49000.0        1         MOMO  dynamic aio qr - momo               MoMo  MOMO5JB020240810   2086531  nvAXWIfmG0zVTmZ7  MOMO5JB020240810_nvAXWIfmG0zVTmZ7       NGÔ MỸ HẠNH        NHÀ HÀNG CHAY TUỆ NGUYÊN               BPU  INDIVIDUAL_SALE_ONBOARDING   SME OFFLINE       Bình Dương    Thủ Dầu Một  Chánh Nghĩa            SME     SME OFFLINE             FNB            FOOD                                                DINING        NHÀ HÀNG CHAY TUỆ NGUYÊN    directsale  dung.nguyen16    luan.huynh    directsale              2. RETENTION                     3.HEAVY                  IPOS                       OFFLINE  1. CH tĩnh qua động               1                         4                                  4                         2024-08-10        2024-08-14 16:18:12     2024-08-10 16:34:27          2024-08-10           2024-08-14 16:18:15                  True                  non-paylater       ctv          inhouse         1                      0          2024-10-31
2  2024-10-09 2024-10-09 19:33:48 2024-10-01  68633764824  m4bhh5v20240809_42061  33855440  54000.0        1         MOMO  dynamic aio qr - momo               MoMo  MOMOHH5V20240809   2085480  0fjIYjV7xq0kIELm  MOMOHH5V20240809_0fjIYjV7xq0kIELm         LÊ NHƯ SỸ  BABA TEA - COOP MART TÂN THÀNH               BPU  INDIVIDUAL_SALE_ONBOARDING   SME OFFLINE  Bà Rịa Vũng Tàu         Phú Mỹ       Phú Mỹ            SME     SME OFFLINE             FNB        BEVERAGE                                              MILK TEA  BABA TEA - COOP MART TÂN THÀNH    directsale  dung.nguyen16    luan.huynh    directsale              2. RETENTION                     3.HEAVY                  IPOS                       OFFLINE  1. CH tĩnh qua động               1                         4                                  5                         2024-08-09        2024-08-14 00:40:04     2024-08-09 19:08:23          2024-08-09           2024-08-14 00:40:08                  True                  non-paylater       ctv          inhouse         1                      0          2025-04-25
3  2024-10-09 2024-10-09 14:21:57 2024-10-01  68611259504  m4bhh5v20240809_42061  42600921  36000.0        6          TTT  dynamic aio qr - momo               MoMo  MOMOHH5V20240809   2085480  0fjIYjV7xq0kIELm  MOMOHH5V20240809_0fjIYjV7xq0kIELm         LÊ NHƯ SỸ  BABA TEA - COOP MART TÂN THÀNH               BPU  INDIVIDUAL_SALE_ONBOARDING   SME OFFLINE  Bà Rịa Vũng Tàu         Phú Mỹ       Phú Mỹ            SME     SME OFFLINE             FNB        BEVERAGE                                              MILK TEA  BABA TEA - COOP MART TÂN THÀNH    directsale  dung.nguyen16    luan.huynh    directsale              2. RETENTION                     3.HEAVY                  IPOS                       OFFLINE  1. CH tĩnh qua động               1                         4                                  5                         2024-08-09        2024-08-14 00:40:04     2024-08-09 19:08:23          2024-08-09           2024-08-14 00:40:08                  True                  non-paylater       ctv          inhouse         1                      0          2025-04-25
4  2024-10-09 2024-10-09 19:55:31 2024-10-01  68635650121        m4bmtjb20240530  48205649  25000.0        6          TTT   static aio qr - momo               MoMo  MOMOMTJB20240530   1963252  dcxsGWwxIaUcxPOi  MOMOMTJB20240530_dcxsGWwxIaUcxPOi        BÙI KIM HÀ                   TRÀ SỮA ỰC ỰC               BPU  INDIVIDUAL_SALE_ONBOARDING   SME OFFLINE       Bình Dương       Tân Uyên    Uyên Hưng            SME     SME OFFLINE          RETAIL         GROCERY  TRADITIONAL MARKET / GROCERY STORE / SPECIALTY STORE   NGUYÊN LIỆU PHA CHẾ KIM KHÁNH    directsale  dung.nguyen16      tra.tran    directsale              2. RETENTION                     3.HEAVY                  IPOS                       OFFLINE  1. CH tĩnh qua động               1                         4                                  4                         2024-06-20        2024-06-06 15:49:17     2024-05-30 14:06:21          2024-05-30           2024-06-03 14:48:13                  True               enable paylater       ctv          inhouse         1                      1          2024-08-26
```

### project-5400504384186300846.MBI_DA.DM_OFF_STORE_PROFILE

**Description**: Profile của các store trong hệ thống M4B. Primary key: store_id. Trong bảng có các cột có tiền tố 'merchant_' là những cột thông tin ở cấp độ merchant, sẽ lặp lại giữa các store có cùng merchant_id. Các cột không có tiền tố 'merchant_' thì được hiểu là thông tin của store, ví dụ cột city_name được hiểu là city của store nhưng merchant_city_name được hiểu là city của merchant.

Thông tin có thể được lấy từ bảng này bao gồm:
- Danh sách store và mã định danh riêng biệt trên M4B
- Thông tin trạng thái và hoạt động của từng store
- Lịch sử giao dịch và thanh toán của store trong các khoảng thời gian xác định

#### Columns

| Column Name | Description |
|-------------|-------------|
| store_id | ID của store bằng số, khác với store_code bằng chữ, mã này unique cho mỗi store trên M4B |
| store_code | Mã store bằng chữ, ví dụ 'Xzyuabc...', khác với mã store bằng số (store ID). Tuy nhiên, field store_code này ở một số bảng raw được đặt là store_id, partner_store_id. Do đó, cần kiểm tra giá trị bên trong cột là store_code hay store_id khi join |
| merchant_code | Mã định danh merchant bằng chữ, còn được gọi là partner_code trong một số bảng dữ liệu hoặc được gọi là 'MID' theo cách gọi của BU. Merchant_code là unique cho mỗi merchant |
| merchant_id | Mã định danh merchant bằng số. Merchant_id là unique cho mỗi merchant |
| latest_state_code | State code (snapshot) của store |
| latest_state_name | Mô tả trạng thái của store dựa vào latest_state_code như: đã duyệt, chưa QA, đã thanh lý... |
| brand_name | Tên thương hiệu trên M4B, nhiều merchant_id có chung brand name |
| merchant_name_m4b | Tên merchant trên M4B, hiển thị trên màn hình thanh toán của user khi giao dịch. Tên này có thể khác với tên merchant trên service list và brand name trên M4B |
| merchant_name_sl | Tên merchant trên service list. Chỉ chọn một agent theo thứ tự ưu tiên để map 1-1 giữa merchant_id và service list |
| store_name | Tên cửa hàng trên M4B |
| representative_name | Tên người đại diện của merchant |
| merchant_created_date | Ngày merchant được tạo ra trên hệ thống M4B |
| merchant_created_datetime | Thời điểm merchant được tạo ra trên hệ thống M4B |
| merchant_qa_approved_datetime | Thời điểm merchant được QA approve theo logic: last datetime if current state_code = 210 (QA Đã Duyệt) else null |
| merchant_qa_approved_date | Ngày merchant được QA approve theo logic: last date if current state_code = 210 (QA Đã Duyệt) else null |
| created_datetime | Thời điểm tạo store trên M4B |
| created_date | Ngày tạo store trên M4B |
| qa_approved_datetime | Thời điểm store được QA approve theo logic: if current state_code = 210 (QA Đã Duyệt) else null |
| qa_approved_date | Ngày store được QA approve theo logic: if current state_code = 210 (QA Đã Duyệt) else null |
| qr_activated_datetime | Thời điểm store lần đầu được gán với 1 mã QR code tĩnh |
| qr_activated_date | Ngày store lần đầu được gán với 1 mã QR code tĩnh |
| dynamic_qr_datetime | Thời điểm store lần đầu phát sinh 1 giao dịch thông qua qr động hoặc scanner pos |
| dynamic_qr_date | Ngày store lần đầu phát sinh 1 giao dịch thông qua qr động hoặc scanner pos |
| acquired_datetime | Thời điểm store được acquired, ngày này được hiểu là ngày store có thể thanh toán được |
| acquired_date | Ngày store được acquired, được tính vào kpi acquire cho sale |
| first_trans_date | Ngày đầu tiên phát sinh giao dịch |
| last_trans_date | Ngày cuối cùng phát sinh giao dịch cho đến thời điểm hiện tại |

*Note: This table contains 77+ columns total. Only the first 24 columns are shown here for brevity. The complete column list includes additional fields for transaction history, merchant categorization, sale team information, and business metrics.*

#### Sample Data

*Empty DataFrame - No sample data available for this table*

## Memory

This section contains business rules, query guidelines, and domain-specific knowledge from the SME team.

### Memory Entry 1

**Created**: 2025-07-10T16:14:01.795378

Để lấy merchant non soundbox, bạn phải lấy tất cả active merchant TRỪ ĐI active soundbox merchant. Cụ thể, để tính MoM retention của Merchant non-soundbox trong tháng 6/2025, sử dụng logic sau:

```sql
WITH mc_sb_active_may AS (
SELECT DISTINCT merchant_code
FROM project-5400504384186300846.MBI_DA.DM_OFF_TRANSACTION
WHERE TRUE
AND DATE_TRUNC(date, MONTH) = '2025-05-01'
AND soundbox_tran_type_id = 1
AND is_valid_transaction = True
),
mc_sb_active_june AS (
SELECT DISTINCT merchant_code
FROM project-5400504384186300846.MBI_DA.DM_OFF_TRANSACTION
WHERE TRUE
AND DATE_TRUNC(date, MONTH) = '2025-06-01'
AND soundbox_tran_type_id = 1
AND is_valid_transaction = True
),
final_sb AS (
SELECT mc_sb_active_may.merchant_code,
IF(mc_sb_active_june.merchant_code IS NOT NULL, 1, 0) AS is_retain_merchant
FROM mc_sb_active_may
LEFT JOIN mc_sb_active_june
USING(merchant_code)
),

mc_non_sb_active_may AS (
SELECT DISTINCT merchant_code
FROM project-5400504384186300846.MBI_DA.DM_OFF_TRANSACTION
WHERE TRUE
AND DATE_TRUNC(date, MONTH) = '2025-05-01'
AND is_valid_transaction = True

EXCEPT DISTINCT

SELECT DISTINCT merchant_code
FROM mc_sb_active_may
),
mc_non_sb_active_june AS (
SELECT DISTINCT merchant_code
FROM project-5400504384186300846.MBI_DA.DM_OFF_TRANSACTION
WHERE TRUE
AND DATE_TRUNC(date, MONTH) = '2025-06-01'
AND is_valid_transaction = True

EXCEPT DISTINCT

SELECT DISTINCT merchant_code
FROM mc_sb_active_june
),
final_non_sb AS (
SELECT mc_non_sb_active_may.merchant_code,
IF(mc_non_sb_active_june.merchant_code IS NOT NULL, 1, 0) AS is_retain_merchant
FROM mc_non_sb_active_may
LEFT JOIN mc_non_sb_active_june
USING(merchant_code)
)

SELECT (COUNT(DISTINCT CASE WHEN final_sb.is_retain_merchant = 1 THEN final_sb.merchant_code END) / COUNT(DISTINCT final_sb.merchant_code)) - (COUNT(DISTINCT CASE WHEN final_non_sb.is_retain_merchant = 1 THEN final_non_sb.merchant_code END) / COUNT(DISTINCT final_non_sb.merchant_code))
FROM final_sb, final_non_sb;
```

---

### Additional Memory Entries

The domain contains 31 total memory entries with business rules, SQL query examples, and team-specific guidance for using the SME OFFLINE PAYMENT dataset. These memories include:

- Complex merchant retention analysis methodologies
- Soundbox tracking and categorization rules
- Query optimization guidelines for large datasets
- Business logic for merchant size classification
- Integration rules between M4B and IPOS systems
- SME team domain usage instructions

**Note**: User sử dụng domain này thuộc team SME. All memory entries preserve original Vietnamese business terminology and SQL logic as specified in the raw data source.

## Usage Guidelines

This dataset is maintained by the SME team and contains sensitive business information. Users should:

1. **Filter valid transactions**: Use `is_valid_transaction = True` for business analysis
2. **Apply amount thresholds**: For offline merchant projects, filter transactions with `amount >= 10000` (rule as of 11/2023)
3. **Handle merchant categorization carefully**: Different merchant types (SME OFFLINE, TOPBRAND OFFLINE, etc.) require specific filtering logic
4. **Preserve Vietnamese terminology**: All business descriptions and column names should remain in their original Vietnamese form
5. **Follow team-specific guidelines**: Consult memory entries for complex business logic and query patterns

Contact: cong.tran1@mservice.com.vn
Maintained by: team CDO-K khai.do@mservice.com.vn