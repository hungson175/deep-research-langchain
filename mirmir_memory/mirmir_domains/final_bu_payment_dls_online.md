# BU-Payment: DLS ONLINE

## Dataset Information

**ID:** ca851de3-b3cb-42bf-96d6-979acde0a7da

**Name:** BU-Payment: DLS ONLINE

**Description:** Chi tiết giao dịch Daily Life Service (DLS) online sử dụng trên MoMo kể từ năm 2024

**Instructions:**

**Error Code:** 200

## Schema Information

### Table 1: DLS_ONLINE_NFC_INFO

**Table Name:** momovn-prod.BU_ECOM.DLS_ONLINE_NFC_INFO

**Description:**

| Column Name | Description |
|-------------|-------------|
| MONTH |  |
| FIRST_NFC_DATE | ngày NFC đầu tiên |
| CATE | luôn viết hoa |
| NFC_USER | NFC_user is not null then NFC else Non_NFC |
| NFC_TYPE | not_nfc là chưa NFC, còn lại là đã NFC |
| DEVICE_OS | DEVICES user đang dùng |
| USECASE_TYPE | 1 usecase, 2 usecase, 3 usecase, 4 usecase |
| GMV |  |
| REVENUE |  |
| USER_ID |  |

### Table 2: DLS_GIFT_V3_VER2

**Table Name:** momovn-prod.BU_ECOM.DLS_GIFT_V3_VER2

**Description:** Bảng này chứa thông tin về các quà tặng trong hệ thống MoMo, bao gồm mã quà, tên quà, giá trị quà, và các thông tin liên quan đến giao dịch và người dùng.
- Theo dõi và quản lý thông tin quà tặng được phát hành và sử dụng.
- Phân tích hiệu quả của các chương trình khuyến mãi thông qua các loại quà tặng.
- Đánh giá và tối ưu hóa các chiến dịch quà tặng dựa trên dữ liệu giao dịch và người dùng.

| Column Name | Description |
|-------------|-------------|
| GIFT_ID | Mã định danh của quà tặng. |
| GIFT_NAME | Tên của quà tặng. |
| GIFT_AMOUNT | Giá trị của quà tặng. |
| AGENT_NAME | Tên của ví Momo. |
| PROMO_TYPE | Loại chương trình khuyến mãi. |
| USER_ID | ID của user, SAFE_CAST(USER_ID AS INT64) khi map với USER_ID của bảng Transaction |
| START_DATE | ngày thả voucher |
| END_DATE | ngày hết hạn voucher |
| STATUS |  |
| TRAN_DATE | ngày giao dịch có sử dụng voucher |
| TRAN_ID | transaction id của giao dịch sử dụng voucher, nếu null tức là voucher không được sử dụng |
| GMV | giá trị giao dịch sử dụng voucher |
| VC_AMOUNT | giá trị voucher giảm |
| CB_AMOUNT |  |
| ERROR |  |
| CATE |  |
| SUB_CATE |  |
| MERCHANT |  |
| SUB_MERCHANT |  |

### Table 3: DLS_ALL_TRANS_V3_1

**Table Name:** momovn-prod.BU_ECOM.DLS_ALL_TRANS_V3_1

**Description:**

| Column Name | Description |
|-------------|-------------|
| DATE | Ngày giao dịch |
| DATETIME | Ngày giờ giao dịch |
| MONTH |  |
| USER_ID | user có giao dịch |
| ORDER_ID | transaction |
| TRANS_TYPE |  |
| ALL_IN_ONE | giao dịch qua QR AIO |
| REQ_TYPE | token,app in app, web in app |
| PARTNER_CODE |  |
| STORE_ID |  |
| MONEY_SOURCE |  |
| MONEY_SOURCE_NAME | bao gồm các giá trị như MoMo wallet, Túi thần tài, Paylater(Ví trả sau), Banklink(Ngân hàng liên kết),... |
| SERVICE_CODE | agent dịch vụ |
| BU_NAME |  |
| BU_GROUP_CODE_L1 |  |
| BU_GROUP_CODE_L2 |  |
| GROUP_CODE_L1 |  |
| CATE | luôn viết hoa |
| SUB_CATE |  |
| MERCHANT | luôn viết hoa |
| SUB_MERCHANT |  |
| GMV |  |
| TOTAL_REV |  |
| REFUND_REV |  |
| NET_REV |  |
| PROMO_AMOUNT |  |
| REFUND_AMOUNT |  |
| CASHBACK_AMOUNT |  |
| CASHBACK_AGENTID |  |
| GENDER |  |
| AGE |  |
| AGE_GROUP |  |
| CITY |  |
| REGION |  |
| IS_KYC | đây là KYC, ko phải định danh bằng CCCD găn chip |
| IS_FACE_MATCHING |  |
| CHEATING | cheat user |
| QD2345_CHECK |  |
| NFC_TYPE |  |

