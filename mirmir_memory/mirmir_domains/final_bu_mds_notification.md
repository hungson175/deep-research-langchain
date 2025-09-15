# BU MDS: Notification for BU

## Error Code
200

## Data

### Basic Information
- **ID**: bcae6a77-3995-49e5-85ca-36b1ed664c13
- **Name**: BU MDS: Notification for BU
- **Description**: Bảng Notification chỉ tổng hợp số lượng notiid giống dạng event, không theo user do bảng user quá nặng không load nổi nên tất cả câu hỏi có chữ "user", "người dùng" đều trả kết quả null. Metric chính sẽ là delivery outapp, Impression inapp, Click inapp, click outapp, CTR inapp, CTR outapp. Phải input đúng tên campaign name, templateid mới trả ra kết quả
- **Instructions**: (empty)

### Schema DDL

**Dataset name**: BU MDS: Notification for BU

#### Table: momovn-prod.GR_NOTIFICATION.daily_notification_metrics

**Description**: Bảng thống kê số lượng notifciation theo các metrics backend và firebase và breakdown theo các nhóm dimensions : event_date, noti_source, bộ 3 dimensions(template_id, condition_name, condition_value), campaign_name, os, touchpoint.

**PIC**: long.pham3

**Columns**:

- **EVENT_DATE**: Ngày event theo local timezone

- **NOTI_SOURCE**: Là source của notification như CAMPAIGN, TEMPLATE, JOURNEY, PROMOTION_FLOW

- **CAMPAIGN_NAME**:
  - Tên của campaign, BU tự đặt tên, chạy 1 lần theo đúng chỉ định của BU
  - Tương ứng với cột campaign_name trong bảng `momovn-prod.GR_NOTIFICATION.campaign_profile`

- **TEMPLATE_ID**: templateid là mã định danh do PO tự đặt khi muốn gửi thông báo. Chỉ cần đúng đk được setup thì sẽ gửi cho user, chạy dài hạn

- **CONDITION_NAME**: tên điều kiện của template id

- **CONDITION_VALUE**: giá trị điều kiện của template id

- **OS**: Hệ điều hành của điện thoại như IOS, ANDROID

- **TOUCHPOINT**:
  - Là điểm chạm trên app.
  - Tương ứng với params là component_name và giá trị của touchpoint trong bảng momovn-prod.GR_NOTIFICATION.D_NOTI_ACTION_STATUS được lưu ở cột "component_name"
  - Cụ thể các touchpoint https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Noti+Type

- **ORGANIC_USER**: Cột phân loại new hay current user.
  - True = new user
  - False = current user

- **A30_USER**: Phân loại user có thuộc nhóm A30 hay không
  - True = Là active user có giao dịch trong 30 ngày gần nhất
  - False= Là active user nhưng không có giao dịch trong vòng 30 ngày gần nhất

- **MAU_USER**: Month-to-date user
  - True = active user có giao dịch từ ngày đầu tháng đến ngày đang xem xét
  - False = active user không có giao dịch từ ngày đầu tháng đến ngày đang xem xét

- **ALLOW_NOTI**: Cho biết user có đồng ý nhận thông báo từ app momo hay không
  - True: user nhận thông báo
  - False: user không đồng ý nhận thông báo

- **BE_SENT**: Tổng số lượng notification được gửi, bao gồm cả sent outapp và sent inapp

- **BE_DELIVERY**: Tổng số lượng notification được deliver, bao gồm cả delivery outapp và delivery inapp

- **BE_RECEIVE**: Tổng số lượng notification user receive, bao gồm cả luồng outapp và inapp. Hiện tại BE dùng chung 1 action receive_outapp cho cả 2 luồng

- **BE_SENT_OUTAPP**: Tổng số lượng notification được gửi outapp

- **BE_DELIVERY_OUTAPP**: Tổng số lượng notification được deliver outapp. Đây là metric Platform noti đang dùng để đánh giá

- **BE_READ**: Tổng số lượng notification có action là "BE_read". Đây là metric Platform noti KHÔNG dùng để đánh giá

- **BE_DELETE**: Tổng số lượng notification có action là "BE_delete"

- **BE_REQUEST**: Tổng số lượng notification được request theo action "BE_request"

- **BE_SENT_MQTT**: Tổng số lượng notification được gửi inapp thông qua giao thức mqtt và được ghi nhận là action BE_sent_mqtt

- **BE_RECEIVE_OUTAPP**: Tổng số lượng noti user nhận được theo action "BE_receive_outapp".

- **BE_IMPRESSION**: Tổng số lượng notification theo action "BE_impression". Đây là metric Platform noti **KHÔNG** dùng để đánh giá

- **BE_CLICK_READ**: Tổng số lượng notification có action là "BE_click_read". Đây là metric Platform noti **KHÔNG** dùng để đánh giá

- **BE_DELIVERY_MQTT_INAPP**: Tổng số lượng notification có action là "BE_delivery_mqtt_inapp" (noti delivery theo luồng inapp)

- **BE_OUT_OF_QUOTA**: Tổng số lượng notification theo action "BE_out_of_quota". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_REQUEST_DUPLICATED**: Tổng số lượng notification theo action "BE_request_duplicated". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_ML_REJECTED**: Tổng số lượng notification theo action "BE_ml_rejected". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_SENT_OUTAPP_UNALLOW_NOTI_SETTING**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_UNALLOW_NOTI_SETTING". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_SENT_OUTAPP_PRELOAD_SUCESS**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_PRELOAD_SUCESS". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_AUTO_SCHEDULED_SUCCESS**: Tổng số lượng notification theo action "BE_AUTO_SCHEDULED_SUCCESS"

