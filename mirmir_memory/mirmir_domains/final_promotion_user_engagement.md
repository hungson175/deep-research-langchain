# Promotion - User Engagement Domain Response

## Error Code
200

## Data

### ID
e9363d1c-6486-4072-8dc5-8d06260e9c7f

### Name
Promotion - User Engagement

### Description
Ghi nhận các tương tác của user với promotion campaign và gift (impression, click). Data được aggregate theo ngày, touchpoint của Promotion, campaign_id và gift_type_id

### Instructions
(empty)

## Schema DDL

### Dataset Name
Promotion - User Engagement

### Table Name
`momovn-mds-dc.dmt.F_PROMO_CAMPAIGN_GIFT_ENGAGEMENT_TOUCHPOINT_LEVEL_DAILY`

### Table Description
Bảng fact này lưu trữ dữ liệu hàng ngày liên quan đến mức độ tương tác của người dùng với các điểm chạm của chiến dịch khuyến mãi quà tặng. Bảng này có thể được sử dụng để:
- Theo dõi hiệu suất của các chiến dịch khuyến mãi hàng ngày
- Đo lường mức độ tương tác và hành vi của người dùng với các quà tặng trong các chiến dịch
- Phân tích tỷ lệ chuyển đổi của các sự kiện với tương tác người dùng qua các điểm chạm

### Columns

#### `DATE_KEY`
- **Description:** Khóa thời gian, định danh duy nhất cho ngày
- **Example data:** ["2025-08-01-month","2025-09-01-month","2025-08-29-day"]

#### `MONTH_DATE`
- **Description:** Ngày trong tháng
- **Example data:** ["2025-08-01","2025-09-01"]

#### `WEEK_DATE`
- **Description:** Ngày trong tuần
- **Example data:** []

#### `DAY_DATE`
- **Description:** Ngày cụ thể
- **Example data:** ["2025-08-29","2025-08-30","2025-08-27"]

#### `GRANULARITY`
- **Description:** Độ chi tiết của dữ liệu
- **Example data:** ["month","day"]

#### `HIERARCHY_LEVEL`
- **Description:** Cấp độ phân cấp của dữ liệu
- **Example data:** ["4","3","2"]

#### `CAMPAIGN_ID`
- **Description:** Mã ID của chiến dịch khuyến mãi (PII value)

#### `GIFT_TYPE_ID`
- **Description:** Mã ID của loại quà tặng (PII value)

#### `TOUCHPOINT_LEVEL_1`
- **Description:** Cấp độ điểm chạm đầu tiên của chiến dịch
- **Example data:** ["DECENTRALIZED_PROMOTION","PROMOTION_HUB","VOUCHER_DETAIL","SAFE_PAYMENT","ALL","MY_VOUCHER","MY_POCKET","POS","SWIPE_VOUCHERS","GLOBAL_SEARCH"]

#### `TOUCHPOINT_LEVEL_2`
- **Description:** Cấp độ điểm chạm thứ hai của chiến dịch
- **Example data:** ["MomoTransactionResult","ALL","","promotion_hub","promotion","voucher_detail","MomoTransactionResult_MoMoQR","HomeScreen","voucher_detail_lite","funds_manager","my_vouchers","gift_category","my_pocket","look_back_month","paylaterverse_cs_home","all_recommended_voucher_collection","investment_goldenpocket_payment_service","payment_vouchers","credit_paylater_home","offline_hub","momo_rewards_view_detail","loyalty_telco","store_applied","brand_promo_detail","all_voucher_collection_standard","W2B_RewardsVoucher","all_voucher_collection_spotlight","all_voucher_collection_ml_occasion","OTAHome","shake_nearby_game","mission_detail","payment_vouchers_search","all_voucher_collection_ipos","all_mission","all_voucher_collection_flashdeal","shopxu2023","all_oa_nearby","swipe_vouchers","auto_cashin_cashout","student_benefits","oa_momo_cornerstone","investment_goldenpocket","MyQR_tabMe_widget","booking_bus","MobileTopup","ins_marketplace_home","booking_bus_select_ticket","all_quiz","paylaterverse_cs_ob","paylaterverse_cs_quick_ob"]

