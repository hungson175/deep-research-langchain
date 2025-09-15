# Business Page

## Dataset Information

**Dataset ID**: 3220e3ea-a817-4cad-a795-6221771b5956

**Dataset Name**: Business Page

**Description**: The dataset records all information about features in BP, including: (1) information about BP (2) Merchant engagement (3) User engagement

**Instructions**:

**Error Code**: 200

## Schema Information

### Table 1: OA_MASTER_INFO

**Table Name**: project-5400504384186300846.MBI_DA.OA_MASTER_INFO

**Description**: Bảng tổng hợp tất cả các thông tin của OA

| Column Name | Description | Data Type | Mode |
|-------------|-------------|-----------|------|
| CREATE_DATE | **Desc**: Ngày tạo của OA_ID trong bảng `project-5400504384186300846.OFFICIAL_ACCOUNT.OFFICIAL_ACCOUNT_20*`<br><br>**Sample value**: ['2022-04-27'] | DATE |  |
| CREATE_DATETIME | **Desc**: Thời gian chi tiết tạo OA_ID<br><br>**Sample value**: ['2022-04-27 13:32:34', '2022-04-27 13:33:59', '2022-04-27 13:35:37'] | DATETIME |  |
| MODIFIED_DATE | **Desc**: Ngày cập nhật thông tin OA<br><br>**Sample value**: ['2022-04-27', '2023-12-14', '2024-11-29', '2024-12-02'] | DATE |  |
| MODIFIED_DATETIME | **Desc**: Ngày giờ cập nhật thông tin OA<br><br>**Sample value**: ['2022-04-27 15:51:12', '2022-04-27 15:52:00', '2022-04-27 15:52:47'] | DATETIME |  |
| OA_ID | **Desc**: ID của Official Account (OA).<br><br>**Sample value**: ['1061276', '1061277', '1061278'] | STRING |  |
| OA_MERCHANT_STORE_ID | **Desc**: Thông tin về ID của bảng `project-5400504384186300846.OFFICIAL_ACCOUNT.OA_MERCHANT_STORE_*`<br>**Sample value**: ['46237.0', '46253.0', '47507.0'] | FLOAT |  |
| MERCHANT_ID | **Desc**: Thông tin về Merchant ID (không phải Partnercode / Merchant Code)<br><br>**Sample value**: ['1019744.0', '1019803.0', '1019804.0'] | FLOAT |  |
| ORI_STORE_ID | **Desc**: Thông tin về Store_id được ghi nhận trong bảng `project-5400504384186300846.OFFICIAL_ACCOUNT.OFFICIAL_ACCOUNT_20*`<br><br>**Sample value**: ['1022000.0', '1022001.0', '1022002.0'] | FLOAT |  |
| STORE_ID_RECODE | **Desc**: Thông tin về Store_id được recode với thông tin của M4B_STORE<br>**Sample value**: ['1022006.0', '1022010.0', '1022011.0'] | FLOAT |  |
| ORI_PARTNER_CODE | **Desc**: Thông tin về Partner code được ghi nhận trong bảng `project-5400504384186300846.OFFICIAL_ACCOUNT.OFFICIAL_ACCOUNT_20*`<br><br>**Sample value**: ['MOMOABFY20220427', 'MOMOCF3V20220427', 'MOMODKKO20190327'] | STRING |  |
| ORI_STORE_CODE | **Desc**: Thông tin về Store code được ghi nhận trong bảng `project-5400504384186300846.OFFICIAL_ACCOUNT.OFFICIAL_ACCOUNT_20*`<br><br>**Sample value**: ['00168', '00170', '00184'] | STRING |  |
| STORE_CODE_RECODE | **Desc**: Mã cửa hàng sau khi mã hóa lại.<br><br>**Sample value**: ['00168', '00170', '00184'] | STRING |  |
| TYPE_RECODE | **Desc**: Thông tin về các store_id được recode<br>**Sample value**: ['Keep', 'Recode'] | STRING |  |
| OA_STORE_NAME | Tên cửa hàng OA | STRING |  |
| OA_STORE_ADDRESS | Địa chỉ cửa hàng OA | STRING |  |
| LATITUDE | Vĩ độ địa lý | FLOAT |  |
| LONGITUDE | Kinh độ địa lý | FLOAT |  |
| HOTLINE_AID | Số hotline theo định dạng agent_id | STRING |  |
| IS_ENABLE_FNB | Trạng thái kích hoạt F&B | FLOAT |  |
| OWNERSHIP_STATUS | Trạng thái sở hữu | FLOAT |  |
| IS_OA_CLAIM | Trạng thái claim OA | INT |  |
| IS_OA_ACTIVE | Trạng thái active của OA | BOOLEAN |  |
| IS_OA_DELETED | Trạng thái xóa của OA | BOOLEAN |  |
| M4B_CAT | Danh mục M4B | STRING |  |
| PAYLATER_CONFIG_TYPE | Loại cấu hình Paylater | STRING |  |
| IMG_MENU | Số lượng hình ảnh menu | INT |  |
| IMG_ITEM | Số lượng hình ảnh sản phẩm | INT |  |
| IMG_BANNER | Số lượng hình ảnh banner | INT |  |
| IMG_LOGO | Số lượng hình ảnh logo | INT |  |
| IMG_SPACE | Số lượng hình ảnh không gian | INT |  |
| MIN_RATING | Điểm đánh giá thấp nhất | FLOAT |  |
| AVG_RATING | Điểm đánh giá trung bình | FLOAT |  |
| MEDIAN_RATING | Điểm đánh giá trung vị | FLOAT |  |
| CNT_REVIEW | Số lượng đánh giá | INT |  |
| CNT_REVIEWER | Số lượng người đánh giá | INT |  |
| CNT_DATE_REVIEW | Số ngày có đánh giá | INT |  |
| LAST_UPDATE | Ngày cập nhật cuối cùng | DATE |  |
| UU_LAST_90_DAYS | Unique users trong 90 ngày qua | INT |  |
| TOTAL_TRANS_LAST_90_DAYS | Tổng giao dịch trong 90 ngày qua | INT |  |
| UU_LAST_30_DAYS | Unique users trong 30 ngày qua | INT |  |
| TOTAL_TRANS_LAST_30_DAYS | Tổng giao dịch trong 30 ngày qua | INT |  |
| UU_LAST_7_DAYS | Unique users trong 7 ngày qua | INT |  |
| TOTAL_TRANS_LAST_7_DAYS | Tổng giao dịch trong 7 ngày qua | INT |  |
| AVG_AOV_LAST_7_DAYS | Giá trị đơn hàng trung bình 7 ngày qua | FLOAT |  |
| AVG_AOV_LAST_30_DAYS | Giá trị đơn hàng trung bình 30 ngày qua | FLOAT |  |
| AVG_AOV_LAST_90_DAYS | Giá trị đơn hàng trung bình 90 ngày qua | FLOAT |  |
| START_TIME | Thời gian bắt đầu hoạt động | STRING |  |
| END_TIME | Thời gian kết thúc hoạt động | STRING |  |
| IPOS_STORE | ID cửa hàng IPOS | FLOAT |  |
| CNT_SKU | Số lượng SKU | INT |  |
| OA_QUALITY | Chất lượng OA | STRING |  |
| OPERATING_STATUS_DEFINE | Định nghĩa trạng thái hoạt động | STRING |  |
| IS_STATUS_SOCIAL_PACKAGE | Trạng thái đăng kí gói Social của OA | STRING |  |
| WARD_NAME | Tên phường/xã | STRING |  |
| DISTRICT_NAME | Tên quận/huyện | STRING |  |
| CITY_NAME | Tên thành phố | STRING |  |
| TYPE_LOCATION | Loại vị trí | STRING |  |
| HOUSE_NUMBER | Số nhà | STRING |  |
| OA_DESCRIPTION | Mô tả OA | STRING |  |
| AVG_PRICE | **Desc**: Giá trung bình.<br><br>**Sample value**: ['100000.0', '200000.0', '50000.0', 'nan'] | FLOAT |  |
| UTILITY_NAME | **Desc**: Tên tiện ích.<br><br>**Sample value**: ['None', 'Phù hợp nhóm bạn \| Bán tại chỗ \| Có wifi \| Giao hàng \| Trả thẻ \| Gửi xe miễn phí \| Bán mang đi'] | STRING |  |
| OA_SOURCE | **Desc**: Nguồn OA.<br><br>**Sample value**: ['M4B', 'OPERATION'] | STRING |  |
| GOOGLE_SOURCE | **Desc**: Nguồn Google.<br><br>**Sample value**: ['N'] | STRING |  |
| AMBIENCE | **Desc**: Không gian.<br><br>**Sample value**: ['cổ điển', 'đậm chất riêng,ấm áp', 'ấm áp'] | STRING |  |
| CNT_UTILITY | **Desc**: Số lượng tiện ích.<br><br>**Sample value**: ['7', '<NA>'] | INT |  |
| CNT_AMBIENCE | **Desc**: Số lượng không gian.<br><br>**Sample value**: ['1', '2'] | INT |  |
| TYPE_PILOT | **Desc**: Loại thử nghiệm.<br><br>**Sample value**: ['MVP', 'Other'] | STRING |  |
| TDMM_DISPLAY | **Desc**: Hiển thị TDMM.<br><br>**Sample value**: ['Hiển thị', 'Không hiển thị'] | STRING |  |
| OA_CATEGORY_NAME | **Desc**: Tên danh mục OA.<br><br>**Sample value**: ['Cơm chiên (cơm rang) \| Nhà hàng - Quán - Dịch vụ Ăn uống', 'Cơm gà \| Cơm văn phòng \| Gà chiên \| Gà rán \| Khoai tây chiên \| Kiểu chiên \| Nhà hàng - Quán - Dịch vụ Ăn uống', 'Cơm gà \| Nhà hàng - Quán - Dịch vụ Ăn uống'] | STRING |  |
| CNT_CATE | **Desc**: Số lượng danh mục.<br><br>**Sample value**: ['2', '7'] | INT |  |
| STREET_NAME | **Desc**: Tên đường.<br><br>**Sample value**: ['Hoàng Văn Thái', 'Lê Hồng Phong', 'None', 'Quán Trung'] | STRING |  |
| TOTAL_RATING | **Desc**: Tổng số điểm đánh giá.<br><br>**Sample value**: ['0.0', '1.0'] | FLOAT |  |
| IS_DELIVERABLE | **Desc**: Trạng thái có thể giao hàng.<br><br>**Sample value**: ['nan'] | FLOAT |  |
| CHECK_LOCATION_ALLEY | **Desc**: Kiểm tra vị trí hẻm.<br><br>**Sample value**: ['Other'] | STRING |  |
| STREET_ID | **Desc**: ID của đường.<br><br>**Sample value**: ['106912.0', '111152.0', '124487.0', 'nan'] | FLOAT |  |
| TYPE_OA | **Desc**: Loại OA.<br><br>**Sample value**: ['OA Store', 'OA Brand'] | STRING |  |
| OA_ID_BRAND | **Desc**: ID của OA Brand/ OA cha<br><br>**Sample value**: ['9892658', 'None'] | STRING |  |
| OA_PARENT_STATUS_DEFINE | **Desc**: Trạng thái của OA cha<br><br>**Sample value**: ['CURRENT LINK', 'REJECT', 'WAITING FOR APPROVE'] | STRING |  |
| OA_PARENT_IS_DELETED | **Desc**: Trạng thái xóa của OA cha.<br><br>**Sample value**: ['0.0', 'nan'] | FLOAT |  |
| PUBLISH | **Desc**: Trạng thái hiển thị của OA trên momo<br><br>**Sample value**: ['0.0', '1.0'] | FLOAT |  |
| DISPUTE_STATUS_DEFINE | **Desc**: Dispute status liên quan đến status Ops check KYB<br><br>**Sample value**: Dispute status có các giá trị: NONE_OR_RESOLVED(1), WAITING_FOR_VERIFICATION(2), WAITING_FOR_RECLAIM_VERIFICATION(3); | STRING |  |
| CLAIM_TS | **Desc**: Thời gian yêu cầu claim<br><br>**Sample value**: ['NaT'] | DATETIME |  |
| OA_CLAIM_STATUS | **Desc**: Trạng thái claim request của OA.<br><br>**Sample value**: WAIT_FOR_APPROVAL, REJECTED, APPROVED | STRING |  |
| FINAL_OA_STATUS | Status cuối cùng của OA<br>UNKNOWN<br>DRAFT_INIT<br>DRAFT_PENDING<br>DELETED<br>CLAIMED<br>DRAFT_CANCELED<br>UNCLAIMED<br>WAITING_FOR_VERIFICATION<br>DRAFT_REJECTED | STRING |  |
| FNB_LEVEL | Thông tin về merchant badge gamification của các store FnB | FLOAT |  |
| CONTACT_NUMBER_AID | SĐT contact của cửa hàng theo định dạng agent_id | STRING |  |

