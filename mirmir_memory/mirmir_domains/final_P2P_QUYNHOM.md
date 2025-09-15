# P2P QUYNHOM

## Dataset Information

**Dataset ID:** 3a52651b-b3a6-4865-8a11-7b06ea99be24

**Dataset Name:** P2P QUYNHOM

**Description:** Domain này bao gồm những thông tin sau của sản phẩm QUỸ (NHÓM)
(1) transaction details: Lịch sử giao dịch trong quỹ
(2) fund creation information: Thông tin quỹ được tạo
(3) ending balance: Số dư quỹ
(4) active users MoMo: User có ít nhất 1 giao dịch trong bảng iDeA_TRANS_CORE
(4) event tracking: Product event thao tác trên miniapp quỹ nhóm
(5) promotion gift: Số user được nhận gift, redeem gift

**Instructions:**

**Error Code:** 200

## Schema Information

### Table 1: momovn-prod.MBI_DA.HA_P2P_MONEYPOOL_FUND_TRANSFER_mimir

**Description:** Bảng này chứa thông tin về việc chuyển tiền trong dịch vụ P2P MONEYPOOL tại MoMo. Nó theo dõi các giao dịch chuyển tiền quỹ nhóm qua từng tháng và ngày, đồng thời ghi nhận các chi tiết liên quan đến quỹ, người dùng và hành động thực hiện. Thông tin có thể được rút ra từ bảng này gồm:
 - Theo dõi số tiền đã chuyển trong các quỹ nhóm trong tháng
 - Xác định loại quỹ và trạng thái hoạt động của quỹ
 - Phân tích hành vi chuyển tiền của người dùng theo loại người dùng và vai trò trong dịch vụ

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng thực hiện giao dịch chuyển tiền quỹ nhóm. | 2022-02-01, 2022-09-01, 2025-07-01 |
| date | Ngày thực hiện giao dịch chuyển tiền quỹ nhóm. | 2025-06-04, 2024-12-30, 2025-05-27 |
| FUND_ID | Mã định danh duy nhất cho mỗi quỹ nhóm. | mp_47842544_26x9q1soodiniaowswfzmb, mp_1193240_5vnack9orbq8x33fbhu7uj, mp_32153732_3honqprihvmkp46vthi4bh |
| FUND_TYPE | Loại quỹ. | [2]. Couple, [3]. Family & Friends, [1]. Individual |
| FUND_TYPE_active | Tình trạng hoạt động của loại quỹ. | [03]. Reactivation, [01]. New to service, [02]. Retention |
| USER_ID | Mã định danh của người dùng. | 39559824, 39092474, 40031228 |
| USER_TYPE_active | Loại người dùng (thường/người dùng đặc biệt) và trạng thái hoạt động. | [03]. Reactivation, [01]. New to service, [02]. Retention |
| USER_ID_OWNER | Mã định danh của chủ sở hữu quỹ nhóm. | 1359625, 24473345, 4632182 |
| UNIQUE_OWNER_active | Trạng thái hoạt động của chủ sở hữu quỹ nhóm. | [03]. Reactivation, [01]. New to service, [02]. Retention |
| ACTION_NAME | Tên của hành động thực hiện trong giao dịch quỹ nhóm. | Cashback scheme NTMM, Withdraw as requested, 1, Cashback SC25 Promotion, Register Golden Pocket(Valid), CashIn AIOQR (bank-ví), Cash In, Withdraw, Payment SOF, Claim Interest, Refund, Cashback scheme NTMM - 20k, Cash In AIOQR (ví-ví), Cashback scheme NTMM - 10k |
| ROLE | Vai trò của người dùng trong giao dịch quỹ nhóm. | [2]. Member, [1]. Owner |
| gender | Giới tính của người dùng. | unknown, male, female |
| TID | ID giao dịch. | 26726757276, 26728788629, 26724022350 |
| CORE_MONEY_SOURCE | Nguồn tiền chính trong giao dịch. | Quỹ nhóm, Banklink, Khác, Newton, Túi thần tài, MoMo wallet |
| AMOUNT | Số tiền được chuyển. | 9500, 1141893, 550000 |
| TOTAL_BALANCE_BY_MONTH | Tổng số dư của các quỹ nhóm theo từng tháng. | 7360382945, 12733879492, 826538343594 |

### Table 2: momovn-prod.MBI_DA.HA_P2P_MONEYPOOL_ENDING_BALANCE_mimir

**Description:** Bảng chứa thông tin Số dư của từng quỹ (FUND_ID) theo ngày, gồm số dư quỹ sinh lời và số dư quỹ không sinh lời. Dữ liệu được cập nhật trong vòng 6 tháng gần nhất. Bảng này có thể được sử dụng để:
 - Theo dõi biến động số dư của từng quỹ theo thời gian
 - Phân tích sự khác biệt giữa quỹ sinh lời và không sinh lời
 - Quản lý và ra quyết định dựa trên loại quỹ và số lượng thành viên trong quỹ

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng | 2025-08-01, 2025-06-01, 2025-05-01 |
| date | Ngày | 2025-07-19, 2025-07-22, 2025-06-06 |
| FUND_ID | Mã định danh FUND_ID của quỹ | mp_61569604_10viordc41vdoop06rnvjy, mp_76134865_5wxobvhjs03x2blaqjmb1b, mp_70372533_6nkytmqmxcmk70kowqwbmy |
| ending_balance | Số dư của từng quỹ (FUND_ID) | 147, 177, 283 |
| BALANCE_TYPE | Loại balance: [1]. Balance quỹ đã bật sinh lời, [2]. Balance quỹ không sinh lời | [2]. Balance quỹ không sinh lời, [1]. Balance quỹ đã bật sinh lời |
| FUND_TYPE | Loại quỹ theo số lượng thành viên trong quỹ: [1]. Individual, [2]. Couple, [3]. Family & Friends | [2]. Couple, , [3]. Family & Friends, [1]. Individual |

### Table 3: momovn-prod.MBI_DA.HA_P2P_MONEYPOOL_EVENT_FUNNEL_mimir

**Description:** Bảng chứa thông tin hành vi của user trên miniapp Quỹ Nhóm, cung cấp dữ liệu về:
- Ngày và tháng thực hiện hành động của người dùng
- Loại người dùng tham gia (mới hoặc đã tồn tại)
- Hành động cụ thể của người dùng trong quỹ nhóm

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| month | Tháng thực hiện action | 2025-07-01, 2025-06-01, 2025-08-01 |
| date | Ngày thực hiện action | 2025-07-27, 2025-08-15, 2025-05-06 |
| USER_ID | Mã định danh USER_ID của user | 53017264, 38795090, 13893375 |
| USER_TYPE | Trạng thái của user trong tháng: [1]. New User: người dùng mới, [2]. Existing (Member/Owner): người dùng hoặc chủ sở hữu đã tồn tại | [2]. Existing (Member/Owner), [1]. New User |
| ACTION_NAME | Hành động của user trên miniapp quỹ nhóm | [Fund Home]. Đổi ảnh bìa, [Goal]. Bấm "Xác nhận" màn góp quỹ lần đầu, [Goal]. Chọn 1 category để đi tạo quỹ (chưa có quỹ) |

### Table 4: momovn-prod.MBI_DA.HA_P2P_MONEYPOOL_FUND_CREATED_mimir

**Description:** Bảng fact này lưu trữ thông tin chi tiết về các quỹ P2P MoneyPool được tạo ra thông qua dự án MIMIR. Từ bảng này, bạn có thể lấy thông tin về tháng và ngày tạo quỹ, chi tiết quỹ như tên quỹ, loại quỹ, mục tiêu của quỹ. Ngoài ra, bảng còn cung cấp trạng thái của đầu tư, trạng thái của quỹ và thành viên, vai trò của người dùng liên quan đến quỹ, cùng với một số thông tin cơ bản về người dùng như nhóm tuổi, giới tính và địa chỉ.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| create_month | Tháng tạo quỹ. | 2023-06-01, 2023-10-01, 2025-06-01 |
| create_date | Ngày tạo quỹ. | 2022-10-08, 2024-02-08, 2023-04-22 |
| FUND_ID | Mã định danh của quỹ. | mp_39693260_idz4yk9osiei693nlgvhg, mp_59160613_5aaf9zl22mjhbppr0e5bam, mp_63744699_4mx5zyyyiwrwd7zmcfpejd |
| FUND_NAME | Tên của quỹ. | Quỹ TN, Tít kịm thoai nào🥰❤️, 1280 |
| DESC_FUND | Mô tả chi tiết về quỹ. | Có công ăn vặt có ngày lên cân, dành tiền, saving |
| CATEGORY | Danh mục hoặc loại của quỹ. | couple_fund, finhub_challenge, purchase_fund, family_fund, other_fund, other_type, personal_fund, coworker_fund, saving_fund, special_day_fund, recreational_fund, sc25, study_fund, friend_fund, TECHDAY2024, travel_fund |
| INVESTMENT_STATUS | Trạng thái đầu tư của quỹ. | [2]. Quỹ không sinh lời, [1]. Quỹ Sinh Lời |
| DEPOSIT_AIO_QR_STATUS | Trạng thái của deposit thông qua mã QR AIO. | [1]. Quỹ bật QR, c |
| TARGET_GOAL | Mục tiêu của quỹ đã chỉ định. | saving, living_expenses, travel, studying, shopping, eat_drink |
| FUND_TYPE | Loại hình của quỹ. | [1]. Individual, [2]. Couple, [3]. Family & Friends |
| STATUS_FUND | Trạng thái hiện tại của quỹ. | [2]. Closed, [1]. Non-closed |
| STATUS_MEMBER | Trạng thái của thành viên liên quan đến quỹ. | [0]. DEACTIVATE, [2]. LEAVE, [6]. REJECT REQUEST, [4]. REJECT INVITATION, [1]. ACTIVE, [3]. INVITE TO JOIN, [5]. REQUEST TO JOIN |
| USER_ID | ID của người dùng liên quan đến quỹ. | 23838367, 43370752, 48083510 |
| ROLE | Vai trò của người dùng liên quan đến quỹ. | [2]. Member, [1]. Owner |
| age_group | Nhóm tuổi của người dùng. | [6].>50, [2].18-22, [4].28-35, [5].36-50, others, [3].23-27, [1].<18  |
| citygroup | Nhóm thành phố của người dùng. | Hà Nội, KCN Miền Bắc, Thành Phố Hồ Chí Minh |
| gender | Giới tính của người dùng. | female, male, unknown |
| CURRENT_BALANCE_BY_FUND | Số dư hiện tại theo quỹ. | 3003981, 455422, 502734 |

