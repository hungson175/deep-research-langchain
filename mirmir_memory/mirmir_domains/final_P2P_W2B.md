# P2P W2B Dataset

## Dataset Information

- **ID**: 526c040d-6956-4cb9-8919-87828de05cfc
- **Name**: P2P W2B
- **Description**: records all transaction of P2P W2B
- **Instructions**: (Not specified)
- **Error Code**: 200

---

## Schema Information

### Dataset Name: P2P W2B

---

## Table 1: momovn-prod.MBI_DA.LOAN_P2P_W2B_RAW_MAPPING

**Description**:
Bảng này chứa dữ liệu chi tiết về các khoản vay P2P với giao dịch từ ví MoMo đến tài khoản ngân hàng. Bảng bao gồm thông tin về lịch sử giao dịch, tài khoản nhận, và chi tiết về khoản vay.

**Main Purposes**:
- Theo dõi lịch sử giao dịch các khoản vay P2P từ ví MoMo đến ngân hàng.
- Quản lý thông tin người sử dụng dịch vụ cho vay P2P.
- Tính toán số liệu về các khoản vay, phí, và tổng số tiền giao dịch.

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| TID | Mã giao dịch cho mỗi lần thực hiện | ["61825452053","61780970758","61831702001"] |
| datetime | Thời gian chi tiết khi giao dịch được thực hiện | ["2024-07-04 21:00:15","2024-07-04 16:52:45","2024-07-04 19:33:19"] |
| DATE | Ngày thực hiện giao dịch | ["2024-04-18","2024-04-05","2025-07-12"] |
| month | Tháng thực hiện giao dịch | ["2024-01-01","2024-05-01","2025-05-01"] |
| user_id | ID của người dùng thực hiện giao dịch | ["1242635","87358202","93216651"] |
| SERVICE_CODE | Mã dịch vụ liên quan đến khoản vay | ["bankcashout_w2b.mbbank14.bank","cardcashout.0911812767","cardcashout.w2b_trunggian_07"] |
| SERVICEID | ID dịch vụ liên quan đến khoản vay | ["transfer_p2b","transfer_p2b_scan_vietqr_upload","transfer_p2b_globalsearch","banklink_cashout_napas","transfer_p2b_search_paste","transfer_p2b_scan_vietqr","banklink_cashout","transfer_p2b_capture","transfer_p2p_globalsearch","transfer_p2p_search_paste"] |
| FUNDID | ID của quỹ liên quan đến khoản vay | ["2","17","3"] |
| AMOUNT | Số tiền giao dịch trong mỗi lần | ["2800000","17400","1696531"] |
| TOTAL_AMOUNT | Tổng số tiền giao dịch | ["271000","528000","2592000"] |
| FEE | Phí liên quan đến giao dịch | ["3534","10318","16234"] |
| BANK_ACC_NO | Số tài khoản ngân hàng nhận tiền |  |
| BANK_NAME | Tên ngân hàng nhận tiền |  |
| ACC_NAME | Tên chủ tài khoản nhận tiền |  |
| BENF_PHONE_NUMBER_DETECT_AID | Số điện thoại của người hưởng lợi được phát hiện | ["26092987","86182397","39959209"] |
| PAYMENT_CHANNEL | Kênh thanh toán sử dụng trong giao dịch | ["w2b_vietqr_copy_paste","w2b_recommend_paste","trans_result_fail","moni_noti_recurring","clipboard_vietqr","trans_his","home_p2p","w2b_clipboard_qr","scan_vietqr_copy_paste","w2b_clipboard_vietqr","chatpay","trans_result_suggestion","meta","bank_list","gallery_vietqr","transfer_reminder","clipboard_text","contact_presearch","bank_paste","contact_paste","scan_null","clipoard_vietqr","w2b_clipboard_text","bank_input_search","tab_p2p","bank_saved","fcm","presearch_saved_contact","contact_bank_popular","trans_result_success","w2b_gallery_qr","contact_input_search","scan_vietqr","scan_vietqr_upload","ocr","presearch_recent_search","w2b_upload_qr","global_contact_presearch","suggestion","create_bank_account","search_p2p","contact_recommend_paste","global_contact_input","trans_detail","vietqr_copy_paste","home_cashout","globalsearch_vietqr_copy_paste","bank_presearch","homep2p_upload","contact_p2p"] |

