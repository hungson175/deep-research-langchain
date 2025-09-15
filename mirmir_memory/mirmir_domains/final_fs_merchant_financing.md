# FS Merchant Financing

## Error Code
200

## Data

### Basic Information
- **ID**: 076f32ab-ad98-46fc-9998-1dd58de7134a
- **Name**: FS Merchant Financing
- **Description**: Data của sản phẩm Vay nhanh cho nhà bán hàng, bao gồm các step accessed/submitted/disbursed
- **Instructions**: (empty)

### Schema DDL

**Dataset name**: FS Merchant Financing

#### Table: momovn-prod.BU_FI.FMOB_PERFORMANCE_BY_OFFER

**Description**: (empty)

**Columns**:
- **ETL_DATE** (DATE): ngày etl_date

- **AGENT_ID** (STRING): user_id của dịch vụ cho vay

- **OFFER_GROUP** (STRING): loại gói vay

- **ACTION** (STRING): hành động của user

- **AMOUNT** (FLOAT): số tiền vay

- **LOAN_ID** (STRING): mã hợp đồng khoản vay

- **TENOR** (FLOAT): kỳ hạn

- **EMI** (FLOAT): số tiền phải trả hàng tháng

- **GMV_3_MONTH** (FLOAT): gmv 3 tháng của user

- **GMV_6_MONTH** (FLOAT): gmv 6 tháng của user

**Data Example**:
```
         loan_id    etl_date  agent_id offer_group     action      amount  tenor        emi   gmv_3_month   gmv_6_month
0  OB13119005432  2025-04-02  25911625         50M  disbursed  31000000.0   15.0  2942260.0  4.493464e+07  2.600697e+07
1  OB10846820036  2025-04-02  65083049         50M  disbursed  30000000.0   12.0  3394614.0  4.620776e+07  3.459872e+07
2  OB13740128800  2025-04-02  65980239         50M  disbursed  14000000.0   12.0  1594820.0  5.473875e+07  4.006524e+07
3  OB18930881141  2025-04-02  57726280         50M  disbursed  10000000.0    6.0  2000500.0  2.628873e+06  4.544434e+06
4  OB15762118312  2025-04-02  37263040         50M  disbursed  20000000.0   12.0  2269743.0  1.633133e+08  9.171997e+07
```

### Knowledge Base
(empty)

### Memory

1. **Memory ID**: acbd3ee0-1020-47bd-a4f8-87e73a3184bf
   - **Content**: GMV = Gross Merchandise Value = Tổng giá trị giao dịch của người dùng trong một khoảng thời gian nhất định. Dữ liệu hiện có bao gồm GMV 3 tháng và GMV 6 tháng của user.
   - **User**: FS Merchant Financing
   - **Created**: 2025-07-16T09:44:52.688596

## Error Message
(empty)