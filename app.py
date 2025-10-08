import streamlit as st
import pandas as pd
from preprocessing import preprocess
from autoeda import generate_eda_report
from automl_module import run_automl
from ai_insights import generate_ai_insights
import os
import io


# ---- Streamlit Page Setup ----
st.set_page_config(page_title="Automated Data Analysis", layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 75px;'>📊 Automated Data Analysis</h1>", unsafe_allow_html=True)
st.subheader("Only for smaller datasets")


# ---- Initialize Session State ----
if "df" not in st.session_state:
    st.session_state.df = None
if "df_clean" not in st.session_state:
    st.session_state.df_clean = None
if "preprocess_ran" not in st.session_state:
    st.session_state.preprocess_ran = False
if "eda_file" not in st.session_state:
    st.session_state.eda_file = None
if "eda_ran" not in st.session_state:
    st.session_state.eda_ran = False
if "automl_report" not in st.session_state:
    st.session_state.automl_report = None
if "ai_insights" not in st.session_state:
    st.session_state.ai_insights = None



# ---- Upload Dataset ----
uploaded = st.file_uploader("Upload CSV/XLSX", type=["csv", "xlsx"])
if uploaded:
    if uploaded.name.endswith(".csv"):
        st.session_state.df = pd.read_csv(uploaded)
    else:
        st.session_state.df = pd.read_excel(uploaded)

    st.subheader("Preview of Data")
    st.dataframe(st.session_state.df.head())



# ---- Run Preprocessing ----
if st.session_state.df is not None:
    if st.session_state.preprocess_ran != True:
        if st.button("Run Preprocessing"):
            st.session_state.df_clean = preprocess(st.session_state.df)
            st.session_state.preprocess_ran = True
            st.success("✅ Preprocessing Completed")

# --- Display only if preprocessing was actually run ---
if st.session_state.preprocess_ran and st.session_state.df_clean is not None:
    st.subheader("Preprocessed Data Preview")
    st.dataframe(st.session_state.df_clean.head())

    # --- Download Button ---
    csv_buffer = io.StringIO()
    st.session_state.df_clean.to_csv(csv_buffer, index=False)
    st.download_button(
        label="Download CSV",
        data=csv_buffer.getvalue(),
        file_name="preprocessed_data.csv",
        mime="text/csv",
    )



# ---- AutoEDA ----
if st.session_state.df is not None:
    if st.session_state.eda_ran != True:
        if st.button("Generate AutoEDA Report"):
            df_to_use = (
                st.session_state.df_clean
                if st.session_state.df_clean is not None
                else st.session_state.df
            )
            st.session_state.eda_file = generate_eda_report(df_to_use)
            st.session_state.eda_ran = True
            st.success("✅ EDA Report Generated")

# --- Display EDA Report only if it was generated ---
if st.session_state.eda_ran and st.session_state.eda_file is not None:
    if os.path.exists(st.session_state.eda_file):
        # Streamlit download button
        st.download_button(
            label="Download EDA Report",
            data=report_bytes,
            file_name=os.path.basename(tmp_file),
            mime="text/html",
        )



# ---- AutoML ----
if st.session_state.df_clean is not None:
    target_col = st.selectbox("Select Target Column", st.session_state.df_clean.columns)
    task = st.radio("Task Type", ["classification", "regression"], index=0)
    if st.button("Run AutoML"):
        df_to_use = st.session_state.df_clean if st.session_state.df_clean is not None else st.session_state.df
        st.session_state.automl_report = run_automl(df_to_use, target_col, task)
        st.success("✅ AutoML Completed")

# Display AutoML report
if st.session_state.automl_report is not None:
    st.json(st.session_state.automl_report)

# ---- AI Insights ----
if st.session_state.df is not None:
    if st.button("Generate AI Insights"):
        df_to_use = st.session_state.df_clean if st.session_state.df_clean is not None else st.session_state.df
        st.session_state.ai_insights = generate_ai_insights(df_to_use, target_col, task)
        st.success("✅ AI Insights Generated")

# Display AI Insights if available
if st.session_state.ai_insights is not None:
    st.subheader("🤖 AI Insights")
    st.write(st.session_state.ai_insights)
