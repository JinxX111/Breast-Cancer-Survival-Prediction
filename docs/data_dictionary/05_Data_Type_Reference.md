# Data Type Reference (Tham chiếu Kiểu Dữ liệu)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | Data Type Reference (Tham chiếu kiểu dữ liệu) |
| Version | 1.0 |

---

## Purpose |  Mục đích

This document summarizes the data types, preprocessing strategies, encoding methods, and machine learning roles for every variable used in this project.

Tài liệu này tổng hợp kiểu dữ liệu, chiến lược tiền xử lý, phương pháp mã hóa và vai trò của từng biến trong quá trình xây dựng mô hình học máy.

---

# Variable Type Reference | Bảng tham chiếu kiểu dữ liệu

| Variable | Spark Type | ML Type | Encoding | Keep | Model Usage |
|-----------|------------|---------|----------|------|-------------|
| Age recode | String | Ordinal | StringIndexer | Yes | Predictor |
| Sex | String | Binary | StringIndexer | Yes | Predictor |
| Race recode | String | Category | StringIndexer | Yes | Predictor |
| Marital status | String | Category | StringIndexer | Yes | Predictor |
| CS tumor size | Integer | Numerical | None | Yes | Predictor |
| Survival months | String → Integer | Numerical | None | Yes | Survival Target |
| Vital status | String | Binary | StringIndexer | Yes | Classification Target |
| Grade Recode | String | Ordinal | StringIndexer | Yes | Predictor |
| ER Status | String | Binary | StringIndexer | Yes | Predictor |
| PR Status | String | Binary | StringIndexer | Yes | Predictor |
| AJCC T | String | Ordinal | StringIndexer | Yes | Predictor |
| AJCC N | String | Ordinal | StringIndexer | Yes | Predictor |
| AJCC M | String | Binary | StringIndexer | Yes | Predictor |
| AJCC Stage | String | Ordinal | StringIndexer | Yes | Predictor |
| Regional Nodes Examined | Integer | Numerical | None | Yes | Predictor |
| Regional Nodes Positive | Integer | Numerical | None | Yes | Predictor |
| Sequence Number | String | Category | StringIndexer | Yes | Filter |
| Patient ID | Integer | Identifier | None | No | Remove before Training |
| Primary Site | Integer | Category | StringIndexer | Yes | Predictor |
| Histologic Type | Integer | Category | StringIndexer | Yes | Predictor |
| Behavior Recode | String | Category | Filter | Yes | Filter |
| Laterality | String | Category | StringIndexer | Yes | Predictor |
| Diagnostic Confirmation | String | Category | StringIndexer | Yes | Predictor |
| Lymph-vascular Invasion | String | Category | StringIndexer | Yes | Predictor |
| Surgery Primary Site | Integer | Category | StringIndexer | Yes | Predictor |
| Surgery Other Region | Integer | Category | StringIndexer | Yes | Predictor |
| Surgery/Radiation Sequence | String | Category | StringIndexer | Yes | Predictor |
| Radiation Recode | String | Category | StringIndexer | Yes | Predictor |
| Chemotherapy Recode | String | Binary | StringIndexer | Yes | Predictor |

---

# Encoding Strategy | Chiến lược mã hóa dữ liệu

| Variable Type | Spark Processing |
|---------------|-----------------|
| Numerical | Keep Original |
| Binary | StringIndexer |
| Ordinal | StringIndexer |
| Nominal | StringIndexer |
| Feature Vector | VectorAssembler |
| Target | Independent Variable |

---

# Machine Learning Pipeline |  Quy trình xử lý dữ liệu

Raw CSV

↓

Load using Spark

↓

Schema Validation

↓

Missing Value Handling

↓

Special Code Processing

↓

Type Conversion

↓

Categorical Encoding

↓

Feature Vector Assembly

↓

Model Training

↓

Evaluation

---

# Notes | Ghi chú

- Patient ID is only used for record identification.
- Survival Months is reserved for survival analysis.
- Vital Status is used as the classification target.
- Final preprocessing decisions may change after Exploratory Data Analysis (EDA).

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |