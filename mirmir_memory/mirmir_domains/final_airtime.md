# Airtime

## Basic Information

**Error Code:** 200
**Data ID:** 3165cb58-8f0a-4c7d-96e6-ae0b189ff572
**Name:** Airtime

## Description

records all transaction (exclude blacklist user), demographic, user segment of Airtime Service since 2021

## Instructions

## Schema DDL

```
###Dataset name: Airtime ---
```

## Tables

### Table 1: AIRTIME_SEGMENT_USER

**Table Name:** `project-5400504384186300846.BU_UTILITIES_TELCO.AIRTIME_SEGMENT_USER`

**Description:** Bảng này ghi nhận dữ liệu về người dùng trong lĩnh vực dịch vụ viễn thông tiện ích. Dữ liệu bao gồm thông tin về các phân đoạn người dùng, chuyển đổi trạng thái người dùng, và các thông số liên quan đến các giao dịch, khuyến mãi, và loại đối tác. Có thể sử dụng bảng này để:
 - Phân tích sự giữ chân và sự chuyển đổi của người dùng trong lĩnh vực dịch vụ viễn thông.
 - Đánh giá hiệu quả của từng loại khuyến mãi dựa trên GMV và số lượt giao dịch.
 - Xác định phân loại đối tác và cách thức tác động lên người dùng.

**Columns:**

| Column Name | Description |
|------------|-------------|
| `month_active` | Tháng mà người dùng hoạt động. |
| `reference` | Tham chiếu liên quan đến người dùng hoặc giao dịch. |
| `month_lead` | Tháng dẫn đầu về hoạt động của người dùng. |
| `retain` | Tháng giữ chân người dùng. |
| `month_churn` | Tháng mà người dùng chuyển đổi hoặc rời bỏ. |
| `user_segment` | Phân đoạn của người dùng dựa trên hoạt động hoặc tương tác. |
| `churn_user` | Trạng thái chuyển đổi của người dùng (ví dụ: đã rời bỏ). |
| `churn_duration` | Thời gian người dùng đã chuyển đổi hoặc rời bỏ, tính bằng ngày. |
| `FIRST_DATE` | Ngày đầu tiên ghi nhận hoạt động của người dùng. |
| `LAST_DATE` | Ngày cuối cùng ghi nhận hoạt động của người dùng. |
| `CHURN_DURATION_DAY` | Số ngày người dùng đã chuyển đổi trạng thái hoặc rời bỏ. |
| `TRANS` | Số lượng giao dịch hiện tại của người dùng. |
| `PREVIOUS_TRANS` | Số lượng giao dịch trước đó của người dùng. |
| `GMV` | Giá trị tổng của tất cả giao dịch hiện tại. |
| `PREVIOUS_GMV` | Giá trị tổng của tất cả giao dịch trước đó. |
| `PROMOTION_COST` | Chi phí dành cho khuyến mãi trong thời gian hiện tại. |
| `PREVIOUS_VC_AMOUNT` | Giá trị của voucher đã sử dụng trước đó. |
| `VOUCHER_TYPE_BY_GMV` | Loại voucher dựa trên giá trị giao dịch hiện tại. |
| `PREVIOUS_VOUCHER_TYPE_BY_GMV` | Loại voucher dựa trên giá trị giao dịch trước đó. |
| `VOUCHER_TYPE_BY_TRANS` | Loại voucher dựa trên số lượng giao dịch hiện tại. |
| `PREVIOUS_VOUCHER_TYPE_BY_TRANS` | Loại voucher dựa trên số lượng giao dịch trước đó. |
| `GMV_TYPE` | Loại giá trị giao dịch hiện tại, có thể là GMV. |
| `PREVIOUS_GMV_TYPE` | Loại giá trị giao dịch trước đó. |
| `partner_type` | Loại đối tác có liên quan đến giao dịch. |
| `num_service` | Số lượng dịch vụ mà người dùng đã sử dụng. |
| `first_tid` | Mã định danh của giao dịch đầu tiên. |

**Smart Top Values:**
```json
{
  "first_tid": ["74871272201", "73969606163", "74459637097"],
  "PREVIOUS_VOUCHER_TYPE_BY_TRANS": ["TRANS MORE ORGANIC", "GMV MORE ORGANIC", "TRANS MORE VOUCHER", "ONLY ORGANIC", "GMV MORE VOUCHER", "ONLY VOUCHER"],
  "num_service": ["9", "18", "15"],
  "partner_type": ["owner_partner", "mathe_partner", "only_partner", "only_mathe", "mathe_owner_partner", "mathe_owner", "only_owner"],
  "GMV_TYPE": ["9. 5TR+", "7. 1TR - 3TR", "8. 3TR - 5TR", "2. 30K - 50K", "6. 500K - 1TR", "5. 200K - 500K", "3. 50K - 100K", "1. 0 - 30K", "4. 100K - 200K"],
  "VOUCHER_TYPE_BY_TRANS": ["TRANS MORE ORGANIC", "TRANS MORE VOUCHER", "ONLY ORGANIC", "ONLY VOUCHER"],
  "PREVIOUS_VC_AMOUNT": ["513000", "35600", "24600"],
  "PREVIOUS_GMV_TYPE": ["9. 5TR+", "7. 1TR - 3TR", "8. 3TR - 5TR", "2. 30K - 50K", "6. 500K - 1TR", "5. 200K - 500K", "4. 100K - 200K", "1. 0 - 30K", "3. 50K - 100K"],
  "PROMOTION_COST": ["720000", "6200", "24600"],
  "VOUCHER_TYPE_BY_GMV": ["GMV MORE ORGANIC", "ONLY ORGANIC", "GMV MORE VOUCHER", "ONLY VOUCHER"],
  "PREVIOUS_VOUCHER_TYPE_BY_GMV": ["GMV MORE ORGANIC", "ONLY ORGANIC", "GMV MORE VOUCHER", "ONLY VOUCHER"],
  "PREVIOUS_TRANS": ["442", "340", "267"],
  "PREVIOUS_GMV": ["2050000", "1830000", "3570000"],
  "TRANS": ["210", "804", "1097"],
  "GMV": ["720000", "7320000", "58800"],
  "CHURN_DURATION_DAY": ["183", "304", "700"],
  "LAST_DATE": ["2020-08-16", "2022-03-02", "2019-10-28"],
  "churn_duration": ["9", "18", "58"],
  "churn_user": ["churn", "retain"],
  "FIRST_DATE": ["2020-12-26", "2024-05-12", "2019-11-29"],
  "user_segment": ["retain_user", "new_user", "recover_user"],
  "retain": ["2017-08-01", "2021-05-01", "2018-09-01"],
  "month_churn": ["2017-08-01", "2021-05-01", "2018-09-01"],
  "month_active": ["2017-08-01", "2021-05-01", "2018-09-01"],
  "month_lead": ["2017-08-01", "2021-05-01", "2018-09-01"],
  "reference": ["278415", "29199723", "22219842"]
}
```

### Table 2: AIRTIME_DETAILS

**Table Name:** `project-5400504384186300846.BU_UTILITIES_TELCO.AIRTIME_DETAILS`

**Description:** Bảng thể hiện chi tiết các giao dịch nạp tiền qua dịch vụ viễn thông trên MoMo. Mỗi giao dịch có thể được phân loại theo loại dịch vụ, đối tượng nhận tiền, và các chương trình khuyến mãi đi kèm.
Thông tin có thể lấy từ bảng này:
- Theo dõi và phân tích giao dịch nạp tiền theo mạng di động và nhà cung cấp dịch vụ
- Phân tích hành vi người dùng dựa trên loại khuyến mãi và nguồn tiền để tối ưu hóa chiến dịch marketing
- Đánh giá mức độ trung thành của người dùng qua các giao dịch và thời gian hoạt động

**Columns:**

| Column Name | Description |
|------------|-------------|
| `id` | Mã định danh của giao dịch. |
| `date` | Ngày thực hiện giao dịch. |
| `datetime` | Thời điểm cụ thể thực hiện giao dịch. |
| `amount` | Số tiền của giao dịch. |
| `mm_amount` | Số tiền từ ví MoMo trong giao dịch, nếu người dùng sử dụng ví MoMo làm phương thức thanh toán. |
| `cate` | Mạng di động liên quan đến giao dịch. |
| `service` | Dịch vụ của giao dịch (TOPUP: dịch vụ Topup, MATHE: dịch vụ mua mã thẻ, OTHER: Dịch vụ khác). |
| `subcategory` | Danh mục phụ liên quan đến giao dịch. |
| `group_service` | Nhóm dịch vụ liên quan đến giao dịch. |
| `merchant` | Tên merchant liên quan đến giao dịch. |
| `region` | Khu vực của merchant. |
| `supplier` | Nhà cung cấp của giao dịch. |
| `service_code` | Mã dịch vụ liên quan đến giao dịch. |
| `bonus` | Tiền thưởng cho người dùng khi thực hiện giao dịch. |
| `gender` | Giới tính của người dùng thực hiện thanh toán. |
| `group_age` | Nhóm tuổi của người dùng thực hiện thanh toán. |
| `age` | Tuổi của người dùng thực hiện thanh toán. |
| `statusid` | Trạng thái của giao dịch (6 = thất bại, 2 = thành công). |
| `province` | Tỉnh của người dùng thực hiện thanh toán. |
| `province_group` | Nhóm tỉnh của người dùng thực hiện thanh toán. |
| `user_payment` | Người dùng thực hiện giao dịch được mã hóa. |
| `money_source` | Nguồn tiền của giao dịch khi người dùng thanh toán. |
| `serviceid` | Mã dịch vụ của giao dịch. |
| `partner` | Số điện thoại được nạp trong giao dịch (nếu dịch vụ là MATHE, thì không có dữ liệu; nếu dịch vụ là TOPUP, nhưng số điện thoại không phải là người dùng MoMo thì không có dữ liệu). |
| `telcosource` | Điểm bắt đầu của giao dịch. |
| `revenue` | Doanh thu của giao dịch. |
| `month_active` | Tháng thực hiện giao dịch. |
| `retain` | Sự giữ lại của khách hàng liên quan đến giao dịch. |
| `user_segment` | Phân khúc người dùng trong tháng. |
| `churn_duration` | Thời gian không sử dụng của người dùng = tháng thực hiện giao dịch - tháng cuối cùng người dùng hoạt động. Nếu phân khúc người dùng là new_user thì churn_duration = 0. |
| `quantity` | Số lượng sản phẩm được nạp khi người dùng thực hiện giao dịch. |
| `menh_gia` | Mệnh giá của sản phẩm. |
| `goi_cuoc` | Mã sản phẩm của giao dịch. |
| `dung_luong` | Dung lượng liên quan đến giao dịch. |
| `expire` | Hạn sử dụng liên quan đến giao dịch. |
| `partner_type` | Loại đối tác trong tháng của người thanh toán (Owner: chỉ nạp cho bản thân, Mathe: mua mã thẻ, Partner: nạp cho người khác). |
| `typeid` | giftid hoặc entercode (với chương trình giảm giá trực tiếp) của giao dịch. Nếu typeid không có dữ liệu thì đây là giao dịch không có khuyến mãi. |
| `vc_amount` | Giá trị voucher trong giao dịch. |
| `voucher_or_not` | Loại khuyến mãi của giao dịch. Voucher: giao dịch có khuyến mãi, Non_voucher: giao dịch không có khuyến mãi. |
| `promotion_type` | Loại khuyến mãi liên quan đến giao dịch. |
| `partner_momo_user` | Loại người dùng được nạp. momo user: người được nạp có sử dụng app Momo, owner: người đi nạp tự nạp cho bản thân, non momo user: người được nạp không sử dụng Momo, mathe: người mua mã thẻ. |
| `voucher_type_by_gmv` | Hành vi của khuyến mãi dựa trên GMV của người dùng trong tháng. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, GMV MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, GMV MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi. |
| `previous_voucher_type_by_gmv` | Hành vi của khuyến mãi dựa trên GMV của người dùng trong tháng trước. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, GMV MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, GMV MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi. |
| `voucher_type_by_trans` | Hành vi của khuyến mãi dựa trên giao dịch của người dùng trong tháng. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, GMV MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, GMV MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi. |
| `previous_voucher_type_by_trans` | Hành vi của khuyến mãi dựa trên giao dịch của người dùng trong tháng trước. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, TRANS MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, TRANS MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi. |
| `prev_aov` | AOV của người dùng trong tháng trước khi hoạt động. |
| `telco_source_raw` | Nguồn gốc ban đầu của dịch vụ viễn thông liên quan đến giao dịch. |
| `suffix` | Chi tiết địa điểm của nguồn dịch vụ viễn thông. |
| `user_raw` | Thông tin ban đầu liên quan đến người dùng. |
| `promotion_cost_type` | Loại chi phí khuyến mãi của giao dịch. BU: ngân sách của đội, organic: không có khuyến mãi, other teams: các đội khác trong MoMo. |
| `rfm_type` | Xếp hạng lòng trung thành của người dùng trong tháng. |
| `last_3_month_rfm_type` | Xếp hạng lòng trung thành của người dùng trong 3 tháng trước. |
| `acquire_user_channel` | Chi phí khuyến mãi của giao dịch đầu tiên của người dùng. BU: ngân sách của đội, organic: không có khuyến mãi, other teams: các đội khác trong MoMo. |
| `movement_status` | Trạng thái lòng trung thành của người dùng trong 3 tháng trước. |
| `ttt_segment` | Phân đoạn túi thần tài liên quan đến giao dịch. |

**Smart Top Values:**
```json
{
  "promotion_cost_type": ["other teams", "organic", "BU"],
  "movement_status": ["educate fail", "maintain customer type", "educate success", "on educate process"],
  "acquire_user_channel": ["other teams", "organic", "BU"],
  "last_3_month_rfm_type": ["Promising", "Lost", "About To Sleep", "Recent Customers", "Champions", "Potential Loyalist", "Loyal Customers", "Customers Needing Attention"],
  "ttt_segment": ["non_TTT", "1.New", "3.Reactive", "churn_TTT", "2.Retain"],
  "rfm_type": ["Promising", "Lost", "About To Sleep", "Recent Customers", "Champions", "Potential Loyalist", "Loyal Customers", "Customers Needing Attention"],
  "suffix": ["button_ttt", "cross_sale_config", "block_recommend", "cross_sale_AI", "cross_sale_both", "cross_sale", "detail", "button_vts", "flash_sale"],
  "user_raw": ["60391774", "60432831", "38590880"],
  "previous_voucher_type_by_gmv": ["ONLY VOUCHER", "GMV MORE VOUCHER", "GMV MORE ORGANIC", "ONLY ORGANIC"],
  "voucher_type_by_trans": ["TRANS MORE ORGANIC", "ONLY VOUCHER", "TRANS MORE VOUCHER", "ONLY ORGANIC"],
  "prev_aov": ["14444.444444444445", "12424.242424242424", "69090.909090909088"],
  "partner_momo_user": ["owner", "momo user", "non momo user", "no data", "mathe"],
  "promotion_type": ["voucher", "entercode", "cashback", "organic"],
  "voucher_or_not": ["Voucher", "Non voucher"],
  "telco_source_raw": ["transfer_received_detail_payX", "progression_tttp_04_revamp_payX", "online_panel_quick_activision_revamp_payX"],
  "vc_amount": ["19999", "1", "6868"],
  "previous_voucher_type_by_trans": ["TRANS MORE ORGANIC", "ONLY VOUCHER", "TRANS MORE VOUCHER", "GMV MORE VOUCHER", "GMV MORE ORGANIC", "ONLY ORGANIC"],
  "voucher_type_by_gmv": ["ONLY VOUCHER", "GMV MORE ORGANIC", "ONLY ORGANIC", "GMV MORE VOUCHER"],
  "typeid": ["220425_fs_tkol_danang_100k", "2212_vtti_airtime_retain_2k", "221124_45_lktk_ot_500k_topup1_20k"],
  "partner_type": ["partner", "owner", "mathe_partner", "only_owner", "only_others", "mathe_owner", "only_mathe", "others_partner", "only_partner", "mathe", "owner_partner", "mathe_owner_partner", "mathe_others"],
  "expire": [],
  "dung_luong": [],
  "month_active": ["2023-08-01", "2022-09-01", "2023-10-01"],
  "churn_duration": ["1", "18", "10"],
  "quantity": ["1", "10", "5"],
  "goi_cuoc": ["BCMBF30", "BCVNP200", "300000vina", "41040708", "40419971", "14626860", "59229884", "38478749", "41432454", "33197687", "49887017", "44306013", "59872969", "6173269", "42385114", "TUMBF500", "6488018", "33250704", "57130896", "14412571", "45521275", "56522317", "TUVNM30", "10", "48641658", "46987048", "38269840", "23153803", "47167944", "41755970", "24172247", "47140902", "18447339", "1535472", "38536894", "19099377", "38771224", "49021042", "54804118", "54466247", "BCRED10", "49276030", "48617635", "45045704", "2946993", "7484952", "66249633", "58310636", "42572820", "60085594"],
  "retain": ["2023-08-01", "2022-09-01", "2016-09-01"],
  "user_segment": ["recover_user", "retain_user", "new_user"],
  "menh_gia": ["60500", "224000", "87300"],
  "revenue": ["18800", "2419.978", "1435.962"],
  "telcosource": ["tabbar_profile", "service_widget", "walking"],
  "money_source": ["others", "group fund", "pay_later", "visa credit", "TTT", "visa ao ccm", "bank_link", "transfer", "direct debit", "napas", "momo", "visa debit"],
  "partner": ["60567889", "44038786", "44881053"],
  "bonus": ["585", "250", "660"],
  "province": ["Trà Vinh", "Long An", "Nam Định"],
  "statusid": ["6", "2"],
  "serviceid": ["topup_Saymee", "MOMOEFWV20240129", "topup_Viettel", "topup_Itel", "EPAY_VIETNAMOBILE", "MOMO0LAX20191108", "topup_Local", "topup_Vietnamobile", "MOMOCHGI20231221", "partnermomo", "EPAY_VIETTEL", "EPAY_MOBIFONE", "topup_Mobifone", "EPAY_VINAFONE", "topup_Reddi", "buycard_Reddi", "topup_Vinaphone", "EPAY_BEELINE"],
  "group_age": ["33_to_37", "[4]. 27 - 30 y/o", "28_to_32", "[5]. 31 - 35 y/o", "23_to_27", ">37", "[2]. 18 - 22 y/o", "[6]. 36 - 40 y/o", "[1]. <18 y/o", "[3]. 23 - 26 y/o", "UNKNOWN", "[7]. >40 y/o", "18_to_22"],
  "gender": ["FEMALE", "male", "UNKNOWN", "unknown", "MALE", "female"],
  "service": ["TOPUP", "MATHE", "OTHERS"],
  "service_code": ["m4btopbrandvtti_20445", "vttiwhypay_vt.airtime", "vttiimedia_mathe_mbp"],
  "region": ["Mien Bac"],
  "province_group": ["Others", "KCN Miền Nam", "Hà Nội", "TP Du lịch", "Hồ Chí Minh", "Tỉnh khác", "Unknown", "TP Lớn", "KCN Miền Bắc"],
  "subcategory": ["Gmobile", "Vietnamobile", "MOBICAST", "IO MEDIA", "EPAY", "VIETTEL DIRECT", "Mobifone", "OCTA/LOGICH", "WHYPAY", "Mservice", "VMG/IMEDIA", "Vinaphone", "IMEDIA", "ZOTA/FIVI", "MEGATEK"],
  "group_service": ["Topup&Mathe"],
  "user_payment": ["69946856", "29097553", "44343506"],
  "date": ["2025-05-02", "2021-08-08", "2025-05-08"],
  "amount": ["1", "84350", "33250"],
  "cate": ["Gmobile", "Vietnamobile", "OTHER", "Mobifone", "Vinaphone", "Reddi", "Viettel"],
  "mm_amount": ["87300", "29400", "403000"],
  "supplier": ["Gmobile", "Vietnamobile", "MOBICAST", "IO MEDIA", "EPAY", "VIETTEL DIRECT", "Mobifone", "OCTA/LOGICH", "WHYPAY", "VMG/IMEDIA", "ZOTA/FIVI", "Mservice", "Vinaphone", "IMEDIA", "MEGATEK"],
  "id": ["25540130231", "25535670917", "25528430906"],
  "age": ["1", "114", "18"],
  "datetime": ["2022-06-25 11:40:47", "2022-06-25 19:20:20", "2022-06-25 13:04:15"]
}
```

### Table 3: AIRTIME_MAU_BY_1ST_TRAN_ALL

**Table Name:** `project-5400504384186300846.BU_UTILITIES_TELCO.AIRTIME_MAU_BY_1ST_TRAN_ALL`

**Description:** Bảng này chứa thông tin về lượng người dùng hàng tháng cho dịch vụ viễn thông, phân tích bằng giao dịch nạp tiền đầu tiên. Bảng này có thể cung cấp thông tin về:
 - Phân khúc người dùng và loại thanh toán của họ
 - Tổng doanh thu và chi phí khuyến mãi liên quan đến việc nạp tiền
 - Phân loại người dùng và xếp hạng dựa trên tuổi, giới tính, và vị trí địa lý

**Columns:**

| Column Name | Description |
|------------|-------------|
| `USER_PAYMENT` | Loại thanh toán của người dùng. |
| `USER_SEGMENT` | Phân khúc người dùng. |
| `VOUCHER_OR_NOT` | Trạng thái [có sử dụng voucher hay không]. |
| `DATE` | Ngày của giao dịch nạp tiền đầu tiên. |
| `DATETIME` | Thời gian chính xác của giao dịch nạp tiền đầu tiên. |
| `MONTH_ACTIVE` | Tháng hoạt động. |
| `CATE` | Danh mục của dịch vụ viễn thông. |
| `SERVICE` | Tên dịch vụ. |
| `AMOUNT` | Số tiền giao dịch nạp tiền. |
| `ID` | Mã định danh giao dịch. |
| `REVENUE` | Doanh thu từ giao dịch nạp tiền. |
| `VC_AMOUNT` | Giá trị của voucher sử dụng trong giao dịch. |
| `typeid` | Loại của giao dịch. |
| `MENH_GIA` | Mệnh giá của giao dịch nạp tiền. |
| `CHURN_DURATION` | Thời gian gián đoạn (khách hàng ngừng sử dụng dịch vụ) tính bằng ngày. |
| `PROVINCE_GROUP` | Nhóm tỉnh thành. |
| `GROUP_AGE` | Nhóm tuổi của người dùng. |
| `GENDER` | Giới tính của người dùng. |
| `PARTNER_TYPE` | Loại đối tác của dịch vụ viễn thông. |
| `promotion_cost_type` | Loại chi phí khuyến mãi. |
| `money_source` | Nguồn tiền của giao dịch. |
| `RANK_USER` | Xếp hạng người dùng. |

**Smart Top Values:**
```json
{
  "GROUP_AGE": ["[4]. 27 - 30 y/o", "[5]. 31 - 35 y/o", "[1]. <18 y/o", "[3]. 23 - 26 y/o", "[2]. 18 - 22 y/o", "[7]. >40 y/o", "[6]. 36 - 40 y/o", "UNKNOWN"],
  "PARTNER_TYPE": ["only_mathe", "only_partner", "only_owner", "mathe_partner", "owner_partner", "mathe_owner_partner", "only_others", "mathe_owner"],
  "GENDER": ["male", "unknown", "female"],
  "CHURN_DURATION": ["46", "60", "12"],
  "PROVINCE_GROUP": ["Hồ Chí Minh", "Unknown", "Hà Nội", "Others", "KCN Miền Nam", "KCN Miền Bắc"],
  "money_source": ["TTT", "pay_later", "visa debit", "visa ao ccm", "group fund", "bank_link", "momo", "direct debit", "napas", "others", "transfer", "visa credit"],
  "RANK_USER": ["1"],
  "VC_AMOUNT": ["19400", "8750", "1600"],
  "REVENUE": ["1600", "13000", "5375"],
  "promotion_cost_type": ["other teams", "organic", "BU"],
  "MENH_GIA": ["16659", "285000", "224000"],
  "SERVICE": ["TOPUP", "OTHERS", "MATHE"],
  "typeid": ["rewards_fund_vtti_sep_240829_discount_100pt10k_55304565", "fs_vts_chu2m_241224_cbttt_100pt30k_kptuk", "crm1908_10_dt250313_giam_100pt10k_ygdn5|fs_vts_churn_250312_cbttt_100pt25k_6yh2z"],
  "MONTH_ACTIVE": ["2025-05-01", "2022-01-01", "2025-06-01"],
  "VOUCHER_OR_NOT": ["Voucher", "Non voucher"],
  "USER_PAYMENT": ["70468827", "62077812", "65431421"],
  "DATE": ["2025-06-16", "2022-06-10", "2025-05-13"],
  "CATE": ["Reddi", "Viettel", "OTHER", "Vinaphone", "Vietnamobile", "Mobifone", "Gmobile"],
  "AMOUNT": ["16659", "285000", "224000"],
  "USER_SEGMENT": ["new_user", "recover_user", "retain_user"],
  "ID": ["21480407209", "21486664212", "24303382915"],
  "DATETIME": ["2022-05-25 06:40:07", "2022-05-25 11:33:06", "2022-05-25 12:16:24"]
}
```