## Memory

**TPU:** number of transactions per user

**TIKTOKSHOP:** Khi hỏi là merchant tiktokshop hoặc TIKTOKSHOP thì lấy merchant = 'TIKTOK', cate = 'MARKETPLACE'

**app store:** CATE = "APPLICATION STORE"

**dịch vụ Transport:** CATE = "LOGISTICS"
AND UPPER(SERVICE_CODE) LIKE "%TRANSPORT%"

**Reactive User:** user thanh toán lifetime trước tháng T-1, không thanh toán tháng T-1, quay lại thanh toán tháng T. Chỉ count lần đầu user quay lại

**Khi xử lý giao dịch với MERCHANT:** sử dụng 'sieu thi aeon' thay vì 'aeon'

**Reactivated user của TikTok shop:** là người dùng từng sử dụng TikTok Shop nhưng tháng T-1 không sử dụng TikTok Shop và tháng T quay lại sử dụng, không count trùng lặp nếu như tháng T tiếp tục sử dụng nhiều lần

**Khi tính MAU cho Token Payment:** cần lọc CORE_RESULT_CODE = 0

**MERCHANT phải là 'MÃ THẺ GOOGLE PLAY':** khi truy vấn GMV và Transaction cho Mã Thẻ Google

**Khi xử lý giao dịch với Spotify:** sử dụng LOWER(MERCHANT) LIKE '%spotify%' thay vì LOWER(MERCHANT) = 'spotify'

**Reactive user của merchant:** là user đã thanh toán merchant đó trước tháng T-1, không thanh toán tháng T-1 nhưng quay lại thanh toán tháng T

**nguồn tiền NHLK:** money_source = 2

**hard, heavy:** SQL: USER_SEGMENT = '1. Heavy'
Definition: Nhóm có GMV > 50tr/tháng

**tài xế:** CASE
    WHEN SERVICE_CODE IN ( 'govietbike', 'm4becomgocar_app') THEN 'Tài xế Gojek'
    WHEN SERVICE_CODE IN ( 'disburse.lalamove_disburse', 'm4becomlalamove') THEN 'Tài xế Lalamove'
    WHEN SERVICE_CODE IN ( 'billpaygrab', 'billpaygrabbike') THEN 'Tài xế Grab'
    WHEN (SERVICE_CODE ='aha20151225001' AND  STORE_ID IN ('aha_supplier_topup', 'aha_supplier_transferCOD'))
        OR SERVICE_CODE IN ('m4becomahamove_taixe', 'disburse.ahamove_disburse_v2') THEN 'Tài xế Ahamove'
    ELSE 'Không phải tài xế'
END AS TAIXE

**số lượng user NFC:** NFC thì cột NFC_TYPE IN ('FIRST_NFC','CURRENT_NFC')
Chưa NFC thì lấy cột: NFC_TYPE = 'NOT_NFC'

**Trong cột `CATE` có các dữ liệu sau:**
SME OFFLINE
LOGISTICS
APPLICATION STORE
MARKETPLACE
RETAIL
ADS PAYMENT
DIGITAL CONTENT
FNB
GAME
OTT
INSURANCE
DEVICE FINANCING
Trong cột `MERCHANT` có các dữ liệu sau:
GRAB-ENDUSER
TIKTOK
APPLE
BE GROUP
GOOGLE
GSM
FACEBOOK
VIETLOTT SMS
MWG - BACH HOA XANH
CIRCLE K
TIKTOK LIVE
JOLLIBEE
GS25
7-ELEVEN
FUNTEK
MINISTOP
HIGHLANDS COFFEE
VÍ MOMO GOOGLE VN
FAMILYMART
LAZADA
SPOTIFY
NETFLIX
KINGFOOD
AHAMOVE
V/MC/JCB GOOGLE VN
LALAMOVE
HỒNG TRÀ NGÔ GIA
MM MEGA MARKET
CO.OPMART
COOP FOOD
(nhiều merchant khác nữa)
----
Khi được hỏi liên quan một loại dịch vụ, merchant thì hãy sử dụng các giá trị trên, nếu thấy tương tự thôi thì nhớ confirm lại user. Nếu bị hỏi tới một dịch vụ hay merchant quá lạ thì phải hỏi lại, không thì nhờ user feedback cách làm đúng tránh truy vấn không ra dữ liệu nào

