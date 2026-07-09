# Survival and Administrative (Thông tin sống còn và Hành chính)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | Survival and Administrative (Thông tin sống còn và Hành chính) |
| Variables | 9 |
| Version | 1.0 |

---

## Purpose | Mục đích

This document describes the survival-related and administrative variables included in the SEER breast cancer dataset. These variables provide essential information for defining prediction targets, identifying patient records, and ensuring data quality throughout the machine learning pipeline.

Tài liệu này mô tả các biến liên quan đến thời gian sống còn và thông tin hành chính trong bộ dữ liệu SEER. Đây là những biến quan trọng giúp xác định biến mục tiêu (target), quản lý hồ sơ bệnh nhân và đảm bảo chất lượng dữ liệu trong toàn bộ quy trình xây dựng mô hình học máy.

---

## Variables Included | Danh sách biến

1. Survival months
2. Vital status recode (study cutoff used)
3. Sequence number
4. Patient ID
5. Behavior recode for analysis
6. Regional nodes examined (1988+)
7. Regional nodes positive (1988+)
8. Sex
9. Marital status at diagnosis

---

# 1. Survival months | Thời gian sống còn

### English Description

Represents the total survival time of a patient from the date of diagnosis until death or the end of follow-up, measured in months.

### Vietnamese Description

Biến này biểu diễn tổng thời gian sống của bệnh nhân kể từ khi được chẩn đoán đến khi tử vong hoặc kết thúc thời gian theo dõi, được tính theo tháng.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Numerical |
| Example | 2, 18, 67, 145 |
| Missing Value | Rare |
| Machine Learning Usage | Target Variable / Survival Analysis |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Convert to Integer.
- Remove invalid or negative values.
- Verify consistency with Vital Status.
- May be transformed into binary survival labels depending on study objectives.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Survival Months is the primary outcome variable for survival prediction studies. It represents the patient's observed survival duration and is essential for both classification and survival analysis.

**Tiếng Việt**

Survival Months là biến đầu ra quan trọng nhất trong nghiên cứu dự đoán sống còn. Đây là thời gian sống quan sát được của bệnh nhân và là nền tảng cho cả mô hình phân loại lẫn phân tích sống còn.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.

---

# 2. Vital status recode (study cutoff used) | Tình trạng sống tại thời điểm kết thúc nghiên cứu

### English Description

Indicates whether the patient was alive or deceased at the study cutoff date.

### Vietnamese Description

Biến này cho biết bệnh nhân còn sống hay đã tử vong tại thời điểm kết thúc nghiên cứu.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Binary Categorical |
| Example | Alive, Dead |
| Missing Value | None |
| Machine Learning Usage | Classification Target |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Convert Alive and Dead into binary labels.
- Verify consistency with Survival Months.
- Remove inconsistent observations if detected.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

This variable is commonly used as the prediction target in machine learning models for survival classification.

**Tiếng Việt**

Đây là biến mục tiêu phổ biến nhất trong các mô hình học máy dự đoán khả năng sống còn của bệnh nhân.

### Reference | Tài liệu tham khảo

SEER Survival Variables Documentation.

---

# 3. Sequence number | Số thứ tự ung thư nguyên phát

### English Description

Indicates the sequence of primary tumors diagnosed in the patient during their lifetime.

### Vietnamese Description

Biến này cho biết thứ tự xuất hiện của các khối u nguyên phát được chẩn đoán ở bệnh nhân trong suốt cuộc đời.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | One Primary Only, First of Two Primaries |
| Missing Value | None |
| Machine Learning Usage | Data Filtering |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Retain "One Primary Only" if the study focuses on first primary breast cancer.
- Remove multiple primary cases if required by study design.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Using only first primary cancers reduces potential confounding caused by previous malignancies.

**Tiếng Việt**

Việc chỉ sử dụng các trường hợp ung thư nguyên phát đầu tiên giúp giảm sai lệch do ảnh hưởng của các bệnh ung thư trước đó.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.

---

# 4. Patient ID

## Mã định danh bệnh nhân

### English Description

A unique identifier assigned to each patient record within the SEER database.

