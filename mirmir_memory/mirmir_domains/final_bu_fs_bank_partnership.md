# BU FS: Bank Partnership

## Dataset Information

- **ID**: 7102da6a-2fdc-4475-a3bf-b66be5bca419
- **Name**: BU FS: Bank Partnership
- **Description**: Thông tin dữ liệu về các dịch vụ liên quan tới ngân hàng (nạp/ rút/ liên kết/ direct debit/ w2b/ ...)
- **Instructions**:
- **Error Code**: 200

## Schema Information

### Table 1: momovn-prod.BU_FI.BANK_W2B_RAW

**Description**: Bảng này chứa thông tin chi tiết về các giao dịch chuyển tiền từ ví MoMo đến ngân hàng (W2B).

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| DATE | DATE | Ngày khởi tạo giao dịch chuyển tiền từ ví MoMo đến ngân hàng. | 2024-07-10 |
| PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi. | |
| BANK_CODE | STRING | Mã ngân hàng dùng để thực hiện chuyển tiền từ ví MoMo đến ngân hàng. | VTB |
| BANK_NAME | STRING | Tên ngân hàng dùng để thực hiện chuyển tiền từ ví MoMo đến ngân hàng. | |
| BANK_RECEIVED | STRING | Mã ngân hàng được nhận tiền từ ví MoMo. | ACB, DongABank, None, VIB |
| TYPE | STRING | Luồng chuyển tiền từ ví MoMo tới ngân hàng<br>1. SAME: luồng internal<br>2. DIFF: luồng external | |
| REQUEST_ID | STRING | Mã định danh duy nhất cho mỗi yêu cầu chuyển tiền từ ví MoMo tới ngân hàng. | 1ec08f95-691b-4e27-90fd-1cd056fe6445, 220c95cb-3669-4ada-a34f-fdd78376bbd5, 50172894-f3a5-4553-b4d9-2d66e3585f11 |
| TID | FLOAT | Mã định danh giao dịch. | 62187421058.0, 62199181951.0, 62210667900.0 |
| USER | STRING | Mã định danh người dùng (còn có thể gọi là agentid) thực hiện chuyển tiền từ ví MoMo tới ngân hàng. | 33938882, 4343039, 47197973 |
| AMOUNT | FLOAT | Số tiền chuyển tiền từ ví MoMo tới ngân hàng. | 150000.0, 1500000.0, 200000.0 |
| AMT_RANGE | STRING | Khoảng giá trị của số tiền chuyển tiền. | 1.1-500K, 2.500001-2M, 3.2000001-300M |
| STATUS | INT | Trạng thái của giao dịch<br>1. 1: giao dịch treo<br>2. 2: giao dịch thành công<br>3. 6: giao dịch thất bại | |
| CHANNEL | STRING | Kênh thực hiện chuyển tiền từ ví MoMo tới ngân hàng<br>1. VietQR: quét mã VietQR<br>2. Other: những kênh khác | |
| CHANNEL_DETAIL | STRING | Chi tiết kênh thực hiện chuyển tiền từ ví MoMo tới ngân hàng. | |
| CASHOUT_ACC_TYPE | STRING | Giao dịch từ tài khoản gì?<br>1. UNKNOWN: không xác định được<br>2. ACCOUNT: giao dịch từ tài khoản<br>3. CARD: giao dịch từ thẻ<br>4. CARD_TQT: giao dịch từ thẻ quốc tế | |
| TRANSFER_TYPE | STRING | Loại chuyển tiền được thực hiện. | APP |
| ROUTE_TYPE | STRING | Chi tiết luồng đi của giao dịch chuyển tiền từ ví MoMo tới ngân hàng. | external |
| DETAIL_FLOW | STRING | Chi tiết 2 của luồng đi của giao dịch chuyển tiền từ ví MoMo tới ngân hàng. | None |
| DATETIME | DATETIME | Ngày và giờ khởi tạo giao dịch chuyển tiền từ ví MoMo đến ngân hàng. | |
| RESPONSE_DATETIME | DATETIME | Thời gian ngân hàng phản hồi lại kết quả chuyển tiền. | |
| PARTNER_ID | STRING | Mã ngân hàng (hiển thị dưới dạng số) dùng để thực hiện chuyển tiền từ ví MoMo đến ngân hàng. | |
| PROCESS_NAME | STRING | Tên của quy trình xử lý chuyển tiền từ ví MoMo tới ngân hàng. | |
| PARTNER_REQUEST_ID | STRING | Mã định danh từ đối tác để trace log. | |
| PARTNER_REF_NUMBER | STRING | Mã định danh 2 từ đối tác để trace log. | |
| STATUS_FINAL | INT | Trạng thái cuối cùng của giao dịch<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch chưa có trạng thái cuối | |
| MS_CODE | STRING | Mã lỗi của MoMo. | |
| PARTNER_MESSAGE | STRING | Diễn giải ý nghĩa mã lỗi đối tác phản hồi. | |
| INQUIRY_STATUS | FLOAT | Trạng thái của giao dịch sau khi được đối soát<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch không đối soát | |
| INQUIRY_FLOW | STRING | Gọi đối soát giao dịch từ luồng nào<br>1. momo_inquiry: MoMo chủ động gọi đối soát<br>2. partner_callback: đối tác gọi trả đối soát | |
| INQUIRY_TIME | INT | Thời gian gọi đối soát lần đầu. | None |
| FINAL_DATETIME | DATETIME | Thời gian thật hoàn tất giao dịch chuyển tiền từ ví MoMo đến ngân hàng (nếu đã có status_final thì = thời gian trong core, còn chưa có status_final thì là response_datetime). | |

