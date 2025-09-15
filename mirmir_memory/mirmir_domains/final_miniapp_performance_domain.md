# MiniApp Performance Domain Response

## Error Code
200

## Data

### Basic Information

#### ID
a8e52ce3-b404-42fe-afff-30201ea2897e

#### Name
MiniApp Performance

#### Description
Lấy các chỉ số của từng Miniapp trong MoMo

#### Instructions
(empty)

### Schema DDL

**Dataset Name**: MiniApp Performance

#### Table 1: STT_APDEX_BY_DETAIL

**Table Name**: `momovn-mini-app-analyst.MINI_APP_PLATFORM.STT_APDEX_BY_DETAIL`

**Table Description**: Bảng này chứa thông tin chi tiết về APDEX (Application Performance Index) cho các miniapp trên nền tảng. Thông tin này bao gồm ngày báo cáo, mã miniapp, mã tính năng liên quan, tên màn hình, phiên bản ứng dụng, số build, phiên bản miniapp, hệ điều hành của thiết bị, và các chỉ số đánh giá hài lòng người dùng như số lượng hài lòng, số lượng chấp nhận được, và tổng số bản ghi. Bảng này có thể được sử dụng để đánh giá hiệu suất của các miniapp, theo dõi trải nghiệm người dùng, và phát hiện vấn đề của từng phiên bản hoặc tính năng cụ thể.

**Columns**:
- `report_date`: Ngày báo cáo của dữ liệu APDEX.
- `miniapp_id`: Mã định danh cho miniapp.
- `feature_code`: Mã tính năng liên quan đến miniapp.
- `screen_name`: Tên màn hình của miniapp được đánh giá.
- `app_version`: Phiên bản ứng dụng của miniapp.
- `build_number`: Số build của miniapp.
- `miniapp_version`: Phiên bản miniapp được đánh giá.
- `device_os`: Hệ điều hành của thiết bị sử dụng miniapp.
- `satisfied`: Số lượng người dùng hài lòng với hiệu suất của miniapp.
- `tolerating`: Số lượng người dùng chấp nhận được hiệu suất của miniapp.
- `total_records`: Tổng số bản ghi được báo cáo trong lượt đánh giá.

**Data Example**:
```
  report_date               miniapp_id             feature_code screen_name app_version build_number miniapp_version device_os  satisfied  tolerating  total_records
0  2025-04-09             vn.momo.bank            bank_agribank                   4.2.2        42020            8474       IOS          0           0             14
1  2025-04-09  vn.momo.ins_marketplace  ins_partners_motorcycle                   4.2.2        42020            6519       IOS          0           0              2
2  2025-04-09             vn.momo.bank                bank_bidv                   4.2.2        42020            8474       IOS          0           0              2
3  2025-04-09             vn.momo.bank                  bank_ab                   4.2.2        42020            8474       IOS          0           0              4
4  2025-04-09             vn.momo.bank               bank_sacom                   4.2.2        42020            8474       IOS          0           0              8
```

#### Table 2: STG_MINIAPP_LOAD_TOAST_SCREEN_ERROR

**Table Name**: `momovn-mini-app-analyst.MINI_APP_PLATFORM.STG_MINIAPP_LOAD_TOAST_SCREEN_ERROR`

**Table Description**: Bảng này lưu trữ thông tin về các lỗi xảy ra khi tải màn hình toast của Mini App trên nền tảng MoMo. Nó có thể được sử dụng để phân tích lỗi theo từng ngày (report_date), theo từng giai đoạn chạy thử nghiệm của Mini App (stage), xác định lỗi dựa trên mã lỗi (error_code).

**Columns**:
- `report_date`: Ngày báo cáo lỗi xảy ra.
- `stage`: Giai đoạn phát triển hoặc môi trường triển khai của Mini App khi lỗi xảy ra.
- `error_code`: Mã lỗi xảy ra khi tải màn hình toast của Mini App.
- `device_os`: Hệ điều hành của thiết bị khi lỗi xảy ra.
- `app_version`: Phiên bản của ứng dụng MoMo khi lỗi xảy ra.
- `app_id`: ID của ứng dụng Mini App khi lỗi xảy ra.
- `feature_code`: Mã của tính năng trong Mini App mà lỗi xảy ra.
- `miniapp_type`: Loại Mini App khi lỗi xảy ra.
- `agent_id`: Mã định danh của thiết bị khi lỗi xảy ra.
- `error_message`: Thông điệp mô tả lỗi xảy ra khi tải màn hình toast của Mini App.
- `mini_app_version`: Phiên bản của Mini App khi lỗi xảy ra.
- `stage_id`: ID của giai đoạn hoặc môi trường triển khai khi lỗi xảy ra.
- `build_number`: Số build của ứng dụng khi lỗi xảy ra.
- `event_id`: ID sự kiện lỗi xảy ra.

**Data Example**:
```
  report_date                       stage error_code device_os app_version                 app_id feature_code          miniapp_type  agent_id error_message mini_app_version  stage_id  build_number               event_id
0  2025-04-08  toast_fail_loading_miniapp  213 - M02       IOS      4.2.14           vn.momo.bank               miniapp_react_native  80785281     213 - M02             8652        18         42140  GQA3sfR_JpgPmvNQPfwR5
1  2025-04-08  toast_fail_loading_miniapp  213 - M02       IOS      4.2.14           vn.momo.bank               miniapp_react_native  75927590     213 - M02             8652        18         42140  YvN2HGLh1bUvZO7cyyfFs
2  2025-04-08  toast_fail_loading_miniapp  213 - M02       IOS      4.2.14           vn.momo.ekyc               miniapp_react_native  48936406     213 - M02             3128        18         42140  W2589Bq1pXrq-l05Lss8a
3  2025-04-08  toast_fail_loading_miniapp  213 - M02       IOS      4.2.14  vn.momo.paylaterverse               miniapp_react_native  64636427     213 - M02              804        18         42140  VP3stl5-67Mqq6tuEiak-
4  2025-04-08  toast_fail_loading_miniapp  213 - M02       IOS      4.2.14   vn.momo.promotionhub               miniapp_react_native  25516626     213 - M02             2060        18         42140  HkQWvM9WYq2546iy99y5I
```

### Knowledge Base
(empty)

### Memory
(empty)

## Error Message
(empty)