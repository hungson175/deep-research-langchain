# OTA Domain Metadata

## Domain Information
- **Domain ID**: 7172ddb9-dc48-40d4-bff7-1aa74f6ff435
- **Domain Name**: OTA
- **Description**: Record information about:
  - (1): User behaviors across airline & non-air booking funnel (search → view → payment)
  - (2): Revenue tracking & performance by provider, route type, booking window, segment, holiday type

## Tables Overview

This domain contains 2 main tables with comprehensive tracking of user behaviors and revenue metrics for Online Travel Agency (OTA) services.

---

## Table 1: momovn-prod.REPORT.2022_HUY_EVENTS_LANDINGPAGE_V2_PIVOTED_UNION

### Table Description
Bảng này tổng hợp các sự kiện người dùng từ trang đích landingpage qua nhiều phiên bản. Dữ liệu trong bảng có thể được sử dụng để phân tích hành vi người dùng, xác định hiệu quả của các tính năng và kiểm soát doanh thu từ các sự kiện trên ứng dụng.

**Key Use Cases:**
- Xác định và phân tích sự kiện người dùng dựa trên các thông số như thời gian, thiết bị và phiên bản ứng dụng
- Kiểm tra doanh thu và lượng giao dịch thành công, thất bại từ các sự kiện
- Theo dõi và đo lường hiệu quả chuyển đổi từ các khối và điểm gắn trên ứng dụng

