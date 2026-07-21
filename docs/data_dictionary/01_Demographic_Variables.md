# Demographic Variables (Đặc điểm nhân khẩu học)

---

## Document Information | Thông tin tài liệu

| Item | Description |
|------|-------------|
| Project | Breast Cancer Survival Prediction using Apache Spark |
| Dataset | SEER Research Data (2004–2015) |
| Category | Demographic Variables (Đặc điểm nhân khẩu học) |
| Variables | 4 |
| Version | 1.0 |

---

## Purpose | Mục đích

This document describes the demographic variables used in this project. These variables represent the baseline characteristics of patients at the time of diagnosis and are commonly used as important predictors in breast cancer survival analysis.

Tài liệu này mô tả các biến nhân khẩu học được sử dụng trong dự án. Các biến này phản ánh đặc điểm cơ bản của bệnh nhân tại thời điểm chẩn đoán và thường được sử dụng làm các biến đầu vào quan trọng trong các mô hình dự đoán khả năng sống còn của bệnh nhân ung thư vú.

---

## Variables Included | Danh sách biến

1. Age recode with <1 year olds and 90+
2. Sex
3. Race recode (W, B, AI, API)
4. Marital status at diagnosis

---

# 1. Age recode with <1 year olds and 90+

### English Description

Represents the patient's age group at the time of breast cancer diagnosis based on the official SEER age recode classification.

### Vietnamese Description

Biểu diễn nhóm tuổi của bệnh nhân tại thời điểm được chẩn đoán ung thư vú theo quy tắc phân nhóm tuổi chính thức của hệ thống SEER.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | 30–34 years, 45–49 years, 65–69 years, 90+ years |
| Missing Value (Giá trị thiếu) | None |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Verify that all age groups follow the official SEER coding rules.
- Convert to an ordered categorical variable if required by the machine learning algorithm.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Age is one of the strongest prognostic factors in breast cancer. It influences tumor characteristics, treatment strategies, and overall survival outcomes.

**Tiếng Việt**
Tuổi là một trong những yếu tố tiên lượng quan trọng nhất của ung thư vú. Biến này ảnh hưởng đến đặc điểm khối u, phương pháp điều trị và khả năng sống còn của bệnh nhân.

### Reference | Tài liệu tham khảo
SEER Program Coding Manual (2004–2015).

---

 # 2.  Sex | Giới tính

### English Description
Represents the biological sex of the patient at diagnosis.

### Vietnamese Description
Biến này biểu diễn giới tính sinh học của bệnh nhân tại thời điểm được chẩn đoán.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Female, Male |
| Missing Value | None |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu
- Preserve all valid categories.
- Encode categorical values before training.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Although breast cancer predominantly occurs in women, male breast cancer represents a rare but clinically important subgroup with different biological characteristics.

**Tiếng Việt**
Mặc dù ung thư vú chủ yếu gặp ở nữ giới, ung thư vú ở nam giới vẫn là một nhóm bệnh hiếm nhưng có đặc điểm lâm sàng và sinh học khác biệt.

### Reference | Tài liệu tham khảo
National Cancer Institute (NCI).

---

# 3. Race recode (W, B, AI, API)

### English Description
Represents the patient's race according to the standardized SEER race classification.

### Vietnamese Description
Biểu diễn chủng tộc của bệnh nhân theo hệ thống phân loại chủng tộc chuẩn của SEER.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Categorical |
| Example (Ví dụ) | White, Black, American Indian/Alaska Native, Asian or Pacific Islander |
| Missing Value (Giá trị thiếu) | Unknown (if applicable) |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu
- Standardize race categories.
- Keep unknown values as a separate category or handle during preprocessing based on the modeling strategy.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Race has been associated with differences in breast cancer incidence, access to healthcare, treatment response, and survival outcomes.

**Tiếng Việt**
Chủng tộc có liên quan đến sự khác biệt về tỷ lệ mắc bệnh, khả năng tiếp cận dịch vụ y tế, đáp ứng điều trị và tiên lượng sống còn.

### Reference | Tài liệu tham khảo
SEER Race Recode Documentation.

---

# 4.  Marital status at diagnosis | Tình trạng hôn nhân tại thời điểm chẩn đoán

### English Description
Represents the marital status of the patient at the time of breast cancer diagnosis.

### Vietnamese Description
Biến này biểu diễn tình trạng hôn nhân của bệnh nhân tại thời điểm được chẩn đoán ung thư vú.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type | Categorical |
| Example | Married, Single, Divorced, Widowed |
| Missing Value | Unknown |
| Machine Learning Usage | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Preserve official SEER categories.
- Group infrequent categories if appropriate.
- Encode categorical values before modeling.

### Research Importance |  Ý nghĩa trong nghiên cứu

**English**
Several epidemiological studies have shown that marital status may influence treatment adherence, social support, psychological well-being, and ultimately survival outcomes.

**Tiếng Việt**
Nhiều nghiên cứu dịch tễ học cho thấy tình trạng hôn nhân có thể ảnh hưởng đến khả năng tuân thủ điều trị, mức độ hỗ trợ xã hội, sức khỏe tâm lý và kết quả sống còn của bệnh nhân.

### Reference | Tài liệu tham khảo

National Cancer Institute (NCI)

---

# 5. Age Group | Phân nhóm độ tuổi

### English Description

Represents the binned age category of the patient derived from the continuous age variable for clinical grouping.

### Vietnamese Description

Biến này biểu diễn nhóm tuổi của bệnh nhân được phân chia từ biến tuổi liên tục (`Age`) thành các khoảng ranh giới lâm sàng.

| Property (Thuộc tính) | Value (Giá trị) |
|------------------------|-----------------|
| Data Type (Kiểu dữ liệu) | Ordinal Categorical |
| Example (Ví dụ) | <40, 40-50, 51-60, 61-70, >70 |
| Missing Value (Giá trị thiếu) | None |
| Machine Learning Usage (Vai trò trong ML) | Predictor Feature |

### Data Cleaning Notes | Ghi chú tiền xử lý dữ liệu

- Binned directly from `Age` column during preprocessing.
- Encoded using `StringIndexer` in Spark ML Pipeline.

### Research Importance | Ý nghĩa trong nghiên cứu

**English**
Age binning helps capture non-linear prognostic risks associated with distinct age brackets in breast cancer progression.

**Tiếng Việt**
Việc phân nhóm độ tuổi giúp mô hình ghi nhận các mối quan hệ phi tuyến tính về rủi ro tiên lượng theo từng giai đoạn tuổi đời của bệnh nhân.

### Reference | Tài liệu tham khảo

NCCN Breast Cancer Guidelines.

---

## Summary | Tóm tắt

| Variable | Data Type | Machine Learning Usage |
|----------|-----------|------------------------|
| Age | Categorical | Predictor Feature |
| Sex | Binary | Predictor Feature |
| Race | Categorical | Predictor Feature |
| Marital Status | Categorical | Predictor Feature |

---

## Revision History | Lịch sử cập nhật

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial documentation created. |