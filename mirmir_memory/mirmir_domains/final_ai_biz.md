# AI Biz Domain

## Domain Metadata

- **ID**: e85b5368-99e4-4cbc-9781-4a7ee221a596
- **Name**: AI Biz
- **Description**: (empty)
- **Instructions**: (empty)

## Schema DDL

### Dataset name: AI Biz

#### Table 1: `momovn-prod.MATTHEW.MATTHEW_GET_OFFER_PACKAGE_INFO_LOG_V1`

```sql
CREATE TABLE `momovn-prod.MATTHEW.MATTHEW_GET_OFFER_PACKAGE_INFO_LOG_V1` (
  request_timestamp -- TIMESTAMP, -- unix timestamp in milliseconds get by clock.instant().toString()
  request -- RECORD, -- request
  response -- RECORD, -- response
  logState -- RECORD, -- log status
  response_sla -- INTEGER, -- SLA
);
```

**Table Data Examples:**
```
               request_timestamp response_sla
0  2023-05-19 02:09:26.121580+00            1
1  2023-05-19 02:49:24.315944+00            2
2  2023-05-19 02:10:48.060801+00           12
3  2023-05-19 02:50:18.675908+00           13
4  2023-05-19 02:49:36.019701+00           11
```

#### Table 2: `momovn-prod.PLUTUS.PLUTUS_GET_LOAN_DECIDER_CHECKER_V1_LOG`

```sql
CREATE TABLE `momovn-prod.PLUTUS.PLUTUS_GET_LOAN_DECIDER_CHECKER_V1_LOG` (
  timestamp -- TIMESTAMP, -- timestamp. get by clock.instant().toString()
  request -- RECORD, -- request
  response -- RECORD, -- response
  logState -- RECORD, -- log status
);
```

**Table Data Examples:**
```
                       timestamp
0  2024-06-20 08:42:24.219202+00
1  2024-04-22 06:23:09.931782+00
2  2024-06-20 08:42:36.322652+00
3  2024-06-20 08:45:40.151465+00
4  2024-06-20 08:42:08.609059+00
```

#### Table 3: `momovn-prod.RONALD.RONALD_COLLECTION_GROUP`

```sql
CREATE TABLE `momovn-prod.RONALD.RONALD_COLLECTION_GROUP` (
  collection_group_id -- STRING,
  collection_group_name -- STRING,
  group_purpose -- STRING,
  start_date -- DATE,
  end_date -- DATE,
  last_update_date -- DATE,
  active_status -- INTEGER,
  start_dpd_value -- INTEGER,
  end_dpd_value -- INTEGER,
  loan_product_code -- STRING,
  lender_id -- STRING,
  group_rank -- STRING,
);
```

**Table Data Examples:**
```
                                  collection_group_id                               collection_group_name  group_purpose  start_date end_date last_update_date active_status start_dpd_value end_dpd_value loan_product_code lender_id group_rank
0  DEBT_REMINDER.PAYLATER_LENDING.ALL_LENDER.TEST.001  DEBT_REMINDER.PAYLATER_LENDING.ALL_LENDER.TEST.001  DEBT_REMINDER  2024-11-12     None       2024-11-12             1            -100           100  PAYLATER_LENDING      None        001
1                                                None                                                None           None        None     None             None          None            None          None              None      None       None
2                                                None                                                None           None        None     None             None          None            None          None              None      None       None
3                                                None                                                None           None        None     None             None          None            None          None              None      None       None
4                                                None                                                None           None        None     None             None          None            None          None              None      None       None
```

#### Table 4: `momovn-prod.RONALD.RONALD_VOICE_BOT_CALL_RESULT_INFO_LOG_V1`

```sql
CREATE TABLE `momovn-prod.RONALD.RONALD_VOICE_BOT_CALL_RESULT_INFO_LOG_V1` (
  request_timestamp -- TIMESTAMP, -- unix timestamp in milliseconds get by clock.instant().toString()
  message -- RECORD, -- message
  record_timestamp -- INTEGER, -- record timestamp
  logState -- RECORD, -- log status
  contact_data -- RECORD, -- contact data
);
```

**Table Data Examples:**
```
Empty DataFrame
Columns: []
Index: []
```

## Knowledgebase

(empty)

## Memory

(empty)