---

## Table 2: momovn-prod.MBI_DA.LOAN_P2P_W2B_FUNNEL_E2E_EVENT_AGG

**Description**:
Bảng tổng hợp sự kiện end-to-end cho tuyến ứng dụng P2P W2B (Wallet to Business) liên quan đến dịch vụ cho vay. Bảng này chứa thông tin về sự kiện hàng tháng, loại sự kiện, ngày diễn ra sự kiện, số lượng người dùng hàng ngày và người dùng đầu tiên.

**Use Cases**:
- Phân tích xu hướng sử dụng dịch vụ cho vay theo thời gian.
- Theo dõi sự thay đổi số lượng người dùng trong các sự kiện ứng dụng dịch vụ cho vay.
- Xác định và dự đoán hành vi của người dùng theo từng loại sự kiện trong dịch vụ cho vay.

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng diễn ra các sự kiện trong bảng tổng hợp. | ["2025-02-01","2025-03-01","2025-09-01"] |
| type_ | Loại sự kiện liên quan đến dịch vụ cho vay P2P W2B. | ["Check account MH input","CVR - Home P2P - Đề Xuất","Home W2B - Click từ PreSearch","Confirm giao dịch TTAT","CVR - Global Search - Pre Search","Home W2B - Click thanh Search","Load Home W2B","CVR - Others - Others","Click CTA MH Input","Check account MH input fail","Load MH input","Check Account","Load KQGD","CVR - Home P2P - QR","CVR - Home W2B - Search","Home W2B - Click 1 contact từ Người nhận đã lưu","Home W2B - Click Block Ngân hàng phổ biến","CVR - Home W2B - Danh sách đã lưu","CVR - Home P2P - Search","Home P2P - Pre-Search - User click vào 1 contact ở contact list","Switch-off toggle risk","Home P2P - Pre-Search - User click vào 1 contact ở Block Tìm Kiếm Gần Đây","Home Momo - Pre-Search - User click vào 1 contact ở Block Người nhận chuyển tiền","Home W2B - Click 1 ngân hàng trong Block Ngân hàng phổ biến","Home W2B - Click contact Chat_pay","CVR - Home W2B - QR","Home Momo - User input - User Click vào 1 contact kết quả Search","Home W2B - Click contact Block Người nhận đề xuất","CVR - CTGD - CTGD","CVR - Home W2B - Others","CVR - Home W2B - Giao dịch gần đây","Home W2B - Click Icon Người nhận mới","Home W2B - Click Icon Người nhận đã lưu - New","Upload QR","CVR - Home W2B - Ngân hàng phổ biến","CVR - Global Search - Search","CVR - Home W2B - Người nhận mới","CVR - Home P2P - Ngân hàng phổ biến","CVR - Home P2P - Pre Search","CVR - Home MoMo - QR","CVR - Home W2B - Retarget","Click home W2B từ Home P2P","Home W2B - Click contact Block Giao dịch gần đây","Click home W2B từ Home Momo","Home W2B - Click từ Search Result","Load TTAT","CVR - Global Search - Others","Home W2B - Click Icon Mẫu chuyển tiền","Home P2P - User click vào 1 bank ở Block NHPB","CVR - Meta - Meta"] |
| date | Ngày diễn ra sự kiện cụ thể theo thông tin trong bảng. | ["2025-03-30","2025-05-08","2025-06-15"] |
| daily_user | Số lượng người dùng hàng ngày tham gia vào các sự kiện cho vay. | ["148299","482658","71956"] |
| first_user | Số lượng người dùng đầu tiên tham gia vào dịch vụ cho vay trong ngày diễn ra sự kiện. | ["208","2187","140913"] |

---

## Table 3: momovn-prod.MBI_DA.LOAN_P2P_W2B_FUNNEL_SCREEN_INTERACTION_AGGRE

**Description**:
Bảng này chứa thông tin về các tương tác màn hình trong quy trình vay P2P W2B. Dữ liệu trong bảng này có thể được sử dụng để phân tích hành vi người dùng trong quá trình vay tiền, đo lường thành công của các màn hình trong funnel giao dịch, và tối ưu hóa các bước trong quy trình vay P2P W2B.

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng trong đó các tương tác màn hình được ghi nhận. | ["2025-09-01","2025-05-01","2025-04-01"] |
| type_ | Loại tương tác màn hình trong quy trình vay P2P W2B. | ["Home W2B - Click contact Block Người nhận đề xuất","Click Banner Auto-detect","Click CTA Block Retarget","Click Icon Lịch nhắc chuyển tiền","Click Icon Upload QR","Click nút Dán - thanh Search","Home W2B - Click 1 ngân hàng trong Block Ngân hàng phổ biến","Home W2B - Click Icon Người nhận mới","Home W2B - Click Icon Người nhận đã lưu","Home W2B - Click contact Block Giao dịch gần đây","Load Home W2B","Click Tìm thêm Bank","Home W2B - Click thanh Search","Click Pin contact Block Người nhận đề xuất","Load Block Retarget","Total - click 1 contact block Đề Xuất","Click Xem thêm"] |
| value | Giá trị hoặc kết quả của tương tác màn hình. | ["","recent","saved"] |
| session_block | Số lượng phiên bị chặn trong quá trình tương tác màn hình. | ["412765","2675","26770"] |
| user_block | Số lượng người dùng bị chặn trong quá trình tương tác màn hình. | ["251119","2607","23877"] |
| session_click_trans | Số lượng click trans trong phiên. | ["120426","0","182295"] |
| user_click_trans | Số lượng click trans của người dùng. | ["113227","0","249195"] |

---

## Table 4: momovn-prod.MBI_DA.P2P_FUNNEL_ERROR_ALL

**Description**:
Bảng này lưu trữ thông tin lỗi phát sinh trong quy trình chuyển tiền P2P. Nó bao gồm các lỗi xảy ra trong các bước khác nhau của quy trình, mã lỗi, và mô tả chi tiết về lỗi.

**Use Purposes**:
- Phân tích quy trình và tìm ra các điểm bị lỗi
- Đánh giá hiệu suất và chất lượng dịch vụ chuyển tiền P2P
- Xử lý và khắc phục lỗi để cải thiện trải nghiệm người dùng trong các giao dịch P2P

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng xảy ra lỗi. | ["2025-05-01","2025-07-01","2025-08-01"] |
| date | Ngày xảy ra lỗi. | ["2025-07-06","2025-08-25","2025-04-14"] |
| step | Bước trong quy trình P2P mà lỗi xảy ra. | ["Init","Confirm"] |
| service | Loại dịch vụ P2P mà lỗi xảy ra. | ["W2W","W2B"] |
| error_code | Mã định danh cho loại lỗi xảy ra. | ["4353","4438","44400"] |
| agent_id | Mã định danh cho mỗi ví MoMo khi lỗi xảy ra. | ["31012328","32297669","3272599"] |
| event_id | Mã định danh cho sự kiện lỗi. | ["Q8okWhpNtbj_5NdgoIH1g","3YaBOHUbzHEGjRTM1Musx","Me_f4w64EYVg9DQuNvNOP"] |
| error_desc | Mô tả chi tiết về lỗi xảy ra. | ["Hình thức liên kết ngân hàng hiện tại của bạn đã ngừng hỗ trợ do không thỏa Thông tư 23 của Ngân hàng Nhà nước. Bạn hãy liên kết lại tài khoản ngân hàng để tiếp tục giao dịch nhé.","User chưa thực hiện KYC & WL NFC","Đã có lỗi xảy ra trong quá trình xử lý, bạn vui lòng thử lại giúp Momo nhé."] |

