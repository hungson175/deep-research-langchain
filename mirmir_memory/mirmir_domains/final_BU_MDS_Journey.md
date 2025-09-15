# BU MDS: Journey

## Basic Information

- **Error Code**: 200
- **ID**: 6471b001-623f-4ce2-a6a5-5bf63b2cf928
- **Name**: BU MDS: Journey
- **Description**: Thông tin về journey camp chạy, gồm CVR enter, goal, ctr noti, ctr adv

Cách tạo journey ở đây https://docs.google.com/presentation/d/17Ql0pm8iCq9zsmCTsyaMLMpms7G_fTdIsal2-VOTkVc/edit?slide=id.g2e2e0b1a5bb_0_1563#slide=id.g2e2e0b1a5bb_0_1563

- **Instructions**:

## Schema DDL

### Dataset name: BU MDS: Journey

## Table information:

**Table Name**: `momovn-prod.MBI_DA.journey_track_node_agg_v2`

**Table Description**: Bảng này chứa dữ liệu tổng hợp về hành trình của người dùng trong mạng lưới MoMo, bao gồm thông tin chi tiết về các node trong hành trình, các campaign và hành động của người dùng.

**Mục đích sử dụng**:
- Theo dõi và phân tích hiệu quả của các chiến dịch quảng cáo và thông báo đến người dùng.
- Đánh giá và tối ưu hóa hành trình của người dùng thông qua các hành động được yêu cầu từ hệ thống.
- Phân loại và đánh giá các loại mục tiêu mà Business Unit đề ra trong các chiến dịch.

**Column Descriptions**:

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| `node_date` | Ngày thực hiện node. | 2024-01-26, 2024-09-14, 2025-01-12 |
| `campaign_id` | Mã định danh chiến dịch. | tSmnAjrVlypk8MlAA4id, 5dMQAErZhSnal6DrJU05, VXxeVen5nNV5UCCcFyiI |
| `campaign_name` | Tên chiến dịch do BU tự đặt. | 241204_GMC_Newuser_Retention_Low_Frequency_Redeem_v2, 241210_JN_W2B_NFC_DEVICE_SUPPORT_1862, 241220_NEWTON_RETARGET_PAYMENT_CLICK_TIEP_TUC_CART_1372 |
| `is_test` | Chiến dịch dùng để test hay chạy thực. True là chạy test, False là chạy thật. | true, false |
| `account_id` | Mã định danh của Business Unit. | UTI - Data, FS - CreditTech – Device Financing, Account Test, Product Owner, FS - FI collection & disbursement, DLS - SME offline merchant, GMC - New User, Gamification, GMC - CRM, Finance Budget Demo, NFC - Ads, DLS - Marketplace, MDS- MoMo OA, GMC Cross-sell, Platform, MDS - Rewards, Notification Operator, DLS - OTA, Big Campaign MKT, CIO, Risk, null, GMC Retention - Notifications, MDS - Promotion Hub, FS - CreditTech, FS - InsurTech, TFBV, MDS - Student Pass, DLS - Food Delivery & Logistic, GMC Monetization - Notifications, Social Payment, FS - InvestTech, DLS - SME online, DLS - Cinema, CIO - Customer Intelligence Analyst, DLS - Ads Inventory, FS - InvestTech - Wealth management, FS - Bank Partnership, Online Payment, DLS - Ads payment, DLS - Offline, retail & FnB, FS - InvestTech - Brokerage, DLS - Game, Application Store & Entertainment, UTI - Billpay, UTI - Public services, MDS - Thổ Địa MoMo, UTI - Airtime, GMC - App Comm |
| `goal_type` | Loại mục tiêu BU tự chọn. Vd: CONSIDERATION_CONVERSION. | ENGAGEMENT_CROSS_SELLING, null, ADVOCACY, CONSIDERATION_CONVERSION, ENGAGEMENT_LOYALTY, REACTIVATION, ENGAGEMENT_ONBOARDING, ENGAGEMENT_UPSELLING |
| `node_id` | Mã định danh của từng node trong hành trình, là node action của notification, advertisement, widget,... | 39581710576, 43642153424, 39581510900 |
| `node_type` | Dạng hành động của node. Vd: noti và các dạng khác. | FLOATING_ICON, SOF_WIDGET, BANNER, CUSTOM_ACTION, CAROUSEL_BANNER, NOTIFICATION, WAIT, THIN_BANNER, MASTHEAD_BANNER, HALF_BANNER, AB_TEST |
| `action_type_lv1` | Mức độ chi tiết hơn của loại hành động của node. | CHAT_TEMPLATE, SURVEY, TEST_TYPE, null, SERVICE_COLLECTION, PROMOTION_WIDGET, ADS, ADS_V2 |
| `caption` | Tên tiêu đề của thông báo. | Tốn 5 bước để nạp điện thoại, Ví Trả Sau đang chờ bạn đó 🤗, Đơn trả góp Apple sắp hết hạn!, Quà hoàn 8K đang đợi bạn 🤑, Thanh toán App Store an toàn, ${lastname} ơi! MoMo tặng bạn 200k, 31226450209, Quà đa năng 20K sắp hết hạn, Có thẻ tín dụng mua sắm thả ga, Chụp Căn Cước, rước 1 triệu |
| `body` | Nội dung của thông báo. | Bí kíp ở đây: Mau liên kết ngân hàng để tận hưởng tính năng chuyển tiền nhanh gọn, mượt mà 24/7 bạn ơi!, 😉 Giúp nhận dễ dàng từ mọi Ngân hàng và không lo nhầm thông tin chuyển khoản. Thử QR Nhận tiền ngay!, Nạp tiền điện thoại thành công, bạn nhận được combo 4 thẻ quà siêu xịn |
| `refid` | Mã tham chiếu. | momo_merchant, https://www.momo.vn/tin-tuc/khuyen-mai/sale-3-3-du-lich-xuan-he-vo-tu-dat-ve-giam-den-33-7221?utm_source=in_app&utm_campaign=ota, https://momo.vn/tin-tuc/thong-bao/chup-can-cuoc-cong-dan-san-trieu-ly-nuoc-0d-5668 |
| `image` | Đường dẫn tới hình ảnh. | https://static.momocdn.net/app/img/01GMC/NewRetention/T10-2024/600x338.jpg, https://static.momocdn.net/app/img/XSell/phase4/600x338-2-the-qua_kv3.jpg, https://homepage.momocdn.net/img/momo-upload-api-240531164133-638527704934796571.jpg |
| `preview_0` | Hình ảnh xem trước phiên bản 0. | 573, 251606_AAT_DATA_TEST_2579_HYPO_5, 250527_WIDGET_TTS_BIND_2681 |
| `preview_1` | Hình ảnh xem trước phiên bản 1. | CVS_Survey_Learning_Stock_Education_5_2025, 20240929_QuyNhom_Complete_1, FLOATING_ICON |
| `preview_2` | Hình ảnh xem trước phiên bản 2. | 08-04-2025 17:46:24 - 01-07-2025 00:00:00, 09-06-2025 10:27:21 - 01-07-2025 00:00:00, 17-06-2025 19:02:05 - 01-07-2025 00:00:00 |
| `preview_3` | Hình ảnh xem trước phiên bản 3. | 1 impression/user/day & 30 impressions/user/all time, 15 impression/user/day & 200 impression/user/all time, https://static.momocdn.net/app/img/0.Student/StudentPassBP.jpg |
| `pre_condition_inf` | Thông tin điều kiện trước khi thực hiện. | AND_User vào màn hình Đăng ký thông tin Ví trả sau_30_MINUTE_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_User vào màn hình đăng ký KYC, luồng đăng ký Ví trả sau_30_MINUTE_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_&AND_User vào màn hình đăng ký KYC, luồng đăng ký Ví trả sau_1_DAY_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_true_&AND_User vào màn hình Đăng ký thông tin Ví trả sau_1_DAY_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_true_&AND_User vào màn hình đăng ký KYC, luồng đăng ký Ví trả sau_1_DAY_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_true_User vào màn hình Đăng ký thông tin Ví trả sau_1_DAY_ACTION_FREQUENCY_OPERATOR_GREATER_THAN_OR_EQUAL_1_true_, AND_AND_User thanh toán 1 hoặc nhiều dịch vụ (theo service_id)_60_MINUTE_, AND_AND_User thanh toán online, token, offline (ví dụ Circle K, 711,...)_3_DAY_ |
| `non_organic_goal_user` | Số lượng người dùng đạt mục tiêu nhờ vào Journey, sau khi được yêu cầu hành động. | 3, 528, 3997 |
| `action_request_cnt` | Số lượng yêu cầu hành động từ Journey tới các đối tác như noti, adv,... | 158, 226, 2148 |
| `noti_request_cnt` | Số lượng yêu cầu gửi thông báo. | 10210, 346, 667 |
| `noti_sent_cnt` | BU không sử dụng cột này. | 12700, 158, 226 |
| `noti_sent_outapp_cnt` | BU không sử dụng cột này. | 1, 45, 890 |
| `noti_sent_mqtt_cnt` | Số lượng thông báo được gửi qua MQTT. | 4164, 158, 226 |
| `noti_delivery_outapp_cnt` | Số lần thông báo được gửi ra ngoài ứng dụng. | 3, 3964, 3624 |
| `noti_impression_inapp_cnt` | Số lần thông báo được hiển thị trong ứng dụng. | 3, 1748, 386 |
| `noti_click_read_inapp_cnt` | Số lần thông báo được nhấp chuột trong ứng dụng. | 3, 2461, 528 |
| `noti_click_read_outapp_cnt` | Số lần thông báo được nhấp chuột ngoài ứng dụng. | 158, 150, 568 |
| `noti_click_read_cnt` | Số lần thông báo được nhấp. | 82, 1, 172 |
| `ad_impresion_cnt` | Số lần quảng cáo được hiển thị. | 18127, 6672, 3 |
| `ad_click_cnt` | Số lần quảng cáo được nhấp chuột. | 1, 45, 175 |
| `Click` | Tổng số lần nhấp chuột từ thông báo và quảng cáo. | 3, 393, 1870 |
| `Traffic` | Tổng số lượng thông báo gửi ngoài ứng dụng + số lần hiển thị trong ứng dụng của thông báo và quảng cáo. | 1, 45, 1018 |
| `goal_classification` | Phân loại mục tiêu gồm 3 loại: trans, non trans, mix. | mix, unknown, trans, non_trans |

---

## Table information:

**Table Name**: `momovn-prod.MBI_DA.journey_track_camp_agg_v2`

**Table Description**: Bảng tổng hợp thông tin chiến dịch trong hành trình người dùng của dự án MBI DA for MoMo.

**Thông tin từ bảng này có thể được sử dụng để**:
- Xác định các chiến dịch đang chạy và thời gian bắt đầu/kết thúc của chúng.
- Đánh giá hiệu quả của từng chiến dịch bằng cách xem số lượng người dùng tham gia và hoàn thành mục tiêu.
- Phân loại mục tiêu chiến dịch để tối ưu hóa chiến lược tiếp thị.

**Column Descriptions**:

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| `node_date` | Ngày của node chạy. | 2025-07-30, 2025-01-28, 2025-01-07 |
| `campaign_id` | ID định danh tên chiến dịch. | pZFAa6Y3KPbroRDQYDwL, GB3OJ4qTtENoq4nlyx2f, K55OLKTqnvHnrBj9IvWo |
| `campaign_name` | Tên do BU tự đặt cho chiến dịch. | 2501_CIO_FeedbackLoop_3_w2bdrop, 250101_JN_VTS_NEW_REG_JOURNEY_1314, 2502_GMC_TTT_CASHIN100K_SOFTTT_HIGHTRUST_2064 |
| `description` | Mô tả của campaign. | Retarget user để bật tính năng AR qua TTT, Remind [Chưa mua-LAL Merchant] vào redeem voucher Flashsale và mua Sounbox từ 1/6-10/5, Tổng hợp 2 nhánh Goal: Convert A60 thường có thanh toán billpay, airtime qua app MoMo thành Ax (mời bạn mới thành công) Trigger: - User thanh toán billpay/airtime bất kỳ CÓ sử dụng voucher - User thanh toán billpay/airtime trên 100K; KHÔNG sử dụng voucher |
| `created_by` | Người tạo chiến dịch. | |
| `camp_startdate` | Ngày chiến dịch được BU chọn bắt đầu chạy. | 2025-01-07, 2025-07-30, 2024-10-17 |
| `camp_enddate` | Ngày chiến dịch được BU chọn dừng chạy. | 2025-06-21, 2025-01-28, 2026-05-31 |
| `segment_type` | Loại phân khúc của chiến dịch. | EVERY_DAY, CUSTOM_CRON, EVERY_MONTH, NOW, EVERY_WEEK |
| `is_test` | Là chiến dịch chạy thử hay không? true: là thử, false: là thật. | true, false |
| `account_id` | Mã định danh từng BU. | Social Payment, UTI - Public services, Account Test, DLS - SME offline merchant, GMC - New User, DLS - Food Delivery & Logistic, Online Payment, DLS - Game, Application Store & Entertainment, FS - InsurTech, FS - InvestTech, Product Owner, FS - CreditTech – Device Financing, CIO - Customer Intelligence Analyst, MDS- MoMo OA, FS - InvestTech - Wealth management, Finance Budget Demo, FS - Bank Partnership, MDS - Thổ Địa MoMo, MDS - Promotion Hub, GMC Monetization - Notifications, DLS - Offline, retail & FnB, DLS - Ads Inventory, MDS - Student Pass, GMC - App Comm, DLS - Ads payment, UTI - Billpay, null, DLS - OTA, FS - InvestTech - Brokerage, DLS - SME online, TFBV, NFC - Ads, Platform, MDS - Rewards, Risk, GMC Retention - Notifications, FS - CreditTech, DLS - Cinema, Notification Operator, UTI - Airtime, CIO, FS - FI collection & disbursement, DLS - Marketplace, GMC Cross-sell, UTI - Data, Gamification, Big Campaign MKT, GMC - CRM |
| `goal_type` | Mục đích từng loại goal do BU tự config trong hành trình, ví dụ: CONSIDERATION_CONVERSION. | ENGAGEMENT_UPSELLING, CONSIDERATION_CONVERSION, ADVOCACY, null, ENGAGEMENT_CROSS_SELLING, ENGAGEMENT_LOYALTY, REACTIVATION, ENGAGEMENT_ONBOARDING |
| `link_flow` | Luồng liên kết của chiến dịch. | https://docs.google.com/spreadsheets/d/1S7HWxmseNOBnWqS3gIllYN, https://docs.google.com/spreadsheets/d/1O9icKr3A8rLPeVr6FULwYPnDg0TytQvsLK6P0YVdpHY/edit, https://docs.google.com/spreadsheets/d/1J3bI8hvxAvZ1ptmHl1p8SnDAL00bkhhzDwAd61P9gv8/edit |
| `target_cvr` | Tỉ lệ chuyển đổi mục tiêu của chiến dịch. | null |
| `baseline_cvr` | Tỷ lệ chuyển đổi cơ bản trước khi chiến dịch bắt đầu. | null |
| `goal_desc` | Mô tả của mục tiêu. | AND_AND_Hiển thị toast mở khóa SC25 thành công_, AND_AND_[Fund_home] Tạo quỹ mới thông thường_, AND_AND_Vay Nhanh - User thực hiện nhập OTP khi đi vay _ New_ |
| `time_enter_user` | Thời gian người dùng tham gia trong chiến dịch. | 3241, 623, 2339 |
| `enter_user_by_camp` | Số lượng user tham gia theo từng hành trình chiến dịch. | 11755, 38508, 172146 |
| `enter_user_by_datecamp` | Số lần user tham gia hành trình theo ngày trong chiến dịch. | 9, 5968, 19900 |
| `goal_user` | Số lượng user đạt mục tiêu, gồm nhờ vào hành trình và không nhờ vào hành trình. | 588, 37268, 155 |
| `non_organic_goal_user` | Số lượng user đạt mục tiêu nhờ vào hành trình; là goal sau khi được request gửi một action. | 3, 185, 100 |
| `exit_user` | Số lần user thoát khỏi hành trình. | 1946, 509, 459 |
| `goal_classification` | Phân loại goal, gồm trans, nontrans, mix (là trans hoặc nontrans). | mix, non_trans, unknown, trans |

## Knowledgebase

[]

## Memory

[]