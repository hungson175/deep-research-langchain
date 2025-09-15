# FS CreditTech Paylater

## Error Code
200

## Data

### Basic Information
- **ID**: 7e23d41a-0baf-4b36-84c3-07fb850bdb6e
- **Name**: FS CreditTech Paylater
- **Description**: Data của sản phẩm Ví Trả Sau/Paylater.
- **Instructions**: (empty)

### Schema DDL

**Dataset name**: FS CreditTech Paylater

#### Table 1: momovn-prod.BU_FI.HTN_PAYLATER_MARKETING_INAPP_RAW

**Description**: (empty)

**Columns**:
- **EV_DATE** (DATE): Event date (YYYY-MM-DD) on which the marketing or product marketing interaction occurred (impression or click). Used for daily-level trend analysis and time-series reporting.

- **EV_TIME** (DATETIME): Precise event timestamp. Useful for event-level tracking and session analysis.

- **AGENT_ID** (STRING): Unique identifier of the user (maps to user_id/user/agentid in behavioral and transactional datasets).

- **CHANNEL** (STRING): In-app entry point where the marketing or product marketing touchpoint occurred. Categorized as:
  - Product Marketing: Buttons on service screens (e.g., TOPUP QA, DATA QA, AIRLINE QA, BUS QA, BILLPAY QA)
  - TTAT Screens: Installment-related screens (e.g., INSTALLMENT TTAT, TTAT QA, TTAT QUICKUNLOCK)
  - Home Screens: Homepage placements (e.g., SERVICE WIDGET, COLLECTION BLOCK, HOME SOF, MMDX ICON, FAV ICON)
  - Other: General placements like VOUCHER HUB, BANNER, NOTI

- **CAMPAIGN_NAME** (STRING): Identifier of the campaign or product session. For channels like NOTI and BANNER, this is the campaign name; for product marketing touchpoints (e.g., TOPUP QA, AIRLINE QA), this represents the session ID of the interaction

- **IMPRESSION** (INT): impressions (typically 1 per event). Indicates content was displayed to the user.

- **CLICK** (INT): 1 if clicked, 0 if not

- **CAPTION** (STRING): Headline or short title of the marketing content shown (marketing channel: Noti)

- **BODY** (STRING): Detailed body text of the marketing message. (marketing channel: Noti)

- **FORMAT** (STRING): Visual format of the content

- **SCREEN** (STRING): Display screen

- **QA_SEGMENT** (STRING): qa_segment = 'new' if user in WL Quick activation (non-register VTS before)

**Data Example**:
```
      ev_date                 ev_time  agent_id           channel campaign_name  impression  click caption body format screen qa_segment
0  2025-05-11 2025-05-11 21:34:31.421  69991547  INSTALLMENT-TTAT                         1      0                               current
1  2025-05-11 2025-05-11 10:39:40.743  66665317  INSTALLMENT-TTAT                         0      1                               current
2  2025-05-11 2025-05-11 16:05:11.138  25821493  INSTALLMENT-TTAT                         1      0                               current
3  2025-05-11 2025-05-11 16:23:23.279  85937619  INSTALLMENT-TTAT                         1      0                               current
4  2025-05-11 2025-05-11 18:42:06.807    389809  INSTALLMENT-TTAT                         1      0                               current
```

#### Table 2: momovn-prod.BU_FI.PAYLATER_MAU_SEGMENT

**Description**: Bảng này lưu trữ thông tin về phân khúc người dùng hoạt động hàng tháng (MAU) liên quan đến dịch vụ Ví Trả Sau (Paylater) tại MoMo. Bảng này có thể được sử dụng để:
- Theo dõi và phân tích hoạt động của người dùng theo tháng.
- Xác định phân khúc người dùng dựa trên hoạt động của họ.
- Dự đoán khả năng hoạt động của người dùng trong tháng tiếp theo.

**Columns**:
- **AGENT_ID** (STRING): Unique user identifier (equivalent to user_id in other systems).

- **MONTH_TRANS** (DATE): Transaction month (YYYY-MM-01 format), used for monthly aggregation and trend analysis.

- **MAU_SEGMENT** (STRING): User segment classification based on monthly PayLater (VTS) usage behavior
  1. New: User made their first-ever payment using VTS in the current month.
  2. Retain: User made a VTS payment in the previous month and continued using VTS this month.
  3. Reactive: User did not use VTS last month, but returned to make a VTS payment in the current month.

- **DATE_TRANS** (DATE): User's first PayLater (VTS) transaction date in the month. Example: For a user with VTS transactions on Jan 5, Jan 15, and Jan 24 → date_trans = '2025-05-01'