### Column Details

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| **EVENT_DATE** | Ngày diễn ra sự kiện | 2021-10-20, 2022-07-20, 2022-10-10 |
| **EVENT_TIME** | Thời gian chi tiết diễn ra sự kiện | 2023-11-09 16:42:03.552, 2023-11-09 07:24:29.218 |
| **USER_ID** | Mã định danh của người dùng thực hiện sự kiện | 52486046, 52835360, 38322143 |
| **DEVICE_OS** | Hệ điều hành của thiết bị người dùng | Android, ANDROID, IOS, iOS |
| **APP_VERSION** | Phiên bản ứng dụng mà người dùng đang sử dụng | 3.0.0-rc4, 4.2.2-beta.10, 4.2.25-beta.4 |
| **SESSION_ID** | Mã định danh của phiên làm việc | 69529956_1679284950, 33007378_1679249913 |
| **EVENT_NAME** | Tên của sự kiện diễn ra | feature_trans_history, service_screen_interacted, service_search_result_clicked, service_image_clicked, service_search_clicked, trans_success, service_product_continued, service_search_result_viewed, service_hotel_agoda, service_field_inputed, service_hotel_agoda_details, service_screen_displayed, service_image_swiped, trans_confirm, service_hotel_merge, service_service_clicked, trans_success_be, service_screen_viewed, service_product_viewed, service_hotel_agoda_guest, trans_fail_be, session_start, service_transport_airlines, service_button_continued, service_product_button_clicked, service_transport_road, service_field_clicked, service_block_viewed, service_hotel_agoda_result, trans_result_payment_multibill, trans_fail, service_search_inputed, service_icon_clicked, service_tab_clicked, service_transport_landing_page, service_pocket, service_purchase_clicked, service_component_inputed, sevice_screenshot, service_component_displayed, ops_request_be, miniapp_load, trans_confirm_screen, service_product_clicked, service_block_swiped, service_component_clicked, service_filter_clicked, service_category_clicked, service_transport_rail, service_button_clicked |
| **SCREEN_DEFINE** | Định nghĩa màn hình nơi sự kiện diễn ra | bus_home, man_hinh_danh_sach_khach_san, flight_information, return_filter, hotel_amenities, mh_thong_tin_phong, sof_selection2, SeatMapScreen, sof_selection1, Trans BE, null, seat_departure, acillary_select_covid_test, bus_departure_loading, hotellist, trip_information, promo, ancillary_select_meal, MerchantImageScreen, Buses, roominfo, manage_recent_search, ancillary, Experience, pocket, mh_thong_tin_dat_phong, home, payment_information, pickup_and_dropoff_point_return, trip_detail, listing screen, bus_departure_seatmap, Hourly Hotel, train_departure_listing, destination, calendar, train_pocket_history, choose_date, listing_filter, hotel_main, arrival_listing, departure_date, departure_listing, dldl, pickup_and_dropoff_point_departure /pickup_and_dropoff_point_return , departure / arrival, pickup_and_dropoff_point_departure / pickup_and_dropoff_point_return, bus_departure_filter, DateScreen, free_ancillary |
| **TYPE_KEY** | Loại khóa của sự kiện | 230815_dls_ota_native_train_all_mshock_15k_min300k, e_s12_aw_500k_241211_giam_100pt40k_oq4sp, 220524_ota_hourlyhotel_btl_69k |
| **BLOCK** | Khối liên quan đến sự kiện | MOMO Đề Xuất, ƯU ĐÃI ĐẶC BIỆT, hotel_widget_location, #HOT GỢI Ý, booking_experiences_vinwonders, booking_hotel_agoda, vietjet, pre_trip_widget, booking_experiences_sunworld, booking_train_vnr, travel_port_1g, Vi vu quốc tế, vna, KHÁM PHÁ THÊM, booking_vexere, HOT HOTEL, bamboo, SIÊU SALE 12.12 - Giảm đến 1,2 TRIỆU, destination, recent_step, ota_train_vnr, FLASH SALES, ota_bus_distribusion, ota_airline_vna, ota_airline_hpl_bav, m4becommiotominiapp, vietjet_flik, booking_experiences_kkday, SPECIAL OFFER, khach_san_gia_tot, MOMO SUGGESTION, MOMO GỢI Ý, ota_bus_futa, recent_search, MoMo Choice giảm đến 1 triệu, popular_service, airline.hpl, booking_experiences_sontien, MOMO ĐỀ XUẤT, SUPER SALE 12.12 - Discounts up to 1,2 MILLION VND, footer, booking_experiences_ezcloud, popular, TOP ĐƯỢC BÌNH CHỌN, booking_hotel_expedia, MOMO Choice, NEW HOTEL, KHÁCH SẠN NỔI BẬT, guidebook, Giảm đến 50% Black Friday |
| **MOUNT_POINT** | Điểm gắn nơi sự kiện xảy ra | 37718360188, 37719100632, 37712361084 |
| **n_block** | Khối mới liên quan đến sự kiện | recent_step, popular_service, guidebook, recommend_service |
| **n_button_name** | Tên nút mới trong sự kiện | faq, price, napas_vnr_paybill_new, hotline_gold, seat_btn, Stelia Beach Resort, delete_history, checkbox_lunar, choose_ticket, invoice, platinum_vietnam_airlines_lotusmiles, chia_se, view_detail, 2024_donate_ota, account, Thừa Thiên - Huế, Anantara Hoi An Resort, change_hotelinfo, hold_coutdown, Mai Tuan Chanh Mon A Hotel, Hotel Nikko Saigon, Diamond Stars Ben Tre Hotel, Đóng, other, Khách sạn Aristo Saigon, activate_now, change_special_request, filter_hotel, save_special_request, checked_baggage, 4, favorite_collection, fare_class, Đà Nẵng, toggle_passbook, Melia Hanoi, business_lounge, Nha Trang, experience_booking, InterContinental Danang Sun Peninsula Resort by IHG, Park Hyatt Saigon, Jardin Du Mekong Homestay, ins_comprehensive_travel, cancel, Sky Gem Central Hotel, trip_information, travelsim, confirm_policy, trip_infomation, vbi_international_travel |
| **n_component_name** | Tên thành phần mới trong sự kiện | quick_filter_seat_type, block, int, student_pass, ticket_share, expand_ancillary_outbound, bus_sorting, box_trip_info, boutique_collection, insurance, hotel_widget_location, resuming_booking, sorting, favorite_collection, snackbar, change_special_request, dom, contact_info, change_hotelinfo, pre_trip_widget, bus_ticket, ticket_price_decrease_popup, trip_information, remind_paxname, button_pay_now_paylater, transit_note, ticket_price_increase_popup, search_recently, activate_paylater_in_airline, option_room, vc_bundled_voucher_bs, trip_infomation, buyer info, pu_screenshot, air_noti, request_check_saved_bill, add_special_request, ancillary, popular_destination, home, student_pass_bts, hotel, departure_info, bottom_sheet, installment_bottomsheet, update_new_ticket, Cancelled_booking_successfully_toast, cross_sell_banner, new_collection, choose_date |
| **n_destination** | Điểm đến mới của sự kiện | Phan Thiết, Đà Nẵng, Vũng Tàu, Hội An, Đà Lạt, Hạ Long, Sa Pa, Ninh Bình, Phú Quốc |
| **n_entry_point** | Điểm vào mới của sự kiện | landing_page_ota |
| **n_feature_10** | Tính năng thứ 10 trong sự kiện mới | (No data) |
| **n_feature_8** | Tính năng thứ 8 trong sự kiện mới | (No data) |
| **n_position** | Vị trí mới trong sự kiện | 6, 8, 6.0 |
| **n_ref_id** | ID tham chiếu mới trong sự kiện | (No data) |
| **n_screen_name** | Tên màn hình mới trong sự kiện | bus_home, man_hinh_danh_sach_khach_san, return_filter, hotel_amenities, flight_information, bus_departure_loading, mh_thong_tin_phong, sof_selection2, ancillary_select_meal, MerchantImageScreen, null, SeatMapScreen, trip_information, sof_selection1, seat_departure, acillary_select_covid_test, manage_recent_search, Experience, hotellist, ancillary, home, payment_information, promo, Buses, train_departure_listing, train_pocket_history, mh_thong_tin_dat_phong, roominfo, hotel_main, listing_filter, pickup_and_dropoff_point_return, arrival_listing, trip_detail, bus_departure_seatmap, Hourly Hotel, pocket, departure_date, choose_date, listing screen, onboarding, departure / arrival, pickup_and_dropoff_point_departure /pickup_and_dropoff_point_return , departure_listing, dldl, calendar, destination, pickup_and_dropoff_point_departure / pickup_and_dropoff_point_return, bus_departure_filter, booking_guide, choose_room_guest |
| **n_service** | Dịch vụ mới liên quan đến sự kiện | landing_page_ota |
| **n_service_id** | ID dịch vụ mới liên quan đến sự kiện | transport_airlines, transport_bus, booking_experiences_vinwonders, go2joy, booking_airline, booking_train, booking_hotel, m4becommiotominiapp, ota_hotel, booking_bus, transport_train |
| **n_service_name** | Tên dịch vụ mới liên quan đến sự kiện | landing_page_ota, ota_landing_page, topbar_paymentcode, topbar_scancode |
| **n_time_load** | Thời gian tải mới của sự kiện | 280, 459, 1148 |
| **n_trans_confirm** | Xác nhận giao dịch mới trong sự kiện | 72578770_1679310469, 65443201_1679301264, 36916612_1679304985 |
| **n_trans_confirm_screen** | Màn hình xác nhận giao dịch mới trong sự kiện | 67565171_1679264301, 43408455_1679272678, 54631593_1679325093 |
| **n_trans_fail** | Giao dịch thất bại mới trong sự kiện | 57927799_1659539667, 19391790_1600214624, 51072305_1647266598 |
| **n_trans_success** | Giao dịch thành công mới trong sự kiện | 42306021_1679295261, 42599303_1679307257, 43204877_1679314077 |
| **SUB_CATE** | Phân loại phụ của sự kiện | 01. AIRLINE, 09. LANDINGPAGE_OTA, 02. TRAIN, 03. BUS, 04. HOTEL, 07. HOTEL HOURLY, 05. EXPERIENCE |
| **TYPE_USER** | Loại người dùng thực hiện sự kiện | DIRECT, LDP |
| **EVENT_TIME_CHECK** | Thời gian kiểm tra sự kiện | 2020-07-28 07:02:39.017079, 2020-07-28 11:26:07.243008, 2020-07-28 12:05:39.271015 |
| **ID** | Mã định danh của sự kiện | 37729025773, 37740484959, 37727853161 |
| **TOTAL_AMOUNT** | Tổng số tiền liên quan đến sự kiện | 827000, 1783000, 3856000 |
| **REVENUE** | Doanh thu từ sự kiện | 7499.9999999999991, 22516.363636363636, 17775.81818181818 |
| **REVENUE_AFTER_REFUND** | Doanh thu sau khi hoàn tiền từ sự kiện | 13480.363636363636, 21818.181818181813, 22017.272727272728 |
| **CONTRIBUTION_SOURCE** | Nguồn đóng góp của sự kiện | home, LDP |
| **new_to_cate_datetime** | Thời gian mới phân loại sự kiện theo danh mục | 2023-01-28 18:53:00, 2022-11-04 10:22:20, 2022-05-13 09:34:26 |
| **is_existing_user** | 0: không phải người dùng hiện có, 1: là người dùng hiện có | 0, 1 |

---

## Table 2: momovn-prod.REPORT.ota_dwd_ota_user_funnel_traffic_source_daily

### Table Description
Bảng này lưu trữ dữ liệu về hành vi người dùng theo từng bước trong quy trình đặt dịch vụ OTA (Online Travel Agency) hàng ngày, bao gồm các nguồn lưu lượng truy cập. Các thông tin có thể thu thập từ bảng này bao gồm: theo dõi liệu người dùng đã tải trang chủ, thực hiện tìm kiếm, hoặc tải thông tin thanh toán hay chưa; xác định liệu người dùng đã nhập thông tin hành khách hay đã thực hiện giao dịch; phân tích các nguồn lưu lượng truy cập dẫn đến sự kiện.

### Column Details

| Column Name | Description | Example Data |
|-------------|-------------|--------------|
| **event_date** | Ngày diễn ra sự kiện | 2025-06-03, 2025-02-17, 2024-12-14 |
| **user_id** | Mã định danh người dùng duy nhất | 79546140, 20277440, 44447911 |
| **sub_cate** | Danh mục phụ của dịch vụ hoặc sự kiện | 03. BUS, 02. TRAIN, 01. AIRLINE, 04. HOTEL |
| **has_load_home** | Biểu thị liệu người dùng đã tải trang chủ hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_search** | Biểu thị liệu người dùng đã thực hiện tìm kiếm hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_load_listing** | Biểu thị liệu người dùng đã tải trang danh sách sản phẩm/dịch vụ hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_load_seat_departure_OR_fare_group_OR_hotel_info** | Biểu thị liệu người dùng đã tải trang chọn chỗ ngồi, nhóm giá vé hoặc thông tin khách sạn hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_passenger_info** | Biểu thị liệu người dùng đã nhập thông tin hành khách hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_ancillary** | Biểu thị liệu người dùng đã chọn các dịch vụ bổ sung hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_load_payment_info** | Biểu thị liệu người dùng đã tải thông tin thanh toán hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_load_ttat** | Biểu thị liệu người dùng đã tải trang TTAT (Thời gian thực hiện hành động) hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **has_transaction** | Biểu thị liệu người dùng đã thực hiện giao dịch hay chưa (1 nếu có, 0 nếu không) | 1, 0 |
| **transaction** | Trạng thái của giao dịch (có thể là mã số hoặc boolean) | 16, 4, 17 |
| **traffic_source_event** | Nguồn lưu lượng truy cập dẫn đến sự kiện này | official_account, offline_hub, hdss_v2, rewards_lotusmiles, slot_08, guide_payment_service_sendo, folder_tra_sau, chatbot, vna, ins_marketplace, transfer_p2p_send_lucky_money, expedia, tabbar_chat, user_profile_ota, earlybirdlx2024, agency_cashout, water_hcm, ekyc_confirm_information, bkhn_school_fee, wheel_90, transaction_result_revamp, credit_bnpl_bill_info, bank_sacom, miniapp.fw3kDtFJDR1pZuoLfw0E.starbucks, credit_paylater_new_installment_management, tabbar_transaction, fund_detail, brand_backtowork_2025, onlinepanel_entry, payment_screen, bv_nhi_ha_noi, source_info, guide_payment_service_google, hourly_hotel, my_qrcode, evnspc_lamdong, topup_data_mobi, market_deal_brand_detail, helpcenter_common_problems, p2p_send_gift, brand_valentine_2025, mobilecombo, folder_hoc_phi, bamboo, wheel_69, airline_landing_page, 105, credit_collection_vietcredit, edit_alias_name, undefined |

