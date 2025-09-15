# MirMir: Natural Language Query System for MoMo Data

## Executive Summary

MirMir is MoMo's internal natural language query system that enables Technical Product Managers and business stakeholders to explore and analyze MoMo's vast data ecosystem through simple Vietnamese or English questions. The system bridges the gap between business needs and complex data structures by providing instant access to insights across 43+ business domains without requiring SQL knowledge.

## What is MirMir?

MirMir acts as an intelligent data assistant that:
- Translates natural language questions into SQL queries
- Executes queries against MoMo's production data warehouses
- Returns structured results with business context
- Covers all major MoMo business units and services

## Available Data Domains (43 Total)

### Core Payment & Transfer Services
- **P2P_W2B**: Wallet-to-Bank transfer transactions and user behaviors
- **P2P_QUYNHOM**: Group collection and payment features
- **P2P_AIO_QR**: All-in-one QR payment solutions

### Financial Services (FS)
- **FS_Vay_Nhanh**: Quick loan services and credit products
- **BU_FS_InsurTech_Insurance**: Insurance products and claims
- **BU_FS_Tui_Than_Tai**: Lucky money and savings features

### Digital Lifestyle Services (DLS)
- **OTA**: Online Travel Agency - flight and hotel bookings
- **Business_Page**: Merchant profiles and engagement metrics
- **M4B_HUB**: Merchant for Business hub activities

### Marketing & Customer Engagement
- **BU_MDS_Journey**: User journey campaigns with CTR and conversion metrics
- **BU_MDS_Notification_for_Platform**: Platform notification performance
- **Promotion_Campaign_Performance**: Campaign effectiveness tracking
- **CEE_USER_SUGGESTIONS**: User recommendation engine data

### Utility Services
- **Airtime_Non_Sensitive**: Mobile top-up transactions
- **BILLPAY_Business_metrics_Non_Sensitive**: Bill payment metrics
- **BU-MDS_Donation**: Charitable donation features

### Internal Operations
- **CS**: Customer service interactions and resolutions
- **Data/Data_Non_Sensitive**: Platform-wide data metrics
- **Data_Ownership**: Data governance and ownership tracking

*[And 20+ additional domains covering all MoMo services]*

## How to Ask Good Questions in MirMir

### Essential Components of a Good Query

Every MirMir question should include these three key elements:

1. **Data Type Specification** (Loại dữ liệu)
   - Specify what metrics you need: GMV, CVM, user count, transaction volume
   - Include the business context: "for Grab merchants", "for Xanh SM users"
   - Example: "GMV của các merchant trong Business Page"

2. **Time Range** (Thời gian cụ thể)
   - Be specific with dates: "from 2/2025 to 3/2025"
   - Use clear time references: "yesterday", "last 7 days", "June 2025"
   - Avoid ambiguous terms like "recently" or "this period"

3. **Output Format** (Định dạng kết quả)
   - For data analysis: Always specify "KHÔNG cần chart" (NO chart needed)
   - MirMir returns tabular data by default

### Good Question Examples

✅ **GOOD**: "How many distinct users made P2P transactions from 1/2025 to 15/2025, grouped by transaction type? KHÔNG cần chart"

✅ **GOOD**: "Total GMV for OTA hotel bookings in Q1 2025, broken down by month. KHÔNG cần chart"

❌ **BAD**: "Show me user data" (Missing: specific metrics, time range, domain)

❌ **BAD**: "Recent transactions" (Missing: specific domain, exact time period, metrics)

## API Integration

### Available APIs
 ```

3. **Send Question**
   ```bash
   POST https://s.dev.mservice.io/mimir-server-to-server/v1/domain/send_question
   {
     "user_email": "your.email@mservice.com.vn",
     "domain_id": "{domain_id}",
     "question": "Your question here with time range and KHÔNG cần chart"
   }
   ```

4. **Get Answer**
   ```bash
   GET https://s.dev.mservice.io/mimir-server-to-server/v1/domain/get_answer?request_id={request_id}
   ```

### Integration Best Practices
- Add 1-second delay between questions to avoid rate limiting
- Check for answers every 30 seconds (queries may take time)
- Store responses systematically for audit and analysis

## Domain Details Reference

For detailed information about specific domains, refer to the individual domain documentation files:

- Each domain file contains:
  - Complete table schemas with column descriptions
  - Data types and example values
  - Business context and use cases
  - Available metrics and dimensions

Files location: `./mirmir_domains/final_[DOMAIN_NAME].md`

## Understanding Each Domain's Data

### Domain File Structure
Each domain documentation includes:
1. **Basic Information**: Domain ID, name, and business description
2. **Table Information**: Source BigQuery tables and their purposes
3. **Column Descriptions**: Detailed field explanations with examples
4. **Business Context**: How the data relates to MoMo operations

### Example: BU_MDS_Journey Domain
- **Purpose**: Track user journey campaigns
- **Key Metrics**: CVR enter, goal achievement, CTR for notifications
- **Use Cases**: Campaign optimization, user flow analysis
- **Table**: `momovn-prod.MBI_DA.journey_track_node_agg_v2`

### Example: P2P_W2B Domain
- **Purpose**: Wallet-to-Bank transfer analytics
- **Key Metrics**: Transaction volumes, fees, channel distribution
- **Use Cases**: Payment flow optimization, user behavior analysis
- **Table**: `momovn-prod.MBI_DA.LOAN_P2P_W2B_RAW_MAPPING`

## What MoMo Data is NOT in MirMir

While MirMir covers extensive operational data, some information remains outside its scope:

1. **Real-time Data**: MirMir works with batch-processed data (usually T+1)
2. **Personal User Information**: PII is masked or excluded for privacy
3. **Internal HR Data**: Employee information and organizational data
4. **Source Code & Technical Architecture**: System implementation details
5. **Third-party Partner Internal Data**: Only MoMo-side transaction data is available
6. **Regulatory Compliance Documents**: Legal and compliance documentation
7. **Future Product Roadmaps**: Strategic planning documents
8. **Detailed Financial Statements**: Consolidated P&L and balance sheets

## Tips for Product Managers

### Getting Started
1. Identify your domain from the 43 available options
2. Review the domain's documentation file for available metrics
3. Formulate specific questions with clear time ranges
4. Always specify "KHÔNG cần chart" for data queries

### Common Use Cases
- **User Acquisition**: Query new user counts by channel and time period
- **Transaction Analysis**: Analyze GMV, transaction volumes by service
- **Campaign Performance**: Measure CTR, conversion rates for campaigns
- **Merchant Analytics**: Track merchant engagement and transaction patterns
- **Service Adoption**: Monitor feature usage and user retention

### Troubleshooting
- If no results: Check if the domain is correct for your data needs
- If incomplete results: Verify time range includes sufficient data
- If unexpected values: Confirm metric definitions in domain documentation

## Quick Reference Card

```
Question Formula:
[Metric] + [Domain/Service] + [Time Period] + "KHÔNG cần chart"

Example:
"Tổng GMV của OTA từ 1/1/2025 đến 31/1/2025, chia theo loại dịch vụ. KHÔNG cần chart"

Common Metrics:
- GMV (Gross Merchandise Value)
- Số lượng user (User count)
- Số lượng giao dịch (Transaction count)
- Tỷ lệ chuyển đổi (Conversion rate)
- CTR (Click-through rate)
```

## Support and Resources

For additional assistance:
- **Domain Documentation**: `./mirmir_domains/final_[DOMAIN_NAME].md`
- **API Documentation**: `./mir_mir_apis.md`
- **Technical Support**: Contact your data team or BI department

---

*Note: This document provides an overview of MirMir's capabilities. For detailed technical specifications and data dictionaries, consult the individual domain documentation files.*