**Reactive User tháng T (theo cate Logistics):** là người dùng đã từng thanh toán bất kỳ merchant của cate Logistics với trước tháng T-1, không phát sinh thanh toán với cate Logistics trong tháng T-1, và quay lại thanh toán với cate Logistics trong tháng T. Reactive user by merchant là khi người dùng quay lại thanh toán với cate Logistics với merchant nào thì chỉ tính cho merchant đó, không tính reactive trùng lặp cho bất kỳ merchant nào khác mà họ có thể thanh toán sau đó.

**Reactive User tháng T (theo merchant Tiktok Shop):** là người dùng đã từng thanh toán tiktok shop với trước tháng T-1, không phát sinh thanh toán Tiktok shop trong tháng T-1, và quay lại thanh toán với Tiktok shop trong tháng T. Không tính reactive trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**RETAINED USER:** = người dùng đã dùng dịch vụ Marketplace vào tháng T-1 và tháng T tiếp tục quay lại sử dụng Marketplace. Không tính retain trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**Khi xử lý giao dịch online:** không sử dụng CORE_RESULT_CODE = 0

**New user (người dùng lần đầu):** is a user who has their first token transaction in the specified month.

**Retain user TikTok Shop:** là user sử dụng TikTok Shop ở tháng T và tháng T+1 tiếp tục sử dụng dịch vụ của TikTok Shop, không count trùng lặp nếu user tiếp tục sử dụng giao dịch tiếp theo trong tháng T+1

**RETAINED USER:** = người dùng đã dùng dịch vụ vào tháng trước và tiếp tục dùng trong tháng này

**'xanh SM', 'GSM', 'xanh':** tương ứng với merchant = 'GSM' trong data

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo)

**ads payment:** CATE = "ADS PAYMENT"

**GRAB-ENDUSER:** MERCHANT = "GRAB-ENDUSER"

**Churn user của tháng T:** là lifetime user thanh toán trước tháng T-1, không quay lại thanh toán trong tháng T

**SPU:** spending per user

**RETAINED USER:** = người dùng đã sử dụng dịch vụ TikTok Shop trong tháng T-1 và tháng T quay lại sử dụng dịch vụ TTS. Không tính retain trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo). new to merchant của tiktok shop là nhóm người dùng lần đầu sử dụng dịch vụ TikTok Shop trong tháng T và không tính new to merchant trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**Retained user của merchant:** là user đã thanh toán merchant đó tháng T-1 và quay lại thanh toán tháng T

**Reactive User tháng T (theo cate):** là người dùng đã từng thanh toán cate đó trước tháng T-1, không thanh toán cate đó trong tháng T-1, và quay lại thanh toán cate đó trong tháng T.

**tiktok:**
# Tiktok Shop
WHERE MERCHANT = "TIKTOK"
  AND CATE = "MARKETPLACE"
# Tiktok Live
WHERE MERCHANT = "TIKTOK LIVE"
# Tiktok Ads
WHERE MERCHANT = "TIKTOK"
  AND CATE = "ADS PAYMENT"

**MAU:** tức là số lượng user

**merchant ads:** MERCHANT = {MERCHANT_NAME}
AND CATE = "ADS PAYMENT"

**NFC:** NFC nghĩa là xác thực sinh trắc học. Để lấy status NFC của người dùng thì sẽ sử dụng
-Table: momovn-prod.BU_ECOM.DLS_ALL_TRANS_V3_1
-Column: NFC_TYPE
-Value:
+NOT_NFC: Tháng đó người dùng chưa NFC
+CURRENT_NFC: Tháng đó người dùng đã từng NFC
+FIRST_NFC: Tháng đó là tháng đầu tiên người dùng NFC

**facebook ads:** MERCHANT = "FACEBOOK"
AND CATE = "ADS PAYMENT"

**User type:**
light user: User có GMV trong tháng < 3tr/ tháng -
medium user: User có GMV từ 3tr đến 50tr/ tháng -
hardcore user: User có GMV trên 50tr/ tháng -
Nhờ hỏi thanh toán này là khoản nào hay toàn bộ

**RETAINED USER:** = người dùng đã dùng dịch vụ vào tháng trước và tiếp tục dùng trong tháng này

**RETAINED USER:** = người dùng đã dùng dịch vụ vào tháng trước và tiếp tục dùng trong tháng này

**NTC:** = New To Category (người dùng thực hiện giao dịch đầu tiên với một danh mục dịch vụ trong kỳ báo cáo)

**Reactive User tháng T (theo cate Marketplace):** là người dùng đã từng thanh toán bất kỳ merchant của cate Marketplace với trước tháng T-1, không phát sinh thanh toán với cate Marketplace trong tháng T-1, và quay lại thanh toán với cate Marketplace trong tháng T. Không tính reactive trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**New user của Ads payment ở tháng T:** là nhóm người dùng lần đầu sử dụng dịch vụ ads payment vào tháng T, không tính lặp lại nếu người dùng tiếp tục sử dụng dịch vụ vào tháng T

