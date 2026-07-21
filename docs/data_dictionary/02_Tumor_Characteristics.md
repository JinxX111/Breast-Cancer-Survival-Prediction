# Tumor Characteristics (Đặc điểm khối u)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | Tumor Characteristics (Đặc điểm khối u) |
| Variables | 10 |
| Version | 1.0 |

---

## Purpose | Mục đích

This document describes the tumor-related variables used in this project. These variables characterize the biological behavior, anatomical extent, pathological findings, and clinical stage of breast cancer. They are among the most influential predictors of patient survival.

Tài liệu này mô tả các biến liên quan đến đặc điểm khối u được sử dụng trong dự án. Các biến này phản ánh đặc điểm sinh học, mức độ lan rộng, kết quả giải phẫu bệnh và giai đoạn lâm sàng của ung thư vú. Đây là nhóm biến quan trọng nhất trong việc dự đoán khả năng sống còn của bệnh nhân.

---

## Variables Included | Danh sách biến

1. CS tumor size (2004–2015)
2. Grade Recode (thru 2017)
3. Breast - Adjusted AJCC 6th Stage (1988–2015)
4. Breast - Adjusted AJCC 6th T (1988–2015)
5. Breast - Adjusted AJCC 6th N (1988–2015)
6. Breast - Adjusted AJCC 6th M (1988–2015)
7. Histologic Type ICD-O-3
8. Primary Site
9. Laterality
10. Diagnostic Confirmation

---

# 1. CS tumor size (2004–2015) | Kích thước khối u nguyên phát

### English Description

Represents the largest recorded diameter of the primary breast tumor at diagnosis, measured in millimeters according to the Collaborative Staging (CS) system.

### Vietnamese Description

Biến này biểu diễn kích thước lớn nhất của khối u nguyên phát tại thời điểm chẩn đoán, được đo bằng milimét theo hệ thống Collaborative Staging (CS).

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Numerical |
| Example (Ví dụ) | 12 mm, 25 mm, 48 mm, 999 |
| Missing Value (Giá trị thiếu) | 999 = Unknown |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Convert to Integer.
- Replace **999** with NULL before preprocessing.
- Check for abnormal values.
- Perform imputation if required.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Tumor size is one of the strongest prognostic indicators in breast cancer. Larger tumors are generally associated with more advanced disease, increased lymph node involvement, and poorer survival outcomes.

**Tiếng Việt**

Kích thước khối u là một trong những yếu tố tiên lượng mạnh nhất của ung thư vú. Khối u càng lớn thường liên quan đến giai đoạn bệnh tiến triển, khả năng di căn hạch cao hơn và tiên lượng sống còn thấp hơn.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual (2004–2015)

---

# 2. Grade Recode (thru 2017) | Độ biệt hóa của khối u

### English Description

Represents the histological differentiation grade describing how closely cancer cells resemble normal breast tissue.

### Vietnamese Description

Biến này biểu diễn mức độ biệt hóa mô học của tế bào ung thư, phản ánh mức độ giống với mô vú bình thường.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | Grade I, Grade II, Grade III, Grade IV, Unknown |
| Missing Value (Giá trị thiếu) | Unknown |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve ordinal order.
- Treat Unknown as a separate category or missing value depending on the preprocessing strategy.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Tumor grade reflects cancer aggressiveness. Higher grades are associated with faster tumor growth, higher recurrence rates, and poorer prognosis.

**Tiếng Việt**

Độ biệt hóa phản ánh mức độ ác tính của khối u. Grade càng cao thì tốc độ phát triển của khối u càng nhanh, nguy cơ tái phát càng lớn và tiên lượng sống còn càng thấp.

### Reference |  Tài liệu tham khảo

AJCC Cancer Staging Manual

---

# 3. Breast - Adjusted AJCC 6th Stage (1988–2015) |  Giai đoạn AJCC tổng thể

### English Description

Represents the overall breast cancer stage according to the AJCC 6th Edition staging system.

### Vietnamese Description

Biến này biểu diễn giai đoạn tổng thể của ung thư vú theo hệ thống phân giai đoạn AJCC phiên bản thứ 6.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | Stage I, Stage IIA, Stage IIIB, Stage IV, UNK Stage |
| Missing Value (Giá trị thiếu) | UNK Stage |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve stage order.
- Review UNK Stage before training.
- Encode as an ordinal feature if appropriate.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