---

## Table 5: momovn-prod.MBI_DA.LOAN_P2P_W2B_ERROR_TRANS_RAW

**Description**:
Bảng lưu trữ thông tin giao dịch P2P và W2B có lỗi trong quá trình xử lý khoản vay, bao gồm mã lỗi, tên ngân hàng và thông điệp phản hồi. Bảng này giúp theo dõi và phân tích các lỗi xảy ra trong giao dịch. Thông tin thu thập được từ bảng này có thể dùng để cải thiện hệ thống xử lý giao dịch, xác định các ngân hàng thường xuyên bị lỗi, và hỗ trợ cho việc khắc phục lỗi nhanh chóng.

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng diễn ra giao dịch bị lỗi. | ["2025-07-01","2025-05-01","2025-01-01"] |
| date | Ngày diễn ra giao dịch bị lỗi. | ["2025-07-27","2025-05-24","2025-06-12"] |
| tid | ID của giao dịch bị lỗi. | ["1744977922366","1744962019461","1744952770346"] |
| user_id | ID của người dùng tham gia giao dịch bị lỗi. | ["24189046","41244775","8087473"] |
| response_code | Mã phản hồi cho giao dịch bị lỗi. | ["4005","-802","-501"] |
| RESPONSE_MESSAGE | Thông điệp phản hồi của giao dịch bị lỗi, cung cấp chi tiết về lỗi xảy ra. | ["Ngan hang phat hanh tai khoan/the tu choi giao dich. Ban lien he voi nguoi nhan de kiem tra thong tin tai khoan hoac thu so the/tai khoan khac nhe.","Giao dich loi. Vui long thuc hien lai giao dich.","Giao dich khong thanh cong do noi dung chuyen tien co ky tu dac biet. Vui long cap nhat noi dung hop le va thuc hien lai."] |
| bank_name | Tên ngân hàng liên quan đến giao dịch bị lỗi. |  |

---

## Table 6: momovn-prod.MBI_DA.TUAN_P2P_W2B_EXC_VIETQR_ACQUISITION_ALL_SOURCES

**Description**:
Bảng này lưu trữ thông tin về các giao dịch từ P2P, W2B và VietQR của tất cả các nguồn. Có thể sử dụng bảng này để phân tích xu hướng giao dịch qua các phương pháp và nguồn khác nhau, đánh giá hiệu quả của VietQR trong việc thu hút khách hàng, cũng như kiểm tra sự phát triển của dịch vụ P2P và W2B trong từng thành phố.