### Table 2: momovn-prod.BU_FI.BANK_CI_DIRECT_DEBIT

**Description**: Bảng này chứa thông tin về các giao dịch nạp tiền hạn mức cao (direct debit) từ nguồn ngân hàng tại MoMo.

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| DATE | DATE | Ngày khởi tạo giao dịch nạp tiền hạn mức cao từ nguồn ngân hàng. | 2022-12-01 |
| DATE_TIME | DATETIME | Ngày và giờ khởi tạo giao dịch nạp tiền hạn mức cao từ nguồn ngân hàng. | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |
| BANK_CODE | STRING | Mã ngân hàng liên kết đang thực hiện giao dịch nạp tiền hạn mức cao. | ABB |
| TYPE | STRING | Giao dịch từ tài khoản gì?<br>1. UNKNOWN: không xác định được<br>2. ACCOUNT: giao dịch từ tài khoản<br>3. CARD: giao dịch từ thẻ<br>4. CARD_TQT: giao dịch từ thẻ quốc tế | |
| TID | STRING | Mã định danh giao dịch. | 32668346071, 32668496078, 32669714366 |
| USER | STRING | Mã định danh người dùng (còn có thể gọi là agentid) thực hiện nạp tiền hạn mức cao. | 33938882, 4343039, 47197973 |
| AMOUNT | FLOAT | Số tiền nạp tiền hạn mức cao. | 10000000.0, 10157000.0, 20000.0 |
| MS_CODE | STRING | Mã lỗi của MoMo. | 1004, 3010, 9000 |
| PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi. | -1 |
| BANK_DESC | STRING | Diễn giải ý nghĩa mã lỗi. | Chặn tổng hạn mức tối đa / ngày, Transaction is pending, Vượt hạn mức giao dịch trong ngày |
| STATUS | INT | Trạng thái của giao dịch<br>1. 1: giao dịch treo<br>2. 2: giao dịch thành công<br>3. 6: giao dịch thất bại | |
| STATUS_FINAL | INT | Trạng thái cuối cùng của giao dịch<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch chưa có trạng thái cuối | |
| IS_OTP | FLOAT | Xác định giao dịch có sử dụng OTP hay không?<br>1. 0: không<br>2. 1: có | |
| IS_AUTO_TOPUP | FLOAT | Xác định giao dịch có phải là nạp tiền tự động hay không?<br>1. 0: không<br>2. 1: có | |
| PAYMENT_SERVICE_ID | STRING | Mã dịch vụ liên quan đến giao dịch nạp tiền, để xác định nạp tiền để dùng vào việc gì? | EVN_HANOI, hdss_v2, investment_mutualfund |
| BANK_AUTH_CODE | STRING | Phân loại loại phương thức xác thực | None |
| BANK_TIME | DATETIME | Thời gian ngân hàng phản hồi lại kết quả nạp tiền hạn mức cao. | 2022-12-01 06:11:10, 2022-12-01 19:40:09, NaT |
| FINAL_TIME | DATETIME | Thời gian thật hoàn tất giao dịch nạp tiền (nếu đã có status_final thì = thời gian trong core, còn chưa có status_final thì là bank_time). | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |

### Table 3: momovn-prod.BU_FI.BANK_CO

**Description**: Bảng này chứa thông tin về các giao dịch rút tiền về ngân hàng từ MoMo.

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| DATE | DATE | Ngày khởi tạo giao dịch rút tiền về ngân hàng. | 2022-12-01 |
| DATE_TIME | DATETIME | Ngày và giờ khởi tạo giao dịch rút tiền về ngân hàng. | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |
| LINKAGE | STRING | Nguồn liên kết của nguồn tiền ngân hàng đang thực hiện giao dịch rút tiền<br>1. NAPAS: là nguồn napas<br>2. VISA: là nguồn visa<br>3. NHLK: là nguồn ngân hàng liên kết | |
| BANK_CODE | STRING | Mã ngân hàng liên kết đang thực hiện giao dịch rút tiền. | ABB |
| LINKING_METHOD | STRING | Phương thức liên kết của nguồn được sử dụng<br>1. APP: liên kết từ app MoMo<br>2. IB (internet banking): liên kết từ app/web của ngân hàng đối tác | |
| TYPE | STRING | Giao dịch từ tài khoản gì?<br>1. UNKNOWN: không xác định được<br>2. ACCOUNT: giao dịch từ tài khoản<br>3. CARD: giao dịch từ thẻ<br>4. CARD_TQT: giao dịch từ thẻ quốc tế | |
| TID | STRING | Mã định danh giao dịch. | 28743491909, 28743513851, 28744374659 |
| USER | STRING | Mã định danh người dùng (còn có thể gọi là agentid) thực hiện rút tiền. | 33938882, 4343039, 47197973 |
| AMOUNT | INT | Số tiền rút tiền. | 10000.0, 100000.0, 17000000.0, 500000.0 |
| MS_CODE | STRING | Mã lỗi của MoMo. | 1004, 3010, 9000 |
| PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi. | -1 |
| DESCRIPTION | STRING | Diễn giải ý nghĩa mã lỗi. | Chặn tổng hạn mức tối đa / ngày, Transaction is pending, Vượt hạn mức giao dịch trong ngày |
| STATUS | INT | Trạng thái của giao dịch<br>1. 1: giao dịch treo<br>2. 2: giao dịch thành công<br>3. 6: giao dịch thất bại | |
| STATUS_FINAL | INT | Trạng thái cuối cùng của giao dịch<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch chưa có trạng thái cuối | |
| G_ | STRING | Người dùng thực hiện giao dịch thuộc nhóm nào?<br>1. SIM: người dùng là sim chủ của MoMo<br>2. AUTO_MERCHANT: người dùng là đối tác<br>3. MERCHANT: người dùng là đối tác<br>4. null: là EU (end user: người dùng thật) | |
| BANK_TIME | DATETIME | Thời gian ngân hàng phản hồi lại kết quả rút tiền. | 2022-12-01 06:11:10, 2022-12-01 19:40:09, NaT |
| FINAL_TIME | DATETIME | Thời gian thật hoàn tất giao dịch rút tiền (nếu đã có status_final thì = thời gian trong core, còn chưa có status_final thì là bank_time). | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |
| LATENCY | INT | Độ trễ (số giây) trong xử lý giao dịch rút tiền (nếu đã có status_final thì = final_time - date_time, còn chưa có status_final thì là bank_time - date_time). | 0 |
| BANK_ID | STRING | Mã định danh từ ngân hàng để trace log. | None |
| PARTNER_TRACE_ID | STRING | Mã định danh 2 từ ngân hàng để trace log. | None |
| FLOW | STRING | Trạng thái của giao dịch sau khi được đối soát<br>1. MANUAL: luồng rút tiền của người dùng bình thường về ngân hàng đang liên kết<br>2. W2B: luồng đảo từ luồng w2b<br>3. AUTO_PAYOUT_TRANS: luồng tự động rút tiền của người dùng là đối tác<br>4. UNKNOWN: không xác định được luồng | |
| INQUIRY_STATUS | INT | Trạng thái của giao dịch sau khi được đối soát<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch không đối soát | |
| INQUIRY_FLOW | STRING | Gọi đối soát giao dịch từ luồng nào<br>1. momo_inquiry: MoMo chủ động gọi đối soát<br>2. partner_callback: đối tác gọi trả đối soát | |
| INQUIRY_TIME | DATETIME | Thời gian gọi đối soát lần đầu. | None |
| INQUIRY_TRY | FLOAT | Số lần gọi đối soát giao dịch. | None |
| INQUIRY_PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi sau khi đối soát | None |
| INQUIRY_TIME_LATEST | DATETIME | Thời gian gọi đối soát gần nhất. | None |

