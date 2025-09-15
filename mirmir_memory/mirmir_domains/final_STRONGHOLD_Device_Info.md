# STRONGHOLD - Device Info

## Domain Overview

**Domain ID:** 7994ad65-873f-4c9d-9c90-f49377367892
**Name:** STRONGHOLD - Device Info
**Description:** This data model captures device information of MoMo users, extracted during specific events at various touchpoints within the MoMo app, such as login, relogin, and refresh token. The tables are designed to support in-depth analysis of user devices, uncover insights, and extract features for AI/ML models.

## Table Information

### Table 1: momovn-prod.STRONGHOLD_ANALYTICS.D_DEVICE

**Description:** Bảng 'momovn-prod.STRONGHOLD_ANALYTICS.D_DEVICE' chứa dữ liệu phân tích chi tiết về các thiết bị, bao gồm thông số kỹ thuật phần cứng, tính năng và khả năng hỗ trợ.

**Các ứng dụng tiềm năng của bảng này bao gồm:**
- Xác định các thương hiệu và model thiết bị phổ biến trong người dùng để hỗ trợ quảng cáo theo mục tiêu và tối ưu hóa ứng dụng.
- Phân tích các thông số thiết bị để đưa ra nội dung hoặc khuyến nghị cá nhân dựa trên khả năng thiết bị.
- Hỗ trợ phát triển và kiểm thử ứng dụng bằng cách cung cấp thông tin tổng quan về tính năng và khả năng tương thích của thiết bị.

#### Column Descriptions

| Column Name | Description |
|-------------|-------------|
| D_DEVICE_KEY | Khóa chính của bảng D_DEVICE. |
| DEVICE_UUID | Key phân biệt giữa các thiết bị. |
| BATTERY__ADR_BATTERY_TYPE | Loại pin của thiết bị (Li-ion, Li-Po, v.v.). Ví dụ: Li-ion. |
| CPU__ACTUAL_RAM | Dung lượng RAM thực tế của thiết bị. Ví dụ: 8GB, 4GB. |
| CPU__ADR_ABI | Hệ kiến trúc của ứng dụng hoặc thiết bị (x86, ARM, v.v.). Ví dụ: arm64-v8a. |
| CPU__CORES | Số lõi CPU của thiết bị. Ví dụ: 8, 6. |
| CPU__CPU_MODEL | Mẫu CPU của thiết bị. Ví dụ: Exynos 2100, A14 Bionic. |
| DEVICE__ADR_BOOT_LOADER | Phiên bản bootloader của thiết bị, giúp khởi động hệ thống. Ví dụ: G991BXXU3AUDA. |
| DEVICE__ADR_HARDWARE_NAME | Phần cứng của thiết bị. Ví dụ: qcom, Apple. |
| DEVICE__ADR_HOST | Tên máy chủ nơi hệ điều hành được build. Ví dụ: abc-host. |
| DEVICE__ADR_ID | ID duy nhất của thiết bị Android. Còn gọi là Secure ID. Ví dụ: 97c9c85ff3b44e. |
| DEVICE__BRAND | Thương hiệu của thiết bị. Ví dụ: Galaxy, iPhone. |
| DEVICE__MANUFACTURER | Nhà sản xuất của thiết bị. Ví dụ: Samsung, Apple. |
| DEVICE__MODEL | Mã model của thiết bị. Ví dụ: SM-G991B, iPhone13,2. |
| DISPLAY__SCREEN_RESOLUTION | Độ phân giải của màn hình. Ví dụ: 1080x2400. |
| FEATURES__HAS_APP_WIDGETS | Thiết bị có hỗ trợ widgets (tiện ích trên màn hình chính) hay không. |
| FEATURES__HAS_AUDIO_LOW_LATENCY | Thiết bị có hỗ trợ âm thanh độ trễ thấp hay không. |
| FEATURES__HAS_BLUETOOTH | Thiết bị có hỗ trợ Bluetooth hay không. |
| FEATURES__HAS_CAMERA_FLASH | Thiết bị có đèn flash cho camera hay không. |
| FEATURES__HAS_CAMERA_FRONT | Thiết bị có camera trước hay không. |
| FEATURES__HAS_CDMA | Thiết bị có hỗ trợ mạng CDMA (một loại mạng di động cũ) hay không. |
| FEATURES__HAS_CONSUMER_IR | Thiết bị có hỗ trợ tia hồng ngoại IR để điều khiển từ xa hay không. |
| FEATURES__HAS_DYNAMIC_ISLAND | Thiết bị có hỗ trợ Dynamic Island (một phần thiết kế động trên màn hình của iPhone) hay không. |
| FEATURES__HAS_FINGERPRINT_RECOGNITION | Thiết bị có hỗ trợ nhận diện vân tay hay không. |
| FEATURES__HAS_GAMEPAD_SUPPORT | Thiết bị có hỗ trợ tay cầm chơi game hay không. |
| FEATURES__HAS_GMS | Thiết bị có hỗ trợ Google Mobile Services (dịch vụ di động của Google) hay không. |
| FEATURES__HAS_GSM | Thiết bị có hỗ trợ mạng GSM hay không. |
| FEATURES__HAS_HIFI_SENSORS | Thiết bị có các cảm biến chất lượng cao (ví dụ như cảm biến chuyển động chính xác cao) hay không. |
| FEATURES__HAS_HMS | Thiết bị có hỗ trợ Huawei Mobile Services hay không. |
| FEATURES__HAS_MICROPHONE | Thiết bị có micro hay không. |
| FEATURES__HAS_MULTITOUCH | Màn hình của thiết bị có hỗ trợ cảm ứng đa điểm hay không. |
| FEATURES__HAS_NFC | Thiết bị có hỗ trợ NFC (giao tiếp tầm ngắn) hay không. |
| FEATURES__HAS_NOTCH | Thiết bị có thiết kế notch (phần khuyết trên màn hình) hay không. |
| FEATURES__HAS_PRINTING | Thiết bị có hỗ trợ in ấn qua mạng hay không. |
| FEATURES__HAS_PROFESSIONAL_AUDIO | Thiết bị có hỗ trợ âm thanh chuyên nghiệp (ví dụ như hỗ trợ âm thanh không nén) hay không. |
| FEATURES__HAS_SIP | Thiết bị có hỗ trợ SIP (giao thức dùng cho gọi thoại qua mạng internet) hay không. |
| FEATURES__HAS_SIP_BASED_VOIP | Thiết bị có hỗ trợ VoIP dựa trên SIP hay không. |
| FEATURES__HAS_USB_ACCESSORY | Thiết bị có hỗ trợ chế độ USB Accessory (kết nối với thiết bị khác qua USB) hay không. |
| FEATURES__HAS_USB_HOST | Thiết bị có hỗ trợ chế độ USB Host (cho phép kết nối các thiết bị ngoại vi như chuột, bàn phím) hay không. |
| FEATURES__HAS_WIFI | Thiết bị có hỗ trợ Wi-Fi hay không. |
| FEATURES__HAS_WIFI_DIRECT | Thiết bị có hỗ trợ Wi-Fi Direct (chia sẻ không dây giữa các thiết bị) hay không. |
| OS__LOCALIZED_MODEL | Tên model của thiết bị. VD: Xiaomi Redmi Note 7, iPhone 15 Pro. |
| SENSORS__LIST_SENSORS | Tên cảm biến. Ví dụ: accelerometer, gyroscope, proximity. |
| SIM__ESIM_SUPPORT | Thiết bị có hỗ trợ esim hay không. |
| STORAGE__STORAGE_TOTAL | Tổng dung lượng bộ nhớ của thiết bị. Ví dụ: 128GB. |
| RECORD_CREATED_DATETIME_VN | Thời gian thông tin của thiết bị này được tạo ra (tương ứng với thời gian start_scan ở phía client). Theo giờ VN. |
| RECORD_UPDATED_DATETIME_VN | Thời gian ghi nhận raw data đó vào bảng data. Theo giờ VN. |

### Table 2: momovn-prod.STRONGHOLD_ANALYTICS.FACT_DEVICE_SCAN

**Description:** Bảng fact này lưu trữ thông tin chi tiết về việc quét thiết bị trên ứng dụng MoMo, liên quan đến hành vi của người dùng khi sử dụng ứng dụng. Thông tin có thể lấy từ bảng này bao gồm:
- Thời gian bắt đầu và kết thúc của quá trình quét thiết bị.
- Thông tin về phiên bản ứng dụng và hệ điều hành trên thiết bị.
- Dữ liệu liên quan đến tình trạng pin và các tính năng của thiết bị.
- Thông tin mạng như tên nhà mạng, địa chỉ IP công cộng, và VPN.

#### Column Descriptions

| Column Name | Description |
|-------------|-------------|
| D_DEVICE_KEY | Foreign key đến bảng D_DEVICE. |
| EVENT_ID | ID của event scan thông tin thiết bị. |
| SESSION_ID | ID của session. |
| AGENT_ID | ID của end user MoMo. |
| CLIENT_START_SCAN_DATETIME_VN | Thời gian thực hiện scan. Sử dụng cột này là PARTITION column. |
| CLIENT_FINISH_SCAN_DATETIME_VN | Thời gian kết thúc scan. |
| SERVER_INIT_TOKEN_DATETIME_VN | Thời điểm BE init token. |
| SERVER_RECEIVE_SCAN_DATETIME_VN | Thời điểm BE nhận được scan result từ APP. |
| APPLICATION__ADR_INSTALLER_PACKAGE_NAME | Tên package của store cài đặt ứng dụng, ví dụ: com.android.vending, com.amazon.venezia. |
| APPLICATION__APP_VERSION_CODE | Mã phiên bản của ứng dụng, ví dụ: 42102. |
| APPLICATION__APP_VERSION_NAME | Tên phiên bản của ứng dụng, ví dụ: 4.2.10. |
| APPLICATION__APPLICATION_FIRST_INSTALL_DATETIME_VN | Thời gian cài ứng dụng lần đầu. |
| APPLICATION__APPLICATION_LAST_UPDATE_DATETIME_VN | Thời gian cập nhật ứng dụng gần nhất. |
| APPLICATION__INSTALLED_APPS | Danh sách ứng dụng đã cài đặt, ví dụ: fb, fb-messenger. |
| APPLICATION__SIGNATURE | Chứng chỉ ký của package, dùng để kiểm tra tampering của ứng dụng, chỉ MoMo giữ. |
| BATTERY__ADR_BATTERY_HEALTH | Sức khỏe của pin, ví dụ: overheat, cold, dead. |
| BATTERY__ADR_BATTERY_INFORMATION_CAPACITY | Dung lượng hiện tại của pin. |
| BATTERY__ADR_BATTERY_SOURCE | Nguồn sạc pin, ví dụ: AC, wireless, usb. |
| BATTERY__ADR_BATTERY_TEMPERATURE | Nhiệt độ của pin, ví dụ: 35°C. |
| BATTERY__ADR_BATTERY_VOLTAGE | Điện áp của pin, ví dụ: 5000 mAh. |
| BATTERY__BATTERY_LEVEL | Mức pin hiện tại của thiết bị. |
| BATTERY__BATTERY_STATE | Trạng thái pin. |
| BATTERY__IS_CHARGING | Trạng thái sạc của thiết bị, ví dụ: true (đang sạc). |
| BATTERY__IS_LOW_POWER_MODE | Chế độ tiết kiệm pin của thiết bị. |
| CPU__ACTUAL_RAM | Dung lượng RAM thực tế của thiết bị, ví dụ: 8GB. |
| DEVICE__DEVICE_LANGUAGE | Ngôn ngữ máy trong cài đặt. |
| DEVICE__TIME_ZONE | Múi giờ trong cài đặt của máy. |
| DISPLAY__ADR_REFRESH_RATE | Tốc độ làm tươi màn hình, ví dụ: 120Hz. |
| DISPLAY__FONT_SCALE | Tỷ lệ kích thước font chữ trên thiết bị. |
| DISPLAY__ORIENTATION | Hướng màn hình, ví dụ: portrait, landscape. |
| DISPLAY__PHYSICAL_SIZE | Kích thước vật lý của màn hình. |
| DISPLAY__SCREEN_BRIGHTNESS | Độ sáng màn hình, ví dụ: 80%. |
| FEATURES__HAS_AUDIO_OUTPUT | Kiểm tra hỗ trợ đầu ra âm thanh, ví dụ: true. |
| FEATURES__HAS_BIOMETRIC | Kiểm tra hỗ trợ nhận diện sinh trắc học, ví dụ: true. |
| FEATURES__HAS_FACE_ID | Kiểm tra hỗ trợ Face ID. |
| FEATURES__HAS_GPS | Kiểm tra hỗ trợ GPS, ví dụ: true. |
| FEATURES__HAS_TOUCH_ID | Kiểm tra hỗ trợ Touch ID. |
| FEATURES__IS_AIRPLANE_MODE | Kiểm tra chế độ máy bay, ví dụ: false. |
| FEATURES__IS_BLUETOOTH_HEADPHONES_CONNECTED | Kiểm tra kết nối tai nghe Bluetooth. |
| FEATURES__IS_DATA_ROAMING | Kiểm tra chuyển vùng dữ liệu. |
| FEATURES__IS_DEVELOPER_MODE | Kiểm tra chế độ nhà phát triển. |
| FEATURES__IS_DISPLAY_ZOOMED | Kiểm tra chế độ zoom màn hình. |
| FEATURES__IS_EMULATOR | Kiểm tra thiết bị giả lập. |
| FEATURES__IS_HEADPHONES_CONNECTED | Kiểm tra kết nối tai nghe. |
| FEATURES__IS_LOCATION_ENABLED | Kiểm tra bật tính năng định vị. |
| FEATURES__IS_LOW_RAM_DEVICE | Kiểm tra thuộc loại thiết bị RAM thấp. |
| FEATURES__IS_NETWORK_ROAMING | Kiểm tra sử dụng mạng chuyển vùng. |
| FEATURES__IS_PIN_OR_FINGERPRINT_SET | Kiểm tra cài đặt PIN hoặc nhận diện vân tay. |
| FEATURES__IS_ROOTED | Kiểm tra thiết bị bị root hay không. |
| FEATURES__IS_WIRED_HEADPHONES_CONNECTED | Kiểm tra kết nối tai nghe có dây. |
| FEATURES__USER_AGENT | Chuỗi nhận diện trình duyệt hoặc ứng dụng của thiết bị. |
| LOCATION__LOCATION | Toạ độ lat, lon của người dùng. |
| NETWORK__ADR_NETWORK_STRENGTH | Độ mạnh tín hiệu mạng. |
| NETWORK__ADR_WIFI_FREQUENCY | Tần số của mạng Wi-Fi. |
| NETWORK__BSSID | Địa chỉ BSSID của mạng Wi-Fi. |
| NETWORK__CARRIER_NAME | Tên nhà mạng di động. |
| NETWORK__CELLULAR_IPV4 | IPv4 của mạng di động (cellular). |
| NETWORK__CELLULAR_IPV6 | IPv6 của mạng di động (cellular). |
| NETWORK__CONNECTION_STATUS | Trạng thái kết nối mạng. |
| NETWORK__COUNTRY_CODE | Mã quốc gia của thiết bị. |
| NETWORK__DATA_TYPE | Loại dữ liệu mạng đang sử dụng. |
| NETWORK__IS_CONNECTION_EXPENSIVE | Kiểm tra kết nối tốn kém. |
| NETWORK__LATEST_BOOT_DATETIME_VN | Thời gian boot gần nhất. |
| NETWORK__LOCAL_IP_ADDRESS | Địa chỉ IP của thiết bị. |
| NETWORK__MAC_ADDRESS | Địa chỉ MAC của thiết bị. |
| NETWORK__MOBILE_COUNTRY_CODE | Country của mạng viễn thông. |
| NETWORK__MOBILE_NETWORK_CODE | Network code của mạng viễn thông. |
| NETWORK__NETWORK_TYPE | Loại mạng kết nối. |
| NETWORK__PUBLIC_IP_ADDRESS | Địa chỉ IP công khai của người dùng. |
| NETWORK__SSID | Tên mạng Wi-Fi. |
| NETWORK__SUBNET | Địa chỉ subnet của mạng. |
| NETWORK__VPN | Kiểm tra sử dụng VPN. |
| OS__ADR_API_LEVEL | API Level của Android. |
| OS__ADR_BUILD_ID | ID phiên bản build của hệ điều hành. |
| OS__ADR_BUILD_TIME | Thời gian hệ điều hành được build. |
| OS__ADR_FINGERPRINT | Chuỗi nhận diện phiên bản hệ điều hành và phần cứng. |
| OS__VERSION | Phiên bản hệ điều hành hiện tại. |
| OS__VERSION_NAME | Tên phiên bản hệ điều hành. |
| SIM__ADR_SIM_PHONE_NUMBER | Số điện thoại của thiết bị. |
| SIM__ADR_SIM_SERIAL_NUMBER | Số serial của SIM. |
| SIM__ADR_SIM_SLOT_INDEX | Số lượng khe sim đang sử dụng. |
| SIM__PHYSICAL_SIM_SUPPORT | Hỗ trợ SIM vật lý. |
| SIM__SIM_COUNT | Số lượng SIM sử dụng. |
| STORAGE__STORAGE_FREE | Dung lượng bộ nhớ còn trống. |
| STORAGE__STORAGE_USED | Dung lượng bộ nhớ đã sử dụng. |
| SOURCE_PARITITION_DATE_UTC | Thời gian partition của bảng raw, giữ nguyên giờ UTC. |

## Memory Section

### Business Rules

1. **String Processing Rule**: Các trường dữ liệu string của STRONGHOLD được xử lý lower case nếu không sensitive về mặt ý nghĩa

2. **Query Convention**: Query đúng là "device_brand" = "iphone" thay vì "iPhone"

## Summary

This domain contains comprehensive device analytics information for MoMo users, captured during various app events. The data includes:

- **Total Tables**: 2
- **Total Columns**: 113 (47 in D_DEVICE + 66 in FACT_DEVICE_SCAN)
- **Key Relationship**: D_DEVICE_KEY serves as the foreign key between tables
- **Data Types**: Device specifications, app information, battery status, network details, location data, and OS information
- **Languages**: Mixed Vietnamese and English content with technical specifications

The domain supports device analytics, user behavior analysis, and AI/ML feature extraction for MoMo's mobile platform.