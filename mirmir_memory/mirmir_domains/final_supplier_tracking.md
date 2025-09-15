# Supplier Tracking Domain Response

## Error Code
200

## Data

### ID
0c367c81-99d6-4b01-90e2-e7bab0b77677

### Name
SUPPLIER TRACKING

### Description
Theo dõi performance của các nhà cung cấp Telco

### Instructions
(empty)

## Schema DDL

### Dataset Name
SUPPLIER TRACKING

### Table Name
`project-5400504384186300846.BU_UTILITIES_TELCO.TELCO_WAREHOUSE_ARGG_ALL`

### Table Description
Bảng này lưu trữ thông tin chi tiết về các giao dịch viễn thông thông qua MoMo. Đây là bảng fact, giúp cung cấp thông tin về ngày phát sinh giao dịch, nhà mạng, dịch vụ và tổng số tiền phát sinh của các giao dịch viễn thông.

**Các thông tin có thể lấy từ bảng này gồm:**
- Theo dõi số lượng giao dịch theo ngày và nhà mạng.
- Phân loại các dịch vụ viễn thông và thống kê dịch vụ nào được sử dụng nhiều nhất.
- Tính toán tổng số tiền phát sinh theo nhóm dịch vụ.

### Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `date` | DATE | Ngày phát sinh giao dịch |
| `cate` | STRING | Nhà mạng của giao dịch |
| `group_service` | STRING | Group dịch vụ của giao dịch: Topup&Mathe = Airtime, 3G/4G = Data |
| `service_code` | STRING | Service code của giao dịch |
| `service` | STRING | Loại dịch vụ. TOPUP: dịch vụ topup, MATHE: dịch vụ mã thẻ, COMBO: dịch vụ data combo, SIM: dịch vụ sim, OTHER: Dịch vụ khác |
| `supplier` | STRING | Nhà cung cấp của giao dịch |
| `menh_gia` | STRING | Mã sản phẩm của giao dịch |
| `amount` | FLOAT | Tổng số tiền phát sinh |
| `quantity` | INTEGER | Tổng số lượng mã sản phẩm |

### Smart Top Values

#### Distinct values for `cate`:
['Vnsky' 'Local' 'Viettel' 'Vietnamobile' 'Vinaphone' 'Saymee' 'Gmobile' 'Xplori' 'OTHER' 'Wintel' 'Gohub' 'itel' 'Reddi' 'Mobifone' 'VNSKY']

#### Distinct values for `supplier`:
['VIETTEL DIRECT' 'MEGATEK' 'EWAVE' 'IMD' 'ASIM' 'VMG/IMEDIA' 'GOHUB' 'WHYPAY' 'Vietnamobile' 'Viettel' 'WINTEL' 'Vinaphone' 'VIETNAMOBILE' 'EPAY' 'Gmobile' 'MOBICAST' 'VIEN PHUONG NAM' 'OCTA/LOGICH' 'IO MEDIA' 'Mobifoneplus' 'XPLORI' 'Mobifone' 'ZOTA/FIVI' 'VIETTEL' 'MobiPlus' 'IMEDIA' 'PHUONG QUAN' 'Mservice' 'My data' 'VNSKY']

#### Distinct values for `group_service`:
['Topup&Mathe' '3G/4G']

#### Distinct values for `service`:
['MATHE' 'COMBO' 'OTHERS' 'TOPUP' 'SIM']

## Knowledgebase
(empty)

## Memory
(empty)

## Error Message
(empty)