## Knowledgebase

[]

## Memory

[
  {
    "id": "629dc392-ee08-40a9-b819-494c54749e5c",
    "memory": "cùng kỳ: extract(day from date) of month_active = extract(day from date) of last month",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:41.262024",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "c0690498-664f-451c-8ab4-c431d23faae4",
    "memory": "Doanh thu cần được chia cho 1.1 khi tính toán",
    "hash": "4e3adc85532b222e551283b476ee6ac6",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-07-30T19:51:14.748530-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "25426610-b957-482c-9821-c644ac5a6209",
    "memory": "Khi xử lý dữ liệu người dùng duy nhất hàng ngày của voucher team khác, sử dụng bảng `BU_UTILITIES_TELCO.AIRTIME_MAU_BY_1ST_TRAN_ALL` thay vì `BU_UTILITIES_TELCO.AIRTIME_DETAILS`",
    "hash": "33e4f831cd082f919908162bef4179e9",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-07T19:38:35.333663-07:00",
    "updated_at": "2025-08-07T19:40:08.112610-07:00",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "637a15b8-0710-462c-8bc3-a75a58d5ddd4",
    "memory": "MAU: phải thêm điều kiện statusid = 2",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:35.303436",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "e87fb4b1-b202-4823-b6a5-9f3618bb8919",
    "memory": "Để lấy số lượng transaction, sử dụng count(distinct id)",
    "hash": "d20a096e8ccb713e542834c3c77a44cd",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-07-31T00:53:42.281361-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "fbee471f-a760-4529-8863-c0a81874379d",
    "memory": "Dữ liệu trong bảng AIRTIME_SEGMENT_USER tự động loại trừ các người dùng trong danh sách đen (blacklist)",
    "hash": "f6a18c5e9b17a66c37901f699a7e496d",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-04T19:59:28.528290-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "d5072878-e5bf-4874-85c2-38d4be4f6ca8",
    "memory": "Khi user hỏi nhà mạng, hỏi user lấy nhà mạng chính hay lấy nhà mạng ảo (mnvo)",
    "hash": "96b2a929ae2997f93da386a13a1f2929",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-04T21:02:42.064861-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "2d2fde30-798d-4e7a-b62e-c9c22e635123",
    "memory": "Bảng AIRTIME_MAU_BY_1ST_TRAN_ALL không chứa thông tin về trạng thái giao dịch",
    "hash": "a7ccb73afee975824229babde6dbbd5c",
    "metadata": null,
    "created_at": "2025-09-07T22:29:05.867749-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "d34e653a-9e28-4f11-b0ef-e95fd3a12ddc",
    "memory": "user: user_payment or reference",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:34.461053",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "73cf409a-579e-44ba-924a-330e188f4fb1",
    "memory": "giftid: typeid",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:49.484911",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "0a531bba-b3c3-4cd8-a7d9-5f407393bcae",
    "memory": "Unique user active từng ngày lấy trong bảng project-5400504384186300846.BU_UTILITIES_TELCO.AIRTIME_MAU_BY_1ST_TRAN_ALL",
    "hash": "e18ddebce4e152f63d992b31e300084a",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-05T23:24:38.614734-07:00",
    "updated_at": "2025-08-07T05:28:26.059546-07:00",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "79eff981-101c-4c5d-a1f2-494e8351c5f9",
    "memory": "Truy vấn MAU nạp điện thoại topup tháng 9 không cần lọc theo trạng thái giao dịch",
    "hash": "30474122bc0de024aa5f21240af8c10e",
    "metadata": null,
    "created_at": "2025-09-07T22:29:05.939007-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "9682b576-8e7e-4328-96eb-dacac8fd86ed",
    "memory": "giao dịch thành công: statusid = 2",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:35.018926",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "53d4c5d8-4ee6-42ce-9e9f-9737fabcab36",
    "memory": "TTT: Túi Thần Tài",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:51.846629",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "a41555d2-1dde-49d8-bb47-8f3106095538",
    "memory": "Khi xử lý dữ liệu nhóm tuổi, sử dụng giá trị group_age = '[2]. 18 - 22 y/o' hoặc group_age = '18_to_22'",
    "hash": "bbaed9727d2f91e7471a82037b015f7d",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-07-31T00:29:50.024864-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-2025",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "d7a21c5d-6f26-49f7-88bb-60ba9c4972cc",
    "memory": "Khi xử lý vấn đề liên quan tới MAU, không cần lọc theo lower(cate)",
    "hash": "4f81964fc7874566c9590c9817441f2a",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-04T20:53:28.304699-07:00",
    "updated_at": "2025-09-07T22:29:05.543081-07:00",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "de55d387-00c4-4367-8841-19edc0f58da4",
    "memory": "Túi thần tài: money_source = TTT",
    "hash": null,
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-05-13T14:20:39.892919",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "1fb173eb-19ea-4a41-9a50-fe7bc5862146",
    "memory": "Để lấy số lượng user active, sử dụng count(distinct user_payment)",
    "hash": "3e630099554c121ca88cc426a1fcedb3",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-07-31T00:53:42.024323-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "fd08ad1b-4147-418a-92c7-b8ce52c3414d",
    "memory": "Nếu user muốn lấy nhà mạng ảo thì dùng câu query với case statement cho các serviceid tương ứng\ncase\n  when serviceid in ('EPAY_VIETTEL', 'topup_Viettel') then 'Viettel'\n  when serviceid in ('topup_Vinaphone', 'EPAY_VINAFONE') then 'Vinaphone'\n  when serviceid = 'topup_Itel' then 'iTel'\n  when serviceid in ('EPAY_VIETNAMOBILE', 'topup_Vietnamobile') then 'Vietnamobile'\n  when serviceid = 'topup_Local' then 'Local'\n  when serviceid in ('buycard_Reddi', 'topup_Reddi') then 'Wintel'\n  when serviceid = 'topup_Saymee' then 'Saymee'\n  when serviceid in ('topup_Mobifone', 'EPAY_MOBIFONE') then 'Mobifone'\n  else 'OUTAPP PAYMENT'\nend as mvno",
    "hash": "c3f9e83cf52e4da6bea0f3aa671e73d2",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-04T21:02:42.144204-07:00",
    "updated_at": "2025-08-04T21:14:43.407934-07:00",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "9f77b8e9-a4ca-4c02-a11c-c7f0cc6dc74e",
    "memory": "Nếu user muốn lấy nhà mạng chính thì dùng cột cate",
    "hash": "7d037ec11dac86a1e9509dd4b28436e0",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-04T21:02:42.098301-07:00",
    "updated_at": "2025-08-04T21:05:04.223409-07:00",
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "134b913a-7f07-42f2-8509-bcc68f26cdf5",
    "memory": "Khi truy vấn số lượng người dùng theo từng nhóm, cần sử dụng count(distinct user_payment)",
    "hash": "72d08715a9dced64cc43767bf1f8868f",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-07-31T01:32:40.034539-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "7cf81968-9edf-4cb6-9043-877db0282fcd",
    "memory": "Số user sử dụng voucher: dùng cột voucher_or_not = 'Voucher'",
    "hash": "d801e7c8fee71f1f48edd1ef216aa3e8",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-05T00:26:09.689664-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  },
  {
    "id": "c17f412d-9492-499a-9d57-2d7ff0341138",
    "memory": "Số user theo loại promotion: cột promotion_cost_type, trong đó: BU = voucher từ budget của Airtime, organic: user không dùng voucher, other teams: voucher từ budget của team khác",
    "hash": "f1e91cde27399602dbe98fa680f9b384",
    "metadata": {
      "user_name": "Airtime"
    },
    "created_at": "2025-08-05T00:26:09.817519-07:00",
    "updated_at": null,
    "user_id": "3165cb58-8f0a-4c7d-96e6-ae0b189ff572"
  }
]