# CEE USER SUGGESTIONS

## Dataset Information

**Dataset ID:** 20e405eb-5b2b-4a23-bacc-35196c4e707d

**Dataset Name:** CEE USER SUGGESTIONS

**Description:** The dataset records information about user suggestions received through Feedback Feature in all CS channel

**Instructions:** (Not provided)

**Error Code:** 200

## Schema Information

### Table 1: momovn-cee-shared.CEE_MAIL.FF_CONTENTS_V2

**Description:** The dataset records information about user suggestions received through Feedback Feature channel

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| created_date | Ngày ghi nhận ticket được tạo | 2025-05-07 |
| bu | Business Unit được phân cho ticket | Xác thực ví |
| service_plus | Phân loại dịch vụ góp ý | Xác Thực eKYC Và TT23 |
| ticket_id | mã phản ánh / ID của ticket | 250112.0000718 |
| source | Nguồn gửi góp ý | Feedback Feature |
| level2 | Level 2 của ticket góp ý | Tài Khoản |
| level3 | Level 3 của ticket góp ý | Xác Thực eKYC Và TT23 |
| category | Phân loại category góp ý | Góp ý khác |
| contents | Nội dung góp ý của khách hàng kèm Ticket ID | nên cho nhiều lì xì hơn (Ticket ID: 250112.0000718) |

### Sample Data Records

1. **2025-05-07** - Xác thực ví - Xác Thực eKYC Và TT23 - 250112.0000718 - Feedback Feature - Tài Khoản - Xác Thực eKYC Và TT23 - Góp ý khác
   Content: nên cho nhiều lì xì hơn (Ticket ID: 250112.0000718)

2. **2025-04-05** - Thu hộ vay tiêu dùng - Thu hộ vay tiêu dùng - 250430.0002956 - FAQs - Tính Năng - Paylater - Góp ý về tính năng
   Content: tránh gian lận và mất uy tín từ MoMo (Ticket ID: 250430.0002956)

3. **2025-05-19** - Ví Trả Sau - Ví Trả Sau - 250116.0003735 - Email - Tài Chính - Bảo Hiểm - Thu hộ vay tiêu dùng - Góp ý về vận hành sản phẩm
   Content: không có nhu cầu dùng những ưu đãi này và những phần quà ttương tự. đã nhiều lần phản ánh rồi \ntặng ra tặng chứ đừng như kiểu gài, cho 50k với điều kiện bỏ ra hơn 50k, khôn vậy dưới xóm khoá mỗm xích lại hết rồi.\nđừng gửi dùm thêm (Ticket ID: 250116.0003735)

4. **2025-04-14** - Chuyển tiền đến Ngân hàng - Chuyển tiền đến Ngân hàng - 250122.0009356 - None - Chi hộ vay tiêu dùng - Captcha Puzzle - Góp ý về chính sách sản phẩm
   Content: thêm nhiều voucher giảm tiền điện, nước (Ticket ID: 250122.0009356)

5. **2025-05-05** - Online Payments - Promotion - 241226.0000914 - None - Chuyển Nhận Tiền - Quỹ nhóm - Money Pool - None
   Content: Phần thông báo "lưu thẻ thành công" đè lên 2 chức năng "bỏ-lưu", phải chờ thông báo này tắt đi mới bấm lưu tiếp được. Gây bất tiện, cũng như mất thời gian cho người dùng. Mong đội ngũ dev thiết kế lại phần này. (Ticket ID: 241226.0000914)

## Memory Guidelines

The dataset includes the following memory guidelines for query processing:

1. **Content Summarization**: Khi được yêu cầu tóm tắt nội dung, hay lấy ngẫu nhiên các contents khoảng 50 dòng, NO LIMIT 10. Rồi đọc các contents sau đó mới tóm tắt

2. **Agent and Request Information**: Không có thông tin về agent_id và request_id trong bảng ghi nhận góp ý của người dùng

3. **General Analysis**: Khi được hỏi về tổng quát, nhận định. Thì hãy lấy toàn bộ thông tin trong cột contents của bu đó. Sao đó đọc và đưa ra tổng quát, nhận định

4. **Data Scope**: Dữ liệu chỉ chứa thông tin về góp ý của người dùng, không có thông tin về ticket và CSAT của dịch vụ

5. **Source Filtering**: Khi user hỏi data từ nguồn ứng dụng thì lấy source = 'FAQs', không phải 'Feedback Feature'

6. **Available BU Values**:
   - Cinema, MoMo Reward + Student Pass, SOF, VTTI Billpay - VTTI Public service, Chi hộ vay tiêu dùng, Thu hộ vay tiêu dùng, Donation, Quỹ nhóm, Túi Thần Tài, QR nhận tiền, Quản lý tài khoản, Bank Partnership, Online Payments, Quản lý chi tiêu, Chuyển tiền đến Ngân hàng, Xác thực ví, Chuyển/nhận tiền Ví - Ví và các dịch vụ khác, Quản lý Ví & Phản ánh lừa đảo, Marketing Platform, OTA, Promotion, Mua Bảo hiểm & Thanh toán Bảo hiểm, VTTI Data - VTTI Airtime, Hạn mức ví, Hủy Ví, Lịch sử/ chi tiết giao dịch, EPS, Chứng khoán, SPS, Điểm tin cậy MoMo, CCM, Tiết kiệm online, App performance

7. **Available Level2 Values**:
   - Du Lịch - Đi Lại, Tính Năng, VTTI, Tài Chính - Bảo Hiểm, Chuyển Nhận Tiền, Tài Khoản, Liên Kết/ Nạp Rút Ngân Hàng, Payment Online - Digital Platform, Quản lý chi tiêu, Chương Trình Khuyến Mãi, Payment Offline - Miniapp MoMo, Merchant Care

   **Note**: Nếu bị hỏi thông tin bên ngoài các giá trị này thì phải confirm lại với user, và suggest user các dịch vụ liên quan.