- **RETAIN** (STRING): retain is not null if users use VTS next month; null means not retained.

- **USECASE** (STRING): User's first VTS service in the month.

- **GIFT_ID** (STRING): gift_id of first VTS transaction in the month

- **USING_VOUCHER** (STRING): using_voucher = 'voucher' if user user voucher of first VTS transaction in the month

- **TRANS_TIME** (DATETIME): Timestamp of the first VTS transaction in the month.

- **TRANSACTION_AGE** (INT): age of user

- **GIFT_SEGMENT** (STRING): gift type ( xu or vts gift...) of first VTS transaction in the month

- **TRANS_TYPE** (STRING): note: pay_ins: installment on trans

**Data Example**:
```
   agent_id month_trans MAU_segment  date_trans    retain      usecase                                   gift_id using_voucher trans_type gift_segment          trans_time  transaction_age
0   8852537  2025-06-01    2.Retain  2025-06-10   8852537  ADS PAYMENT       250516_ads250516_giam_10pt30k_cfjms       voucher     pay_pl    2.BU gift 2025-06-10 09:56:29               29
1  85401427  2025-06-01       1.New  2025-06-10  85401427      AIRTIME    fs_vts_new_250515_cbttt_100pt30k_4z0m8       voucher     pay_pl   1.VTS gift 2025-06-10 19:33:18               18
2  79395409  2025-06-01       1.New  2025-06-10  79395409      AIRTIME  fs_vts_telco_250523_cbttt_100pt10k_u6eb9       voucher     pay_pl   1.VTS gift 2025-06-10 08:09:34               18
3  92924711  2025-06-01    2.Retain  2025-06-10  92924711      AIRTIME   churn_60_90_v2_250605_giam_10pt5k_f7lds       voucher     pay_pl    2.BU gift 2025-06-10 19:48:29               18
4  53582047  2025-06-01       1.New  2025-06-10  53582047      AIRTIME   gmc_xsell_cm_at250528_giam_10pt3k_k6hph       voucher     pay_pl    2.BU gift 2025-06-10 11:20:20               18
```

#### Table 3: momovn-prod.BU_FI.MT_PAYLATER_ACCOUNT_MANAGEMENT

**Description**: (empty)

**Columns**:
- **ID** (FLOAT): (empty)

- **CREATED_MILLIS** (INT): Ngày tạo hồ sơ với ví trả sau, được xem là ngày user mở ví. Một user có thể hủy ví & mở ví lại nhiều lần.

- **PL_LOAN_ID** (STRING): mã hồ sơ khoản vay của ví trả sau

- **AGENTID_MM** (STRING): agent_id của user với ví MoMo

- **MODIFIED_MILLIS** (INT): Thời gian sửa đổi lần cuối của loan_id

- **DELETED_MILLIS** (INT): Thời gian user hủy ví trả sau. Null nếu ví đó còn hoạt động (status_desc != DEACTIVED). Lưu ý với miliscecond đang ở UTC 0, cần +7 nếu chuyển đổi thành datetime value

- **DELETED** (FLOAT): Thời gian user hủy ví trả sau. Null nếu ví đó còn hoạt động (status_desc != DEACTIVED).

- **CREATED_DATE** (DATE): Ngày mở ví trả sau của user, ngày mà user được bank trả kết quả duyệt hồ sơ & cấp hạn mức cho user.

- **DEACTIVED_DATE** (DATE): ngày user hủy VTS, được extract từ deleted_date

- **STATUS** (STRING): trạng thái ví, dưới dạng số. 0,1,2,3

- **STATUS_DESC** (STRING): desctiption của trạng thái ví, bao gồm:
  - ACTIVED - ví còn hoạt động.
  - LOCKED_BY_USER - user tự khóa VTS tạm thời, có thể mở lại theo ý muốn.
  - LOCKED_BY_MOMO - user bị khóa vĩnh viễn do trễ hạn thanh toán theo thời gian quy định. Việc có mở lại hay không tùy theo chính sách giữa MoMo & bank, nhưng được xem là những user không eligible để thanh toán.
  - DEACTIVED - user đã hủy VTS.

  VTS register là những user xuất hiện trong bảng này.
  Eligible user: là những user có trạng thái gần nhất là ACTIVED & LOCKED_BY_USER.

- **LENDER_CODE** (STRING): (empty)

- **LATEST_RECORD** (INT): Ghi nhận thứ tự ví của user, nếu latest_record = 1 thì được hiểu là trạng thái ví gần nhất của user. Nếu cần check 1 user hiện tại có VTS không thì chỉ cần filter latest_record = 1

- **PARTNER_NAME** (STRING): Tên đối tác (ngân hàng) mà user ký hợp đồng khoản vay. TPB là ngân hàng Tiên Phong, MBV là ngân hàng MB.

**Data Example**:
```
           ID  CREATED_MILLIS        PL_LOAN_ID AGENTID_MM LENDER_CODE  MODIFIED_MILLIS  DELETED_MILLIS     DELETED CREATED_DATE DEACTIVED_DATE STATUS STATUS_DESC  LATEST_RECORD PARTNER_NAME
0  67492283.0   1732641804000  SL00000091980926   83520793         105    1732642153000   1732642153000  83665712.0   2024-11-27     2024-11-27      1   DEACTIVED              1          TPB
1  67492315.0   1732642129000  SL00000091981243   84469374         105    1732642303000   1732642304000  83665744.0   2024-11-27     2024-11-27      1   DEACTIVED              1          TPB
2  67492453.0   1732642904000  SL00000091981870   94912251         105    1732643066000   1732643066000  83665882.0   2024-11-27     2024-11-27      1   DEACTIVED              1          TPB
3  67492347.0   1732642243000  SL00000091981320   76485211         105    1732643267000   1732643267000  83665776.0   2024-11-27     2024-11-27      0   DEACTIVED              2          TPB
4  67492505.0   1732643232000  SL00000091982163   46942860         105    1732643372000   1732643372000  83665934.0   2024-11-27     2024-11-27      1   DEACTIVED              1          TPB
```

#### Table 4: momovn-prod.BU_FI.PAYLATER_ALL_TRANS

**Description**: Bảng fact này chứa thông tin chi tiết về tất cả các giao dịch liên quan đến dịch vụ Paylater của MoMo. Bảng này có thể được sử dụng để:
- Theo dõi và phân tích các giao dịch Paylater theo thời gian.
- Đánh giá hiệu suất của các dịch vụ và đối tác liên quan đến Paylater.
- Quản lý và giám sát các khoản vay và hạn mức tín dụng của người dùng.

**Columns**:
- **ID** (INT): mã giao dịch riêng của core ví trả sau, không phải mã giao dịch trên momo

- **CORE_ID** (STRING): mã giao dịch trên momo, dùng chung cho toàn bộ platform

- **CREATED_MILLIS** (INT): Thời gian tạo giao dịch tính bằng milliseconds. Đây sẽ được xem là thời gian user thực hiện giao dịch. Note là thời gian ở đây đang là UTC 0. Khi cần filter field này, cần cộng thêm 7 giờ cho phù hợp với múi giờ Việt Nam.

- **CREATED_DATE** (DATE): Ngày tạo giao dịch. Đây được xem là ngày user thực hiện giao dịch.

- **SERVICE_ID** (STRING): ID dịch vụ của giao dịch, dữ liệu nhạy cảm

- **USER_ID** (STRING): ID của người dùng thực hiện giao dịch, đây là metric để tính số lượng user

- **BILL_ID** (STRING): ID hóa đơn liên quan đến giao dịch, quản lý bill của user bằng field này

- **AMOUNT** (FLOAT): Số tiền/giá trị của giao dịch.

- **RESULT_CODE** (INT): Mã kết quả của giao dịch. Giao dịch thành công có result_code bằng 0. Khi tính toán các chỉ số MAU (active users), GMV/disbursement/giải ngân thì cần phải filter result_code = 0.

- **TRANS_TYPE** (STRING): Loại giao dịch, ví dụ: 'send_ins', 'pay_pl_fee_min_record'. Giao dịch thanh toán, dùng để tính GMV/disbursement, MAU (active user): pay_ins, pay_pl, send_pl.

- **ACCOUNT_TYPE** (INT): Loại tài khoản liên quan đến giao dịch. các giao dịch chính của paylater sẽ có account_type = 21

- **PAYLATER_LOAN_ID** (STRING): ID khoản vay Paylater liên quan đến giao dịch. Sample value: ['SL00000020827779', 'SL00000043141252']

- **LEVEL_** (STRING): Hạng của hợp đồng khoản vay, gồm Vàng, Bạc, Đồng. Rank của loan ảnh hưởng đến initial limit & due date. Sample value: ['GOLD']

- **PARENT_ID** (STRING): ID cha của giao dịch, dùng để liên kết với các giao dịch khác. Sample value: ['2203738138', '2203738453']

- **BILL_TYPE** (STRING): (empty)

