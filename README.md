# Breast Cancer Survival Prediction using Apache Spark MLlib

An end-to-end machine learning pipeline for predicting breast cancer patient survival status using the SEER Research Database and Apache Spark MLlib.

---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-orange)
![Spark MLlib](https://img.shields.io/badge/Spark%20MLlib-Machine%20Learning-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 1. Project Overview

Breast cancer is one of the most common cancers worldwide and remains a major cause of cancer-related mortality.

Accurate identification of high-risk patients can support treatment planning, patient monitoring, and clinical decision-making.

This project develops an end-to-end machine learning pipeline to predict breast cancer patient survival status using clinical data from the SEER (Surveillance, Epidemiology, and End Results) Research Database.

The system applies Apache Spark MLlib for large-scale data processing and machine learning, covering the complete workflow from data preprocessing and feature engineering to model training, evaluation, and interpretation.

---

# 2. Research Objective

The main objective of this project is to develop a scalable machine learning system capable of predicting breast cancer patient survival status based on clinical characteristics.

The project focuses on:

- Processing large-scale cancer registry data using Apache Spark
- Designing an effective feature engineering pipeline
- Comparing multiple classification algorithms
- Optimizing prediction thresholds for classification performance analysis
- Interpreting model decisions using explainable machine learning techniques

---

# 3. Dataset Description

## Data Source

SEER Research Database  
(National Cancer Institute)

Dataset:

Incidence - SEER Research Data,  
17 Registries, Nov 2025 Sub (2000–2023)

## Dataset Selection

Cancer type:

Breast Cancer (Site recode ICD-O-3/WHO 2008)

Diagnosis period:

2004 - 2015

## Target Variable

The prediction target is:

**Vital Status**

Mapping:

0 → Alive

1 → Dead

---

# 3. Dataset Description

## Data Source

SEER Research Database  
(National Cancer Institute)

Dataset:
Incidence - SEER Research Data,
17 Registries, Nov 2025 Sub (2000–2023)

## Dataset Selection

Cancer type: 
Breast Cancer (Site recode ICD-O-3/WHO 2008)

Diagnosis period: 2004 - 2015

## Target Variable

The prediction target is: Vital Status

Mapping:
0 → Alive

1 → Dead

---

# 4. System Architecture

The proposed system consists of six major stages:
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Machine Learning Model Training
5. Model Evaluation
6. Model Interpretation

---

# 5. Data Processing Pipeline

## Data Preprocessing
The preprocessing stage includes:

- Handling missing values
- Removing SEER special codes
- Data type conversion
- Duplicate checking
- Data cleaning and standardization

## Feature Engineering

Selected clinical features include:

### Demographic Features

- Age
- Sex
- Race
- Marital Status


### Tumor Characteristics

- Tumor Size
- AJCC Stage
- AJCC T
- AJCC N
- AJCC M
- Regional Lymph Nodes


### Treatment Information

- Surgery
- Radiation
- Chemotherapy


### Pathological Information

- Histologic Type
- Grade
- Hormone-related variables


---

# 6. Machine Learning Models

Four classification algorithms were implemented:

| Model | Description |
|---|---|
| Logistic Regression | Baseline linear classification model |
| Decision Tree | Rule-based classification |
| Random Forest | Ensemble tree-based learning |
| Gradient Boosted Trees (GBT) | Boosting-based high-performance model |


The models were developed using:  Apache Spark MLlib

---

# 7. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Additional analysis:

- Threshold optimization
- False Positive analysis
- False Negative analysis
- Prediction confidence analysis

---

# 8. Model Interpretation and Explainability

The selected GBT model was further analyzed to understand the factors influencing survival prediction.

The interpretation stage includes:

- Feature importance analysis
- Clinical feature contribution analysis
- Misclassified sample analysis
- False Positive and False Negative investigation
- Prediction confidence analysis
- Clinical interpretation of model outputs


# 9. Experimental Results

Four classification models were evaluated using Apache Spark MLlib:

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC | Training Time (s) |
|---|---:|---:|---:|---:|---:|---:|
| GBT Classifier | 0.7866 | 0.7886 | 0.7866 | 0.7874 | **0.8560** | 118.61 |
| Logistic Regression | 0.7782 | 0.7818 | 0.7782 | 0.7796 | 0.8433 | 55.76 |
| Random Forest | 0.7592 | 0.7679 | 0.7592 | 0.7617 | 0.8326 | 22.90 |
| Decision Tree | 0.7792 | 0.7791 | 0.7792 | 0.7791 | 0.5532 | 13.12 |


Based on ROC-AUC and F1-score, the Gradient Boosted Trees (GBT) classifier achieved the best overall performance and was selected for further model interpretation and clinical analysis.

To improve model transparency, the project performs:

## Feature Importance Analysis
Identify the clinical variables contributing most to survival prediction.

Examples of important clinical factors:

- Age
- Tumor characteristics
- AJCC staging
- Treatment-related features

## Error Analysis
The analysis includes:

- False Positive cases
- False Negative cases

False Negative cases are especially important because high-risk patients may be incorrectly classified as survivors.

## Clinical Interpretation
The model results are interpreted from a clinical perspective to understand relationships between patient characteristics and survival outcomes.

---

# 10. Project Structure

```text
Project_Breast_Cancer_SEER/

│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│   └── trained_models/
│       ├── logistic_regression_model/
│       ├── decision_tree_model/
│       ├── random_forest_model/
│       ├── gbt_classifier_model/
│       ├── logistic_regression_pipeline/
│       └── tree_models_pipeline/
│
├── notebooks/
│ ├── 01_Data_Exploration.ipynb
│ ├── 02_Data_Preprocessing.ipynb
│ ├── 03_Feature_Engineering.ipynb
│ ├── 04_Model_Training.ipynb
│ ├── 05_Model_Evaluation.ipynb
│ └── 06_Model_Interpretation.ipynb
│
├── reports/
│ ├── figures/
│ └── tables/
│
├── results/
│
├── src/
│ ├── data/
│ ├── features/
│ ├── models/
│ ├── visualization/
│ └── utils/
│
├── docs/
│ ├── proposal/
│ ├── report/
│ └── data_dictionary/
```

---

# 11. Technologies Used

Programming Language:
- Python 3.10

Big Data Framework:
- Apache Spark


Machine Learning:
- Spark MLlib

Data Processing:
- Pandas
- PySpark

Visualization:
- Matplotlib
- Seaborn

Development Tools:
- Jupyter Notebook
- Git

---

# 12. Future Improvements

Future development directions include:
- Applying Survival Analysis methods:
  - Cox Proportional Hazards
  - Random Survival Forest

- Applying Explainable AI:
  - SHAP
  - LIME

- Evaluating advanced boosting algorithms:
  - XGBoost
  - LightGBM
  - CatBoost

- Developing an interactive clinical prediction system using:
  - Streamlit
  - Flask

---

# 13. Conclusion

This project presents an end-to-end machine learning pipeline for breast cancer survival status prediction using Apache Spark MLlib and the SEER Research Database.

The proposed system integrates:

- Large-scale clinical data processing using Apache Spark
- Data preprocessing and feature engineering for SEER cancer records
- Machine learning classification with multiple algorithms
- Model evaluation using comprehensive performance metrics
- Model interpretation through feature importance and error analysis
- Clinical analysis to understand factors influencing survival prediction

Experimental results show that the Gradient Boosted Trees (GBT) classifier achieved the best overall performance among the evaluated models, with the highest ROC-AUC score and competitive F1-score.

The interpretation analysis identified important clinical factors contributing to survival prediction and highlighted the importance of analyzing prediction errors, especially False Negative cases in healthcare applications.

Although the current system provides valuable insights into breast cancer survival prediction, further improvements can be achieved by incorporating survival analysis methods, advanced explainable AI techniques, and additional clinical information.

This project demonstrates the potential of scalable machine learning approaches in supporting healthcare analytics and developing intelligent clinical decision support systems.

---

# Author

**JinxX**

Data Science Project 
Breast Cancer Survival Prediction using Apache Spark MLlib