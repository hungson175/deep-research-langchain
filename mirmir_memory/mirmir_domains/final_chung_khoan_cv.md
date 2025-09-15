# Chứng khoán CV

## Error Code
200

## Data

### Basic Information
- **ID**: ef8cc111-d13a-4b0b-a1fd-8cccb065fc74
- **Name**: Chứng khoán CV
- **Description**: Hỏi về thông tin đăng ký tài khoản, giao dịch chứng khoán và traffic user.
- **Instructions**: (empty)

### Schema DDL

**Dataset name**: Chứng khoán CV

#### Table 1: momovn-cvs.BU_CVS.MIMIR_CVS_TRANSACTION

**Description**: Bảng data chứa toàn bộ giao dịch người dùng sản phẩm Chứng khoán CV (cũng hay gọi tắt là CVS). Bảng này có thể dùng độc lập để tra cứu giao dịch trading của user. Ngoài ra cũng có thể mapping bằng cột AGENT_ID với bảng KHÁC để tìm ra hành vi user. Các dữ liệu khảo sát trong bảng bao gồm loại giao dịch, tài khoản chứng khoán, thời gian và trạng thái giao dịch, cùng với số lượng và giá trị giao dịch.

**Columns**:
- **TRANS_CATE**: Loại giao dịch record: "MONEY" là giao dịch nạp/ rút tiền, "STOCK" là lệnh đặt mua/ bán chứng khoán.

- **AGENT_ID**: Mã định danh của khách hàng trên ứng dụng MoMo, đây là khóa chính dùng để mapping các bảng với nhau.

- **ACCO_NAME**: Loại tài khoản chứng khoán user thao tác nạp/ rút tiền, đặt lệnh mua/ bán chứng khoán: "CASH" là tài khoản tiền mặt, chỉ dùng tiền mặt để mua; "MARGIN" là tài khoản margin, có thể dùng tiền mượn để mua chứng khoán.

- **TRADE_MONTH**: Tháng giao dịch, lưu với giá trị 01 đầu mỗi tháng, thời điểm giao dịch có thể rơi vào tháng trước nhưng được hạch toán vào ngày giao dịch nào sau đó.

- **TRADE_DATE**: Ngày giao dịch, lưu ý các lệnh có thể được đặt trước và rơi vào tháng trước nhưng được hạch toán vào ngày giao dịch thực tế.

- **CREATE_TIME**: Đối với giao dịch "MONEY" là thời gian user thực hiện giao dịch, còn giao dịch "STOCK" là thời gian user đặt lệnh. Định dạng theo GMT+7.

- **CONFIRM_TIME**: Thời gian lệnh đó được xác nhận. Định dạng theo GMT+7.

- **TRANS_ID**: Mã giao dịch/ đặt lệnh, thường dùng để đếm số lượng giao dịch/ đặt lệnh.

- **STATUS_NAME**: Đối với giao dịch "MONEY" có giá trị "Đã duyệt" là thành công, các giá trị khác là chưa thành công; giao dịch "STOCK" có các giá trị thành công là "Khớp hết" và "Khớp 1 phần".

- **TRANS_TYPE**: Loại giao dịch: Đối với "MONEY", "CASH_IN" là nạp tiền và "CASH_OUT" là rút tiền; đối với "STOCK", "BUY" là mua và "SELL" là bán chứng khoán.

- **MONEY_SOURCE_RECEIPT**: Chỉ có giá trị nếu TRANS_CATE = "MONEY": Nguồn tiền user nạp vào tài khoản chứng khoán (nếu TRANS_TYPE = "CASH_IN") hoặc đích tài khoản rút tiền ra (nếu TRANS_TYPE = "CASH_OUT").

- **AMOUNT**: Giá trị nạp/ rút tiền hoặc giá trị khớp lệnh giao dịch mua/ bán chứng khoán.

- **MAT_QTY**: Số lượng cổ phiếu khớp lệnh (mua/ bán).

- **ORD_QTY**: Số lượng cổ phiếu đặt lệnh ban đầu.

- **ORD_PRICE**: Giá đặt lúc mua cổ phiếu.

- **FEE_AMT**: Phí giao dịch mua/ bán chứng khoán.

- **STOCK_CD**: Mã cổ phiếu.

- **TRADE_LOT_TYPE**: Loại giao dịch lô cổ phiếu: "Lô chẵn" hay "Lô lẻ".

- **MAU**: Phân loại người dùng có thực hiện giao dịch nạp/rút tiền (thành công) trong tháng theo hành vi.

- **MTU**: Phân loại người dùng có thực hiện giao dịch đặt và khớp lệnh mua/bán chứng khoán thành công trong tháng theo hành vi.

**Data Example**: Empty DataFrame
Columns: [TRANS_CATE, AGENT_ID, ACCO_NAME, TRADE_MONTH, TRADE_DATE, CREATE_TIME, CONFIRM_TIME, TRANS_ID, STATUS_NAME, TRANS_TYPE, MONEY_SOURCE_RECEIPT, AMOUNT, MAT_QTY, ORD_QTY, ORD_PRICE, FEE_AMT, STOCK_CD, TRADE_LOT_TYPE, MAU, MTU]
Index: []

#### Table 2: momovn-cvs.BU_CVS.CVS_USER_REGISTER

**Description**: Bảng data chứa thông tin user đăng ký tài khoản Chứng khoán CV (CVS). Bảng lưu trữ thời gian user SUBMIT (đăng ký register) và thời gian được duyệt tài khoản.

Thông tin có thể lấy từ bảng này bao gồm:
- Mã định danh của khách hàng trên ứng dụng MoMo thông qua AGENT_ID.
- Thời gian user submit đơn đăng ký tài khoản CVS và thời điểm tài khoản được duyệt.
- Thông tin thời gian phê duyệt tiểu khoản CASH và MARGIN trên tài khoản CVS.

**Columns**:
- **AGENT_ID**: Mã định danh của khách hàng trên ứng dụng MoMo, đây khóa chính dùng để mapping các table với nhau.

- **USER_SUBMIT_TIME**: Thời gian user submit đơn đăng ký tài khoản CVS. Tài khoản sẽ được duyệt sau đó. Tuy nhiên nếu xét hành vi đăng ký thì nên lấy thời gian này. Định dạng DATETIME theo GMT+7.

- **USER_REGISTER_TIME**: Thời gian user được duyệt tài khoản Chứng khoán CV.

- **CASH_REGISTER_TIME**: Thời gian user được duyệt tiểu khoản CASH trên tài khoản CVS.

- **MARGIN_REGISTER_TIME**: Thời gian user được duyệt tiểu khoản MARGIN trên tài khoản CVS.

**Data Example**:
```
   AGENT_ID        USER_SUBMIT_TIME  USER_REGISTER_TIME  CASH_REGISTER_TIME MARGIN_REGISTER_TIME
0  42050727 2024-07-22 01:15:20.546 2024-07-22 08:06:10 2024-07-22 08:06:10  2025-03-22 17:05:40
1  44440929 2024-07-22 01:13:45.584 2024-07-22 08:06:28 2024-07-22 08:06:28  2025-03-22 01:29:06
2  55928840 2024-07-22 08:13:31.739 2024-07-22 08:14:01 2024-07-22 08:14:01  2025-05-19 08:56:51
3  73813700 2024-07-22 08:32:17.707 2024-07-22 08:43:39 2024-07-22 08:43:39  2025-03-05 19:00:13
4  92703525 2024-07-22 08:41:59.873 2024-07-22 08:44:27 2024-07-22 08:44:27  2025-03-24 02:16:49
```

### Knowledge Base
(empty)

### Memory

1. **Memory ID**: 5f8a2726-9666-4f7b-b5fd-819ccb9806f8
   - **Content**: Màn hình Home có screen_name = 'stock_home'
   - **Hash**: a766bc0513fcfea92aaf68e988e4d600
   - **User**: Chứng khoán CV
   - **Created**: 2025-07-16T03:35:33.616060-07:00

2. **Memory ID**: 0e6496bc-5bbd-4fd2-b619-00160ca4d064
   - **Content**: Xem stock_detail có nghĩa là VIEW SCREEN với screen_name = 'stock_detail'
   - **Hash**: a3cd60d073aef47a3f38470280d41706
   - **User**: Chứng khoán CV
   - **Created**: 2025-07-16T03:26:16.170340-07:00

## Error Message
(empty)