- **RANK** (STRING): Rank của hợp đồng cấp cho user, bao gồm Vàng, Bạc, Đồng. Rank của user ảnh hưởng đến hạn mức cấp ban đầu cho user và ngày đến hạn của user.

- **CREDIT_LIMIT** (INT): Hạn mức tín dụng được cấp trong tháng của người dùng. 1 user có thể có nhiều hơn 1 giá trị hạn mức (do tăng/giảm hạn mức trong tháng), khi nhắc đến hạn mức user có trong 1 tháng, lấy giá trị lớn nhất. Sample value: ['5000000']

- **ERROR_DESC** (STRING): Mô tả lỗi của giao dịch. Sample value: ['Success']

- **VI_ERROR_DESC** (STRING): Mô tả lỗi bằng tiếng Việt của giao dịch. Sample value: ['Thành công']

- **PARTNER_AGENT** (STRING): Service code của giao dịch, primary key để map lấy tên merchant (service_name) and service_category. Sample value: ['None']

- **SERVICE_NAME** (STRING): Tên đối tác mà user thực hiện thanh toán, khác với partner_name là tên ngân hàng ký kết hợp đồng với user để cho user mua trước trả sau. Ví dụ: User này đang có VTS được ký kết hợp đồng với ngân hàng MBV thì sẽ ghi nhận partner_name của khoản vay này là MBV. User thực hiện thanh toán giao dịch mua trước trả sau bằng việc mua ly cafe Phuc Long thì ghi nhận service_name là Phuc Long.

- **SERVICE_CATEGORY** (STRING): Danh mục dịch vụ của giao dịch. Sample value: ['None']

- **NEWVERTICAL** (STRING): Ngành dọc mới liên quan đến giao dịch. Sample value: ['None']

- **BU_GROUP_CODE_L1** (STRING): Mã nhóm kinh doanh cấp 1 liên quan đến giao dịch. Sample value: ['None']

- **TYPEID** (ARRAY): Loại ID liên quan đến giao dịch. Sample value: ['None']

- **VC_AMT** (FLOAT): Số tiền nhận được từ voucher. Sample value: ['nan']

- **CB_AMT** (FLOAT): Số tiền nhận được từ cashback. Sample value: ['nan']

- **BILL** (STRING): Thông tin hóa đơn liên quan đến giao dịch. Sample value: ['ins_convert']

- **PARTNER_NAME** (STRING): Tên đối tác mà user ký hợp đồng khoản vay. TPB là ngân hàng Tiên Phong, MBV là ngân hàng MBV. Sample value: ['TPB']

- **TRANSACTION_AGE** (INT): Tuổi của user thực hiện giao dịch. Sample value: ['26', '42']

**Data Example**:
```
           id      core_id  created_millis created_date       service_id   user_id    amount  result_code trans_type  account_type  paylater_loan_id  level_    parent_id    bill_type    rank  credit_limit error_desc vi_error_desc        partner_agent   service_name service_category newvertical bu_group_code_l1 typeid  vc_amt  cb_amt         bill partner_name  transaction_age
0  2605728443  89461584281   1748883828000   2025-06-03     EPAY_VIETTEL   1016792   66666.0            0   send_ins            27  SL00000093707685  BRONZE  89461584281  ins_payment  BRONZE       1000000    Success    Thành công  vttiwhypay_mathe_vt        VIETTEL          AIRTIME     AIRTIME          TELECOM     []     0.0     0.0  ins_payment          TPB               20
1  2605728441  89461584281   1748883828000   2025-06-03     EPAY_VIETTEL   1016792   66667.0            0   send_ins            27  SL00000093707685  BRONZE  89461584281  ins_payment  BRONZE       1000000    Success    Thành công  vttiwhypay_mathe_vt        VIETTEL          AIRTIME     AIRTIME          TELECOM     []     0.0     0.0  ins_payment          TPB               20
2  2605728442  89461584281   1748883828000   2025-06-03     EPAY_VIETTEL   1016792   66667.0            0   send_ins            27  SL00000093707685  BRONZE  89461584281  ins_payment  BRONZE       1000000    Success    Thành công  vttiwhypay_mathe_vt        VIETTEL          AIRTIME     AIRTIME          TELECOM     []     0.0     0.0  ins_payment          TPB               20
3  2605733112  89462154882   1748883745000   2025-06-03  evnspc_dongthap  20393932  490286.0            0   send_ins            27  SL00000132821902  BRONZE  89462154882  ins_payment  BRONZE       1000000    Success    Thành công     vttievndtp_lapvo  EVN DONG THAP        UTILITIES   UTILITIES      BILLPAYMENT     []     0.0     0.0  ins_payment          TPB               19
4  2605733111  89462154882   1748883745000   2025-06-03  evnspc_dongthap  20393932  490287.0            0   send_ins            27  SL00000132821902  BRONZE  89462154882  ins_payment  BRONZE       1000000    Success    Thành công     vttievndtp_lapvo  EVN DONG THAP        UTILITIES   UTILITIES      BILLPAYMENT     []     0.0     0.0  ins_payment          TPB               19
```