---

## Memory Section: Business Rules and Guidelines

The OTA domain contains 27 critical memory entries that define business logic, calculation methods, and operational guidelines. These rules must be followed when working with OTA data:

### User Calculation Rules
1. **MAU Calculation**: Luôn sử dụng cột user_payment trong bảng momovn-prod.REPORT.2023_TAN_OTA_COMPREHENSIVE_ALL_WITH_INCENTIVE để tính các chỉ số MAU/ active user/ user đã mua/ user thanh toán
2. **International Flight MAU**: Để tính số MAU của máy bay quốc tế, dùng COUNT(DISTINCT USER_PAYMENT)
3. **MoMo New Users**: Khi hỏi số lượng người dùng mới của MoMo, luôn dùng cột NEWUSER_MOMO_EXCL_CASHIN_OUT
4. **Date Column for MAU**: Dùng cột date trong bảng momovn-prod.REPORT.2023_TAN_OTA_COMPREHENSIVE_ALL_WITH_INCENTIVE để tính MAU
5. **User Payment Restriction**: Không dùng cột INITIATOR để tính toán metrics liên quan đến user

### Transaction Status and Revenue Rules
6. **Successful Transactions**: STATUSID = 2 đại diện cho giao dịch thành công
7. **Failed Transactions**: Statusid = 6 để lọc các giao dịch thất bại
8. **Revenue Calculation**: Khi tính doanh thu, cần thêm điều kiện STATUSID = 2
9. **Default Transaction Filter**: Luôn thêm statusid = 2 để lọc ra những giao dịch thành công