### Table 4: momovn-prod.BU_FI.BANK_CI

**Description**: Bảng này chứa thông tin về các giao dịch nạp tiền từ nguồn ngân hàng tại MoMo.

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| DATE | DATE | Ngày khởi tạo giao dịch nạp tiền từ nguồn ngân hàng. | 2022-12-01 |
| DATE_TIME | DATETIME | Ngày và giờ khởi tạo giao dịch nạp tiền từ nguồn ngân hàng. | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |
| LINKAGE | STRING | Nguồn liên kết của nguồn tiền ngân hàng đang thực hiện giao dịch nạp tiền<br>1. NAPAS: là nguồn napas<br>2. VISA: là nguồn visa<br>3. NHLK: là nguồn ngân hàng liên kết | |
| BANK_CODE | STRING | Mã ngân hàng liên kết đang thực hiện giao dịch nạp tiền. | ABB |
| LINKING_METHOD | STRING | Phương thức liên kết của nguồn được sử dụng<br>1. APP: liên kết từ app MoMo<br>2. IB (internet banking): liên kết từ app/web của ngân hàng đối tác | |
| TYPE | STRING | Giao dịch từ tài khoản gì?<br>1. IN-APP: giao dịch trên app MoMo<br>2. GATEWAY: giao dịch từ app/web đối tác<br>3. UNKNOWN: không xác định được<br>4. ACCOUNT: giao dịch từ tài khoản<br>5. CARD: giao dịch từ thẻ<br>6. IB: giao dịch từ app đối tác<br>7. CARD_TQT: giao dịch từ thẻ quốc tế<br>8. VISA-CREDIT: giao dịch từ thẻ Visa Credit<br>9. VISA-DEBIT: giao dịch từ thẻ Visa Debit<br>10. VISA-PREPAID: giao dịch từ thẻ Visa Prepaid<br>11. GATEWAY-AMERICAN EXPRESS: giao dịch từ cổng thanh toán & thẻ american express<br>12. GATEWAY-JCB: giao dịch từ cổng thanh toán & thẻ JCB<br>13. GATEWAY-VISA: giao dịch từ cổng thanh toán & thẻ Visa<br>14. GATEWAY-MASTERCARD: giao dịch từ cổng thanh toán & thẻ Mastercard<br>15. JCB-CREDIT: giao dịch từ thẻ JCB Credit<br>16. JCB-DEBIT: giao dịch từ thẻ JCB Debit<br>17. MASTERCARD-CREDIT: giao dịch từ thẻ Mastercard Credit<br>18. MASTERCARD-DEBIT: giao dịch từ thẻ Mastercard Debit<br>19. MASTERCARD-PREPAID: giao dịch từ thẻ Mastercard Prepaid | |
| TID | STRING | Mã định danh giao dịch. | 32668346071, 32668496078, 32669714366 |
| USER | STRING | Mã định danh người dùng (còn có thể gọi là agentid) thực hiện nạp tiền. | 33938882, 4343039, 47197973 |
| AMOUNT | FLOAT | Số tiền nạp tiền. | 10000.0, 100000.0, 17000000.0, 500000.0 |
| MS_CODE | STRING | Mã lỗi của MoMo. | 1004, 3010, 9000 |
| PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi. | -1 |
| DESCRIPTION | STRING | Diễn giải ý nghĩa mã lỗi. | Chặn tổng hạn mức tối đa / ngày, Transaction is pending, Vượt hạn mức giao dịch trong ngày |
| STATUS | INT | Trạng thái của giao dịch<br>1. 1: giao dịch treo<br>2. 2: giao dịch thành công<br>3. 6: giao dịch thất bại | |
| STATUS_FINAL | INT | Trạng thái cuối cùng của giao dịch<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch chưa có trạng thái cuối | |
| ISPAYMENT | STRING | Mục đích giao dịch nạp tiền dùng để làm gì?<br>1. ONLY CI: giao dịch thuần nạp tiền<br>2. CI FOR PAYMENT: giao dịch nạp tiền để thanh toán dịch vụ<br>3. CI FOR TTT: giao dịch nạp tiền để nạp tiền vào TTT (Túi Thần Tài)<br>4. CI FOR TRANSFER: giao dịch nạp tiền để chuyển tiền cho người khác<br>5. CI FOR MONEYPOOL: giao dịch nạp tiền để nạp tiền vào quỹ nhóm<br>6. null: không xác định được mục đích | |
| G_ | STRING | Người dùng thực hiện giao dịch thuộc nhóm nào?<br>1. SIM: người dùng là sim chủ của MoMo<br>2. AUTO_MERCHANT: người dùng là đối tác<br>3. null: là EU (end user: người dùng thật) | |
| EXCL | INT | Giao dịch có cần loại trừ khỏi báo cáo hay không (tùy vào góc nhìn)<br>1. 1: loại<br>2. 0: không loại | |
| IS_OTP | FLOAT | Xác định giao dịch có sử dụng OTP hay không?<br>1. 0: không<br>2. 1: có | |
| IS_AUTO_TOPUP | FLOAT | Xác định giao dịch có phải là nạp tiền tự động hay không?<br>1. 0: không<br>2. 1: có | |
| SERVICEID | STRING | Mã dịch vụ liên quan đến giao dịch nạp tiền, để xác định nạp tiền để dùng vào việc gì? | 9704, N/A, banklink_cashin, napas_cashin |
| BANK_AUTH_CODE | STRING | Phân loại loại phương thức xác thực | None |
| BANK_TIME | DATETIME | Thời gian ngân hàng phản hồi lại kết quả nạp tiền. | 2022-12-01 06:11:10, 2022-12-01 19:40:09, NaT |
| FINAL_TIME | DATETIME | Thời gian thật hoàn tất giao dịch nạp tiền (nếu đã có status_final thì = thời gian trong core, còn chưa có status_final thì là bank_time). | 2022-12-01 04:12:21, 2022-12-01 04:19:31, 2022-12-01 06:11:10 |
| LATENCY | INT | Độ trễ (số giây) trong xử lý giao dịch nạp tiền (nếu đã có status_final thì = final_time - date_time, còn chưa có status_final thì là bank_time - date_time). | 0 |
| BANK_ID | STRING | Mã định danh từ ngân hàng để trace log. | None |
| PARTNER_TRACE_ID | STRING | Mã định danh 2 từ ngân hàng để trace log. | None |
| INQUIRY_STATUS | INT | Trạng thái của giao dịch sau khi được đối soát<br>1. 2: giao dịch thành công<br>2. 6: giao dịch thất bại<br>3. null: giao dịch không đối soát | |
| INQUIRY_FLOW | STRING | Gọi đối soát giao dịch từ luồng nào<br>1. momo_inquiry: MoMo chủ động gọi đối soát<br>2. partner_callback: đối tác gọi trả đối soát | |
| INQUIRY_TIME | DATETIME | Thời gian gọi đối soát lần đầu. | None |
| INQUIRY_TRY | FLOAT | Số lần gọi đối soát giao dịch. | None |
| INQUIRY_PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi sau khi đối soát | None |
| INQUIRY_TIME_LATEST | DATETIME | Thời gian gọi đối soát gần nhất. | None |

