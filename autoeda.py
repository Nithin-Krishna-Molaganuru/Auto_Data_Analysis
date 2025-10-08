from ydata_profiling import ProfileReport
import uuid
import os
import streamlit as st

def generate_eda_report(df, target_column=None):
    """
    Generates an EDA report using YData-Profiling (v4.6.4)
    and saves it as an HTML file in the 'outputs' directory.
    If a target column is specified, it will be highlighted
    in correlations and key statistics.
    """
    os.makedirs("outputs", exist_ok=True)

    # If a target column is specified, mark it for correlation emphasis
    title = f"EDA Report{' - Target: ' + target_column if target_column else ''}"

    # Configure the profiling report
    profile = ProfileReport(
        df,
        title=title,
        explorative=True,
        correlations={
            "pearson": {"calculate": True},
            "spearman": {"calculate": True},
            "kendall": {"calculate": False},
        },
        vars={"num": {"low_categorical_threshold": 10}},
        interactions={"continuous": True, "targets": [target_column] if target_column else []},
    )

    # Save the report
    tmp_file = f"outputs/ydata_{uuid.uuid4().hex}.html"
    profile.to_file(tmp_file)

    # # Read the report content for download
    # with open(tmp_file, "rb") as f:
    #     report_bytes = f.read()

    # # Streamlit download button
    # st.download_button(
    #     label="Download EDA Report",
    #     data=report_bytes,
    #     file_name=os.path.basename(tmp_file),
    #     mime="text/html",
    # )

    # # Optionally show it inside Streamlit
    # with open(tmp_file, "r", encoding="utf-8") as f:
    #     st.components.v1.html(f.read(), height=800, scrolling=True)

    return tmp_file

