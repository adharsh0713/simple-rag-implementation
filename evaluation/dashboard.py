import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt


st.title("RAG Evaluation Dashboard")


with open(
    "evaluation/results.json"
) as f:
    data = json.load(f)


df = pd.DataFrame(
    data["results"]
)


st.subheader(
    "Similarity Scores"
)


st.dataframe(df)


fig, ax = plt.subplots()

ax.bar(
    df["question"],
    df["top_score"]
)

plt.xticks(
    rotation=45,
    ha="right"
)


st.pyplot(fig)


st.subheader(
    "Average Retrieval Score"
)


st.metric(
    "Average Score",
    round(
        df["top_score"].mean(),
        3
    )
)