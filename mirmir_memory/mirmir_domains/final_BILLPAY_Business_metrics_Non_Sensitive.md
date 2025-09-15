# BILLPAY - Business metrics (Non Sensitive)

## Basic Information

**Error Code:** 200
**Data ID:** f9ccec9b-d24b-47b8-9e81-1805aa865726
**Name:** BILLPAY - Business metrics (Non Sensitive)

## Description

Records all business information of Billpay services (including mau, transaction details, user demographics, etc.)

## Instructions

## Schema DDL

```
###Dataset name: BILLPAY - Business metrics (Non Sensitive) ---

## Table information : {"schema_ddl":"{'table_name': 'project-5400504384186300846.BU_UTILITIES_TELCO.MIMIR_BILLPAY_DETAILS', 'table_desc': 'Bảng này thuộc dự án MIMIR và chứa thông tin chi tiết về các giao dịch thanh toán hóa đơn qua MoMo trong lĩnh vực tiện ích. Dữ liệu trong bảng này bao gồm tháng hoạt động của người dùng, ngày giao dịch, số lượng và giá trị giao dịch, thông tin về nhà cung cấp dịch vụ cũng như thông tin chi tiết về người dùng như độ tuổi, giới tính, và hành vi sử dụng. Bảng này có thể được sử dụng để:\\n - Phân tích các mẫu thanh toán hóa đơn của người dùng theo thời gian.\\n - Đánh giá hiệu quả của các chiến dịch sử dụng voucher khuyến mãi.\\n - Phân tích đặc điểm nhân khẩu học của người dùng dựa trên địa điểm, độ tuổi và giới tính.\\n - Tính toán doanh thu thuần từ các giao dịch của các nhà cung cấp dịch vụ tiện ích.', 'column_desc': [{'column_name': 'month_active', 'description': 'Tháng mà người dùng thực hiện thanh toán.\\n ', 'children': []}, {'column_name': 'date', 'description': 'Ngày diễn ra giao dịch.\\n ', 'children': []}, {'column_name': 'user_id', 'description': 'ID duy nhất của người dùng.\\n ', 'children': []}, {'column_name': 'subcategory', 'description': 'Danh mục dịch vụ: \"DIEN\" - Điện, \"NUOC\" - Nước, \"INTERNET\" - Internet, \"TRUONG HOC\" - trường học.\\n ', 'children': []}, {'column_name': 'merchant', 'description': 'Tên nhà cung cấp dịch vụ.\\n ', 'children': []}, {'column_name': 'transaction_count', 'description': 'Số lượng giao dịch đã thực hiện.\\n ', 'children': []}, {'column_name': 'amount', 'description': 'Số tiền của các giao dịch (đơn vị: VND).\\n ', 'children': []}, {'column_name': 'voucher_amount', 'description': 'Số tiền được chiết khấu nhờ sử dụng voucher.\\n ', 'children': []}, {'column_name': 'voucher_or_not', 'description': 'Cho biết người dùng có sử dụng voucher hay không: \"Voucher\" - có sử dụng voucher, \"Non voucher\" hoặc \"Non_voucher\" - không sử dụng voucher cho giao dịch cụ thể đó.\\n ', 'children': []}, {'column_name': 'revenue', 'description': 'Doanh thu công ty chúng tôi thu được từ các giao dịch.\\n ', 'children': []}, {'column_name': 'user_type', 'description': 'Phân khúc người dùng (theo lĩnh vực thanh toán hóa đơn): \"retain_user\" - người dùng thanh toán trong 2 tháng liên tiếp, \"new_user\" - người dùng thanh toán lần đầu tiên trong tháng, \"churn_user\" - người dùng không thanh toán tháng trước nhưng quay lại thanh toán trong tháng.\\n ', 'children': []}, {'column_name': 'user_type_sub', 'description': 'Phân khúc người dùng theo danh mục dịch vụ.\\n ', 'children': []}, {'column_name': 'user_type_mer', 'description': 'Phân khúc người dùng theo nhà cung cấp dịch vụ.\\n ', 'children': []}, {'column_name': 'region', 'description': 'Vùng miền của địa điểm của người dùng.\\n ', 'children': []}, {'column_name': 'city_group', 'description': 'Nhóm thành phố của địa điểm của người dùng.\\n ', 'children': []}, {'column_name': 'city', 'description': 'Tên thành phố trong địa chỉ của người dùng.\\n ', 'children': []}, {'column_name': 'age', 'description': 'Tuổi của người dùng (null nghĩa là không biết).\\n ', 'children': []}, {'column_name': 'age_group', 'description': 'Nhóm tuổi của người dùng.\\n ', 'children': []}, {'column_name': 'gender', 'description': 'Giới tính của người dùng.\\n ', 'children': []}, {'column_name': 'login_app_count', 'description': 'Số lần người dùng đăng nhập vào ứng dụng di động của chúng tôi.\\n ', 'children': []}, {'column_name': 'login_billpay_center_count', 'description': 'Số lần người dùng đăng nhập vào trung tâm dịch vụ thanh toán hóa đơn trong ứng dụng di động của chúng tôi.\\n ', 'children': []}, {'column_name': 'display_xbanner_count', 'description': 'Số lần người dùng thấy xbanner của chúng tôi. Xbanner là banner nhắc nhở nợ mà chúng tôi hiển thị cho người dùng trong ứng dụng khi đến ngày đáo hạn.\\n ', 'children': []}, {'column_name': 'click_xbanner_count', 'description': 'Số lần người dùng nhấp vào xbanner của chúng tôi.\\n ', 'children': []}]}","smart_top_value":"- Distinct value `gender` là ['male' 'female' 'unknown']\n- Distinct value `age_group` là ['[1].<18 ' '[5].36-50' '[6].>50' '[2].18-22' 'unknown' 'others'\n '[4].28-35' '[3].23-27']\n- Distinct value `user_type_mer` là ['new_user' 'recover_user' 'retain_user' 'unknown']\n- Distinct value `user_type` là ['new_user' 'recover_user' 'retain_user' 'unknown']\n- Distinct value `user_type_sub` là ['new_user' 'retain_user' 'recover_user' 'unknown']\n- Distinct value `voucher_or_not` là ['Non_voucher' 'Voucher']\n- Distinct value `subcategory` là ['OTHER SERVICE' 'DIEN' 'Y TE' 'TRUONG HOC' 'NUOC' 'CHUNG CU' 'XANG DAU'\n 'OTHER' 'INTERNET' 'HCC' 'MOI TRUONG' 'TRUYEN HINH' 'PHI KHONG DUNG'\n 'VAN TAI' 'DIEN THOAI TRA SAU']"}}
```

## Knowledgebase

[]

## Memory

[]