### Table 5: momovn-prod.BU_FI.BANK_MAP_ERROR

**Description**: Bảng này chứa thông tin về các lỗi xảy ra trong quá trình liên kết ngân hàng với ví MoMo.

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| REQUEST_ID | STRING | Mã định danh duy nhất cho mỗi yêu cầu liên kết ngân hàng. | ABB106987712024-02-28 10:22:25, ABB227538812024-02-28 07:55:12, ABB457042402024-02-28 16:39:45 |
| USER | STRING | Mã định danh người dùng (còn có thể gọi là agentid) thực hiện liên kết ngân hàng. | 33938882, 4343039, 47197973 |
| PROCESS_NAME | STRING | Tên của quy trình xử lý liên kết ngân hàng<br>1. click_logo: bước chọn logo ngân hàng cần liên kết<br>2. verifyMap, verify_map_one_click: thực hiện liên kết<br>3. map, register, confirm_map_one_click: bước kết quả cuối (liên kết thành công hay thất bại) | |
| LINKAGE | STRING | Nguồn liên kết của nguồn tiền ngân hàng đang thực hiện liên kết<br>1. NAPAS: là nguồn napas<br>2. VISA: là nguồn visa<br>3. NHLK: là nguồn ngân hàng liên kết | |
| BANK_CODE | STRING | Mã ngân hàng liên kết đang thực hiện liên kết. | ABB |
| DATE | DATE | Ngày khởi tạo liên kết ngân hàng. | 2024-02-28 |
| DATE_TIME | DATETIME | Ngày và giờ khởi tạo liên kết ngân hàng. | 2024-02-28 07:55:12, 2024-02-28 10:22:25, 2024-02-28 14:14:59 |
| HOUR | INT | Giờ khởi tạo liên kết ngân hàng. | 10, 14, 16 |
| TYPE | STRING | Loại liên kết<br>1. UNKNOWN: không xác định được<br>2. ACCOUNT: tài khoản<br>3. CARD: thẻ<br>4. CARD_TQT: thẻ quốc tế | |
| MS_CODE | STRING | Mã lỗi của MoMo. | 1004, 3010, 9000 |
| PARTNER_CODE | STRING | Mã lỗi đối tác phản hồi. | -1 |
| ERROR_CATEGORY | STRING | Danh mục level 1 lỗi xảy ra trong quá trình liên kết. | SUCCESS |
| ERROR_SUB_CATEGORY | STRING | Danh mục level 2 lỗi xảy ra trong quá trình liên kết. | THÀNH CÔNG |
| DESCRIPTION | STRING | Diễn giải ý nghĩa mã lỗi. | Chặn tổng hạn mức tối đa / ngày, Transaction is pending, Vượt hạn mức giao dịch trong ngày |
| VI_DESC | STRING | Diễn giải ý nghĩa mã lỗi để show cho người dùng. | Chặn tổng hạn mức tối đa / ngày, Transaction is pending, Vượt hạn mức giao dịch trong ngày |
| FLOW | STRING | Người dùng liên kết từ luồng nào<br>1. normal: liên kết luồng bình thường<br>2. one_click: liên kết luồng một chạm<br>3. counter: liên kết dưới quầy<br>4. null: không xác định | |
| STAGE | STRING | Xác định dòng record thuộc bước nào<br>1. 01. select_map: chọn ngân hàng<br>2. 02. try_map: thực hiện liên kết<br>3. 03. success_map: kết quả liên kết thành công hay thất bại | |
| BANK_ID | STRING | Mã định danh từ ngân hàng để trace log. | None |
| PARTNER_TRACE_ID | STRING | Mã định danh 2 từ ngân hàng để trace log. | None |
| MOMO_REQUEST_ID | STRING | Mã định danh từ MoMo để trace log. | None |
| FULL_NAME | STRING | Tên người dùng thực hiện liên kết | |
| ACCOUNT_NO | STRING | Tài khoản ngân hàng/ thẻ được dùng để liên kết | |
| APP_PERSONALID | STRING | CMND/ CCCD của người dùng thực hiện liên kết | |
| INQUIRY_FLOW | STRING | Gọi đối soát từ luồng nào. | |
| INQUIRY_STATUS | FLOAT | Trạng thái sau khi được đối soát | |