### Knowledge Base
(empty)

### Memory

1. **Memory ID**: 73c53c8c-6fff-4ce1-a177-262e2183dbef
   - **Content**: MAU_SEGMENT = '1.New' là new mau (first time active PayLater), không phải New register
   - **Hash**: 392ac6ed19285c7b5eb348af78d73730
   - **Created**: 2025-08-25T01:42:19.361994-07:00
   - **Updated**: 2025-08-25T01:42:43.414438-07:00

2. **Memory ID**: 95c4e4d9-4119-4eb2-9c25-dfd04b769dde
   - **Content**: MAU = monthly active user, là user có hành vi thanh toán với Paylater trong tháng, tính tới ngày t-1 so với ngày lấy data
   - **Hash**: 0ab456ddb86ffd65ed21c629bc163505
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-13T08:47:21.975389-07:00

3. **Memory ID**: deed3dba-e40c-4ead-8a2b-dbb451299c21
   - **Content**: Active user bao gồm 3 trans_type: pay_pl, pay_ins, send_pl
   - **Hash**: d90f3fea02eca4729fc0e828c0288da9
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-11T03:12:41.055738-07:00
   - **Updated**: 2025-07-11T03:22:10.911280-07:00

4. **Memory ID**: eaae3663-fea7-46c4-9fa0-29b77d421cc6
   - **Content**: VTS là ví trả sau - paylater
   - **Hash**: 24a4ede5cc1114df353203e6b1c06db5
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-11T03:12:41.008569-07:00
   - **Updated**: 2025-07-13T08:47:21.718051-07:00

5. **Memory ID**: bf89934d-ff6e-4104-886a-77bda1644fc4
   - **Content**: Luôn lấy data đến ngày hôm qua, không lấy data hôm nay vì không đủ
   - **Hash**: 5359874474c689774dec504668378ea5
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-14T00:51:57.636696-07:00

6. **Memory ID**: bef72bbb-0374-4327-ba5d-d3e647fb3042
   - **Content**: Khi được hỏi tới một tên merchant hay dùng giá trị của cột service_name trong bảng PAYLATER_ALL_TRANS, dưới đây là top các giá trị trong cột service_name, nếu bị hỏi tên merchant lạ quá hay hỏi cụ thể service_name của merchant là gì: (followed by extensive list of service names including VIETTEL, TIKTOK, MOBIFONE, APPLE, etc.)
   - **Hash**: 04a3a9de8d7acfd8bd9271ea758deaa5
   - **User**: FS CreditTech Paylater
   - **Created**: 2025-07-18T16:53:05.461697
   - **Updated**: 2025-07-20T20:16:19.754420-07:00

7. **Memory ID**: 7cda57db-f087-4238-98aa-a56b6a23906b
   - **Content**: GMV chỉ tính cho giao dịch thành công (result_code = 0)
   - **Hash**: efe9ec1fe3586efd3472d9de44a5369a
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-11T03:53:24.790375-07:00

8. **Memory ID**: 9390593c-517c-4ac0-a259-66745e78b728
   - **Content**: GMV = amount của các trans_type = pay_ins, pay_pl, send_pl
   - **Hash**: 80669beb71c6dbd4150ad04b743a516d
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-11T03:53:24.732698-07:00
   - **Updated**: 2025-07-11T03:55:57.308211-07:00

9. **Memory ID**: d3375203-5088-4337-8478-25121abb9ff7
   - **Content**: User thanh toán VTS là user có transaction_type = pay_pl, pay_ins, send_pl
   - **Hash**: 8f8910ecfbe32cb8d607d79dea68de6d
   - **User**: FS CREDITTECH PAYLATER
   - **Created**: 2025-07-13T08:47:22.012261-07:00

10. **Memory ID**: 546b660e-71de-45eb-a066-41b55cc11b86
    - **Content**: Khi truy vấn trường service_name, sử dụng tìm kiếm theo mẫu thay vì khớp chính xác, dùng chữ thường và hàm like
    - **Hash**: 2f4ca97adaadfb509f60f3f31bc38c0e
    - **User**: FS CreditTech Paylater
    - **Created**: 2025-07-18T03:20:17.862742-07:00

## Error Message
(empty)