### Table 5: momovn-prod.MBI_DA.HA_P2P_MONEYPOOL_GIFT_RAW

**Description:** Bảng lưu trữ thông tin về các giao dịch P2P MONEYPOOL liên quan đến quà tặng và voucher. Bảng này cung cấp dữ liệu để phân tích xu hướng sử dụng quà tặng và voucher trong giao dịch P2P MONEYPOOL.
 - Xác định loại quà tặng và mã liên quan
 - Theo dõi thời gian giao dịch và các chiến dịch liên quan
 - Phân tích giá trị giao dịch và voucher được sử dụng

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| gift_type | Loại quà tặng được phát trong giao dịch P2P MONEYPOOL. | voucher |
| typeid | Mã định danh cho loại quà tặng hoặc voucher trong giao dịch. | qn_2k_churn_250521_giam_100pt2k_tpz6f, rw_p2p_quy_250730_giam_100pt20k_zfk21, simdl_xsell_qn250707_giam_50pt500k_6za2g |
| startdate_1 | Ngày bắt đầu áp dụng quà tặng hoặc voucher. | 2024-12-05, 2024-09-21, 2025-04-10 |
| ngay_su_dung_voucher | Ngày mà voucher được sử dụng trong giao dịch. | 2024-12-05, 2025-05-08, 2025-04-10 |
| trans_datetime | Thời gian thực hiện giao dịch P2P MONEYPOOL có liên quan đến voucher. | 2025-03-12 06:26:09, 2025-03-11 19:50:47, 2025-03-12 12:51:29 |
| status_2 | Tình trạng của giao dịch P2P MONEYPOOL. | Voucher còn hạn nhưng User xóa, Voucher Refund, Voucher hết hạn, Voucher còn hạn, Voucher bị treo, Voucher đã sử dụng |
| TRANID | Mã định danh duy nhất cho giao dịch. | 81371787393, 81328625528, 81309579380 |
| source | Nguồn gốc của giao dịch P2P MONEYPOOL. | mmp_dls307_kai_30pt30k_0724, kgs_sp301_250731_0046_reward, kgs_sp301_20250410_0018 |
| campaignid | Mã định danh của chiến dịch liên quan đến quà tặng hoặc voucher. | quy_rewards_budget_coin_reward_250731_4rbu444ga, rw_stp_quy_budget_coin_reward_250804_8a1izidp6, 1730776534399 |
| Giatri_voucher_sudung | Giá trị mà voucher mang lại khi được sử dụng trong giao dịch. | 7400, 100000, 9890 |
| Giatri_giaodich | Tổng giá trị của giao dịch P2P MONEYPOOL. | 145000, 100000, 110470 |
| name | Tên người dùng hoặc tên liên quan đến giao dịch quà tặng. | Giảm 10K khi thanh toán bằng Quỹ Nhóm, Giảm 30% Tối đa 40K cho đơn từ 1.2Tr, Giảm 50% Tối đa 100K cho đơn từ 300K |
| USER_ID | Mã định danh của người sử dụng quà tặng hoặc voucher trong giao dịch. | 50015440, 83575597, 82571848 |
| usecase_redeem | Trường hợp sử dụng khi quà tặng hoặc voucher được đổi trong giao dịch. | MARKETPLACE, FI SOLUTIONS, SCAN VIETQR, P2P - EWALLET TO EWALLET, UTILITIES, DATA, PUBLIC SERVICE, DIGITAL CONTENT, GAME, CINEMA, FNB, SME OFFLINE, RETAIL, P2P - EWALLET TO BANK, OTA, INSURANCE, AIRTIME |
| FUND_TYPE | Loại quỹ được sử dụng trong giao dịch P2P MONEYPOOL. | [2]. Couple, [1]. Individual, [3]. Family & Friends |
| UniqueOwner_to_service | Chủ sở hữu duy nhất và dịch vụ liên quan đến giao dịch quà tặng. | [03]. Reactivation, [01]. New to service, [02]. Retention |