### Table 6: momovn-bu-fi-shared.GOOGLE_SHEETS_IMPORT.D_BANK_ERROR

**Description**: Bảng dim để nối với các bảng BANK_CI, BANK_CO, BANK_W2B_RAW, BANK_CI_DIRECT_DEBIT để xác định category của mã lỗi & nội dung của lỗi.

| Column Name | Type | Description | Sample Values |
|-------------|------|-------------|---------------|
| error_code | STRING | Mã lỗi unique được kết hợp từ bank_code,ms_code,partner_code,function | |
| s_date | DATE | Thời gian bắt đầu có hiệu lực của bộ mã lỗi | |
| e_date | DATE | Thời gian kết thúc hiệu lực của bộ mã lỗi | |
| stt | STRING | Số thứ tự để đối chiếu với data khác, không cần quan tâm | |
| bank_id | STRING | Mã ngân hàng dạng số | |
| bank_code | STRING | Mã ngân hàng dạng chữ | |
| ms_code_old | STRING | Mã lỗi cũ của MoMo, không cần quan tâm | |
| ms_code | STRING | Mã lỗi của MoMo | |
| ms_status | STRING | Ý nghĩa mã lỗi của MoMo chia theo category<br>1. SUCCESS: thành công<br>2. FAIL: thất bại<br>3. PENDING: treo<br>4. OTP: Chờ nhập OTP | |
| ms_sub_status | STRING | Ý nghĩa mã lỗi của MoMo chia theo sub-category | |
| partner_code | STRING | Mã lỗi của đối tác | |
| function | STRING | Dịch vụ mà bộ mã lỗi áp dụng<br>1. CI: nạp tiền<br>2. CO: rút tiền<br>3. MAP: liên kết ngân hàng<br>4. UM: huỷ liên kết ngân hàng<br>5. null: dùng cho tất cả dịch vụ | |
| partner_error_category | STRING | Ý nghĩa mã lỗi của đối tác chia theo category | |
| partner_error_sub_category | STRING | Ý nghĩa mã lỗi của đối tác chia theo sub-category | |
| partner_error_category_old | STRING | Ý nghĩa mã lỗi cũ của đối tác chia theo category, không cần quan tâm | |
| partner_error_sub_category_old | STRING | Ý nghĩa mã lỗi cũ của đối tác chia theo sub-category, không cần quan tâm | |
| description | STRING | mô tả ý nghĩa bộ mã lỗi là gì | |
| vi_desc | STRING | nội dung hiển thị trên app cho người dùng nhìn thấy khi gặp bộ mã lỗi. | |
| status | STRING | tình trạng của lỗi này là gì. | |
| reason | STRING | lý do tại sao người dùng lại găp lỗi này | |