### Service Category and Platform Filtering
10. **Airline Filter**: Khi user đề cập đến từ 'bay', phải filter sub_cate = '01. AIRLINE'
11. **International Flights**: Khi đề cập đến vé máy bay quốc tế thì filter flight_region <> 'VN'
12. **Payment Gateway**: Nếu đề cập đến payment gateway, pmt hay cổng thanh toán, filter platform = 'Partner'
13. **Native App Filter**: Nếu đề cập đến native hay app momo, filter platform = 'App Momo'
14. **Flight Average Calculation**: Khi tính trung bình số chuyến bay tháng 07, cần lọc dữ liệu với PLATFORM = 'App Momo' và SUB_CATE = '01. AIRLINE'
15. **Flight Number Usage**: Khi tính trung bình số chuyến bay, dùng cột flight_no thay vì pnr_booking_code

### New User Identification
16. **New User Fields**: NEWUSER_MOMO và NEWUSER_OTA chứa ID người dùng thay vì cờ 0 hoặc 1
17. **OTA New User Logic**: Nếu cột NEWUSER_OTA có giá trị (không phải NULL), người dùng đó là người dùng mới của dịch vụ OTA
18. **MoMo New User Logic**: Nếu cột NEWUSER_MOMO có giá trị (không phải NULL), người dùng đó là người dùng mới của MoMo

### Payment Source Mapping (MONEYSOURCE)
19. **Payment Source Codes**:
    - 1 = MOMO
    - 2 = NHLK (Ngân hàng liên kết)
    - 3 = NAPAS
    - 4 = VISA_DEBIT
    - 5 = VISA_CREDIT
    - 6 = GOLDEN_POCKET (Túi thần tài)
    - 7 = PAYLATER (Ví trả sau)
    - 8 = CASHBACK
    - 9 = CCM_VIRTUAL_CREDIT_CARD
    - 10 = BNPL
    - 11 = Newton
    - 12 = Direct Debit
    - 13 = Quy Nhom

### Service Code to Merchant Mapping
20. **Airline Merchant Mapping**:
    - SERVICE_CODE 'm4bthaiairasia' maps to MERCHANT 'AIRASIA'
    - SERVICE_CODE 'm4becomvnaweb' maps to MERCHANT 'VN AIRLINES'
21. **Vietnam Airlines Service**: Khi xử lý dữ liệu Vietnam Airlines luồng Inapp, sử dụng SERVICE_ID_MBI in ('ota_airline_vna', 'airline.hpl') thay vì SERVICE_CODE = 'm4becomvnaweb'

### Geographic Classification
22. **Regional Classification**: Phân loại địa điểm theo miền Bắc, Trung, Nam dựa trên danh sách các tỉnh/thành
23. **North-South Division**: Phân loại khu vực Bắc và Nam dựa trên vĩ tuyến 17: từ vĩ tuyến 17 về phía Bắc là Bắc, về phía Nam là Nam
24. **SGN Departure**: Khi xử lý vấn đề liên quan tới danh sách người dùng mua vé bay từ SGN, dùng departure_ư_code cho cột departure_station_code

### Business Metrics and Calculations
25. **Conversion Rate Formula**: CR được tính bằng công thức: count(distinct case WHEN EVENT_DATE <= date'2022-05-25' and c_trans_success is not null then USER_ID when EVENT_DATE > date'2022-05-25' and EVENT_NAME = 'trans_success_be' THEN USER_ID end)/count(distinct USER_ID) trong bảng momovn-prod.REPORT.2022_HUY_EVENTS_LANDINGPAGE_V2_PIVOTED_UNION
26. **Retention Calculation**: Retention được tính bằng số lượng người dùng cùng tồn tại ở tháng trước và tháng hiện tại, sau đó chia cho số lượng người dùng tháng trước đó
27. **Return User Percentage**: Tính phần trăm người dùng quay lại bằng cách lấy số lượng người dùng tìm kiếm trong cả tháng 4 và tháng 5 chia cho tổng số người dùng tìm kiếm trong tháng 4, không phải tháng 5

### Primary Data Source
**Main Table**: Dùng data thuộc bảng momovn-prod.REPORT.2023_TAN_OTA_COMPREHENSIVE_ALL_WITH_INCENTIVE

---

## Data Quality Notes

- **Content Language**: Vietnamese business descriptions and column names are preserved as they appear in the source system
- **Data Types**: All example data represents actual production values with realistic formats and ranges
- **Memory Rules**: All 27 business rules must be applied when querying or analyzing this data
- **Schema Integrity**: Two-table structure covers complete user journey from landing page through transaction completion
- **Revenue Tracking**: Comprehensive revenue metrics including pre and post-refund calculations