- **BE_AUTO_SCHEDULED_PUSH_SUCCESS**: Tổng số lượng notification theo action "BE_AUTO_SCHEDULED_PUSH_SUCCESS"

- **BE_RISK_USER_BLACKLIST**: Tổng số lượng notification theo action "BE_RISK_USER_BLACKLIST". Cụ thể: https://atlassiantool.mservice.com.vn:9443/display/COR/%5BFRD%5D+Action+Status

- **BE_UNKNOW_ERROR**: Tổng số lượng notification theo action "BE_UNKNOW_ERROR"

- **BE_SENT_OUTAPP_FCM_TOKEN_EMPTY**: Tổng số lượng notifcaition theo action "BE_SENT_OUTAPP_FCM_TOKEN_EMPTY"

- **BE_SENT_OUTAPP_FCM_TOKEN_INVALID**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_FCM_TOKEN_INVALID"

- **BE_MISMATCH_USERID**: Tổng số lượng notification theo action "BE_MISMATCH_USERID"

- **BE_SENT_OUTAPP_FCM_SERVICE_UNAVAILABLE**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_FCM_SERVICE_UNAVAILABLE"

- **BE_TEMPLATE_ERROR**: Tổng số lượng notification "BE_template_error"

- **BE_INVALID_CONTENT**: Tổng số lượng notification theo action "BE_INVALID_CONTENT"

- **BE_SENT_OUTAPP_FCM_TOKEN_UNREGISTERED**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_FCM_TOKEN_UNREGISTERED"

- **BE_SENT_OUTAPP_FCM_INVALID_JSON**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_FCM_INVALID_JSON"

- **BE_SENT_OUTAPP_FCM_BAD_REGISTRATION**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_FCM_BAD_REGISTRATION"

- **BE_SENT_OUTAPP_APN_EXCEPTION**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_APN_EXCEPTION"

- **BE_SENT_MQTT_BUILD_TOPIC_FAILED**: Tổng số lượng notification theo action "BE_SENT_MQTT_BUILD_TOPIC_FAILED"

- **BE_SENT_OUTAPP_APN_TOKEN_UNREGISTERED**: Tổng số lượng notification theo action "BE_SENT_MQTT_BUILD_TOPIC_FAILED"

- **BE_SENT_OUTAPP_APN_TOKEN_BAD**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_APN_TOKEN_BAD"

- **BE_SENT_OUTAPP_APN_TOKEN_DEVICE**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_APN_TOKEN_DEVICE"

- **BE_SENT_MQTT_PUSH_FAILED**: Tổng số lượng notification theo action "BE_SENT_MQTT_PUSH_FAILED"

- **BE_AUTO_SCHEDULED_FAILED**: Tổng số lượng notifcation theo action "BE_AUTO_SCHEDULED_FAILED"

- **BE_REQUEST_RETRY_MAX**: Tổng số lượng notification theo action "BE_REQUEST_RETRY_MAX"

- **BE_SENT_OUTAPP_RETRY_MAX**: Tổng số lượng notification theo action "BE_SENT_OUTAPP_RETRY_MAX"

- **BE_SENT_MQTT_CONFLIG_VERSION**: Tổng số lượng notification theo action "BE_SENT_MQTT_CONFLIG_VERSION"

- **BE_AUTO_SCHEDULED_INVALID**: Tổng số lượng notification theo action "BE_AUTO_SCHEDULED_INVALID"

- **BE_OUT_OF_SURVEY_QUOTA**: Tổng số lượng notification theo action "BE_OUT_OF_SURVEY_QUOTA"

- **BE_STORE_CENTER**: Tổng số lượng notifcation theo action "BE_store_center"

- **BE_STORE_CENTER_REJECTED**: Tổng số lượng notification theo action "BE_STORE_CENTER_REJECTED"

- **BE_ACCEPTED**: Tổng số lương notification theo action "BE_accepted".

- **FB2_IMPRESSION**: Tổng số lượng notification được user impress. Đây là metric Platform noti đang dùng để đánh giá

- **FB2_CLICK_DELETE**: Tổng số lượng notification deleted

- **FB2_CLICK_MORE**: Tổng số lượng notification clicked mở rộng

- **FB2_CLICK_BACK**: Tổng số lượng notification clicked back (có thể xuất hiện ở man hình noti_center, noti setting, snackbar)

- **FB2_CLICK_CLOSE**: Tổng số lượng notifcation theo action "FB2_click_close"

- **FB2_CLICK_READ**: Tổng số lượng notifcation theo action "FB2_click_read". Đây là metric Platform noti đang dùng để đánh giá

- **FB2_CLICK_SMALL**: Tổng số lượng notification theo action "FB2_click_small"

- **FB2_CLICK_UNREAD**: Tổng số lượng notification theo action "FB2_click_unread"

- **UNIQ_IDX**: Là unique index được tạo bởi nhiều dimension kết hợp với nhau ở từng ngày. ` , array_to_string([ format_date('%Y-%m-%d', event_date), noti_source, campaign_name, template_id, condition_name, condition_value, os, touchpoint , cast(organic_user as string), cast(a30_user as string), cast(mau_user as string), cast(allow_noti as string) ], ' | ') as uniq_idx `

- **UPDATE_TIME**: = current_timestamp(), time of this change

- **EXP_TAG**: (empty)

### Knowledge Base
(empty)

### Memory
(empty)

## Error Message
(empty)