### Table 2: F_OA_USER_ACTION

**Table Name**: project-5400504384186300846.MBI_DA.F_OA_USER_ACTION

**Description**: Bảng tổng hợp các action của user có tương tác engage với BP

| Column Name | Description | Data Type | Mode |
|-------------|-------------|-----------|------|
| DATETIME | Ngày giờ engage | DATETIME |  |
| DATE | Ngày engage | DATE |  |
| AGENT_ID | AGENT_ID của user engage | STRING |  |
| OA_ID | ID của OA được engage | STRING |  |
| ACTION_TYPE_DETAIL | Chi tiết các action của user (VD: click button nào) | STRING |  |
| EVENT_ID | ID của event user engage | STRING |  |
| ACTION_TYPE | Các action của user, bao gồm chat_engage<br>click_any_button<br>save_collection<br>review_rating<br>follow_oa<br>post_engage<br>screen_OA_detail | STRING |  |
| INTERNAL_OR_EXTERNAL | OA đó là OA internal hay external | STRING |  |
| M4B_CAT | M4B category của OA | STRING |  |

### Table 3: F_OA_MERCHANT_ACTION_TRACKING

**Table Name**: project-5400504384186300846.MBI_DA.F_OA_MERCHANT_ACTION_TRACKING

**Description**: Bảng record tất cả action engage của Merchant

