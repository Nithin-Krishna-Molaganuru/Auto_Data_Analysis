🚀 AutoDA — Automated Data Analysis and Machine Learning Platform
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

✅ Interactive Dashboard

Clean, user-friendly Streamlit interface.

Real-time visualizations and downloadable reports.

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

💡 Future Enhancements

Custom visualization panel with drag-and-drop charts

Integration with Google Sheets / BigQuery

Option to export trained models

Enhanced AI interpretation (LLM-based analytics summaries)

👨‍💻 Author

Nithin M.
🎓 B.F.Sc Graduate → Aspiring Data Analyst | Entrepreneur in Tech
📧 [your.email@example.com]
🌐 LinkedIn
 | GitHub