## Memory

### Business Rules and Query Guidelines

1. Để tìm số lượng giao dịch loại C D, sử dụng điều kiện regexp_contains(bank_auth_code,'C|D|CD')
2. Dùng câu lệnh SQL: REGEXP_CONTAINS(bank_auth_code, 'C|D|CD') để phân biệt loại CD trong bank_auth_code
3. Khi truy vấn số lượng khách hàng liên kết ví thành công, sử dụng mã ngân hàng 'mbb' cho cột BANK_CODE
4. Mã ngân hàng Sacombank là 'SACOM'
5. Tỉ lệ cashin thành công dưới 90% là đúng do dữ liệu báo cáo có loại giao dịch dính lỗi số dư
6. Tỷ lệ liên kết ví thành công được tính bằng: safe_divide(count(distinct case when stage = '03. success_map' then user end), count(distinct case when process_name not in ('click_logo') then user end))
7. Cần chuyển đổi DATE_TIME sang kiểu TIMESTAMP để tính toán
8. Khi lấy số lượt liên kết ví ngân hàng BIDV theo ngày, sử dụng COUNT(DISTINCT request_id) thay vì COUNT(DISTINCT USER)
9. Khi người dùng hỏi về loại giao dịch CD thì có nghĩa là đang đề cập tới cột bank_auth_code trong bảng BANK_CI
10. Khi tính tỉ lệ nạp tiền thành công, thêm điều kiện ci.LINKAGE = 'NHLK'
11. Bank code EXIM
12. Để lấy số tiền giao dịch loại CD của ngân hàng MBB, sử dụng mã REGEXP_CONTAINS(BANK_AUTH_CODE, 'C|D|CD')
13. Mã ngân hàng Vietinbank là 'VTB'
14. Khi tính tỉ lệ nạp tiền thành công, sử dụng cột STATUS_FINAL thay vì STATUS
15. Khi tính tỉ lệ nạp tiền thành công, sử dụng cột BANK_CODE thay vì BANK_NAME
16. Cột thời gian trong bảng BANK_CO là DATE_TIME, không phải DATETIME
17. Loại bỏ lỗi có partner_error_sub_category/ms_sub_status = 'FAIL - SỐ DƯ' khi tính tỷ lệ giao dịch nạp tiền ngân hàng liên kết thành công
18. Trong tháng 7 năm 2025, có 32 ngân hàng liên kết hoạt động

## Notes

This dataset contains critical financial operations data for MoMo's bank partnership services, including:

- **W2B Transactions**: Wallet-to-bank transfers with detailed transaction tracking
- **Direct Debit**: High-limit direct debit transactions from banks to MoMo wallets
- **Cash Out (CO)**: Bank withdrawal transactions with reconciliation data
- **Cash In (CI)**: Bank deposit transactions with comprehensive error tracking
- **Bank Mapping Errors**: Bank linking process error tracking and categorization
- **Error Code Mapping**: Dimension table for error code categorization and descriptions

All data maintains Vietnamese business terminology and includes comprehensive memory rules for query optimization and business logic implementation.