**MERCHANT 'tch':** tương ứng với 'the coffee house'

**Khi xử lý MERCHANT:** sử dụng LIKE '%value%' thay vì = 'value'

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo).

**Khi truy vấn giao dịch token:** cần lọc CORE_RESULT_CODE = 0

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo). new to merchant của tiktok shop là nhóm người dùng lần đầu sử dụng dịch vụ TikTok Shop trong tháng T và không tính new to merchant trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**New to cate Marketplace:** là số lượng user lần đầu sử dụng market place trong tháng T, không count lặp lại nếu tiếp tục sử dụng trong tháng T

**Cột AGE_GROUP:** lưu trữ nhóm tuổi dưới dạng chuỗi văn bản theo một định dạng cụ thể. Ví dụ, giá trị '[2].18-22' đại diện cho nhóm người dùng có độ tuổi từ 18 đến 22. Khi truy vấn, cần sử dụng chính xác định dạng này (ví dụ: AGE_GROUP = '[2].18-22' ).

**medium:** SQL: USER_SEGMENT = '2. Medium'
Definition: Nhóm có GMV > 3-50tr/tháng

**youtube premium:** Để lấy được giao dịch này cần sử dụng cột SUB_MERCHANT như sau:
SUB_MERCHANT IN ("APPLE YOUTUBE PREMIUM"', "GOOGLE YOUTUBE PREMIUM")

**tiktok ads:** MERCHANT = "TIKTOK"
AND CATE = "ADS PAYMENT"

**usecase:** Usecase: số cate user sử dụng 1 tháng, tính trong PAYMENT và TRANSFER

**RETAINED USER:** = người dùng đã sử dụng dịch vụ TikTok Shop trong tháng T-1 và tháng T quay lại sử dụng dịch vụ TTS. Không tính retain trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo)

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo). new to merchant của tiktok shop là nhóm người dùng lần đầu sử dụng dịch vụ TikTok Shop trong tháng T và không tính new to merchant trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**Reactive User tháng T (theo cate Marketplace):** là người dùng đã từng thanh toán bất kỳ merchant của cate Marketplace với trước tháng T-1, không phát sinh thanh toán với cate Marketplace trong tháng T-1, và quay lại thanh toán với cate Marketplace trong tháng T. Không tính reactive trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**Reactive User tháng T (theo cate Marketplace):** là người dùng đã từng thanh toán bất kỳ merchant của cate Marketplace với trước tháng T-1, không phát sinh thanh toán với cate Marketplace trong tháng T-1, và quay lại thanh toán với cate Marketplace trong tháng T. Không tính reactive trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**retention rate:** = user có thanh toán tháng T-1 và quay lại thanh toán trong tháng T

**Reactive User tháng T (theo cate Marketplace):** là người dùng đã từng thanh toán bất kỳ merchant của cate Marketplace với trước tháng T-1, không phát sinh thanh toán với cate Marketplace trong tháng T-1, và quay lại thanh toán với cate Marketplace trong tháng T. Không tính reactive trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**RETAINED USER:** = người dùng đã sử dụng dịch vụ TikTok Shop trong tháng T-1 và tháng T quay lại sử dụng dịch vụ TTS. Không tính retain trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**Cột ngày giao dịch trong bảng `momovn-prod.BU_ECOM.DLS_ALL_TRANS_V3_1`:** là `DATE`

**NTMC:** = New To Merchant (người dùng thực hiện giao dịch đầu tiên với merchant trong kỳ báo cáo). new to merchant của tiktok shop là nhóm người dùng lần đầu sử dụng dịch vụ TikTok Shop trong tháng T và không tính new to merchant trùng lặp nếu họ có thể thanh toán sau đó trong tháng T.

**New to merchant ở tháng T:** là user lần đầu thanh toán merchant đó trong tháng T. Retained user với merchant là user đã thanh toán merchant đó tháng T-1 và quay lại thanh toán merchant đó tháng T. Reactive user với merchant là user đã thanh toán merchant đó trước tháng T-1, không thanh toán tháng T-1 và quay lại thanh toán merchant đó tháng T

**Reactive user của TikTok shop:** là người dùng từng sử dụng TikTok Shop nhưng tháng T-1 không sử dụng TikTok Shop và tháng T quay lại sử dụng, không count trùng lặp nếu như tháng T tiếp tục sử dụng nhiều lần

**Retain user TikTok Shop:** là user sử dụng TikTok Shop ở tháng T và tháng T+1 tiếp tục sử dụng dịch vụ của TikTok Shop, không count trùng lặp nếu user tiếp tục sử dụng giao dịch tiếp theo trong tháng T+1