| Column Name | Description | Data Type | Mode |
|-------------|-------------|-----------|------|
| DATETIME | Ngày giờ engage | DATETIME |  |
| DATE | Ngày engage | DATE |  |
| OA_ID | ID của OA engage | STRING |  |
| ACTION_TYPE | Tên action engage của MC, bao gồm:<br>post_create<br>content_update<br>story_create<br>campaign_join<br>banner_update<br>image_upload<br>broadcast_create | STRING |  |
| SUB_ACTION | Tên của các action phụ mà MC engage | STRING |  |
| SOURCE | Source engage của MC | STRING |  |
| CREATE_SOURCE | Source OA được tạo | STRING |  |
| PARTNER_CODE | Code định danh merchant | STRING |  |
| STORE_CODE | Code định danh store | STRING |  |
| OA_STORE_NAME | Tên của OA | STRING |  |
| OA_CATEGORY | Category của OA | STRING |  |
| TYPE_OA | Phân loại OA: OA Store/ OA Brand | STRING |  |
| IS_OA_ACTIVE | OA có active và tìm kiếm được trên momo không | BOOLEAN |  |
| OA_QUALITY | Level quality của OA | STRING |  |
| IS_STATUS_SOCIAL_PACKAGE | Trạng thái đăng kí gói Social của OA | STRING |  |
| OA_ID_CHILD | ID của OA con | STRING |  |
| INTERNAL_OR_EXTERNAL | OA đó là internal hay external | STRING |  |
| M4B_CAT | M4B_CATEGORY của OA | STRING |  |

### Table 4: OA_TDMM_EVENT_v2_converted

**Table Name**: project-5400504384186300846.MBI_DA.OA_TDMM_EVENT_v2_converted

**Description**: Bảng chứa tất cả các event của BP và TĐMM

| Column Name | Description | Data Type | Mode |
|-------------|-------------|-----------|------|
| DATE_PARTITION | **Desc**: Thời gian phân vùng dữ liệu.<br><br>**Sample value**: ['2024-11-21 00:20:44.123000+00:00', '2024-11-21 02:59:15.035000+00:00', '2024-11-21 03:57:25.043000+00:00'] | TIMESTAMP |  |
| DATE | **Desc**: Ngày diễn ra sự kiện.<br><br>**Sample value**: ['2024-11-21'] | DATE |  |
| DATETIME | **Desc**: Thời gian cụ thể diễn ra sự kiện.<br><br>**Sample value**: ['2024-11-21 07:20:44.123', '2024-11-21 09:59:15.035', '2024-11-21 10:57:25.043'] | DATETIME |  |
| USER_ID | **Desc**: ID của người dùng thực hiện sự kiện.<br><br>**Sample value**: ['32377539', '34061292', '44141058'] | STRING |  |
| EVENT_NAME | **Desc**: Tên của sự kiện diễn ra.<br><br>**Sample value**: ['service_block_clicked'] | STRING |  |
| SCREEN_NAME | **Desc**: Tên màn hình nơi sự kiện diễn ra.<br><br>**Sample value**: ['destination_pages', 'home', 'voucher_detail'] | STRING |  |
| TAB_NAME | **Desc**: Tên tab nơi sự kiện diễn ra.<br><br>**Sample value**: [''] | STRING |  |
| BUTTON_NAME | **Desc**: Tên nút bấm được người dùng tương tác.<br><br>**Sample value**: [''] | STRING |  |
| COMPONENT_NAME | **Desc**: Tên thành phần của ứng dụng liên quan đến sự kiện.<br><br>**Sample value**: ['', 'list_medium', 'single_card'] | STRING |  |
| OA_ID | **Desc**: ID của Official Account liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| STORE_CODE | Mã cửa hàng | STRING |  |
| PARTNER_CODE | Mã đối tác | STRING |  |
| OA_STORE_NAME | Tên cửa hàng OA | STRING |  |
| SERVICE_NAME | Tên dịch vụ | STRING |  |
| BLOCK_NAME | Tên khối | STRING |  |
| ICON_NAME | Tên biểu tượng | STRING |  |
| FIELD_NAME | Tên trường | STRING |  |
| TRAIL_ID | ID theo dõi | STRING |  |
| OA_CATEGORY | Danh mục OA | STRING |  |
| MOMO_SESSION_ID_V2 | ID phiên MoMo v2 | STRING |  |
| EVENT_ID | ID sự kiện | STRING |  |
| GIFT_TYPE | Loại quà tặng | STRING |  |
| CAMPAIGN_ID | ID chiến dịch | STRING |  |
| UTM_MEDIUM | UTM medium | STRING |  |
| STATUS | Trạng thái | STRING |  |
| FIREBASE_ERROR | Lỗi Firebase | STRING |  |
| GLOBAL_TRIGGER_ID | ID trigger toàn cục | STRING |  |
| SEARCH | Tìm kiếm | STRING |  |
| ERROR_VALUE | Giá trị lỗi | STRING |  |
| SOURCEFROMFORTRACKING | Nguồn theo dõi | STRING |  |
| SERVICENAME | Tên dịch vụ | STRING |  |
| ACTION | Hành động | STRING |  |
| GIFT_ID | ID quà tặng | STRING |  |
| MINIAPP_VERSION | Phiên bản miniapp | STRING |  |
| STAGE | Giai đoạn | STRING |  |
| COMPONENT_TYE | Loại thành phần | STRING |  |
| FIREBASE_SCREEN_CLASS | Class màn hình Firebase | STRING |  |
| SLOT | Vị trí | STRING |  |
| TIMESTAMP__ | Dấu thời gian | STRING |  |
| UTM_CAMPAIGN | UTM campaign | STRING |  |
| PRODUCT_LIST | Danh sách sản phẩm | STRING |  |
| REDIRECTTO | Chuyển hướng tới | STRING |  |
| FIREBASE_EVENT_ORIGIN | Nguồn sự kiện Firebase | STRING |  |
| BUILD_NUMBER | Số build | STRING |  |
| USER_PSEUDO_ID | ID giả của user | STRING |  |
| OA_ID_PARAM | Tham số OA ID | STRING |  |
| DEEPLINK_ID | ID deeplink | STRING |  |
| UTM_SOURCE | UTM source | STRING |  |
| LABEL_NAME | Tên nhãn | STRING |  |
| STOREID | ID cửa hàng | STRING |  |
| ATTRIBUTION_ID | ID gán thuộc | STRING |  |
| ZERO_BANNER | Banner zero | STRING |  |
| SOURCE | Nguồn | STRING |  |
| EVENT_COUNT | Số lượng sự kiện | STRING |  |
| BUTTON | Nút bấm | STRING |  |
| PRODUCT_NAME | Tên sản phẩm | STRING |  |
| PRODUCT_ID | ID sản phẩm | STRING |  |
| IMAGE_NAME | Tên hình ảnh | STRING |  |
| NETWORK_TYPE | Loại mạng | STRING |  |
| TRAN_ID | ID giao dịch | STRING |  |
| COMPONENT_TYPE | Loại thành phần | STRING |  |
| ENGAGED_SESSION_EVENT | Sự kiện phiên tương tác | STRING |  |
| TRIGGER_ID | ID trigger | STRING |  |
| STORE_ID | ID cửa hàng | STRING |  |
| PROVIDER | Nhà cung cấp | STRING |  |
| MERCHANT_ID | ID merchant | STRING |  |
| PRODUCT | Sản phẩm | STRING |  |
| USERSESSIONTOKEN | Token phiên user | STRING |  |
| PRODUCT_IDS | **Desc**: Danh sách ID sản phẩm liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| TIME_LOAD | **Desc**: Thời gian tải liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| TIMESTAMP | **Desc**: Dấu thời gian của sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| ORDER_NUMBER | **Desc**: Số đơn hàng liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| MINIAPPID | **Desc**: ID của miniapp liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| KEYWORD | **Desc**: Từ khóa liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| CAMPAIGN_NAME | **Desc**: Tên chiến dịch liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| TIME_SLOT | **Desc**: Khoảng thời gian của sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |
| BLOCK | **Desc**: Block liên quan đến sự kiện.<br><br>**Sample value**: ['None'] | STRING |  |

## Memory Information

The dataset includes memory entries containing business rules and context:

1. **Internal OA Classifications**: Various OAs classified as internal including Hệ thống Chứng khoán CV, Quỹ Toàn Năng, Mini App, Vũ Trụ Game, MoMo Building, and others.

2. **Data Processing Rules**:
   - Use OA_QUALITY = 'Level_1' for level 1 OA account issues
   - Round averages to 2 decimal places in output

3. **Business Context**: Contains information about specific OAs and their internal/external classification status.

## Data Quality Notes

- **Table 1 (OA_MASTER_INFO)**: Contains comprehensive OA information with 74 columns covering all aspects of Official Account metadata, transactions, ratings, and business details.
- **Table 2 (F_OA_USER_ACTION)**: Tracks user engagement actions with 9 core columns for behavioral analysis.
- **Table 3 (F_OA_MERCHANT_ACTION_TRACKING)**: Records merchant engagement activities with 18 columns for business activity monitoring.
- **Table 4 (OA_TDMM_EVENT_v2_converted)**: Extensive event tracking with 69 columns capturing detailed user interactions and system events.

This dataset provides comprehensive insights into Business Page features, merchant engagement patterns, and user interaction behaviors within the MoMo ecosystem.