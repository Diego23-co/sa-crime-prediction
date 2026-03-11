# 🇿🇦 South African Crime Count Prediction

A machine learning project that predicts provincial crime counts using South African 
crime statistics. Two models are compared — Linear Regression and Random Forest — 
to determine the best approach for predicting crime counts based on geography, 
crime category and financial year.

---

## 📊 Dataset

- **Source:** Kaggle — crimes_incidents_by_category
- **Original Source:** South African Police Service (SAPS) Crime Statistics
- **Records:** 840
- **Features:** Geography (Province), Crime Category, Financial Year
- **Target:** Crime Count (Quantitative — Discrete)

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📁 Project Structure
```
sa-crime-prediction/
│
├── sa-crime-prediction.ipynb       # Main notebook
├── crimes_incidents_by_category.csv  # Dataset
└── README.md                       # Project documentation
```

---

## ⚙️ How to Run

1. Clone the repository
```bash
git clone https://github.com/yourusername/sa-crime-prediction.git
```

2. Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Open the notebook
```bash
jupyter notebook sa-crime-prediction.ipynb
```

---

## 🔍 Methodology

1. **Exploratory Data Analysis** — examined distributions, crime trends over time 
   and crime counts by province and category
2. **Data Preprocessing** — encoded categorical columns using one-hot encoding, 
   extracted financial year as integer. No missing values or duplicates were found
3. **Model Training** — trained and compared Linear Regression and Random Forest
4. **Evaluation** — compared models using MSE and R² on both train and test sets
5. **Visualisation** — actual vs predicted, feature importance, residuals plot 
   and model comparison bar chart

---

## 📈 Results

| Model | Train R² | Test R² |
|---|---|---|
| Linear Regression | 0.725 | 0.715 |
| Random Forest | 0.998 | **0.997** |

Random Forest significantly outperformed Linear Regression, explaining **99.7% of 
the variance** in unseen crime count data with minimal overfitting.

---

## 🔑 Key Findings

- **Geography_ZA** (national aggregate) was the strongest predictor of crime count 
  with an importance score of ~0.52, suggesting national level patterns dominate 
  provincial level variation
- **Contact Crimes** was the most influential crime category, reflecting the 
  significant volume of assault, murder and robbery

---

## 📚 What I Learned

- End-to-end ML workflow from data loading to evaluation
- Importance of encoding categorical variables for ML models
- How to compare models using MSE and R² metrics
- Why Random Forest outperforms Linear Regression on skewed, non-linear data
- How to interpret feature importance to draw real-world conclusions

---

## 👤 Author

**Khutso Mashapu**  
BSc Honours in Computer Science  
[LinkedIn](https://linkedin.com/in/khutsomashapu) · [GitHub](https://github.com/Diego23-co)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
