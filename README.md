# 🏥 AI Insurance Charges Predictor

> A production-ready Machine Learning web application that predicts annual medical insurance charges based on an individual's demographic and health-related information.

<p align="center">
  <img src="screenshots/home.png" width="90%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</p>

---

# 🌐 Live Demo

🔗 **Application:** https://YOUR-STREAMLIT-APP.streamlit.app

📂 **GitHub Repository:** https://github.com/YOUR_USERNAME/insurance-charges-predictor

---

# 📖 Overview

Medical insurance costs depend on multiple factors such as age, BMI, smoking habits, number of children, gender, and region.

This project uses a **Linear Regression** model trained on the Medical Cost Personal Dataset to estimate annual insurance charges. The model is deployed through a professional multi-page Streamlit application with an intuitive and responsive interface.

The project demonstrates the complete Machine Learning workflow—from data preprocessing and feature engineering to model deployment.

---

# ✨ Features

- 🔮 Real-time insurance cost prediction
- 📊 Interactive analytics dashboard
- 📈 Model performance metrics
- 🧠 Machine Learning insights
- 🎨 Modern responsive UI
- 🌙 Premium dark theme
- ⚡ Fast predictions
- 📱 Mobile-friendly interface

---

# 🧠 Machine Learning Pipeline

### Data Preprocessing

- Missing value analysis
- Feature encoding
- Feature scaling
- BMI category creation
- Data cleaning

### Feature Engineering

- Gender Encoding
- Smoker Encoding
- Region Encoding
- BMI Category
- Standard Scaling

### Model Training

- Train-Test Split
- Linear Regression
- Model Evaluation
- Cross Validation

---

# 📊 Model Performance

| Metric | Score |
|---------|-------:|
| R² Score | **0.804** |
| Adjusted R² | **0.799** |
| MAE | **₹4,295** |
| RMSE | **₹6,000** |
| Cross Validation Score | **0.751** |

---

# 🖥️ Application Pages

## 🏠 Home

Project overview and introduction.

---

## 🔮 Prediction

Enter user information and receive an estimated annual insurance charge.

<p align="center">
<img src="screenshots/prediction.png" width="85%">
</p>

---

## 📊 Analytics

Interactive visualizations showing trends within the dataset.

Examples include:

- Age Distribution
- BMI Distribution
- Charges Distribution
- Smoking Impact
- Regional Analysis

---

## 📈 Model Performance

Displays evaluation metrics including:

- R² Score
- MAE
- RMSE
- Adjusted R²
- Cross Validation

---

## 👨‍💻 About

Project information, technologies used, and developer details.

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| ML Library | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Frontend | Streamlit |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
insurance-charges-predictor/

│
├── app.py
├── requirements.txt
├── README.md
├── insurance_model.pkl
├── scaler.pkl
│
├── pages_home.py
├── pages_predict.py
├── pages_analytics.py
├── pages_performance.py
├── pages_about.py
│
├── components.py
├── theme.py
│
├── assets/
│
├── screenshots/
│   ├── home.png
│   ├── prediction.png
│   ├── analytics.png
│   └── performance.png
│
└── notebooks/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/insurance-charges-predictor.git
```

Navigate to the project

```bash
cd insurance-charges-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📋 Dataset

**Medical Cost Personal Dataset**

Features:

- Age
- Sex
- BMI
- Children
- Smoker
- Region

Target:

- Insurance Charges

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Machine Learning
- Regression Analysis
- Feature Engineering
- Data Preprocessing
- Model Evaluation
- Model Deployment
- Streamlit Development
- Git & GitHub
- Data Visualization

---

# 🔮 Future Improvements

- Random Forest & XGBoost comparison
- SHAP explainability
- Prediction confidence intervals
- PDF report generation
- User authentication
- Docker support
- CI/CD pipeline
- Cloud deployment on AWS/Azure

---

# 👨‍💻 Developer

**Kunal**

B.Tech CSE (AI & ML)

- GitHub: https://github.com/YOUR_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN
- Email: YOUR_EMAIL

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the MIT License.