### Vietnamese Description

Mã định danh duy nhất của từng bệnh nhân trong cơ sở dữ liệu SEER.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Integer |
| Example | 60161363 |
| Missing Value | None |
| Machine Learning Usage | Identifier Only |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Keep for traceability.
- Remove before model training.
- Never use as a predictive feature.

### Research Importance | Ý nghĩa trong nghiên cứu
**English**

Patient ID is used solely for data management and record tracking. It has no predictive value.

**Tiếng Việt**

Patient ID chỉ phục vụ mục đích quản lý dữ liệu và theo dõi hồ sơ, hoàn toàn không mang ý nghĩa dự đoán.

### Reference | Tài liệu tham khảo

SEER Research Data Documentation.

---

# 5. Behavior recode for analysis | Hành vi của khối u

### English Description

Describes the biological behavior of the tumor, such as benign, in situ, borderline, or malignant.

### Vietnamese Description

Biến này mô tả đặc điểm sinh học của khối u như lành tính, tại chỗ, giáp biên hay ác tính.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Malignant |
| Missing Value | None |
| Machine Learning Usage | Data Filtering / Predictor Feature |

### Data Cleaning Notes |  Ghi chú tiền xử lý dữ liệu

- Retain only malignant tumors for this project.
- Remove non-malignant records if present.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Restricting analysis to malignant tumors ensures consistency with the study objective of predicting breast cancer survival.

**Tiếng Việt**
Chỉ sử dụng các trường hợp ung thư ác tính giúp đảm bảo tính nhất quán với mục tiêu nghiên cứu dự đoán khả năng sống còn của bệnh nhân ung thư vú.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.
---

# 6. Regional nodes examined (1988+) | Số lượng hạch vùng được kiểm tra

### English Description

Represents the total number of regional lymph nodes surgically removed and pathologically examined.

### Vietnamese Description

Biến này biểu diễn tổng số hạch bạch huyết vùng được lấy ra và kiểm tra bằng giải phẫu bệnh.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Numerical |
| Example | 0, 3, 12, 28 |
| Missing Value | 99 = Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Convert to Integer.
- Replace unknown codes (e.g., 99) with NULL if necessary.
- Verify that examined nodes are greater than or equal to positive nodes.

### Research Importance |  Ý nghĩa trong nghiên cứu

**English**
The number of examined lymph nodes reflects the extent of surgical staging and is associated with diagnostic accuracy and prognosis.

**Tiếng Việt**
Số lượng hạch được kiểm tra phản ánh mức độ đánh giá giai đoạn bệnh trong quá trình phẫu thuật và có liên quan đến độ chính xác của chẩn đoán cũng như tiên lượng.

---

# 7. Regional nodes positive (1988+) | Số lượng hạch vùng dương tính

### English Description
Represents the number of regional lymph nodes containing metastatic cancer cells.

### Vietnamese Description
Biến này biểu diễn số lượng hạch bạch huyết vùng có chứa tế bào ung thư di căn.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Numerical |
| Example | 0, 1, 4, 12 |
| Missing Value | 99 = Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Convert to Integer.
- Replace unknown values appropriately.
- Ensure the value does not exceed the number of examined nodes.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
The number of positive lymph nodes is one of the strongest indicators of disease progression and long-term survival in breast cancer.

**Tiếng Việt**
Số lượng hạch dương tính là một trong những yếu tố tiên lượng mạnh nhất đối với sự tiến triển của bệnh và khả năng sống còn lâu dài.

### Reference | Tài liệu tham khảo

AJCC TNM Classification.

---

## Summary | Tóm tắt

| Variable | Data Type | Machine Learning Usage |
|----------|-----------|------------------------|
| Survival Months | Numerical | Target Variable / Survival Analysis |
| Vital Status | Binary Categorical | Classification Target |
| Sequence Number | Categorical | Data Filtering |
| Patient ID | Integer | Identifier Only |
| Behavior Recode | Categorical | Data Filtering / Predictor Feature |
| Regional Nodes Examined | Numerical | Predictor Feature |
| Regional Nodes Positive | Numerical | Predictor Feature |

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |