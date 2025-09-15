# Thổ Địa MoMo Dataset

## Error Code

200

## Data

### ID
c123d8bc-9569-4dfd-955f-69d587062069

### Name
Thổ Địa MoMo

### Description
The dataset records information about 4 core features of TĐMM, including (1) login (2) engage (3) review (4) delivery

### Instructions
(empty)

## Schema DDL

### Dataset name: Thổ Địa MoMo

---

## Table 1: project-5400504384186300846.MBI_DA.DM_MART_PROFILE_USER_LOGIN

**Description:** Bảng chứa thông tin về tất cả user có login TĐMM, detail về demographic của user như giới tính, location

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| DATE | DATE | Ngày login | 2024-05-21 |
| DATETIME | DATETIME | Ngày giờ login | 2024-05-21 02:28:29.375000, 2024-05-21 03:03:39.008034, 2024-05-21 13:04:54.058000 |
| USER_ID | STRING | ID của user | 10118242, 4205365, 82296893 |
| SCREEN_NAME | STRING | Tên màn user đăng nhập vào | Home TDMM, Detail BST, Filter Delivery |
| EVENT_NAME | STRING | Tên của event | service_screen_viewed |
| SOURCE | STRING | Source login của user | shopxu2023, tabbar_home, tabbar_promotion |
| EVENT_ID | STRING | ID của event | 6XuI5UG12hNRhGOMCrLoy, FAmem5nvzdeFKFG_INU85, G7OPfXHyJVr0_N-ky868- |
| MOMO_SESSION_ID_V2 | STRING | Session của action login | 26BE4FA3-79BB-445D-9C64-1B93EEA5A722, 51A24449-4770-4332-AA9B-FCD90DF7CB7D, 5AF2664C-48F4-411E-94C0-127624DFBBB0 |
| CITY | STRING | Thành phố nơi user login | - |
| DISTRICT | STRING | Quận nơi user login | - |
| GENDER | STRING | Giới tính của user login | female, male, unknown |
| AGE_GROUP | STRING | Nhóm tuổi của user login | - |

### Data Example:
```
         DATE                   DATETIME   user_id screen_name             event_name  source               event_id                    momo_session_id_v2        city       district gender         age_group
0  2024-08-05 2024-08-05 03:42:42.270052  76759501   Home TDMM  service_screen_viewed     web  iVT42jT859JkzWJRx2I48  3c270aca-93e0-457a-87e4-6450076f8617      Hà Nội        Hà Đông   male  [4]. 27 - 30 y/o
1  2024-08-05 2024-08-05 14:22:44.486000  57985348   Home TDMM  service_screen_viewed   inapp  DdUjNWugIe0B3mlq43lLf  c3de3a03-9f11-429b-80ad-c372f70e11fb   Đồng Tháp       Tam Nông   male  [5]. 31 - 35 y/o
2  2024-08-05 2024-08-05 15:19:58.815000  57187196   Home TDMM  service_screen_viewed   inapp  xsibyCtAVsb4JQD7g50NO  2e20023d-bc28-41c9-bcd1-52e8239d0175      Hà Nội      Hoàn Kiếm   male  [4]. 27 - 30 y/o
3  2024-08-05 2024-08-05 04:40:40.465057  83904664   Home TDMM  service_screen_viewed   inapp  DUlc1Y8ULc5Gxj2x9xP6I  848d2d7e-02a9-4c38-a1b3-08499c098c47  Bình Thuận  Hàm Thuận Nam   male  [2]. 18 - 22 y/o
4  2024-08-05 2024-08-05 19:50:56.221000  74146005   Home TDMM  service_screen_viewed  school  uHMNAlGnd333gwoPZVZrE  e1671e2a-367d-4fe4-b290-2bd378399b9d     Long An       Cần Đước   male  [2]. 18 - 22 y/o
```

---

## Table 2: project-5400504384186300846.MBI_DA.DM_MDS_TDMM_USER_ENGAGE

**Description:** Bảng record các event engage của user trên TĐMM

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| USER_ID | STRING | ID của user | 117238, 118587, 189237 |
| DATE | DATE | Ngày user engage | 2024-06-03 |
| DATETIME | DATETIME | Ngày giờ user engage | 2024-06-03 01:26:46.566057, 2024-06-03 01:56:22.043060, 2024-06-03 08:21:43.987000 |
| EVENT_NAME | STRING | Tên event | service_button_clicked |
| MOMO_SESSION_ID_V2 | STRING | Session engage của user | 64C1FB10-7397-4DE4-8FBD-ADF8672BCE26, 75DF7E16-A0EE-4844-A13C-57655131A83D, 7a6c5af3-52be-46a6-833f-0f54bd7cbddf |
| EVENT_ID | STRING | ID của event | 1_4y-tUOqtHlL0jgPqya6, 3Z_QaupaDhND9RoFQ_CSi, 4-0FOOkSBIfAWZAzFb_tU |
| IMPRESSION_OR_CLICK | STRING | Loại hành động của người dùng: 'impression' hoặc 'click' | click, view |
| TOUCH_POINT | STRING | Các block/ component mà user engage | engage_BP_detail |
| STATUS | STRING | Trạng thái của event engage | hide, failed, success |
| SERVICE_NAME | STRING | Tên service mà user engage | local_discovery, oa_miniapp |
| SCREEN_NAME | STRING | Tên màn hình user engage | tdmm_collection_home, oa, home, group_sku |
| BLOCK_NAME | STRING | Tên block mà user engage | search, user_location, page_info |
| ICON_NAME | STRING | Tên icon mà user engage | change_address, view_all_sku, save, back |
| COMPONENT_NAME | STRING | Tên component mà user engage | oa_familiar, trigger_review |
| BUTTON_NAME | STRING | Tên button mà user engage | category, save, Bánh Mì - Xôi |
| COMPONENT_TYPE | STRING | Loại component mà user engage | promotion_card, QUICK_CARD, filter_bar |
| LABEL_NAME | STRING | Tên label mà user engage | EARLYMORNING, CHILL_CHILL_CUOI_NGAY, BLOCK_QUAN_NGON_QUANH_BAN |
| TIME_SLOT | STRING | Timeslot mà user engage với các block | AFTERNOON, NOON, MORNING, EARLYMORNING, EVENING |
| OA_ID | STRING | ID của OA được user engage | 123456 |

### Data Example:
```
Empty DataFrame
Columns: [user_id, date, datetime, event_name, momo_session_id_v2, event_id, impression_or_click, touch_point, status, service_name, screen_name, block_name, icon_name, component_name, button_name, component_type, label_name, time_slot, OA_ID]
Index: []
```

---

## Table 3: project-5400504384186300846.MBI_DA.DM_MDS_TDMM_DELIVERY_ORDER_last_update

**Description:** Bảng record thông tin về các đơn hàng delivery trên TĐMM

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| ID | FLOAT | ID của hành động đặt hàng | 1862410.0, 1862419.0 |
| USER_ID | STRING | Mã định danh của người dùng thực hiện đơn hàng | 49279214 |
| DATE | DATE | Ngày tạo đơn hàng | 2024-09-10 |
| LAST_MODIFIED | INT | Timestamp chỉnh sửa cuối cùng của đơn hàng | 1725938306000, 1725938466000 |
| OA_ID | STRING | Mã định danh của Official Account liên quan đến đơn hàng | 1009393 |
| OA_STORE_NAME | STRING | Tên cửa hàng của Official Account liên quan đến đơn hàng | - |
| ORDER_NUMBER | STRING | Mã định danh của đơn hàng | 100924-RDK1512, 100924-XQN7484 |
| IS_DELETED | FLOAT | Trạng thái xóa của đơn hàng, 0: chưa xóa, 1: đã xóa | 0.0 |
| STATUS | STRING | Trạng thái của đơn hàng (ví dụ: INIT, COMPLETED) | DISH_READY, COMPLETED, ORDER_FAILED, DELIVERING, PREPARING, INIT, CANCELED, ORDER_SUCCESS |
| PAYMENT_STATUS | STRING | Trạng thái thanh toán của đơn hàng (ví dụ: WAITING, PAID) | WAITING |
| DELIVERY_STATUS | STRING | Trạng thái giao hàng của đơn hàng | DELIVERED, DELIVERING, FOUND_A_DRIVER, CANCELED, FINDING_DRIVER |
| SERVING_TYPE | STRING | Loại hình phục vụ của đơn hàng (ví dụ: DELIVERY, PICKUP) | DELIVERY |
| ORIGINAL_AMOUNT | FLOAT | Tổng số tiền gốc của đơn hàng trước khi áp dụng khuyến mãi | 165000.0, 95000.0 |
| PAY_AMOUNT | FLOAT | Số tiền thực tế phải trả sau khi áp dụng khuyến mãi | 165000.0, 95000.0 |
| DISCOUNT_AMOUNT | FLOAT | Số tiền được giảm giá từ khuyến mãi | 0.0 |
| CUSTOMER_NOTE | STRING | Ghi chú của khách hàng cho đơn hàng | None |
| PAYMENT_METHOD | STRING | Phương thức thanh toán của đơn hàng | None |
| CANCELED_BY | STRING | Người hủy đơn hàng | System, Merchant |
| CANCELED_REASON | STRING | Lý do hủy đơn hàng | None |
| PARTNER_ORDER_NUMBER | STRING | Mã đơn hàng của đối tác | 060525-AOX4111 |
| PAYMENT_TID | STRING | ID của giao dịch (Transaction_id) | None |

### Data Example:
```
Empty DataFrame
Columns: [ID, user_id, date, LAST_MODIFIED, OA_ID, ORDER_NUMBER, IS_DELETED, status, payment_status, delivery_status, SERVING_TYPE, ORIGINAL_AMOUNT, PAY_AMOUNT, DISCOUNT_AMOUNT, CUSTOMER_NOTE, PAYMENT_METHOD, CANCELED_BY, CANCELED_REASON, PARTNER_ORDER_NUMBER, PAYMENT_TID]
Index: []
```

---

## Table 4: project-5400504384186300846.MBI_DA.MART_ORDER_INFO

**Description:** Bảng record các thông tin tổng hợp về đơn hàng Delivery trên TĐMM

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| PAYMENT_TID | STRING | Mã giao dịch thanh toán, định danh duy nhất cho mỗi giao dịch | 75067906441, 75072801619, 75085887421 |
| VOUCHER_AMOUNT | FLOAT | Số tiền được giảm giá từ voucher trong giao dịch | 0.0, nan |
| DATE | DATE | Ngày thực hiện giao dịch | 2024-12-28 |
| BUDGET_TYPES | STRING | Loại ngân sách được sử dụng trong giao dịch, ví dụ: MoMo_Fund | MoMo_Fund, MC_Fund |
| GIFT_ID | STRING | Mã định danh của 1 gift_type_id liên quan đến giao dịch | None |
| CAMPAIGN_ID | STRING | Mã định danh của chiến dịch khuyến mãi liên quan đến giao dịch | None |
| GIFT_TYPE_ID | STRING | Mã định của gift config trên Athena liên quan đến giao dịch | None |

### Data Example:
```
   payment_tid  voucher_amount        date budget_types        GIFT_ID                   campaign_id                  GIFT_TYPE_ID
0  91238773263         10800.0  2025-06-18      MC_Fund  0M27ERMVPDYY0   IPDL_06_1384796532917780480   IPDL_06_1384796532917780480
1  91210119533         30000.0  2025-06-18      MC_Fund  0M2585ZN4DTC0  IPDL_AWO_1379621666451210240  IPDL_AWO_1379621666451210240
2  91238771782          4500.0  2025-06-18      MC_Fund  0M27E7KHS1BE0           1376446118344343552           1376446118344343552
3  83407969007         21000.0  2025-04-03      MC_Fund  0K9TEZ085BH60  IP_44_25_1356843192945156096  IP_44_25_1356843192945156096
4  83384375865         30000.0  2025-04-03      MC_Fund  0K9RV4G6NBH60  IPDL_AWO_1355424258211651584  IPDL_AWO_1355424258211651584
```

---

## Table 5: project-5400504384186300846.MBI_DA.DM_MDS_TDMM_REVIEWER_CLUB

**Description:** Bảng record các bài review của user trên Reviewer Club thuộc TĐMM (Review cho các cửa hàng FnB)

### Columns:

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| REVIEW_ID | FLOAT | ID của bài đánh giá | 111835355104227.0, 111835431481138.0, 111836244495419.0 |
| REVIEW_DESC | STRING | Nội dung của bài đánh giá | Ko, Momo, None, 👍 |
| IMG_COUNT | FLOAT | Số lượng hình ảnh trong bài đánh giá | 0.0, 1.0 |
| VIDEO_COUNT | FLOAT | Số lượng video trong bài đánh giá | 0.0 |
| PRODUCT_ID | FLOAT | ID của sản phẩm được đánh giá | nan |
| GROUP_ID | FLOAT | ID của nhóm sản phẩm | nan |
| TYPE_ID | FLOAT | ID của loại sản phẩm | 107059573304974.0, 107250683969276.0, 107799895377533.0, 109505859350662.0 |
| PRODUCT_NAME | STRING | Tên của sản phẩm được đánh giá | Chuyển Tiền Miễn Phí, Heo Đất MoMo, Hóng hớt MoMo, MaMa Đầu Tư |
| PAID | FLOAT | Trạng thái thanh toán của bài đánh giá (1: đã thanh toán, 0: chưa thanh toán) | 1, 0 |
| CREATOR_ID | STRING | ID của người tạo bài đánh giá | 10055322, 17020961, 39691779 |
| PRODUCT_TYPE_NAME | STRING | Tên loại sản phẩm | OA Brand |
| POST_STATUS | FLOAT | Trạng thái bài viết (chờ duyệt, published,deleted,hidden) tại thời điểm hiện tại; chờ duyệt = 1, duyệt = 5 (visibility = 1), thu hồi (visibility = 0, status =5), xóa (visibility = 0, status =5) - có thể khôi phục, gỡ bỏ (xóa khỏi DBeaver) | - |
| OUTSTANDING_STATUS | FLOAT | Trạng thái nổi bật của bài viết (1: nổi bật, 0: không nổi bật) | 0.0 |
| PUBLIC_TAG_NAMES | STRING | Tên các thẻ công khai gắn với bài đánh giá | '' |
| INTERNAL_TAG_NAMES | STRING | Tên các thẻ nội bộ gắn với bài đánh giá | None |
| DATE | DATE | Ngày tạo bài đánh giá | 2024-01-29 |
| DATE_TIME | DATETIME | Ngày giờ tạo bài đánh giá | 2024-01-29 03:01:33.000, 2024-01-29 03:20:58.000, 2024-01-29 06:47:44.000 |
| UPDATED_DATE_TIME | DATETIME | Thời gian cập nhật bài đánh giá | 2024-01-29 03:01:33.783, 2024-01-29 03:20:58.764, 2024-01-29 06:47:44.198 |
| RATING | FLOAT | Đánh giá của người dùng cho sản phẩm | 1, 2, 3, 4, 5 |
| REVIEW_TYPE | STRING | Loại bài đánh giá | Review, Advanced_review |
| OA_ID | STRING | ID của Official Account được user đánh giá | 9898513, 9926377, 9926379, 9926837 |
| POST_TYPE | FLOAT | Phân loại bài viết: 1 Fanpage post, 3 User post public, 9 User post friend, 10 User post only me, 4 Activity post, 11 Activity post public, 12 Activity post friend, 13 Activity post only me, 99 Review, 17 QR post public, 18 QR post friend, 19 QR post only me | - |
| M4B_CAT | STRING | Danh mục M4B liên quan đến sản phẩm | Food and Beverage |

### Data Example:
```
      REVIEW_ID REVIEW_DESC  IMG_COUNT  VIDEO_COUNT    PRODUCT_ID      GROUP_ID       TYPE_ID                                      PRODUCT_NAME  PAID CREATOR_ID PRODUCT_TYPE_NAME  POST_STATUS  OUTSTANDING_STATUS                                                                                                                            PUBLIC_TAG_NAMES                           INTERNAL_TAG_NAMES        date               date_time       updated_date_time  rating review_type    oa_id  post_type   M4B_CAT
0  3.946208e+14          Ok        0.0          0.0  2.814750e+14  1.098666e+14  1.098667e+14                             Coffee 24/24 - Lê Lợi   1.0   84502827          OA Brand          2.0                 0.0  [Cực kỳ thỏa mãn, Không gian xịn, Vượt mong đợi, Rất thoải mái, Vô cùng ưng ý, Đáng tiền, Đáng để thử, Sẽ quay lại, Quá là xịn, Tuyệt vời]                       [Được AI duyệt review]  2024-09-16 2024-09-16 13:23:39.632 2024-09-16 13:30:24.297     5.0      Review  1048312       99.0  Beverage
1  3.946218e+14          Ok        1.0          0.0  2.814750e+14  1.098666e+14  1.098667e+14  Bún Riêu, Canh Bún Phương Trinh - An Dương Vương   1.0   83125682          OA Brand          2.0                 0.0                                                                                                                                          []                                           []  2024-09-16 2024-09-16 17:33:36.300 2024-09-17 00:10:24.393     5.0      Review  9875572       99.0      Food
2  3.946187e+14          Ok        0.0          0.0  2.814750e+14  1.098666e+14  1.098667e+14                             Coffee 24/24 - Lê Lợi   1.0   84502827          OA Brand          2.0                 0.0  [Vượt mong đợi, Cực kỳ thỏa mãn, Không gian xịn, Rất thoải mái, Vô cùng ưng ý, Đáng tiền, Đáng để thử, Sẽ quay lại, Quá là xịn, Tuyệt vời]                       [Được AI duyệt review]  2024-09-16 2024-09-16 04:29:50.845 2024-09-16 04:40:24.228     5.0      Review  1048312       99.0  Beverage
3  3.946180e+14         ??y        0.0          0.0  2.814750e+14  1.098666e+14  1.098667e+14                    Jollibee - Vincom Phan Văn Trị   1.0   87216097          OA Brand          2.0                 0.0                                                                                                                                          []                       [Được AI duyệt review]  2024-09-16 2024-09-16 01:50:22.387 2024-09-16 01:50:36.861     5.0      Review  9887837       99.0      Food
4  3.946229e+14        Good        0.0          0.0  2.814750e+14  1.098666e+14  1.098667e+14                         Pizza 4P's - SaiGon Pearl   1.0   84384240          OA Brand          2.0                 0.0                                                                                                                             [Vượt mong đợi]  [Được duyệt hình ảnh, Được AI duyệt review]  2024-09-16 2024-09-16 22:13:10.027 2024-09-16 22:13:40.280     5.0      Review  1025810       99.0      Food
```

## Knowledgebase

(empty)

## Memory

(empty)

## Error Message

(empty)