AJCC Stage summarizes tumor size, lymph node involvement, and distant metastasis into a single clinical stage, making it one of the most important predictors of survival.

**Tiếng Việt**

Giai đoạn AJCC tổng hợp thông tin về kích thước khối u, tình trạng hạch lympho và di căn xa thành một chỉ số duy nhất, là một trong những biến dự đoán sống còn quan trọng nhất.

### Reference |  Tài liệu tham khảo

AJCC 6th Edition

---

# 4. Breast - Adjusted AJCC 6th T (1988–2015) | Chỉ số T (Khối u nguyên phát)

### English Description

Represents the size and local extent of the primary tumor according to the TNM classification.

### Vietnamese Description

Biến này biểu diễn kích thước và mức độ xâm lấn của khối u nguyên phát theo hệ thống TNM.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | Tis, T1, T2, T3, T4, TX |
| Missing Value (Giá trị thiếu) | TX |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve ordinal order.
- TX indicates that the primary tumor cannot be assessed.
- Review unknown values before modeling.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

The T category describes tumor burden and local invasion, serving as a key component of the TNM staging system.

**Tiếng Việt**

Chỉ số T phản ánh mức độ phát triển và xâm lấn của khối u nguyên phát, là thành phần quan trọng trong hệ thống phân giai đoạn TNM.

### Reference | Tài liệu tham khảo

AJCC TNM Classification

---

# 5. Breast - Adjusted AJCC 6th N (1988–2015) | Chỉ số N (Hạch lympho vùng)

### English Description

Represents the involvement of regional lymph nodes according to the AJCC TNM staging system.

### Vietnamese Description

Biến này biểu diễn tình trạng di căn hạch lympho vùng theo hệ thống TNM của AJCC.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | N0, N1, N2, N3, NX |
| Missing Value (Giá trị thiếu) | NX |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve ordinal order.
- NX indicates regional lymph nodes cannot be assessed.
- Keep unknown values for further evaluation during preprocessing.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Regional lymph node involvement is one of the strongest indicators of disease progression and survival in breast cancer patients.

**Tiếng Việt**

Tình trạng di căn hạch lympho vùng là một trong những yếu tố tiên lượng mạnh nhất đối với sự tiến triển của bệnh và khả năng sống còn của bệnh nhân ung thư vú.

### Reference |  Tài liệu tham khảo

AJCC TNM Classification

---

# 6. Breast - Adjusted AJCC 6th M (1988–2015) | Chỉ số M (Di căn xa)

### English Description

Represents the presence or absence of distant metastasis according to the AJCC TNM staging system.

### Vietnamese Description

Biến này biểu diễn tình trạng di căn xa của bệnh nhân theo hệ thống phân giai đoạn TNM của AJCC.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Binary / Categorical |
| Example (Ví dụ) | M0, M1, MX |
| Missing Value (Giá trị thiếu) | MX |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve the original coding.
- MX indicates distant metastasis cannot be assessed.
- Review unknown values before model training.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

The presence of distant metastasis is the defining characteristic of Stage IV breast cancer and is strongly associated with poor prognosis and reduced survival.

**Tiếng Việt**

Di căn xa là đặc điểm xác định ung thư vú giai đoạn IV và có mối liên hệ rất mạnh với tiên lượng xấu cũng như thời gian sống còn ngắn hơn.

### Reference | Tài liệu tham khảo

AJCC TNM Classification.

---

# 7. Histologic Type ICD-O-3 | Loại mô học theo ICD-O-3

### English Description

Represents the microscopic histological subtype of breast cancer using the International Classification of Diseases for Oncology, Third Edition (ICD-O-3).

### Vietnamese Description

Biến này biểu diễn loại mô học của ung thư vú theo hệ thống phân loại ICD-O-3.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | 8500, 8520, 8480 |
| Missing Value (Giá trị thiếu) | Rare |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve official ICD-O-3 codes.
- Rare histologic types may be grouped into an "Other" category during preprocessing.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Different histological subtypes exhibit distinct biological behavior, treatment response, recurrence patterns, and survival outcomes.

**Tiếng Việt**

Các loại mô học khác nhau có đặc điểm sinh học, đáp ứng điều trị, nguy cơ tái phát và tiên lượng sống còn khác nhau.

### Reference | Tài liệu tham khảo

International Classification of Diseases for Oncology (ICD-O-3).

---

# 8. Primary Site | Vị trí khối u nguyên phát

### English Description

Represents the anatomical location where the primary breast tumor originated.

### Vietnamese Description

Biến này biểu diễn vị trí giải phẫu của khối u nguyên phát trong tuyến vú.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | C50.0, C50.4, C50.9 |
| Missing Value (Giá trị thiếu) | Rare |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Verify valid ICD-O site codes.
- Preserve anatomical site categories.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Tumor location may influence surgical planning, lymphatic drainage, and treatment strategy.

**Tiếng Việt**

Vị trí của khối u có thể ảnh hưởng đến phương pháp phẫu thuật, đường dẫn lưu bạch huyết và chiến lược điều trị.

### Reference | Tài liệu tham khảo

ICD-O-3 Topography Manual.

---

# 9. Laterality | Bên xuất hiện khối u

### English Description

Represents the side of the body where the primary breast cancer originated.

### Vietnamese Description

Biến này biểu diễn bên cơ thể xuất hiện khối u nguyên phát.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | Left, Right, Bilateral |
| Missing Value (Giá trị thiếu) | Rare |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve all valid categories.
- Bilateral cases may be analyzed separately depending on study objectives.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Although laterality has limited prognostic value, it is an important clinical variable for diagnosis, treatment documentation, and epidemiological analysis.

**Tiếng Việt**

Mặc dù giá trị tiên lượng không lớn, biến Laterality vẫn rất quan trọng trong chẩn đoán, lập hồ sơ điều trị và nghiên cứu dịch tễ học.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.

---

# 10. Diagnostic Confirmation | Phương pháp xác nhận chẩn đoán

### English Description

Represents the method used to confirm the diagnosis of breast cancer.

### Vietnamese Description

Biến này biểu diễn phương pháp được sử dụng để xác nhận chẩn đoán ung thư vú.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | Positive Histology, Cytology, Clinical Diagnosis |
| Missing Value (Giá trị thiếu) | Rare |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Histologically confirmed cases are preferred for analysis.
- Verify consistency of diagnostic methods.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**

Diagnostic confirmation reflects the reliability of the cancer diagnosis and the overall quality of the registry data.

**Tiếng Việt**

Phương pháp xác nhận chẩn đoán phản ánh mức độ tin cậy của chẩn đoán ung thư và chất lượng dữ liệu của hệ thống SEER.

### Reference | Tài liệu tham khảo

SEER Program Coding Manual.

---

# 11. Tumor Size Group | Phân nhóm kích thước khối u

### English Description

Represents the binned primary tumor size categories derived from `Tumor_Size` based on clinical T-stage cutoffs.

### Vietnamese Description

Biến này biểu diễn nhóm kích thước khối u được phân loại từ `Tumor_Size` dựa trên các ngưỡng phân loại T trong lâm sàng.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | <=20mm (T1), 21-50mm (T2), >50mm (T3/T4) |
| Missing Value (Giá trị thiếu) | Unknown |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Categorized from continuous tumor size values in millimeters.
- Encoded using `StringIndexer` prior to model training.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Grouping tumor sizes aligns continuous measurement with clinical T-staging standards used in risk stratification.

**Tiếng Việt**
Phân nhóm kích thước u giúp đồng bộ dữ liệu đo lường liên tục với các tiêu chuẩn phân giai đoạn T trong phân tầng rủi ro lâm sàng.

### Reference | Tài liệu tham khảo

AJCC Cancer Staging Manual.

---

## Summary | Tóm tắt

| Variable | Data Type | Machine Learning Usage |
|----------|-----------|------------------------|
| Tumor Size | Numerical | Predictor Feature |
| Grade | Ordinal Categorical | Predictor Feature |
| AJCC Stage | Ordinal Categorical | Predictor Feature |
| AJCC T | Ordinal Categorical | Predictor Feature |
| AJCC N | Ordinal Categorical | Predictor Feature |
| AJCC M | Binary / Categorical | Predictor Feature |
| Histologic Type | Categorical | Predictor Feature |
| Primary Site | Categorical | Predictor Feature |
| Laterality | Categorical | Predictor Feature |
| Diagnostic Confirmation | Categorical | Predictor Feature |

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |