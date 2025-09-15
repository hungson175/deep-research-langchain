# Promotion - Campaign Performance API Response

## Error Code

200

## Data

### ID
9d86b9d9-bf1e-4bab-8e11-86279716984a

### Name
Promotion - Campaign Performance

### Description
Data của campaign performance theo funnel từ delivery -> redeem, và các metric liên quan đến cost và gmv của Promotion (toàn MoMo). Note: chỉ có data của voucher code mềm (không bao gồm voucher code cứng)

### Instructions
(empty)

## Schema DDL

### Dataset name: Promotion - Campaign Performance

**Table information:**
- **Table name:** `momovn-prod.MBI_DA.PROMOTION_PERFORMANCE_AGG`
- **Table description:** Bảng này tổng hợp thông tin hiệu suất của các chương trình khuyến mãi và gift trong MoMo. Dữ liệu từ bảng này có thể được sử dụng cho các mục đích như đánh giá hiệu quả của chương trình khuyến mãi, theo dõi tình trạng sử dụng gift và phân tích chi phí liên quan đến gift.
  - Theo dõi hiệu suất và tình trạng của các gift được phát hành và sử dụng.
  - Phân tích hiệu quả và chi phí của các chương trình khuyến mãi.
  - Đánh giá mức độ thành công của các campaign dựa trên các tiêu chí như GMV và số lượng user sử dụng gift.

**Column descriptions:**

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| DELIVER_DATE | Ngày thả gift | 2025-01-24, 2025-04-20, 2025-05-15 |
| END_DATE | Ngày hết hạn gift | 2025-06-21, 2025-06-28, 2025-03-18 |
| REDEEM_DATE | Ngày sử dụng gift | 2025-03-24, 2025-03-28, 2025-03-31 |
| CAMPAIGN_ID | ID của campaign | 1341738947242397696, 1344570166793166848, 1344979770159730688 |
| GIFT_TYPE_ID | ID của gift_type | 0325_newretention_10k_allser, 1341738947242397696, 1344570166793166848 |
| STATUS_DESC | Mô tả của trạng thái của gift | Voucher Refund, Voucher bị treo, Voucher đã thu hồi, Voucher hết hạn, Voucher đã sử dụng, Voucher còn hạn nhưng User xóa, Voucher còn hạn, Voucher hiện disabled trên UI |
| IS_TID | Liệu có phải là TID hay không (1: có) | 1, 0 |
| AGENT | Agent của gift | kgs_vtti_billpay_cs_csat_2404, kgs_fs_newuser_affiliate_ndgt_0522, kgs_dls324_mcinv_b2b_20250612_0076 |
| VOUCHER_DELIVERY | Số lượng gift được phát | 69, 9, 16 |
| VOUCHER_REDEEM | Số lượng gift được sử dụng | 1397, 2866, 335 |
| VOUCHER_COST | Chi phí sử dụng gift | 520000, 11400, 3000 |
| GMV | GMV từ các giao dịch sử dụng gift | 355765, 133492, 3438949 |
| REFUND_VOUCHER_COST | Chi phí được hoàn lại của gift | -24339, -2900, -50000 |
| REFUND_GMV | GMV từ các giao dịch được hoàn lại | -142000, -124000, -24000 |
| DELIVER_USER | Số lượng deliver user (đã gom nhóm theo các dimension của table) | 130, 72, 64 |
| REDEEM_USER | Số lượng redeem user (đã gom nhóm theo các dimension của table) | 1397, 2866, 335 |
| PARTITION_DATE | Ngày partition | 20250406, 20250204, 20250607 |
| CAMPAIGN_NAME | Tên chương trình | Giảm 25% cho 1 phần Steak (Steak Diane/Steak Au Poirve), "Mua vé Metro - nhận combo quà lên đến 500k", Milano Coffee 2074 |
| CAMPAIGN_START_DATE | Thời gian campaign bắt đầu | 2025-06-06, 2025-06-09, 2025-04-25 |
| CAMPAIGN_END_DATE | Thời gian campaign kết thúc | 2025-03-31, 2025-03-28, 2025-03-24 |
| CAMPAIGN_SCHEME | Scheme của campaign theo thông tin hệ thống | coin_reward, open_app, kindle, campaign_event, cosmos, direct_push_reward, collect_voucher, budget_coin_reward, no_budget_kindle, budget_direct_push_reward, no_budget_open_app, compensation, open_app_kindle, no_budget_open_app_kindle, m4b_collect_voucher, campaign_collect, budget_collect_voucher |
| SOURCE | Nguồn tạo campaign (ipos, builder, etc.) | IPOS_CAMPAIGN, BUILDER_CAMPAIGN |
| BU_CREATED | BU tạo gift | DLS - Marketplace, GMC Monetization - Notifications, DLS - SME offline merchant, MDS - Student Pass, DLS - Offline, Key Account, UTI - Billpay, DLS - Ads Inventory, DLS - Offline, retail & FnB, FS - Bank Partnership, GMC Cross-sell, DLS - OTA, FS - FI collection & disbursement, GMC - New User, MDS - Promotion Hub, Social Payment, DLS - Cinema, MDS - Thổ Địa MoMo, DLS - OTT, DLS - Food Delivery & Logistic, Product Owner, Online Payment, Platform, EPS Growth, FS - InvestTech - Brokerage, GMC Retention - Notifications, MDS - Rewards, FS - InsurTech, UTI - Airtime, Business Camp Budget, Promotion_QC&Dev, Promotion - Ops Nike, NFC - Ads, GMC - CRM, DLS - Game, Application Store & Entertainment, FS - CreditTech, [PCS] PCS Platform Account, UTI - Public services, DLS - Ads payment, (Inactive) DLS, UTI - Data |
| DISTRIBUTION_GROUP | Nhóm scheme campaign (level 1) | collect, delivery_by_trans, delivery_by_engagement, unknown, mission, passive |
| DELIVERY_SCHEME | Scheme của campaign (level 2) | pay_bill_core, social_sync_level, w2w_transfer_core, pay_bill_core_only, coin_reward, user_open_app, campaign_event, open_app, map_third_party, direct_push_reward, event_cornerstone_click, budget_direct_push_reward, merchant_map_third_party, no_budget_open_app_kindle, budget_collect_voucher, mission, aio_transfer, user_referral_student_pass, cvs_order_matching, open_app_kindle, user_follow_oa, m4b_collect_voucher, collect_voucher, budget_coin_reward, campaign_collect, kyc, compensation, source_of_fund_reorder, w2b_transfer_core, user_enter_code, no_budget_open_app, user_input_paybill |
| GIFT_TYPE_NAME | Tên của gift | SHANGCHI - Giảm 100.000đ cho đơn từ 500K, Sausaushop.vn - Giảm 20% tối đa 100K cho đơn từ 0đ, Giảm 20K Thẻ quà giảm 20K cho hoá đơn từ 100K khi thanh toán các dịch vụ trên MoMo |
| GIFT_TYPE_CATEGORY | Nhóm của gift_type | 9, 1, 5, 4, 7, 8, 0 |
| GIFT_TYPE_SOURCE | Nguồn tạo gift (ipos, athena, nike) | athena, nike, ipos |
| GIFT_TYPE_GROUP | Loại gift (discount, voucher_code, cashback, etc.) | physical_gift, voucher_code, others, cashback, discount |
| GIFT_TYPE_TYPE | Hình thức khuyến mãi (percent, etc.) | amount, percent, film_discount |
| DISCOUNT_PERCENT | Phần trăm giảm giá | 15, 95, 9 |
| GIFT_TYPE_CAP | Số tiền tối đa được giảm của gift | 200, 53000.0, 11000.0 |
| MIN_BILL_SIZE | Số tiền tối thiểu của bill để được sử dụng gift | 99000, 67000, 509000 |
| IS_STACKING | Liệu gift được stacking hay không | 1, 0 |
| IS_AUTO_PICK | Liệu gift có được autopick hay không | 1, 0 |
| IS_HARDCODE_VOUCHER | Liệu gift có phải là code cứng không | 1, 0 |
| ETL_TIME | Thời gian ETL | 2025-07-03 22:32:16.482881+00, 2025-09-01 16:48:37.355085+00, 2025-08-14 18:36:28.387632+00 |

## Knowledgebase

[]

## Memory

- **ID:** 63bb26a9-f5b2-40c2-a8d6-68559e9095b2
  **Memory:** redemption_rate = sum(voucher_redeem) / sum(voucher_delivery)
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T14:05:42.231378

- **ID:** 8b15fa33-911c-456c-932b-a71bca6aab8e
  **Memory:** gmv_after_refund = sum(gmv) + sum(refund_gmv)
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T14:05:46.426702

- **ID:** e97f96cb-dc49-41e1-b4fb-ac20fa99c533
  **Memory:** voucher_delivery: Số lượng gift được phát
  voucher_redeem: Số lượng gift được sử dụng
  voucher_cost: Chi phí sử dụng gift
  gmv: gmv từ các giao dịch sử dụng gift
  refund_voucher_cost: Chi phí được hoàn lại của gift
  refund_gmv: GMV từ các giao dịch được hoàn lại
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T14:03:44.400001

- **ID:** 51811fcb-cd44-40ed-9a60-56a0eb26556a
  **Memory:** Metric definition: voucher_cost_after_refund = SUM(voucher_cost) + SUM(refund_voucher_cost)
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T11:28:28.008211

- **ID:** c0923a7f-b8bf-4d3a-a0b1-672b5b28b9b4
  **Memory:** Metric definition: gmv_after_refund = sum(gmv) + sum(refund_gmv)
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T10:03:17.403723

- **ID:** a275e62f-d872-40d4-8eeb-4203ce0f31cb
  **Memory:** Metric definition: redemption_rate = sum(voucher_redeem) / sum(voucher_delivery)
  **User:** Promotion - Campaign Performance
  **Created:** 2025-07-29T10:03:14.114595

- **ID:** f3b35372-82dc-43cc-b8d0-0963e849f9c9
  **Memory:** Số lượng users vào PromoHub = số lượng user thu thập promo/đổi xu thành công trong PromoHub
  **User:** Promotion - Campaign Performance
  **Created:** 2025-08-12T15:03:48.997395

## Error Message

(empty)