#### `TOUCHPOINT_LEVEL_3`
- **Description:** Cấp độ điểm chạm thứ ba của chiến dịch
- **Example data:** ["ALL","bd867df3-6074-4ead-a886-c2384f2ef7fc","a614f0f1-32a3-4200-9074-87f14a43c1b8"]

#### `TOUCHPOINT_LEVEL_4`
- **Description:** Cấp độ điểm chạm thứ tư của chiến dịch
- **Example data:** ["ALL","","-","HomeNative","topup_Viettel","banklink_cashin","transfer_via_link_w2w","transfer_p2p","topup_Mobifone","topup_Vinaphone","topup_data_viettel","INFINITY_SCROLL_BLOCK","MY_VOUCHER_BLOCK","transfer_p2b","topup_data_mobi","topup_data_vina","urgent_list","evn_hcm","topup_Vietnamobile","EPAY_VIETTEL","transfer_p2p_search_paste","EVN_HANOI","evnspc_dongnai","EPAY_MOBIFONE","RECOMMENDED_BLOCK","STANDARD_BLOCK_VOUCHER_REWARD","NUOCCHOLON","evn_danang","topup_Itel","investment_goldenpocket","transfer_p2b_globalsearch","topup_Local","buycard_data_mobifone","transfer_p2b_scan_vietqr_upload","transfer_p2p_global_presearch","topup_Reddi","transfer_p2b_scan_vietqr","topup_Saymee","banklink_cashout","transfer_p2p_globalsearch","transfer_p2b_search_paste","nshn2","EPAY_VIETNAMOBILE","EPAY_VINAFONE","buycard_data_vinaphone","IFPT","OCCASION_MORNING","SPOTLIGHT_BLOCK_SUMMER_CAMP","transfer_luckymoney","OCCASION_LUNCH"]

#### `VOUCHER_IMPRESSION`
- **Description:** Số lần hiển thị voucher
- **Example data:** ["0","1","2"]

#### `VOUCHER_IMPRESSION_USER`
- **Description:** Số người dùng đã xem voucher
- **Example data:** ["0","1","2"]

#### `VOUCHER_ENGAGEMENT`
- **Description:** Số lần tương tác với voucher
- **Example data:** ["0","1","2"]

#### `VOUCHER_ENGAGEMENT_USER`
- **Description:** Số người dùng đã tương tác với voucher
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_COLLECT`
- **Description:** Số lượt nhấp vào voucher để thu thập
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_COLLECT_USER`
- **Description:** Số người dùng đã nhấp vào voucher để thu thập
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_VIEW_DETAIL`
- **Description:** Số lượt nhấp vào voucher để xem chi tiết
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_VIEW_DETAIL_USER`
- **Description:** Số người dùng đã nhấp vào voucher để xem chi tiết
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_USE`
- **Description:** Số lượt nhấp vào voucher để sử dụng
- **Example data:** ["0","1","2"]

#### `VOUCHER_CLICK_USE_USER`
- **Description:** Số người dùng đã nhấp vào voucher để sử dụng
- **Example data:** ["0","1","2"]

#### `CTR_EVENT`
- **Description:** Tỷ lệ chuyển đổi của sự kiện
- **Example data:** ["0","1","0.5"]

#### `CTR_USER`
- **Description:** Tỷ lệ chuyển đổi theo người dùng
- **Example data:** ["0","1","0.5"]

#### `ETL_TIME`
- **Description:** Thời gian ETL
- **Example data:** ["2025-09-01 20:11:40.398400+00","2025-09-03 01:57:57.474874+00","2025-09-01 16:26:14.656103+00"]

## Knowledgebase
(empty)

## Memory

### 1. Bounce user definition
Bounce user được định nghĩa là người dùng đã thấy voucher nhưng không thực hiện bất kỳ tương tác nào

### 2. Touchpoint analysis
Khi phân tích theo một cấp độ touchpoint_level cụ thể (ví dụ: touchpoint_level = 2), cần bao gồm các cột touchpoint_level trước đó (ví dụ: touchpoint_level_1) trong truy vấn.

## Error Message
(empty)