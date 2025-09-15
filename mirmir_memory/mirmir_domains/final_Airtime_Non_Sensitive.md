# Airtime (Non Sensitive)

## Basic Information

**Error Code:** 200
**Data ID:** 63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8
**Name:** Airtime (Non Sensitive)

## Description

records all transaction (exclude blacklist user), demographic, user segment of Airtime Service since 2021

## Instructions

## Schema DDL

```
###Dataset name: Airtime (Non Sensitive) ---

## Table information :

{
  "schema_ddl": {
    "table_name": "project-5400504384186300846.BU_UTILITIES_TELCO.AIRTIME_DETAILS",
    "table_desc": "Bảng này chứa thông tin chi tiết về các giao dịch nạp tiền điện thoại qua Momo. Có thể sử dụng bảng để: \n - Theo dõi số lượng tiền nạp và thông tin liên quan đến giao dịch nạp tiền \n - Phân tích các dịch vụ và nhà cung cấp dịch vụ di động mà người dùng đang sử dụng \n - Đánh giá hành vi khuyến mãi và hoạt động của người dùng dựa trên loại voucher và thói quen sử dụng dịch vụ.",
    "column_desc": [
      {
        "column_name": "id",
        "description": "Mã giao dịch."
      },
      {
        "column_name": "date",
        "description": "Ngày thực hiện giao dịch."
      },
      {
        "column_name": "datetime",
        "description": "Ngày giờ thực hiện giao dịch."
      },
      {
        "column_name": "amount",
        "description": "Số tiền của giao dịch."
      },
      {
        "column_name": "mm_amount",
        "description": "Số tiền đã thanh toán bằng ví Momo (nếu có)."
      },
      {
        "column_name": "cate",
        "description": "Mạng di động liên quan đến giao dịch."
      },
      {
        "column_name": "service",
        "description": "Dịch vụ của giao dịch. Các giá trị bao gồm: TOPUP: dịch vụ Topup, MATHE: dịch vụ mua mã thẻ, OTHER: Dịch vụ khác."
      },
      {
        "column_name": "subcategory",
        "description": "Danh mục phụ của giao dịch."
      },
      {
        "column_name": "group_service",
        "description": "Nhóm dịch vụ của giao dịch."
      },
      {
        "column_name": "merchant",
        "description": "Tên nhà bán hàng của giao dịch."
      },
      {
        "column_name": "region",
        "description": "Khu vực của nhà bán hàng."
      },
      {
        "column_name": "supplier",
        "description": "Nhà cung cấp của giao dịch."
      },
      {
        "column_name": "service_code",
        "description": "Mã dịch vụ liên quan đến giao dịch."
      },
      {
        "column_name": "bonus",
        "description": "Tiền thưởng cho người dùng khi thực hiện giao dịch."
      },
      {
        "column_name": "gender",
        "description": "Giới tính của người thực hiện thanh toán giao dịch."
      },
      {
        "column_name": "group_age",
        "description": "Nhóm tuổi của người thực hiện thanh toán."
      },
      {
        "column_name": "age",
        "description": "Tuổi của người thực hiện thanh toán."
      },
      {
        "column_name": "statusid",
        "description": "Trạng thái của giao dịch, với 6 là thất bại, 2 là thành công."
      },
      {
        "column_name": "province",
        "description": "Tỉnh thành của người thực hiện thanh toán."
      },
      {
        "column_name": "province_group",
        "description": "Nhóm tỉnh thành của người thực hiện thanh toán."
      },
      {
        "column_name": "user_payment",
        "description": "Người thực hiện giao dịch, định dạng băm."
      },
      {
        "column_name": "money_source",
        "description": "Nguồn tiền của giao dịch khi người dùng thanh toán."
      },
      {
        "column_name": "serviceid",
        "description": "Mã dịch vụ của giao dịch."
      },
      {
        "column_name": "partner",
        "description": "Số điện thoại được nạp trong giao dịch (nếu dịch vụ là MATHE, thì không có dữ liệu; nếu dịch vụ là TOPUP, nhưng số điện thoại không phải người dùng Momo thì không có dữ liệu)."
      },
      {
        "column_name": "telcosource",
        "description": "Điểm bắt đầu của giao dịch."
      },
      {
        "column_name": "revenue",
        "description": "Doanh thu của giao dịch."
      },
      {
        "column_name": "month_active",
        "description": "Tháng của giao dịch."
      },
      {
        "column_name": "retain",
        "description": "Không có thông tin."
      },
      {
        "column_name": "user_segment",
        "description": "Đoạn phân khúc của người dùng trong tháng."
      },
      {
        "column_name": "churn_duration",
        "description": "Thời gian gián đoạn của người dùng bằng month_active trừ tháng cuối cùng người dùng hoạt động. Nếu user_segment là new_user thì churn_duration là 0."
      },
      {
        "column_name": "quantity",
        "description": "Số lượng sản phẩm khi người dùng thực hiện giao dịch."
      },
      {
        "column_name": "menh_gia",
        "description": "Mệnh giá của sản phẩm."
      },
      {
        "column_name": "goi_cuoc",
        "description": "ID sản phẩm của giao dịch."
      },
      {
        "column_name": "dung_luong",
        "description": "Không có thông tin."
      },
      {
        "column_name": "expire",
        "description": "Không có thông tin."
      },
      {
        "column_name": "partner_type",
        "description": "Loại đối tác trong tháng của người thanh toán. Owner: chỉ nạp cho bản thân, Mathe: mua mã thẻ, Partner: nạp cho người khác."
      },
      {
        "column_name": "typeid",
        "description": "ID quà tặng hoặc nhập mã (với chương trình giảm giá trực tiếp) của giao dịch. Nếu không có dữ liệu, đây là giao dịch không có khuyến mãi."
      },
      {
        "column_name": "vc_amount",
        "description": "Số tiền voucher."
      },
      {
        "column_name": "voucher_or_not",
        "description": "Loại khuyến mãi của giao dịch. Voucher: giao dịch có khuyến mãi, Non_voucher: giao dịch không có khuyến mãi."
      },
      {
        "column_name": "promotion_type",
        "description": "Không có thông tin."
      },
      {
        "column_name": "partner_momo_user",
        "description": "Loại người dùng được nạp. Momo user: người được nạp có sử dụng app Momo, owner: người đi nạp tự nạp cho bản thân, non momo user: người được nạp không sử dụng Momo, mathe: user mua mã thẻ."
      },
      {
        "column_name": "voucher_type_by_gmv",
        "description": "Hành vi sử dụng gmv khuyến mãi của người dùng trong tháng. ONLY ORGANIC: Không sử dụng bất kỳ promotion nào, GMV MORE ORGANIC: Có sử dụng promotion, nhưng phần lớn là không sử dụng promotion, GMV MORE VOUCHER: Chủ yếu sử dụng promotion, ONLY VOUCHER: Chỉ sử dụng promotion."
      },
      {
        "column_name": "previous_voucher_type_by_gmv",
        "description": "Hành vi sử dụng gmv khuyến mãi của người dùng trong tháng trước khi sử dụng dịch vụ Airtime. ONLY ORGANIC: Không sử dụng bất kỳ promotion nào, GMV MORE ORGANIC: Có sử dụng promotion, nhưng phần lớn là không sử dụng promotion, GMV MORE VOUCHER: Chủ yếu sử dụng promotion, ONLY VOUCHER: Chỉ sử dụng promotion."
      },
      {
        "column_name": "voucher_type_by_trans",
        "description": "Hành vi sử dụng khuyến mãi trong giao dịch của người dùng trong tháng. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, GMV MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, GMV MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi."
      },
      {
        "column_name": "previous_voucher_type_by_trans",
        "description": "Hành vi sử dụng khuyến mãi trong giao dịch của người dùng trong tháng trước khi sử dụng dịch vụ Airtime. ONLY ORGANIC: Không sử dụng bất kỳ khuyến mãi nào, TRANS MORE ORGANIC: Có sử dụng khuyến mãi, nhưng phần lớn là không sử dụng khuyến mãi, TRANS MORE VOUCHER: Chủ yếu sử dụng khuyến mãi, ONLY VOUCHER: Chỉ sử dụng khuyến mãi."
      },
      {
        "column_name": "prev_aov",
        "description": "Giá trị trung bình của giao dịch của người dùng trong tháng trước khi hoạt động."
      },
      {
        "column_name": "telco_source_raw",
        "description": "Không có thông tin."
      },
      {
        "column_name": "suffix",
        "description": "Chi tiết vị trí của telco_source."
      },
      {
        "column_name": "user_raw",
        "description": "Không có thông tin."
      },
      {
        "column_name": "promotion_cost_type",
        "description": "Loại chi phí khuyến mãi của giao dịch. BU: ngân sách của đội chúng tôi, organic: không có khuyến mãi, other teams: các đội khác trong Momo."
      },
      {
        "column_name": "rfm_type",
        "description": "Xếp hạng lòng trung thành của người dùng trong tháng."
      },
      {
        "column_name": "last_3_month_rfm_type",
        "description": "Xếp hạng lòng trung thành của người dùng trong 3 tháng trước."
      },
      {
        "column_name": "acquire_user_channel",
        "description": "Loại chi phí khuyến mãi của giao dịch đầu tiên của người dùng. BU: ngân sách của đội chúng tôi, organic: không có khuyến mãi, other teams: các đội khác trong Momo."
      },
      {
        "column_name": "movement_status",
        "description": "Trạng thái lòng trung thành của người dùng trong 3 tháng qua."
      },
      {
        "column_name": "ttt_segment",
        "description": "Không có thông tin."
      }
    ]
  },
  "smart_top_value": "- Distinct value `previous_voucher_type_by_trans` là ['TRANS MORE VOUCHER' 'ONLY VOUCHER' 'ONLY ORGANIC' 'GMV MORE VOUCHER'\n 'TRANS MORE ORGANIC' 'GMV MORE ORGANIC']\n- Distinct value `voucher_type_by_gmv` là ['ONLY VOUCHER' 'ONLY ORGANIC' 'GMV MORE VOUCHER' 'GMV MORE ORGANIC']\n- Distinct value `voucher_or_not` là ['Non voucher' 'Voucher']\n- Distinct value `partner_type` là ['mathe_owner_partner' 'owner_partner' 'owner' 'only_owner' 'only_others'\n 'mathe_owner' 'only_partner' 'others_partner' 'only_mathe' 'partner'\n 'mathe_partner' 'mathe_others' 'mathe']\n- Distinct value `voucher_type_by_trans` là ['TRANS MORE VOUCHER' 'ONLY VOUCHER' 'ONLY ORGANIC' 'TRANS MORE ORGANIC']\n- Distinct value `partner_momo_user` là ['owner' 'momo user' 'non momo user' 'no data' 'mathe']\n- Distinct value `suffix` là ['cross_sale_config' 'button_vts' 'flash_sale' 'button_ttt'\n 'cross_sale_AI' 'detail' 'cross_sale_both' 'block_recommend' 'cross_sale']\n- Distinct value `rfm_type` là ['Customers Needing Attention' 'Champions' 'Potential Loyalist'\n 'About To Sleep' 'Promising' 'Lost' 'Recent Customers' 'Loyal Customers']\n- Distinct value `last_3_month_rfm_type` là ['Customers Needing Attention' 'Champions' 'Potential Loyalist'\n 'About To Sleep' 'Promising' 'Lost' 'Recent Customers' 'Loyal Customers']\n- Distinct value `promotion_type` là ['entercode' 'cashback' 'organic' 'voucher']\n- Distinct value `movement_status` là ['on educate process' 'educate fail' 'maintain customer type'\n 'educate success']\n- Distinct value `user_segment` là ['recover_user' 'retain_user' 'new_user']\n- Distinct value `ttt_segment` là ['3.Reactive' '2.Retain' '1.New' 'non_TTT' 'churn_TTT']\n- Distinct value `acquire_user_channel` là ['other teams' 'organic' 'BU']\n- Distinct value `promotion_cost_type` là ['other teams' 'organic' 'BU']\n- Distinct value `province_group` là ['Others' 'TP Lớn' 'Unknown' 'TP Du lịch' 'KCN Miền Nam' 'Hồ Chí Minh'\n 'Hà Nội' 'KCN Miền Bắc' 'Tỉnh khác']\n- Distinct value `supplier` là ['MEGATEK' 'ZOTA/FIVI' 'Mobifone' 'WHYPAY' 'VIETTEL DIRECT' 'Vinaphone'\n 'IMEDIA' 'Vietnamobile' 'IO MEDIA' 'Mservice' 'MOBICAST' 'VMG/IMEDIA'\n 'EPAY' 'OCTA/LOGICH' 'Gmobile']\n- Distinct value `subcategory` là ['MEGATEK' 'ZOTA/FIVI' 'Mobifone' 'WHYPAY' 'VIETTEL DIRECT' 'Vinaphone'\n 'Vietnamobile' 'IMEDIA' 'IO MEDIA' 'Mservice' 'VMG/IMEDIA' 'EPAY'\n 'OCTA/LOGICH' 'Gmobile' 'MOBICAST']\n- Distinct value `cate` là ['OTHER' 'Mobifone' 'Vinaphone' 'Vietnamobile' 'Reddi' 'Viettel' 'Gmobile']\n- Distinct value `service` là ['MATHE' 'TOPUP' 'OTHERS']\n- Distinct value `group_age` là ['[1]. <18 y/o' '>37' '33_to_37' 'UNKNOWN' '[5]. 31 - 35 y/o'\n '[2]. 18 - 22 y/o' '18_to_22' '[4]. 27 - 30 y/o' '[6]. 36 - 40 y/o'\n '23_to_27' '[3]. 23 - 26 y/o' '[7]. >40 y/o' '28_to_32']\n- Distinct value `group_service` là ['Topup&Mathe']\n- Distinct value `previous_voucher_type_by_gmv` là ['ONLY VOUCHER' 'ONLY ORGANIC' 'GMV MORE VOUCHER' 'GMV MORE ORGANIC']\n- Distinct value `money_source` là ['transfer' 'direct debit' 'napas' 'visa debit' 'momo' 'pay_later' 'TTT'\n 'group fund' 'others' 'visa ao ccm' 'bank_link' 'visa credit']\n- Distinct value `gender` là ['male' 'unknown' 'UNKNOWN' 'FEMALE' 'MALE' 'female']"
}
```

## Knowledgebase

[]

## Memory

[
  {
    "id": "4a8f4626-1196-472b-8598-0cddaf925766",
    "memory": "Khi lấy thông tin về user và TID gần nhất, cần sử dụng hàm MAX cho id để lấy latest_TID",
    "hash": "f6f07f13ac04037d3ff34116af524aad",
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-07-31T00:49:13.353075-07:00",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "ca5c5415-3509-4701-97fb-5c12e6c9ba21",
    "memory": "TTT: Túi Thần Tài",
    "hash": null,
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-05-13T14:20:39.613073",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "7d590e0e-92d5-4fa9-ad3d-0a4b400abd80",
    "memory": "Khi lọc dữ liệu theo tháng, sử dụng điều kiện HAVING latest_month_active = '2025-07-01' thay vì BETWEEN '2025-07-01' AND '2025-07-31'",
    "hash": "cbf0bb364ca20b2f05e62c36958e5afd",
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-07-31T01:10:12.021541-07:00",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "72a43f46-dc2e-4507-a31c-bc284a8664a0",
    "memory": "giao dịch thành công: statusid = 2",
    "hash": null,
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-05-13T14:20:28.768685",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "ff5e6c7e-ee41-40d3-8fd2-b079472ed5c0",
    "memory": "Khi truy vấn số lượng giao dịch active, cần kiểm tra user_raw không null",
    "hash": "b050926891c1c55fc3c9b3213d3682d0",
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-07-31T01:01:09.469923-07:00",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "c977eaea-9db1-4591-8bc1-acdcd002405a",
    "memory": "giftid: typeid ",
    "hash": null,
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-05-13T14:20:21.970390",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "a0e067b0-631a-4e49-81e6-006fe8437c2e",
    "memory": "MAU: phải thêm điều kiện statusid = 2",
    "hash": null,
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-05-13T14:20:23.629890",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  },
  {
    "id": "0b6e5f4f-6ba7-4bdd-8e83-a07359fb8742",
    "memory": "Khi xử lý yêu cầu lấy 10 user có số transaction active nhiều nhất, cần sử dụng khoảng thời gian từ '2022-07-01' đến '2025-07-31' cho cột date",
    "hash": "44a28a9d48feaa7748f70ca740433c8d",
    "metadata": {
      "user_name": "Airtime (Non Sensitive)"
    },
    "created_at": "2025-07-31T00:59:29.707253-07:00",
    "updated_at": null,
    "user_id": "63e7a2bc-2f9d-4b8f-9a1d-03c5ea7e16e8"
  }
]