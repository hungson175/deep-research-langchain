# Data Ownership Dataset

## Dataset Information

- **ID**: 51216294-46c7-4058-8ba2-aa53f7409fe6
- **Name**: Data Ownership
- **Description**: Thông tin về data contract, data owner, những bảng đã được lên contract và data quality của những bảng đã được lên contract.
- **Instructions**: (Not specified)
- **Error Code**: 200

---

## Schema Information

### Dataset Name: Data Ownership

**Description**:
Thông tin về data contract, data owner, những bảng đã được lên contract và data quality của những bảng đã được lên contract.

---

## Table 1: momovn-cdo-shared.DATA_OWNERSHIP.DIM_CONTRACT_LAST_VERSION

### Schema DDL

```sql
CREATE TABLE `momovn-cdo-shared.DATA_OWNERSHIP.DIM_CONTRACT_LAST_VERSION` (
  id -- INTEGER, -- ID của phiên bản hợp đồng
  contract_id -- INTEGER, -- ID của hợp đồng.
  version -- INTEGER, -- Phiên bản của hợp đồng.
  status -- STRING, -- Trạng thái của hợp đồng.
  name -- STRING, -- Tên của hợp đồng
  description -- STRING, -- Mô tả chi tiết về hợp đồng.
  effective_date -- DATE, -- Ngày hiệu lực của hợp đồng
  data_owner -- STRING, -- Chủ sở hữu dữ liệu của hợp đồng.
  data_producer -- STRING, -- Người tạo ra các bảng được định nghĩa trong hợp đồng.
  frequency -- STRING, -- Tần suất cập nhật hoặc kiểm tra hợp đồng
  stakeholders -- STRING, -- Stakeholder của các bảng trong hợp đồng
  update_time -- TIMESTAMP, -- Ngày tạo hợp đồng
  project_name -- STRING, -- Tên dự án liên quan đến hợp đồng
  retention -- STRING, -- Ngày dữ liệu được lưu trữ trong bảng
  expiration_date -- DATE, -- Ngày hết hạn của hợp đồng.
  db_type -- STRING, -- Loại cơ sở dữ liệu liên quan đến hợp đồng.
  db_name -- STRING, -- Tên cơ sở dữ liệu liên quan đến hợp đồng.
  contract_type -- STRING, -- Loại hợp đồng.
);
```

### Table Data Examples

| id | contract_id | version | status | name | description | effective_date | data_owner | data_producer | frequency | stakeholders | update_time | project_name | retention | expiration_date | db_type | db_name | contract_type |
|----|-------------|---------|--------|------|-------------|----------------|------------|---------------|-----------|--------------|-------------|--------------|-----------|----------------|---------|---------|---------------|
| 1045 | 149 | 2 | terminated | Test-TERMINATED | None | 2024-01-01 | ngoc.nguyen21 | ngoc.nguyen21 | daily | None | 2024-08-16 08:12:52.648343+00 | Notification | None | 2024-12-31 | None | None | Data Model |
| 790 | 152 | 3 | awaiting signing | Core_Trans-Data Platform-CDO-TERMINATED | This document records the data services provided by the ITC Department to provide data for the Notification project team started on 22nd December 2023... | 2024-07-02 | tuyen.tran4 | tuyen.tran4 | Daily | | 2024-06-17 03:41:55.970829+00 | Accounting-Finance | 90 | 2025-08-02 | ORACLE | | Ingestion |
| 828 | 161 | 1 | signed | Test-Ngoc | None | 2024-08-02 | toan.vo | thu.vu | 1 | ngoc.nguyen21 | 2024-07-02 09:35:12.422557+00 | enrich_data | 365 | 2025-08-08 | | membership | Deletion |
| 845 | 158 | 4 | None | Test-Ngoc-TERMINATED | None | 2024-06-06 | | vu.nguyen4 | T-1: daily | thanh.luong; tri.chung; quynh.nguyen; nguyen.bui1 | 2024-07-03 02:26:52.037267+00 | OTA | | 2025-09-09 | STAR_ROCKS | b2ccfg | None |
| 1031 | 210 | 6 | None | Social Feed - Ingestion Contract - CDO - SOAP_ADMIN - V1-TERMINATED | None | 2024-03-25 | anh.pham16 | quang.nguyen2 | weekly | ngan.dong1 | 2024-08-09 03:26:52.629277+00 | None | 1 | 2025-05-28 | Oracle | 1 | None |

---

## Table 2: momovn-cdo-shared.DATA_OWNERSHIP.AURORA_FACT_TABLES_IN_CONTRACT

### Schema DDL

```sql
CREATE TABLE `momovn-cdo-shared.DATA_OWNERSHIP.AURORA_FACT_TABLES_IN_CONTRACT` (
  contract_id -- INTEGER, -- ID của hợp đồng
  contract_type -- STRING, -- Loại hợp đồng
  contract_name -- STRING, -- Tên của hợp đồng
  contract_status -- STRING, -- Trạng thái của hợp đồng
  origin_Table -- STRING, -- Bảng từ source gốc
  table_name -- STRING, -- Tên bảng bao gồm project_id, dataset_id và table_name
  bq_table_name -- STRING, -- Tên bảng trong BigQuery bao gồm project_id, dataset_id và table_name
  dag -- STRING, -- DAG liên quan đến bảng
  schedule_interval -- STRING, -- Khoảng thời gian chạy dag
  bq_table_type -- STRING, -- Loại bảng trong BigQuery
);
```

### Table Data Examples

| contract_id | contract_type | contract_name | contract_status | origin_Table | table_name | bq_table_name | dag | schedule_interval | bq_table_type |
|-------------|---------------|---------------|----------------|--------------|------------|---------------|-----|-------------------|---------------|
| 209 | Data Model | Enrich data - model contract - PROD - SOAP_ADMIN | awaiting signing | None | None | None | None | None | None |
| 208 | Deletion | Enrich data - model contract - MMV2 - SOAP_ADMIN | signed | F_NOTI_CONTENT | project-5400504384186300846.PUBSUB_STREAMING.USER_NOTIFICATION_V2 | project-5400504384186300846.PUBSUB_STREAMING.USER_NOTIFICATION_V2 | v2_soap_admin__9 | 20 3 * * * | PARTITION |
| 335 | Ingestion | Credit Score Backtest - Deletion Contract - BUFI_DATA_SERVICES - Ver1 | terminated | D_NOTI_FLOW | momovn-prod.HYDRA.NOTI_CAMPAIGN | momovn-prod.HYDRA.NOTI_CAMPAIGN | v2_b2c_cinema | 0 7 * * * | SHARD |
| 194 | None | Data Dynamic Pricing - Deletion Contract - Giang.tran5 - V0 | None | F_NOTI_ACTION | momovn-prod.HYDRA.NOTI_TEMPLATE | momovn-prod.HYDRA.NOTI_TEMPLATE | v2_soap_admin__10 | 30 4 * * * | None |
| 282 | None | SOF Golden Record - Data Engineer - Product DA | None | D_NOTI_TYPE | project-5400504384186300846.MBI_DA.D_OP_USER_PROFILE | project-5400504384186300846.MBI_DA.D_OP_USER_PROFILE | v2_b2c_ota_airline | 20 3,4 * * * | None |

---

## Table 3: momovn-cdo-shared.DATA_OWNERSHIP.AURORA_FACT_APPROVALS

### Schema DDL

```sql
CREATE TABLE `momovn-cdo-shared.DATA_OWNERSHIP.AURORA_FACT_APPROVALS` (
  name -- STRING, -- Tên của hợp đồng trong hệ thống Aurora.
  contract_id -- INTEGER, -- ID của hợp đồng.
  contract_type -- STRING, -- Loại hợp đồng: Data Model, Ingestion, Deletion.
  status -- STRING, -- Trạng thái của hợp đồng (ví dụ: signed).
  last_update -- TIMESTAMP, -- Thời gian cập nhật cuối cùng của hợp đồng.
  start_date -- TIMESTAMP, -- Ngày đầu tiên hợp đồng được ký bởi người phê duyệt
  user -- STRING, -- Người phê duyệt hợp đồng. (Người ký)
  role -- STRING, -- Vai trò của người phê duyệt trong hợp đồng (ví dụ: data_producer, approval, data_consumer).
  end_date -- TIMESTAMP, -- Ngày cuối cùng hợp đồng được ký bởi người phê duyệt
);
```

### Table Data Examples

| name | contract_id | contract_type | status | last_update | start_date | user | role | end_date |
|------|-------------|---------------|--------|-------------|------------|------|------|----------|
| OTA - Ingestion Contract - PROD - B2C_DSL.OTA_HOTEL_RECORD | 278 | Ingestion | signed | 2024-11-11 08:01:04.626956+00 | None | None | approval | None |
| Student Pass-Ingestion Contract-PROD-coyote-V0 | 294 | Data Model | terminated | 2024-10-18 07:11:59.669648+00 | 2024-10-31 09:51:47.573133+00 | toan.vo | data_producer | 2024-09-05 08:35:42.662265+00 |
| CS-Ingestion Contract-Customer Service-CRM_CSTECH_CSKH-V0 | 330 | Deletion | awaiting signing | 2024-11-07 10:06:19.574023+00 | 2024-09-13 10:31:11.632723+00 | hoang.nguyen15 | data_owner | 2024-09-11 09:47:18.554511+00 |
| Online Panel-Ingestion Contract-CIO-SphinxV0 | 280 | None | None | 2024-11-11 07:47:08.992716+00 | 2024-10-09 11:08:16.192708+00 | quoc.ho | None | 2024-01-15 07:36:43.934104+00 |
| Insurtech-Ingestion Contract-FS Data Team-INSUR-V0 | 214 | None | None | 2024-08-27 04:16:07.412505+00 | 2024-10-07 07:23:13.645630+00 | minh.dang7 | data_consumer | 2024-04-03 10:41:18.328194+00 |

---

## Knowledge Base

(Empty)

---

## Memory

- **Phân biệt data owner, data consumer và data producer** (2025-05-13T14:20:38.445719): Detailed explanation of roles and responsibilities
- **Làm sao để làm contract cho luồng ingestion hoặc luồng deletion?** (2025-05-13T14:20:51.284575): Reference to documentation
- **Quy trình làm data contract ở đâu và như thế nào?** (2025-05-13T14:20:42.956530): Step-by-step process with documentation link
- **Data Ownership là gì?** (2025-05-13T14:20:58.629764): Definition and benefits with links
- **Muốn lên contract cho luồng deletion và ingestion thì làm như thế nào?** (2025-05-13T14:20:38.733529): Process documentation link
- **Tại sao cần Data Contract?** (2025-05-13T14:20:42.678833): Detailed explanation of reasons and benefits
- **Vai trò của data owner là gì?** (2025-05-13T14:20:55.244875): Role definition

---

## Error Message

(Empty)