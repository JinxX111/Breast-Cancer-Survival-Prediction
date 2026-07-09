# SEER Special Codes (Các Mã Đặc Biệt trong SEER)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | SEER Special Codes |
| Version | 1.0 |

---

## Purpose | Mục đích

This document summarizes the special values and coding conventions used in the SEER database. Understanding these codes is essential for accurate preprocessing and machine learning model development.

Tài liệu này tổng hợp các mã đặc biệt và quy ước mã hóa được sử dụng trong cơ sở dữ liệu SEER. Việc hiểu đúng các mã này là rất quan trọng để tiền xử lý dữ liệu chính xác và xây dựng mô hình học máy.

---

# Common SEER Special Codes | Các mã đặc biệt thường gặp trong SEER

| Code | Meaning | Vietnamese | Suggested Processing |
|------|---------|------------|----------------------|
| 999 | Unknown Tumor Size | Không xác định kích thước khối u | Convert to NULL |
| 998 | Not Applicable | Không áp dụng | Convert to NULL |
| 997 | Unknown / Not Recorded | Không ghi nhận | Convert to NULL |
| 99 | Unknown Count | Không xác định | Convert to NULL |
| 95–98 | Special Registry Codes | Mã đặc biệt của SEER | Review before processing |
| Blank | Missing Information | Thiếu dữ liệu | Convert to NULL |

---

# AJCC Special Codes | Các mã đặc biệt của AJCC

| Code | Meaning | Suggested Processing |
|------|---------|----------------------|
| TX | Primary Tumor Cannot Be Assessed | Keep as Unknown Category |
| NX | Regional Nodes Cannot Be Assessed | Keep as Unknown Category |
| MX | Distant Metastasis Cannot Be Assessed | Keep as Unknown Category |
| Tis | Carcinoma In Situ | Keep |
| N0 | No Regional Lymph Node Metastasis | Keep |
| M0 | No Distant Metastasis | Keep |
| M1 | Distant Metastasis Present | Keep |

---

# Biomarker Special Values | Giá trị đặc biệt của Biomarker

| Value | Meaning | Suggested Processing |
|-------|---------|----------------------|
| Positive | Positive Expression | Keep |
| Negative | Negative Expression | Keep |
| Borderline | Borderline Result | Separate Category |
| Unknown | Unknown Result | Review During EDA |

---

# Treatment Special Values | Giá trị đặc biệt của Điều trị

| Value | Meaning | Suggested Processing |
|-------|---------|----------------------|
| Yes | Treatment Received | Keep |
| No | Treatment Not Received | Keep |
| Unknown | Treatment Unknown | Separate Category |

---

# Data Cleaning Strategy | Chiến lược làm sạch dữ liệu

| Situation | Recommended Action |
|-----------|--------------------|
| Missing Numerical Values | Convert to NULL |
| Missing Categorical Values | Keep Unknown Category if Clinically Meaningful |
| Registry Special Codes | Review Before Conversion |
| Identifier Variables | Never Use for Training |
| Target Variables | Validate Carefully Before Modeling |

---

# Important Notes | Lưu ý quan trọng

- Do not remove unknown values without understanding their clinical meaning.
- Some SEER special codes contain valuable medical information.
- Always consult the SEER Coding Manual before modifying registry variables.
- Preserve the original raw dataset before performing any preprocessing.

---

# References | Tài liệu tham khảo

1. SEER Program Coding Manual.
2. SEER Research Data Documentation.
3. AJCC Cancer Staging Manual (6th Edition).
4. National Cancer Institute (NCI).
5. National Comprehensive Cancer Network (NCCN).

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |