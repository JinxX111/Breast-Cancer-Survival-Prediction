# Breast Cancer Survival Prediction using Apache Spark MLlib

An end-to-end machine learning pipeline for predicting breast cancer patient survival status using the SEER Research Database and Apache Spark MLlib.

---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-orange)
![Spark MLlib](https://img.shields.io/badge/Spark%20MLlib-Machine%20Learning-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 1. Project Overview

Breast cancer is one of the most common cancers worldwide and remains a major cause of cancer-related mortality. Accurate identification of high-risk patients can support treatment planning, patient monitoring, and clinical decision-making.

This project develops an end-to-end machine learning pipeline to predict breast cancer patient survival status using clinical data from the SEER (Surveillance, Epidemiology, and End Results) Research Database.

The system applies Apache Spark MLlib for large-scale data processing and machine learning, covering the complete workflow from data preprocessing, feature engineering, model training, evaluation, threshold optimization, and clinical error analysis.

---

## 2. Research Objectives

The main objective of this project is to develop a scalable machine learning system capable of predicting breast cancer patient survival status based on clinical characteristics.

The prediction task is formulated as a **binary survival status classification problem**.

Key project milestones include:

- Processing large-scale cancer registry data using **Apache Spark**.
- Designing an effective **Feature Engineering pipeline** tailored for oncological variables.
- Handling class imbalance using **class weighting (`weight`)**.
- Comparing multiple classification algorithms.
- Optimizing prediction thresholds for classification performance analysis.
- Interpreting model decisions and misclassifications (**False Positives** & **False Negatives**) using explainable machine learning techniques.

---

# 3. Dataset Description

## Data Source

- **Database:** SEER Research Database (National Cancer Institute - NCI)
- **Dataset Submission:** *Incidence - SEER Research Data, 17 Registries, Nov 2025 Sub (2000–2023)*

## Cohort Selection Criteria

- **Cancer Site:** Breast Cancer (Site recode ICD-O-3/WHO 2008)
- **Diagnosis Period:** 2004 - 2015

## Target Variable

The prediction target is derived from the patient's vital status.

| Variable | Description |
|---|---|
| `label = 0` | Alive / Survived at last follow-up |
| `label = 1` | Dead / Deceased |

### Note

`Survival_Months` is not used as a predictive feature in this classification pipeline.

The current project focuses on **binary survival status prediction**, while time-to-event survival modeling will be considered as a future extension.

---

# 4. System Architecture

The proposed system consists of six major stages:

```text
+-----------------------+     +-----------------------+     +-----------------------+
|  1. Data Collection   | --> | 2. Data Preprocessing | --> |3. Feature Engineering |
|     (SEER Database)   |     | (Cleaning & Casting)  |     |  (Derived Features)   |
+-----------------------+     +-----------------------+     +-----------------------+
                                                                        |
                                                                        v
+-----------------------+     +-----------------------+     +-----------------------+
|6. Model Interpretation| <-- |  5. Model Evaluation  | <-- | 4. ML Model Training  |
|  (Error Analysis)     |     | (Metrics & Threshold) |     |     (Spark MLlib)     |
+-----------------------+     +-----------------------+     +-----------------------+
```
---
## 5. Data Processing & Feature Engineering

### Data Preprocessing

The preprocessing stage prepares raw SEER data for machine learning modeling:

- Handling missing values and standardizing SEER special codes (`Unknown`, `999`, etc.).
- Data type conversion and schema standardization.
- Removing duplicated records and applying cohort filtering.
- Preparing clean Spark DataFrames for downstream feature engineering.

### Feature Engineering

To improve predictive capability, several clinically meaningful features were constructed:

- **`Node_Ratio`**: Ratio between positive regional lymph nodes and examined regional lymph nodes.

  Formula:
  $$\text{Node\_Ratio} = \frac{\text{Regional\_Nodes\_Positive}}{\text{Regional\_Nodes\_Examined}}$$

  This feature represents lymph node involvement severity.

- **`Hormone_Status`**: Composite biomarker feature derived from Estrogen Receptor (ER) and Progesterone Receptor (PR) status.

  Categories:
  - `HR_Positive`
  - `HR_Negative`
  - `HR_Mixed`
  - `Unknown`

- **Age and Tumor Characteristics**:
  - Age and tumor-related variables were retained as important clinical predictors.
  - Tumor size, AJCC staging information, and pathological characteristics were prepared for machine learning models.

- **`weight`**:
  - Inverse class frequency weighting was applied to handle class imbalance.
  - The weight column was used during model training:

### Feature Summary

| Feature Group | Features Included |
|---|---|
| **Demographics** | `Age`, `Sex`, `Race`, `Marital_Status` |
| **Tumor Characteristics** | `Tumor_Size`, `AJCC_Stage`, `AJCC_T`, `AJCC_N`, `AJCC_M`, `Grade`, `Histologic_Type` |
| **Lymph Node Status** | `Regional_Nodes_Examined`, `Regional_Nodes_Positive`, `Node_Ratio` |
| **Biomarkers & Treatment** | `Hormone_Status`, `Surgery_Primary_Site`, `Surgery_Other_Regional`, `Surgery_Radiation_Sequence`, `Radiation`, `Chemotherapy` |

--- 

## 6. Machine Learning Models

Four classification algorithms were trained and evaluated using **Apache Spark MLlib Pipelines**:

| Model | Description |
|---|---|
| **Logistic Regression** | Baseline linear classifier with class weighting |
| **Decision Tree** | Rule-based non-linear classifier |
| **Random Forest** | Ensemble tree-based bagging classifier |
| **Gradient Boosted Trees (GBT)** | Sequential boosting-based high-performance classifier |

---

# 7. Experimental Results

The models were evaluated using standard classification metrics and execution efficiency.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Training Time (s) |
|---|---:|---:|---:|---:|---:|---:|
| **GBT Classifier** | **0.7866** | **0.7886** | **0.7866** | **0.7874** | **0.8560** | 118.61 |
| Logistic Regression | 0.7782 | 0.7818 | 0.7782 | 0.7796 | 0.8433 | 55.76 |
| Random Forest | 0.7592 | 0.7679 | 0.7592 | 0.7617 | 0.8326 | 22.90 |
| Decision Tree | 0.7792 | 0.7791 | 0.7792 | 0.7791 | 0.5532 | 13.12 |

> **Key Finding:**  
> Based on ROC-AUC and F1-score among evaluated classification models, the Gradient Boosted Trees (GBT) classifier achieved the best overall performance and was selected for further interpretation and clinical error analysis.

---

## 8. Model Interpretation & Misclassification Case Study

To move beyond "black-box" predictions, the best-performing GBT model underwent rigorous interpretation:

---

### Feature Importance

The main predictors contributing to model decisions include:

1. **Node_Ratio & Regional_Nodes_Positive**  
   - Represents lymph node involvement and disease spread.

2. **Age**
   - Represents baseline mortality risk associated with patient characteristics.

3. **Tumor_Size & AJCC_Stage**
   - Represents anatomical disease extent.

4. **Hormone_Status & Treatment Variables**
   - Includes chemotherapy and radiation-related information.

---

# Misclassified Sample Analysis

Model predictions were investigated through False Negative (FN) and False Positive (FP) analysis.

| Error Type | Definition | Total Cases | Average Age | Average Tumor Size (mm) | Average Positive Nodes | Average Node Ratio |
|---|---|---:|---:|---:|---:|---:|
| False Negative | Predicted Alive, Actual Dead | 9,032 | 54.67 | 21.84 | 0.77 | 0.096 |
| False Positive | Predicted Dead, Actual Alive | 10,332 | 64.10 | 28.78 | 2.21 | 0.184 |

---

# Clinical Insights from Error Analysis

## False Negative (FN) Cases

**Predicted Alive, Actual Dead**

Observed pattern:

- Average age: approximately 54.67 years
- Average tumor size: approximately 21.84 mm
- Average positive nodes: approximately 0.77
- Average Node_Ratio: 0.096

Clinical interpretation:

The model may underestimate risk in patients with apparently favorable clinical characteristics.

The observed mortality may be influenced by biological characteristics or clinical factors that are not captured in the available SEER variables.

---

## False Positive (FP) Cases

**Predicted Dead, Actual Alive**

Observed pattern:

- Average age: approximately 64.10 years
- Average tumor size: approximately 28.78 mm
- Average positive nodes: approximately 2.21
- Average Node_Ratio: 0.184

Clinical interpretation:

The model may overestimate mortality risk in patients with advanced clinical characteristics.

Differences in survival outcomes may be affected by treatment variations, comorbidities, and other unavailable clinical factors.

---

# 9. Project Structure

```text
Project_Breast_Cancer_SEER/
│
├── data/
│   ├── raw/                      # Raw SEER ASCII / CSV files
│   ├── interim/                  # Intermediate cleaned DataFrames
│   └── processed/                # Parquet files ready for ML modeling
│
├── models/
│   └── trained_models/
│       ├── logistic_regression_model/
│       ├── decision_tree_model/
│       ├── random_forest_model/
│       └── gbt_classifier_model/
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   ├── 05_Model_Evaluation.ipynb
│   └── 06_Model_Interpretation.ipynb
│
├── reports/
│   ├── figures/                  # ROC curves, confusion matrices, importance plots
│   └── tables/                   # Metric tables and misclassification exports
│
├── src/
│   ├── data/                     # Reserved for future modularization
│   ├── features/                 # Reserved for future feature pipeline
│   ├── models/                   # Reserved for future model scripts
│   └── utils/                    # Reserved for helper functions
│
└── docs/
    ├── proposal/                 # Initial project proposals
    ├── report/                   # Final research reports
    └── data_dictionary/          # Detailed dataset documentation
```

---

## 10. Technologies Used

- **Language:** Python 3.10
- **Big Data Computing:** Apache Spark 3.x / PySpark
- **Machine Learning:** Spark MLlib
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook, VS Code, Git

---

## 11. Future Improvements

- **Survival Analysis:** Extend the project with time-to-event survival models (e.g., Cox Proportional Hazards, Random Survival Forests) to estimate survival time and risk over follow-up periods.- **Explainable AI (XAI):** Integrate SHAP (SHapley Additive exPlanations) or LIME for instance-level model explanation.
- **Advanced Boosting Ensembles:** Explore integration with XGBoost4J-Spark or LightGBM on Spark.
- **Clinical Web Application:** Deploy a real-time risk assessment dashboard using Streamlit or Flask.

---

## 12. Conclusion

This project successfully establishes a scalable, big-data-ready machine learning framework for predicting breast cancer survival using Apache Spark MLlib. By leveraging clinical feature engineering (**`Node_Ratio`**, **`Hormone_Status`**) and class weighting, the pipeline achieved competitive survival prediction performance. Beyond standard predictive metrics, the clinical misclassification study highlights the importance of understanding biological heterogeneity in healthcare AI systems.

---

## Author

- **JinxX**
 Data Science & Machine Learning Project
 
Breast Cancer Survival Prediction using Apache Spark MLlib