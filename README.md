🚀 Automated Data Analysis and Machine Learning Platform
📊 End-to-End Data Exploration, Visualization & AutoML in One Click

AutoDA is an interactive Streamlit web app that simplifies data analysis, exploration, and model building for beginners, analysts, and data scientists.
It automatically handles data preprocessing, visualization, EDA, and machine learning model selection using FLAML, delivering AI-powered insights in seconds — all without writing a single line of code.

🧠 Key Features

✅ Automated Data Analysis (AutoEDA)

Upload your dataset (CSV/XLSX) and instantly view summaries, missing values, correlations, and profiling reports via ydata-profiling.

Generates visual insights using Matplotlib and Seaborn.

✅ Automated Machine Learning (AutoML)

Leverages FLAML to automatically find the best model with optimized hyperparameters.

Supports LightGBM, XGBoost, and CatBoost seamlessly.

Displays metrics like accuracy, precision, recall, F1-score, and ROC-AUC.

✅ AI Insights (Experimental)

Uses Hugging Face Inference API to generate natural-language insights about dataset patterns and trends.

Helps users interpret results in plain English.



🏗️ Tech Stack

Layer	Technology
Frontend/UI	Streamlit
Backend	Python
AutoML	FLAML
EDA & Visualization	Pandas, NumPy, Matplotlib, Seaborn, ydata-profiling
Modeling Frameworks	LightGBM, XGBoost, CatBoost
AI Insight Engine	Hugging Face API
File Handling	openpyxl, requests

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AutoDA.git
cd AutoDA

2️⃣ Create a Virtual Environment
python -m venv AutoDA
source AutoDA/bin/activate  # or AutoDA\Scripts\activate on Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Hugging Face API Token

Create a .streamlit/secrets.toml file or set environment variables:

HF_TOKEN = "your_huggingface_api_token_here"
(Make sure not to commit your token to GitHub)

5️⃣ Run the App
streamlit run app.py


☁️ Deployment

You can deploy this project on:

Streamlit Cloud

Hugging Face Spaces (Gradio/Streamlit mode)

Render

Vercel (via Python backend)


🧩 Folder Structure
AutoDA/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── data/                 # Uploaded datasets (ignored in .gitignore)
└── assets/               # Visuals, logos, or static files



🔍 Example Use Case

Upload your dataset (e.g., sales.csv)

Perform full EDA profiling in seconds

Automatically build and validate ML models (classification/regression)

View AI-driven insights explaining patterns and relationships



🏆 Project Highlights

Built with modular code design for scalability.

Designed for non-technical users to perform advanced analytics.

Demonstrates data analyst + product-building mindset.

Ready for portfolio showcase and production deployment.



⚠️ Precautions and 🚧 Limitations

This is a app suitable for smaller datasets which doesnt have high token size

This is not a complete replacement for Data Anlaysis, as every dataset is unique and each requires specific processing to get accurate results.

This is a best tool for Beginners and Amateurs, and helpful for AutoEDA tasks for professionals in reducing the step of EDA even for Large Datasets.

ML predictions are not posiible for every dataset for the reason that it requires extensive preprocessing and data structuring to fit in the models and estimators, thus few datasets might not get any ML Predictions, thus AI Insights

AI insights could to restricted for few datasets for the fact that more tokens analysis required stronger models which are not economical, thus when low end models are used they can't handle much of data at a time, thus resulting in crashes or errors.



👨‍💻 Author

Nithin Krishna Molaganuru

Aspiring Data Analyst | Entrepreneur in Tech

E-Mail : nithinkrishnamolaganuru@gmail.com

LinkedIn : www.linkedin.com/in/nithin-krishna-molaganuru

GitHub : 