### Table 6: momovn-mimir.MIMIR.iDeA_TRANS_CORE

**Description:** Bảng này lưu trữ thông tin về các giao dịch trong hệ thống Momo. Thông tin từ bảng này có thể được sử dụng để:
 - Theo dõi từng giao dịch thông qua tranid
 - Xác định người thực hiện giao dịch bằng user_id
 - Tìm kiếm các giao dịch dựa trên loại giao dịch và nguồn tiền.

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| tranid | Mã định danh duy nhất cho mỗi giao dịch. | 52847525749, 52821170440, 52833316136 |
| date | Ngày thực hiện giao dịch. | 2024-08-06, 2024-10-11, 2024-10-05 |
| user_id | Mã định danh của người dùng thực hiện giao dịch. | 79809383, 39249685, 36095297 |
| usecase | Trường hợp sử dụng liên quan đến giao dịch. | PAYLATER, DEVICE FINANCING, FNB, INBOUND REMITTANCE, PUBLIC SERVICE, CASHOUT OTC AGENT, FI SOLUTIONS, INSURANCE, P2P - EWALLET TO BANK, OTT, OTA, P2P - EWALLET TO EWALLET, DATA, CINEMA, CASHIN OTC AGENT, LOGISTICS, APPLICATION STORE, CREDIT CARD MARKETPLACE, CASHIN OTC CHAIN, MONEY MARKET FUNDS, RETAIL, CASHOUT BANK, AIRTIME, MARKETPLACE, UTILITIES, GAME, DIGITAL CONTENT, PAID CASHIN, ADS PAYMENT, INVESTMENT PRODUCT, CASHIN BANK, SME OFFLINE |
| transaction_type | Loại giao dịch được thực hiện. | CASHOUT, CASHIN, PAYMENT, TRANSFER, MONEY DISBURSEMENT |
| merchant | Mã định danh hoặc tên của merchant liên quan đến giao dịch, có độ nhạy cao. |  |
| transaction_amount | Số tiền của giao dịch. | 29000, 203000, 1321000 |
| voucher_amount | Số tiền được giảm giá bằng voucher trong giao dịch. | 4312, 658, 14520 |
| source_of_fund | Nguồn tiền sử dụng cho giao dịch. | VTS, Visa Debit,  Ví Momo, Napas, TTT, Visa Credit, NHLK, undefined, Ví Momo |

## Memory

- **MoMo A30:** số lượng active user trên hệ thống MoMo của 30 ngày gần nhất, sử dụng bảng momovn-mimir.MIMIR.iDeA_TRANS_CORE

- **Churned User:** Người dùng được coi là rời bỏ của tháng X, nếu họ không thực hiện bất kỳ giao dịch nào trong tháng X-1, nhưng đã có giao dịch nạp quỹ trong tháng X-2.

- **Khi đếm số lượng quỹ:** sử dụng COUNT(DISTINCT FUND_ID) thay vì COUNT(FUND_ID)

- **User churn (P2P Moneypool):** A user is considered churned in month M if they had at least one transaction in any month prior to M, but had no transactions in month M.

- **Nạp quỹ bao gồm 3 ACTION:** Cash In, CashIn AIOQR (bank-ví), Cash In AIOQR (ví-ví)

- **Người dùng rời bỏ của tháng X:** là những người đã có giao dịch nạp quỹ trong tháng X-1 nhưng không thực hiện bất kỳ giao dịch nào trong tháng X

- **Khi query quỹ có tên ở dạng 'đấu trường tri thức':** sử dụng điều kiện lower(FUND_NAME) LIKE '%đấu trường tri thức%'