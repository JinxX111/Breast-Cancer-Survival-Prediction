# Biomarkers and Treatment (Dấu ấn sinh học và Điều trị)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | Biomarkers and Treatment (Dấu ấn sinh học và Điều trị) |
| Variables | 8 |
| Version | 1.0 |

---

## Purpose | Mục đích

This document describes the biomarker and treatment variables included in the SEER breast cancer dataset. These variables reflect tumor molecular characteristics and treatment strategies received by patients, providing essential information for predicting survival outcomes.

Tài liệu này mô tả các biến liên quan đến dấu ấn sinh học và phương pháp điều trị trong bộ dữ liệu ung thư vú SEER. Những biến này phản ánh đặc điểm sinh học của khối u cũng như các phương pháp điều trị bệnh nhân đã được áp dụng, từ đó đóng vai trò quan trọng trong việc dự đoán khả năng sống còn.

---

## Variables Included | Danh sách biến

1. ER Status Recode Breast Cancer (1990+)
2. PR Status Recode Breast Cancer (1990+)
3. Lymph-vascular Invasion (2004+ varying by schema)
4. RX Summ--Surg Prim Site (1998–2022)
5. RX Summ--Surg Oth Reg/Dis (2003+)
6. RX Summ--Surg/Rad Seq
7. Radiation recode
8. Chemotherapy recode (yes, no/unk)

---

# 1. ER Status Recode Breast Cancer (1990+) | Thụ thể Estrogen (ER)

### English Description

Represents the estrogen receptor (ER) status of the primary breast tumor.

### Vietnamese Description

Biến này biểu diễn tình trạng thụ thể Estrogen (ER) của khối u nguyên phát.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Positive, Negative, Borderline, Unknown |
| Missing Value | Unknown / Borderline |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve Positive and Negative categories.
- Review Borderline and Unknown values before modeling.
- Encode categorical values during preprocessing.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

ER status is one of the most important prognostic and predictive biomarkers in breast cancer. It determines hormone therapy eligibility and is strongly associated with long-term survival.

**Tiếng Việt**

ER là một trong những dấu ấn sinh học quan trọng nhất trong ung thư vú. Biến này quyết định khả năng điều trị nội tiết và có ảnh hưởng lớn đến tiên lượng sống còn.

### Reference | Tài liệu tham khảo

NCCN Breast Cancer Guidelines.

---

# 2. PR Status Recode Breast Cancer (1990+) | Thụ thể Progesterone (PR)
 
### English Description

Represents the progesterone receptor (PR) status of the primary breast tumor.

### Vietnamese Description

Biến này biểu diễn tình trạng thụ thể Progesterone (PR) của khối u nguyên phát.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Positive, Negative, Borderline, Unknown |
| Missing Value | Unknown / Borderline |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve Positive and Negative categories.
- Handle Borderline and Unknown consistently.
- Apply categorical encoding before training.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

PR status complements ER status in determining tumor subtype, treatment planning, and prognosis.

**Tiếng Việt**

PR thường được đánh giá cùng ER nhằm xác định phân nhóm ung thư vú, lựa chọn phương pháp điều trị và tiên lượng bệnh.

### Reference | Tài liệu tham khảo

NCCN Breast Cancer Guidelines.

---

# 3. Lymph-vascular Invasion (2004+ varying by schema) | Xâm lấn mạch bạch huyết và mạch máu

### English Description

Indicates whether tumor cells have invaded lymphatic vessels or blood vessels surrounding the primary tumor.

### Vietnamese Description

Biến này cho biết tế bào ung thư có xâm lấn vào mạch bạch huyết hoặc mạch máu quanh khối u hay không.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Present, Absent, Unknown |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve all valid categories.
- Evaluate Unknown values before training.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Lymph-vascular invasion is associated with increased risk of lymph node metastasis, recurrence, and reduced survival.

**Tiếng Việt**

Xâm lấn mạch bạch huyết là yếu tố tiên lượng quan trọng, liên quan đến nguy cơ di căn hạch, tái phát và giảm khả năng sống còn.

### Reference | Tài liệu tham khảo

AJCC Cancer Staging Manual.

---

# 4. RX Summ--Surg Prim Site (1998–2022) | Phẫu thuật khối u nguyên phát

### English Description

Represents the surgical procedure performed on the primary breast tumor.

### Vietnamese Description

Biến này mô tả phương pháp phẫu thuật được thực hiện đối với khối u nguyên phát.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Lumpectomy, Mastectomy, None |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Keep official SEER surgery codes.
- Group similar procedures if necessary for modeling.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Primary surgery is a major treatment modality and has significant influence on patient survival and recurrence.

**Tiếng Việt**

Phẫu thuật khối u nguyên phát là phương pháp điều trị quan trọng, ảnh hưởng trực tiếp đến tiên lượng và nguy cơ tái phát của bệnh nhân.

### Reference | Tài liệu tham khảo

SEER Surgery Codes Manual.

---

# 5. RX Summ--Surg Oth Reg/Dis (2003+) | Phẫu thuật vùng hoặc cơ quan khác

### English Description

Represents surgical procedures performed on regional or distant tissues other than the primary tumor site.

### Vietnamese Description

Biến này biểu diễn các thủ thuật phẫu thuật được thực hiện trên mô hoặc cơ quan vùng, hoặc cơ quan xa ngoài khối u nguyên phát.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | None, Regional Surgery, Distant Surgery |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve official SEER surgery codes.
- Group infrequent categories when appropriate.
- Keep "None" as an independent category.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Additional regional or distant surgical procedures often indicate more advanced disease or metastatic management strategies and may influence survival outcomes.

**Tiếng Việt**

Các phẫu thuật vùng hoặc cơ quan xa thường phản ánh bệnh ở giai đoạn tiến triển hơn hoặc chiến lược điều trị di căn, do đó có thể ảnh hưởng đến tiên lượng sống còn.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.

---

# 6. RX Summ--Surg/Rad Seq | Trình tự giữa phẫu thuật và xạ trị

### English Description

Represents the chronological sequence between surgery and radiation therapy.

### Vietnamese Description

Biến này biểu diễn trình tự thực hiện giữa phẫu thuật và xạ trị.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Radiation before surgery, Radiation after surgery, Surgery only |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve all valid treatment sequences.
- Merge rare categories if necessary.
- Unknown values should be reviewed before modeling.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

The treatment sequence may reflect different clinical protocols and can influence recurrence risk and overall survival.

**Tiếng Việt**

Trình tự giữa phẫu thuật và xạ trị phản ánh chiến lược điều trị khác nhau và có thể ảnh hưởng đến nguy cơ tái phát cũng như khả năng sống còn.

### Reference | Tài liệu tham khảo

NCCN Breast Cancer Treatment Guidelines.

---

# 7. Radiation recode | Điều trị xạ trị

### English Description

Indicates whether radiation therapy was administered as part of the patient's treatment.

### Vietnamese Description

Biến này cho biết bệnh nhân có được điều trị bằng xạ trị hay không.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Beam Radiation, Combination Therapy, None, Unknown |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve treatment categories.
- Unknown values should be evaluated before model training.
- Consider grouping uncommon radiation types.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Radiation therapy reduces local recurrence after surgery and is an important component of breast cancer treatment.

**Tiếng Việt**

Xạ trị giúp giảm nguy cơ tái phát tại chỗ sau phẫu thuật và là một trong những phương pháp điều trị quan trọng đối với ung thư vú.

### Reference | Tài liệu tham khảo

NCCN Breast Cancer Guidelines.

---

# 8. Chemotherapy recode (yes, no/unk) | Điều trị hóa trị

### English Description

Indicates whether chemotherapy was administered during the patient's treatment course.

### Vietnamese Description

Biến này cho biết bệnh nhân có được điều trị bằng hóa trị hay không.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Yes, No, Unknown |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve Yes and No categories.
- Evaluate Unknown cases separately.
- Encode categorical values during preprocessing.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Chemotherapy is one of the primary systemic treatments for breast cancer and has substantial impact on disease recurrence and patient survival.

**Tiếng Việt**

Hóa trị là một trong những phương pháp điều trị toàn thân quan trọng nhất đối với ung thư vú và có ảnh hưởng lớn đến nguy cơ tái phát cũng như thời gian sống còn của bệnh nhân.

### Reference | Tài liệu tham khảo

National Comprehensive Cancer Network (NCCN).

---

# 9. Hormone Status | Tình trạng thụ thể nội tiết tổng hợp

### English Description

Represents the combined hormone receptor status derived from ER and PR status indicators.

### Vietnamese Description

Biến này biểu diễn tình trạng thụ thể nội tiết tổng hợp được kết hợp từ kết quả của ER và PR.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | HR_Positive, HR_Negative, HR_Mixed, Unknown |
| Missing Value (Giá trị thiếu) | Unknown |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Combined logic: Positive if ER+ or PR+, Negative if both ER- and PR-.
- Encoded via `StringIndexer` in the Spark ML pipeline.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Combined hormone receptor status is a key determinant for endocrine therapy selection and long-term prognosis.

**Tiếng Việt**
Tình trạng thụ thể nội tiết tổng hợp là yếu tố then chốt quyết định chỉ định điều trị nội tiết và tiên lượng sống còn dài hạn.

### Reference | Tài liệu tham khảo

NCCN Clinical Practice Guidelines in Oncology.

---

## Summary | Tóm tắt

| Variable | Data Type | Machine Learning Usage |
|----------|-----------|------------------------|
| ER Status | Categorical | Predictor Feature |
| PR Status | Categorical | Predictor Feature |
| Lymph-vascular Invasion | Categorical | Predictor Feature |
| Surgery of Primary Site | Categorical | Predictor Feature |
| Surgery of Other Regional/Distant Sites | Categorical | Predictor Feature |
| Surgery/Radiation Sequence | Categorical | Predictor Feature |
| Radiation Therapy | Categorical | Predictor Feature |
| Chemotherapy | Categorical | Predictor Feature |

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |