# Offline User Domain Response

## Error Code
200

## Data

### ID
be87091d-f9df-4324-9451-d34e65c06256

### Name
Offline User

### Description
Bảng chi tiết các giao dịch offline của users theo từng tid

### Instructions
(empty)

## Schema DDL

**Dataset name:** Offline User

**Description:** Bảng chi tiết các giao dịch offline của users theo từng tid

**Table:** `project-5400504384186300846.MBI_DA.DM_AOS_TRANSACTION`

### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `tid` | INTEGER | |
| `date` | DATE | |
| `date_time` | DATETIME | |
| `agent_id` | INTEGER | |
| `amount` | FLOAT | |
| `service_lv1` | STRING | |
| `merchant_code` | STRING | |
| `store_code` | STRING | |
| `service_code` | STRING | |
| `merchant` | STRING | |
| `sender_bank_code` | STRING | |
| `sender_bank_name` | STRING | |
| `sender_acc_no_unique` | STRING | |
| `receiver_bank_code` | STRING | |
| `receiver_bank_name` | STRING | |
| `receiver_acc_no_unique` | STRING | |
| `d_aos_user_type_monthly_by_service_key` | STRING | |
| `d_aos_user_type_monthly_key` | STRING | |
| `payment_method` | STRING | |
| `payment_channel` | STRING | |
| `month_diff_from_last_active_total` | INTEGER | |
| `user_retain_total` | INTEGER | |
| `user_type_monthly_active_total` | STRING | |
| `user_type_monthly_trans_total` | STRING | |
| `user_type_monthly_overlap_total` | STRING | |
| `month_diff_from_last_active_service` | INTEGER | |
| `user_retain_service` | INTEGER | |
| `user_type_monthly_active_service` | STRING | |
| `user_type_monthly_trans_service` | STRING | |
| `city` | STRING | |
| `city_group_focus_province` | STRING | |
| `yob` | INTEGER | |
| `age` | INTEGER | |
| `age_group_big` | STRING | |
| `age_group` | STRING | |
| `merchant_name_m4b` | STRING | |
| `store_name` | STRING | |
| `city_store` | STRING | |
| `cate` | STRING | |
| `category_sl_lv1` | STRING | |
| `category_sl_lv2` | STRING | |
| `category_sl_lv3` | STRING | |
| `category_sl_lv4` | STRING | |
| `payment_type_lv1` | STRING | |
| `payment_type_lv2` | STRING | |
| `payment_type_lv3` | STRING | |
| `tid_new_offline_total` | INTEGER | |
| `tid_new_service` | INTEGER | |
| `tid_new_momo` | FLOAT | |
| `promo_type` | INTEGER | |
| `promo_amount` | FLOAT | |
| `agent_id_mapping` | INTEGER | |
| `rank_trans_by_month_service` | INTEGER | |
| `fund_id` | INTEGER | |

## Knowledgebase
(empty)

## Memory

The domain contains extensive memory entries with various calculations and analysis instructions. Key entries include:

### 1. MAU calculation for VietQR
Filter by service_lv1 = 'offline_m2b' for VietQR transactions

### 2. Service definitions
- **offline_m2b:** MoMo to Bank (VietQR)
- **offline_m2m:** MoMo to MoMo
- **offline_b2m:** Bank to MoMo

### 3. SME data
Use 'cate' column with value 'SME' for SME-related queries

### 4. User segmentation
Analysis by user_type_monthly_overlap_total groups (m2m_and_m2b, only_m2m, only_m2b, neither m2m nor m2b)

### 5. Transaction groups
Values include 'a. 1', 'b. 2-3', 'c. 4-8', 'd. 9-14', 'e. 15+' (with spaces)

### 6. New user calculations
Use tid_new_service for service-specific new users, tid_new_momo for MoMo new users

### 7. Retention rate
Calculate based on users active in consecutive months

### 8. City data
Use Vietnamese format with proper diacritics (e.g., "Hồ Chí Minh")

### 9. Promotion analysis
Use promo_type and promo_amount for promotional data

### 10. Merchant analysis
Use merchant column for merchant-specific queries

### 11. Geographic analysis
Use city, city_group_focus_province columns

### 12. Age group analysis
Use age_group columns for demographic segmentation

### 13. A30 users
Users who made at least one transaction in the last 30 days

### 14. Transaction counting
Use unique tid values for transaction counts

## Error Message
(empty)