### Columns

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng diễn ra giao dịch. | ["2023-03-01","2025-07-01","2023-01-01"] |
| date | Ngày diễn ra giao dịch. | ["2025-08-21","2025-08-22","2025-03-25"] |
| datetime | Mốc thời gian chi tiết của giao dịch. | ["2025-04-30 02:16:35","2025-04-30 18:41:50","2025-04-30 10:23:44"] |
| tid | Mã định danh của giao dịch. | ["44172826235","44139652957","44155622313"] |
| serviceid | Mã dịch vụ cho từng giao dịch. | ["transfer_gp2b","transfer_p2b_search_paste","transfer_p2b","transfer_p2b_capture","transfer_p2p","transfer_p2p_globalsearch","banklink_cashout_napas","banklink_cashout","transfer_p2b_scan_vietqr_upload","transfer_p2b_globalsearch","transfer_p2p_search_paste"] |
| user_id | Mã định danh của người dùng thực hiện giao dịch. | ["92358010","12205234","64335348"] |
| amount | Giá trị tiền của giao dịch. | ["9970000","392261","222000"] |
| user_type | Loại người dùng thực hiện giao dịch. | ["1. New","02. Retention","03. Reactivation","3.Reactive","01. New to service","2. Retention"] |
| citygroup | Nhóm thành phố nơi giao dịch diễn ra. | ["Thành Phố Hồ Chí Minh","Hồ Chí Minh","Tỉnh khác","TP Lớn","KCN Miền Nam","Hà Nội","KCN Miền Bắc","TP Du lịch"] |
| lv1_acq | Cấp độ 1 của thông tin tiếp nhận. | ["[1]. Organic","[2]. Scheme"] |
| lv2_acq | Cấp độ 2 của thông tin tiếp nhận. | ["06. CRM","05. Noti Journey","04. Comm","[1]. <= 10K","03. Game","01. Voucher","[2]. > 10K","02. Fixed Amount","07. Trigger condition"] |
| lv3_acq | Cấp độ 3 của thông tin tiếp nhận. | ["6371 W2B New x Package 125K","w2b_5k_250819_cbttt_100pt5k_vvh62","231130_w2b_churn_3k"] |

---

## Knowledge Base

(Empty)

---

## Memory

- **Nhóm 'hard core'** (2025-06-10T01:35:02.074212-07:00): bao gồm '[3]. Super hardcore' hoặc '[4]. Hardcore upload'

- **Tính số lượng user active hàng ngày của dịch vụ W2B** (2025-06-19T20:49:58.868632-07:00): cần sử dụng bảng MINH_P2P_W2B_ALL_TRANS_MIMIR thay vì LOAN_P2P_W2B_FUNNEL_E2E_EVENT_AGG

- **Schema 5M - CASE 3** (2025-06-05T02:08:39.655890-07:00): amount + amount_before > 50M THEN (amount - (5000000 - amount_before) - 45000000) * 0.008 + 45000000 * 0.0065 + 3300 if amount_before < 5M, else (50000000 - amount_before) * 0.0065 + (amount + amount_before - 50000000) * 0.008 + 3300 if amount_before < 50M, else amount * 0.008 + 3300

- **Điều kiện lọc giao dịch W2B** (2025-06-05T02:23:58.478969-07:00): (SERVICEID <> 'transfer_p2b_scan_vietqr' OR SERVICEID IS NULL)

- **TTT** (2025-06-19T01:20:09.594871-07:00): là viết tắt của Túi Thần Tài, tương ứng với FUNDID = 6

- **Cách tính revenue** (2025-06-05T01:24:04.733942-07:00): theo các schema dựa vào số lượng giao dịch và amount trong tháng

- **Schema 5M - CASE 1** (2025-06-05T02:08:39.612425-07:00): amount + amount_before <= 5M THEN (amount * 0.0065 + 3300) if tran_before > 30, else 0

- **Schema 5M và money_source** (2025-06-05T02:23:58.439481-07:00): Trong "schema 5M", không có quy định liên quan đến money_source

- **FUNDID mapping** (2025-06-05T02:50:13.425043-07:00): 1=momo, 2=bank_link, 3=napas, 4=visa debit, 5=visa credit, 6=TTT, 7=pay_later, 8=cashback, 9=visa ao ccm, 10=BNPL, 11=newton, 12=direct debit, 13=group fund, 14=transfer

- **Schema 5M - CASE 2** (2025-06-05T02:08:39.637437-07:00): 5M < amount + amount_before <= 50M THEN (amount - (5000000 - amount_before)) * 0.0065 + 3300 if amount_before < 5M, else amount * 0.0065 + 3300

- **Mã lỗi -100031** (2025-07-22T15:55:40.103875): có nghĩa là "Thẻ quà tạm hết lượt sử dụng."

- **Người dùng mới của MoMo** (2025-08-11T17:11:44.941547): = người có 1st active trans (trong cả lifetime) trong tháng

---

## Error Message

(Empty)