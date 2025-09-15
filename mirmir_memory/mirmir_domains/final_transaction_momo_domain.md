# Transaction MoMo

## Dataset Information

**Dataset ID:** e5beb7b6-4273-47ff-9755-a5bcf8d51b97

**Dataset Name:** Transaction MoMo

**Description:** Lưu trữ thông tin cơ bản các giao dịch của ví điện tử MoMo

**Instructions:**

**Error Code:** 200

## Schema Information

### Table 1: momovn-mimir.MIMIR.iDeA_TRANS_CORE

**Description:** Bảng iDeA_TRANS_CORE của MIMIR chứa thông tin chi tiết về các giao dịch khác nhau được thực hiện thông qua MoMo. Những thông tin này bao gồm mã giao dịch, ngày giao dịch, mã định danh người dùng, và các loại giao dịch.
- Ghi nhận chi tiết các giao dịch thực hiện trên nền tảng.
- Theo dõi số tiền giao dịch và số tiền voucher áp dụng.
- Phân loại giao dịch dựa trên loại hình và nguồn tiền sử dụng.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| tranid | Mã định danh duy nhất của giao dịch. | 69209883114, 81839872026, 81894008971 |
| date | Ngày diễn ra giao dịch. | 2024-10-10, 2025-06-10, 2025-01-10 |
| user_id | Mã định danh của người dùng thực hiện giao dịch. | 72926319, 58549182, 98383901 |
| usecase | Trường hợp sử dụng hoặc mục đích của giao dịch. | CASHIN BANK, P2P - EWALLET TO EWALLET, P2P - EWALLET TO BANK, MONEY MARKET FUNDS, AIRTIME, LOGISTICS, PAYLATER, APPLICATION STORE, CASHOUT BANK, DATA, UTILITIES, MARKETPLACE, RETAIL, SME OFFLINE, FI SOLUTIONS, DIGITAL CONTENT, ADS PAYMENT, FNB, GAME, CINEMA, PUBLIC SERVICE, OTT, OTA, INSURANCE, PAID CASHIN, CREDIT CARD MARKETPLACE, INVESTMENT PRODUCT, INBOUND REMITTANCE, CASHIN OTC AGENT, DEVICE FINANCING, CASHOUT OTC AGENT |
| transaction_type | Loại giao dịch được thực hiện, ví dụ: chuyển tiền, thanh toán hóa đơn, etc. | PAYMENT, CASHIN, TRANSFER, CASHOUT, MONEY DISBURSEMENT |
| merchant | Mã định danh của điểm chấp nhận MoMo hoặc nhà cung cấp liên quan đến giao dịch. |  |
| transaction_amount | Số tiền giao dịch được thực hiện. | 100000, 50000, 10000 |
| voucher_amount | Số tiền được giảm giá bằng voucher áp dụng trong giao dịch. | 0, 10000, 5000 |
| source_of_fund | Nguồn tiền được sử dụng trong giao dịch, ví dụ: tài khoản ngân hàng, ví MoMo. | NHLK,  Ví Momo, TTT, undefined, Ví Momo, VTS, Napas, Visa Credit, Visa Debit |

### Table 2: momovn-mimir.MIMIR.iDeA_TRANS_DEMOGRAPHIC

**Description:** Bảng chứa thông tin nhân khẩu học liên quan đến giao dịch của người dùng, bao gồm mã định danh, thành phố và nhóm thành phố của người dùng. Có thể sử dụng bảng để phân tích hành vi của người dùng theo độ tuổi và địa lý, nghiên cứu xu hướng giao dịch dựa trên nhân khẩu học, tạo các phân khúc tiếp thị hiệu quả theo độ tuổi và địa lý.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| user_id | Mã định danh của người dùng. | 59086927, 77916136, 57322300 |
| city | Thành phố nơi người dùng cư trú. | Hồ Chí Minh, Hà Nội, Bình Dương |
| city_group | Nhóm thành phố nơi người dùng cư trú, phân loại theo tiêu chuẩn nhất định. | Thành Phố Hồ Chí Minh, Tỉnh khác, Hà Nội, KCN Miền Nam, KCN Miền Bắc, TP Lớn, TP Du lịch |
| age | Tuổi của người dùng. | 22, 21, 20 |
| age_group | Nhóm tuổi của người dùng, thường được phân loại theo độ tuổi nhất định. | [2].18-22, [4].28-35, [3].23-27, [5].36-50, [1].<18 , [6].>50 |

## Memory

**Memory Entry 1:**
Tên thành phố 'dongnai' tương ứng với LOWER(t2.city) = 'đồng nai'

**Memory Entry 2:**
MoMo nay đã là trợ thủ tài chính với AI, không còn là ví điện tử

**Memory Entry 3:**
Giao dịch P2P (Peer-to-Peer) là giao dịch chuyển tiền trực tiếp giữa hai người dùng cá nhân với nhau, không thông qua một bên trung gian truyền thống như ngân hàng. Các loại giao dịch khác thường liên quan đến việc thanh toán cho hàng hóa, dịch vụ, hoặc các giao dịch với doanh nghiệp/tổ chức.

**Memory Entry 4:**
A30 active user: người dùng thực hiện ít nhất một giao dịch trong vòng 30 ngày gần nhất.

**Memory Entry 5:**
Khi đếm số lượng giao dịch, sử dụng count(distinct t1.tranid)