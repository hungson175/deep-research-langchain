# BILLPAY - Business metrics

## Dataset Overview

**Domain ID:** 28214cde-da94-48ef-9039-00fa6f448da7
**Domain Name:** BILLPAY - Business metrics
**Description:** Records all business information of Billpay services (including mau, transaction details, user demographics, etc.)

## Database Schema

### Table 1: MIMIR_BILLPAY_DETAILS
**Full Table Name:** `project-5400504384186300846.BU_UTILITIES_TELCO.MIMIR_BILLPAY_DETAILS`

This table contains detailed transaction records for bill payment services.

#### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| month_active | DATE | The month that the user has payment |
| date | DATE | Date of the transaction |
| user_id | STRING | Unique ID of a user |
| subcategory | STRING | The category of the service. "DIEN" means Electricity, "NUOC" means Water, "INTERNET" means Internet, "TRUONG HOC" means trường học |
| merchant | STRING | Name of the supplier |
| transaction_count | INTEGER | The number of transaction made |
| amount | FLOAT | The amount of the transactions (currency: VND) |
| voucher_amount | FLOAT | The discounted amount |
| voucher_or_not | STRING | This shows if the user used voucher or not. "Voucher" means the user used voucher, "Non voucher" or "Non_voucher" means the user did not use voucher for that specific transaction |
| revenue | FLOAT | Revenue our company gets from the transactions |
| user_type | STRING | Segment of the user (considered across our domain billpay). "retain_user" means the user pay in 2 consecutive months. "new_user" means the user pay the first time in the stated month. "churn_user" means the user did not pay in the month before but come back and pay in the stated month |
| user_type_sub | STRING | Segment of the user (by subcategory) |
| user_type_mer | STRING | Segment of the user (by merchant) |
| region | STRING | Region of user's location |
| city_group | STRING | Group of city of user's location |
| city | STRING | The city name of user's location |
| age | NUMERIC | User's age (null means unknown) |
| age_group | STRING | User's age group |
| gender | STRING | User's gender |
| login_app_count | INTEGER | The number of session that the user login our mobile application |
| login_billpay_center_count | INTEGER | The number of session that the user login our service center inside our mobile application |
| display_xbanner_count | INTEGER | The number of session that the user saw our xbanner (or x-banner). Xbanner is debt remind banner that we show the user inside our app when it comes to the due date |
| click_xbanner_count | INTEGER | The number of clicks that the user clicked on our xbanner |

#### Sample Data
| month_active | date | user_id | subcategory | merchant | transaction_count | amount | voucher_amount | voucher_or_not | revenue | user_type | user_type_sub | user_type_mer | region | city_group | city | age | age_group | gender | login_app_count | login_billpay_center_count | display_xbanner_count | click_xbanner_count |
|--------------|------|---------|-------------|----------|-------------------|--------|----------------|----------------|---------|-----------|---------------|---------------|--------|------------|------|-----|-----------|--------|-----------------|---------------------------|---------------------|-------------------|
| 2024-10-01 | 2024-10-03 | 22879770 | DIEN | EVN HO CHI MINH | 1 | 600000 | 0 | Non_voucher | 0 | retain_user | retain_user | retain_user | Đông Nam Bộ | Thành Phố Hồ Chí Minh | Hồ Chí Minh | None | [4].28-35 | male | 0 | 0 | 0 | 0 |
| 2024-08-01 | 2024-05-02 | 85111949 | NUOC | ADSL FPT | 2 | 1200000 | 20000 | Voucher | 11999.999999999998 | recover_user | recover_user | recover_user | Đồng bằng sông Hồng | Tỉnh khác | Hà Nội | 31 | [5].36-50 | female | 12 | 24 | 12 | 12 |
| 2024-09-01 | 2024-08-03 | 40718935 | INTERNET | MY VIETTEL | 3 | 1000000 | 60000 | None | 23999.999999999996 | new_user | new_user | new_user | Nam Trung Bộ | Hà Nội | Bình Dương | 29 | [3].23-27 | unknown | 4 | 12 | 24 | 8 |
| 2024-07-01 | 2024-10-04 | 9020814 | DIEN THOAI TRA SAU | EVN HA NOI | 4 | 800000 | 30000 | None | 17999.999999999996 | unknown | unknown | unknown | Đồng bằng sông Cửu Long | KCN Miền Nam | Đồng Nai | 30 | [2].18-22 | None | 6 | 48 | 6 | 24 |
| 2024-11-01 | 2024-07-03 | 43416840 | OTHER | VNPT TOAN QUOC | 5 | 1800000 | 10000 | None | 35999.999999999993 | None | None | None | Bắc Trung Bộ | TP Lớn | Đà Nẵng | 28 | [6].>50 | None | 24 | 60 | 4 | 6 |

### Table 2: USER_JOURNEY_BILLPAY_PIVOT
**Full Table Name:** `momovn-prod.BU_UTILITIES_TELCO.USER_JOURNEY_BILLPAY_PIVOT`

This table tracks user journey events and interactions within the billpay service.

#### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| dt | DATE | date |
| user_id | STRING | Unique ID of each user |
| bill_detail_screen | INTEGER | Number of events of viewing or displaying bill detail screen |
| billpay_center_screen | INTEGER | Number of events of viewing or displaying billpay center service home screen. Billpay is our domain |
| Button_save_bill | INTEGER | Number of event that user check bill information successfully, and that bill is saved |
| button_trans_result | INTEGER | |
| click_noti | INTEGER | Number of event that user click a notification about billpay service |
| click_xbanner | INTEGER | Number of event that user click X-banner (or xbanner). X-banner (or Xbanner) is a special notification of our domain. |
| close_xbanner | INTEGER | Number of event that user close X-banner (or xbanner). X-banner (or Xbanner) is a special notification of our domain. |
| displayed_xbanner | INTEGER | Number of event that X-banner is displayed to user |
| MHTTAT | INTEGER | Number of event that secured payment screen (MHTTAT means màn hình thanh toán an toàn or secured payment screen) is displayed to user |
| my_wallet | INTEGER | |
| search | INTEGER | |
| trans_confirmation | INTEGER | |
| icon_click | INTEGER | Number of event that user click the icon in Momo Home screen to visit Billpay center screen. (Momo is our mobile application, Billpay is our domain or a service inside Momo) |

#### Sample Data
| dt | user_id | bill_detail_screen | billpay_center_screen | Button_save_bill | button_trans_result | click_noti | click_xbanner | close_xbanner | displayed_xbanner | MHTTAT | my_wallet | search | trans_confirmation | icon_click |
|----|---------|-------------------|----------------------|------------------|-------------------|------------|---------------|---------------|-------------------|--------|-----------|--------|-------------------|------------|
| 2023-03-10 | 0 | None | None | None | None | None | None | None | 1 | None | None | None | None | None |
| 2023-03-15 | 1832507 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | None | 1 | 1 | 1 | 1 | 1 |
| 2023-03-14 | 39324865 | 4 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2023-03-16 | 39192740 | 1 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2023-03-13 | 69846347 | 6 | 6 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |

### Table 3: BILLPAY_ADD_BILLS
**Full Table Name:** `momovn-prod.BU_UTILITIES_TELCO.BILLPAY_ADD_BILLS`

This table contains information about bills added by users to their digital wallet.

#### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| user_id | STRING | Unique ID of the user |
| bill_id | STRING | Unique ID of the bill |
| category | STRING | Service that the bill belongs to |
| add_bill_date | DATE | The date that user check and add the bill successfully to user's digital wallet |
| age_group | STRING | User's age group |
| most_city_a60 | STRING | Name of the city of user's location over the last 60 days |
| most_district_a60 | STRING | Name of the district of user's location over the last 60 days |
| most_ward_a60 | STRING | Name of the ward of user's location over the last 60 days |
| most_region | STRING | Name of the region of user's location over the last 60 days |

#### Sample Data
| user_id | bill_id | category | add_bill_date | age_group | most_city_a60 | most_district_a60 | most_ward_a60 | most_region |
|---------|---------|----------|---------------|-----------|---------------|-------------------|---------------|-------------|
| 41202429 | 39622905 | Điện | None | [5]. 31 - 35 Y/O | UNKNOWN | UNKNOWN | I3WZl7PFmITcTA/1Mg1jAbDn9jvw9kg6e1TX1DvFzNE= | ĐÔNG NAM BỘ |
| 41625780 | 49031342 | Finance Collection Inapp | 2022-06-23 | [4]. 27 - 30 Y/O | HỒ CHÍ MINH | BÌNH THẠNH | BnnIqBxxFh3k9WzmC4mBEGEmOPCFQkAj8GUAxF2+rN0= | UNKNOWN |
| 19006549 | 45301099 | Nước | 2024-09-10 | [7]. >40 Y/O | HÀ NỘI | BIÊN HÒA | zySpLLwKrFsHFEk5t+uv+ohM+k24nREiVpemRxqncpI= | ĐỒNG BẰNG SÔNG HỒNG |
| 33520679 | 71056150 | Internet | 2021-03-13 | [3]. 23 - 26 Y/O | BÌNH DƯƠNG | GÒ VẤP | BPk3wG15rYobEe2LIxzaFstQanPOkGCyRtDEAAF6WyA= | ĐỒNG BẰNG SÔNG CỬU LONG |
| 45642856 | 27126295 | Điện thoại | 2021-03-10 | [6]. 36 - 40 Y/O | ĐỒNG NAI | TÂN BÌNH | yW8kJ9OhdaESUYQYxBjE2FEYenEnaRA8xL3KIwz+Xxk= | NAM TRUNG BỘ |

## Business Rules and Memory

### Memory Entries

1. **Current Month Calculation**
   - **Rule ID:** c3b205ad-58ab-4913-9f91-b96c77c6959b
   - **Vietnamese:** Tháng này: tháng này là date_trunc(date(current_date('+7')), month )
   - **Translation:** Current month: current month is date_trunc(date(current_date('+7')), month )
   - **Created:** 2025-05-13T14:20:39.328061

2. **Billpay Visitors Count**
   - **Rule ID:** 23e155a8-6f66-45e7-898d-bf0b75aa98c9
   - **Vietnamese:** Số người truy cập billpay: Số người truy cập billpay = count(distinct case when billpay_center_screen > 0 then user_id end)
   - **Translation:** Number of billpay visitors: Number of billpay visitors = count(distinct case when billpay_center_screen > 0 then user_id end)
   - **Created:** 2025-05-13T14:20:59.202907

## Business Context

This dataset provides comprehensive business intelligence for MoMo's bill payment services:

### Key Business Areas
- **Transaction Analytics:** Revenue tracking, voucher usage, and payment patterns
- **User Behavior:** Journey tracking, engagement metrics, and interaction patterns
- **Demographics:** Age, gender, and location-based segmentation
- **Service Categories:** Electricity (DIEN), Water (NUOC), Internet, Education (TRUONG HOC)
- **User Lifecycle:** New users, retained users, churned users, and recovered users

### Vietnamese Business Terms
- **DIEN:** Electricity services
- **NUOC:** Water services
- **INTERNET:** Internet services
- **TRUONG HOC:** Educational institution payments
- **MHTTAT:** Màn hình thanh toán an toàn (Secure payment screen)
- **X-banner:** Debt reminder banner shown to users approaching due dates

### Revenue Model
The dataset tracks both transaction amounts and company revenue, with voucher discounts affecting the final revenue calculations. Revenue figures are in Vietnamese Dong (VND).

### Geographic Coverage
The data includes detailed location information across Vietnamese regions:
- **Đông Nam Bộ** (Southeast region)
- **Đồng bằng sông Hồng** (Red River Delta)
- **Nam Trung Bộ** (South Central region)
- **Đồng bằng sông Cửu Long** (Mekong Delta)
- **Bắc Trung Bộ** (North Central region)