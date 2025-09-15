# User Consent Dataset

## Error Code

200

## Data

### ID
350f9466-757c-4292-af88-5e7e16e65d6a

### Name
User Consent

### Description
Dữ liệu user đồng ý chia sẻ dữ liệu cá nhân với MoMo

### Instructions
(empty)

## Schema DDL

### Dataset name: User Consent

**Description:** Dữ liệu user đồng ý chia sẻ dữ liệu cá nhân với MoMo

---

## Table 1: momovn-prod.MBI_DA.BEHALF_USERS_CONSENT_HISTORY

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| CHANGE_ID | STRING | Change identifier |
| PERMISSION_ID | STRING | Permission identifier |
| ACTION | INTEGER | Action type |
| AGENT_ID | STRING | Agent identifier |
| ATTRIBUTE | STRING | Attribute type |
| MINI_APP_ID | STRING | Mini app identifier |
| MINI_APP_USER_ID | STRING | Mini app user identifier |
| PARTNER_CODE | STRING | Partner code |
| PARTNER_USER_ID | STRING | Partner user identifier |
| UPDATE_AT | DATETIME | Update timestamp |
| USER_ID | STRING | User identifier |
| DT | DATE | Date |

### Table Data Examples:
```
                          CHANGE_ID PERMISSION_ID ACTION  AGENT_ID                 ATTRIBUTE                             MINI_APP_ID                     MINI_APP_USER_ID          PARTNER_CODE                      PARTNER_USER_ID            UPDATE_AT          DT
0  1732671984887-c18736b8-085f-460d            80      1  42115499   privacy_ttat_require_v1      internal.mservice.MOMODWGS20231103                                 None      MOMODWGS20231103                                 None  2025-01-03 03:52:23  2025-01-12
1  1733847696522-2beb5e48-93ea-46e2            81      2  68583044  privacy_ttat_optional_v1                            vn.momo.appx  MqDcMpDabMXPzgABOfTs5lJakHNKf4_TY_Q                                                             2025-01-03 03:52:22  2025-01-11
2  1733389718968-a68a6daa-cdbd-4c9f            75      0  45755800           policy_1.0_0623       internal.mservice.service-bank-v2  MlQtVB7Z9-61o5rYZRAxPNw06Zhrkw4keNw       service-bank-v2  MtXASbVuolV9bcvSeUXAh1V_sWFiazCXfHQ  2025-01-03 03:52:21  2025-01-10
3  1729773076296-ac6a9e70-7664-4cea             1   None  34030482                     phone   internal.mservice.onboarding_paylater  M11ONnwtD4Ub9tdvhVY4W2h5haE9hNrUw5A   onboarding_paylater  MirRhfaSu0EqYc29_ZaVRzxXB_uW769yTiA  2024-09-10 02:26:33  2025-01-09
4  1731304942182-5311b083-b936-4cee           250   None  96027878                dataGroup2  internal.mservice.onboarding_fastmoney  MQ7Zh2h1i-GAnyBPBqT9wVK30InZlrVk2Jg  onboarding_fastmoney  MBRRFPzbkgHFMzPKQA8XtZNmdlj3LB4vQdw  2024-08-26 06:50:31  2025-01-08
```

---

## Table 2: momovn-prod.MBI_DA.USER_CONSENT_BREAKDOWN_BY_TRANS

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| AGENT_ID | STRING | Agent identifier |
| IS_A30_USER | STRING | Is A30 user flag |
| IS_A60_USER | STRING | Is A60 user flag |
| IS_A90_USER | STRING | Is A90 user flag |
| HAVE_TRANS | STRING | Has transactions flag |
| last_trans | DATETIME | Last transaction timestamp |
| TTAT_REQUIRE | BOOLEAN | TTAT require flag |
| TTAT_OPTIONAL | BOOLEAN | TTAT optional flag |
| OLD_POLICY | BOOLEAN | Old policy flag |
| NO_CONSENT | BOOLEAN | No consent flag |
| type_consent | STRING | Type of consent |

### Table Data Examples:
```
   AGENT_ID IS_A30_USER IS_A60_USER IS_A90_USER             HAVE_TRANS           last_trans TTAT_REQUIRE TTAT_OPTIONAL OLD_POLICY NO_CONSENT                               type_consent
0  76659972        None        None        None  Have at least 1 trans  2025-01-12 21:54:42        false         false      false      false                          [4]. Chưa consent
1   4305813         A30         A60         A90                   None  2025-01-12 19:48:13         true          true       true       true  [1]. Consent cho cả Platform và 3rd Party
2  95867484        None        None        None                   None  2025-01-12 21:00:04         None          None       None       None              [3]. Chỉ consent cho Platform
3  39851017        None        None        None                   None  2025-01-12 20:45:14         None          None       None       None              [2]. Consent chung (luồng cũ)
4  36541445        None        None        None                   None  2025-01-12 20:15:19         None          None       None       None                                       None
```

---

## Table 3: momovn-prod.MBI_DA.USER_CONSENT_BREAKDOWN_BY_LOGIN

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| AGENT_ID | STRING | Agent identifier |
| IS_A30_LOGIN | STRING | Is A30 login flag |
| IS_A60_LOGIN | STRING | Is A60 login flag |
| IS_A90_LOGIN | STRING | Is A90 login flag |
| LOGIN_SINCE_2022 | STRING | Login since 2022 flag |
| LAST_LOGIN | DATE | Last login date |
| TTAT_REQUIRE | BOOLEAN | TTAT require flag |
| TTAT_OPTIONAL | BOOLEAN | TTAT optional flag |
| OLD_POLICY | BOOLEAN | Old policy flag |
| NO_CONSENT | BOOLEAN | No consent flag |
| type_consent | STRING | Type of consent |

### Table Data Examples:
```
   AGENT_ID IS_A30_LOGIN IS_A60_LOGIN IS_A90_LOGIN                        LOGIN_SINCE_2022  LAST_LOGIN TTAT_REQUIRE TTAT_OPTIONAL OLD_POLICY NO_CONSENT                               type_consent
0  30288282         None         None         None  Login at least 1 time since 2022-01-01        None        false         false      false       true                          [4]. Chưa consent
1  49394264          A30          A60          A90                                    None  2025-01-12         true          true       true      false  [1]. Consent cho cả Platform và 3rd Party
2  29371068         None         None         None                                    None  2025-01-11         None          None       None       None              [3]. Chỉ consent cho Platform
3  84257224         None         None         None                                    None  2025-01-10         None          None       None       None              [2]. Consent chung (luồng cũ)
4  81216804         None         None         None                                    None  2025-01-09         None          None       None       None                                       None
```

---

## Table 4: momovn-prod.MBI_DA.USER_CONSENT_BREAKDOWN_BY_MINIAPP

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| AGENT_ID | STRING | Agent identifier |
| MINIAPP_NAME | STRING | Mini app name |
| MINIAPP_LOGIN_NO | INTEGER | Mini app login count |
| IS_CONSENT_MINIAPP | BOOLEAN | Is consent for mini app |
| MINIAPP_WITH_TRANS_NO | INTEGER | Mini app with transaction count |
| MINIAPP_CONSENT_NO | INTEGER | Mini app consent count |
| ATTRIBITE_CONSENT_NO | INTEGER | Attribute consent count |

### Table Data Examples:
```
   AGENT_ID      MINIAPP_NAME MINIAPP_LOGIN_NO IS_CONSENT_MINIAPP MINIAPP_WITH_TRANS_NO MINIAPP_CONSENT_NO ATTRIBITE_CONSENT_NO
0  52130895  Highlands Coffee                1               true                     0                  0                    0
1  90557627               KFC                2              false                     1                  1                    2
2  95251291  The Coffee House                3               None                     2                  2                    3
3  42115499          Jollibee                4               None                     3                  3                   37
4  68583044            Gofood                5               None                     4                  4                   14
```

---

## Table 5: momovn-prod.MBI_DA.USER_CONSENT_DAILY

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| CONSENT_DAY | DATE | Consent day |
| TOTAL_USER_CONSENT | INTEGER | Total user consent count |
| TOTAL_CONSENT_REQUIRE_POPUP | INTEGER | Total consent require popup count |
| TOTAL_CONSENT_OPTIONAL_POPUP | INTEGER | Total consent optional popup count |
| TOTAL_CONSENT_OLD_POPUP | INTEGER | Total consent old popup count |
| TOTAL_CONSENT_MINIAPP | INTEGER | Total consent mini app count |

### Table Data Examples:
```
  CONSENT_DAY TOTAL_USER_CONSENT TOTAL_CONSENT_REQUIRE_POPUP TOTAL_CONSENT_OPTIONAL_POPUP TOTAL_CONSENT_OLD_POPUP TOTAL_CONSENT_MINIAPP
0  2023-11-24              39430                        None                         None                      48                  1852
1  2024-08-21              36190                          68                           35                      33                  3030
2  2024-03-21              27938                         148                           38                      39                  1912
3  2024-09-01              49941                       13036                           21                      41                  1534
4  2023-08-25              45693                         131                           32                      40                  3143
```

---

## Table 6: momovn-prod.MBI_DA.USER_CONSENT_MONTHLY

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| CONSENT_MONTH | DATE | Consent month |
| TOTAL_USER_CONSENT | INTEGER | Total user consent count |
| TOTAL_CONSENT_REQUIRE_POPUP | INTEGER | Total consent require popup count |
| TOTAL_CONSENT_OPTIONAL_POPUP | INTEGER | Total consent optional popup count |
| TOTAL_CONSENT_OLD_POPUP | INTEGER | Total consent old popup count |
| TOTAL_CONSENT_MINIAPP | INTEGER | Total consent mini app count |

### Table Data Examples:
```
  CONSENT_MONTH TOTAL_USER_CONSENT TOTAL_CONSENT_REQUIRE_POPUP TOTAL_CONSENT_OPTIONAL_POPUP TOTAL_CONSENT_OLD_POPUP TOTAL_CONSENT_MINIAPP
0    2024-07-01             433511                        None                         None                  598851                255216
1    2024-06-01            1318263                     1049566                       212964                    1236                 30955
2    2023-11-01             798132                      323247                       246716                    1730                 49733
3    2023-12-01            3835940                      659068                      3540891                   56479                 80712
4    2024-12-01             507520                      312822                       122752                  417026                624547
```

---

## Table 7: project-5400504384186300846.MBI_DA.D_OP_USER_PROFILE

### Columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| agent_id | INTEGER | Agent identifier |
| phone_new | STRING | New phone number |
| phone_old | STRING | Old phone number |
| is_end_user | BOOLEAN | Is end user flag |
| is_deleted | BOOLEAN | Is deleted flag |
| is_active | BOOLEAN | Is active flag |
| register_datetime | DATETIME | Registration timestamp |
| deletion_datetime | DATETIME | Deletion timestamp |
| email | STRING | Email address |
| phone_carrier | STRING | Phone carrier |
| device_os | STRING | Device OS |
| capset | STRING | Capability set |
| last_login | DATE | Last login date |
| is_momo_employee | BOOLEAN | Is MoMo employee flag |
| user_name | STRING | User name |
| gender | STRING | Gender |
| gender_source | STRING | Gender source |
| age | INTEGER | Age |
| yob | INTEGER | Year of birth |
| dob | DATE | Date of birth |
| age_group | STRING | Age group |
| age_source | STRING | Age source |
| is_face_matching | BOOLEAN | Is face matching flag |
| is_kyc | BOOLEAN | Is KYC flag |
| verify_info | STRING | Verification info |
| kyc_confirm | STRING | KYC confirmation |
| kyc_id_card_type | STRING | KYC ID card type |
| kyc_id_card_type_detail | STRING | KYC ID card type detail |
| kyc_issue_place | STRING | KYC issue place |
| kyc_level | STRING | KYC level |
| kyc_nationality | STRING | KYC nationality |
| kyc_name | STRING | KYC name |
| kyc_address | STRING | KYC address |
| kyc_dob | DATE | KYC date of birth |
| kyc_issue_date | DATE | KYC issue date |
| kyc_expired_date | DATE | KYC expired date |
| kyc_gender | STRING | KYC gender |
| kyc_expiration_type | STRING | KYC expiration type |
| bank_code | STRING | Bank code |
| bank_name | STRING | Bank name |
| bank_verify_name | STRING | Bank verification name |
| bank_verify_personalid | STRING | Bank verification personal ID |
| bank_acc_no | STRING | Bank account number |
| bank_verify_dob | DATE | Bank verification date of birth |
| email_bank | STRING | Bank email |
| map_visa | BOOLEAN | Map Visa flag |
| first_map_visa | DATETIME | First map Visa timestamp |
| map_bank | BOOLEAN | Map bank flag |
| first_map_bank | DATE | First map bank date |
| name_first_bank_cashin | STRING | Name first bank cash in |
| first_date_bank_cashin | DATETIME | First date bank cash in |
| name_last_bank_cashin | STRING | Name last bank cash in |
| last_date_bank_cashin | DATETIME | Last date bank cash in |
| n_time_map_bank | INTEGER | Number of times map bank |
| n_time_unmap_bank | INTEGER | Number of times unmap bank |
| last_date_unmap_bank | DATETIME | Last date unmap bank |
| map_napas | BOOLEAN | Map NAPAS flag |
| first_map_napas | DATE | First map NAPAS date |
| n_time_map_napas | INTEGER | Number of times map NAPAS |
| n_time_unmap_napas | INTEGER | Number of times unmap NAPAS |
| last_date_unmap_napas | DATETIME | Last date unmap NAPAS |
| name_last_bank_napas | STRING | Name last bank NAPAS |
| map_sacom_card | BOOLEAN | Map Sacom card flag |
| first_map_sacom_card | DATE | First map Sacom card date |
| first_a30_trans | DATETIME | First A30 transaction timestamp |
| is_a30_user | BOOLEAN | Is A30 user flag |
| last_trans | DATETIME | Last transaction timestamp |
| first_service_code | STRING | First service code |
| first_group_code_l1 | STRING | First group code level 1 |
| first_newvertical_merchant | STRING | First new vertical merchant |
| first_service_description | STRING | First service description |
| first_specialproject | STRING | First special project |
| second_service_code | STRING | Second service code |
| second_group_code_l1 | STRING | Second group code level 1 |
| second_newvertical_merchant | STRING | Second new vertical merchant |
| second_service_description | STRING | Second service description |
| second_specialproject | STRING | Second special project |
| third_service_code | STRING | Third service code |
| third_group_code_l1 | STRING | Third group code level 1 |
| third_newvertical_merchant | STRING | Third new vertical merchant |
| third_service_description | STRING | Third service description |
| third_specialproject | STRING | Third special project |
| most_service_code | STRING | Most service code |
| most_newvertical_merchant | STRING | Most new vertical merchant |
| most_service_description | STRING | Most service description |
| most_specialproject | STRING | Most special project |
| is_cheat_user | BOOLEAN | Is cheat user flag |
| cheat_source | STRING | Cheat source |
| location_month | DATE | Location month |
| most_city_a60 | STRING | Most city A60 |
| most_district_a60 | STRING | Most district A60 |
| most_ward_a60 | STRING | Most ward A60 |
| location_method | STRING | Location method |
| most_region | STRING | Most region |
| most_group_region_vn | STRING | Most group region VN |
| creation_date | DATE | Creation date |

### Table Data Examples:
```
   agent_id is_end_user is_deleted is_active    register_datetime    deletion_datetime              email phone_carrier device_os    capset  last_login is_momo_employee                                     user_name   gender gender_source   age   yob         dob         age_group     age_source is_face_matching is_kyc           verify_info kyc_confirm kyc_id_card_type kyc_id_card_type_detail                                                kyc_issue_place kyc_level kyc_nationality                                      kyc_name               kyc_address     kyc_dob kyc_issue_date kyc_expired_date kyc_gender   kyc_expiration_type bank_code                   bank_name                              bank_verify_name                        bank_verify_personalid                                   bank_acc_no bank_verify_dob                email_bank map_visa       first_map_visa map_bank first_map_bank name_first_bank_cashin first_date_bank_cashin name_last_bank_cashin last_date_bank_cashin n_time_map_bank n_time_unmap_bank last_date_unmap_bank map_napas first_map_napas n_time_map_napas n_time_unmap_napas last_date_unmap_napas name_last_bank_napas map_sacom_card first_map_sacom_card      first_a30_trans is_a30_user           last_trans          first_service_code first_group_code_l1 first_newvertical_merchant first_service_description      first_specialproject          second_service_code second_group_code_l1 second_newvertical_merchant second_service_description     second_specialproject           third_service_code third_group_code_l1 third_newvertical_merchant third_service_description      third_specialproject            most_service_code most_newvertical_merchant most_service_description       most_specialproject is_cheat_user                         cheat_source location_month most_city_a60 most_district_a60 most_ward_a60    location_method              most_region most_group_region_vn creation_date
0  87943228        true      false      true  2021-02-18 15:30:51                 None               None          None      None      None        None            false  uD1zhBTfPuy6of1/MB0zSbY4nZFAQTelIr/YaFbjkw8=  unknown       unknown  None  None        None           UNKNOWN        UNKNOWN            false  false                  None        None             None                    None                                                           None      None            None                                          None                      None        None           None             None       None                  None      None                        None                                          None                                          None                                          None            None  4ABQ3SAClk89tBxqYGPX1w==    false                 None    false           None                   None                   None                  None                  None            None              None                 None     false            None             None               None                  None                 None          false                 None                 None       false                 None                        None                None                       None                      None                      None                         None                 None                        None                       None                      None                         None                None                       None                      None                      None                         None                      None                     None                      None         false                                 None           None          None              None          None               None                     None                 None    2025-01-12
```

## Knowledgebase

(empty)

## Memory

(empty)

## Error Message

(empty)