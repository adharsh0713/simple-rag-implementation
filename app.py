import streamlit as st
import requests


st.title("Simple RAG Assistant")


question = st.text_input(
    "Ask a question about your documents"
)


if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "question": question
        }
    )


    result = response.json()


    st.subheader("Answer")

    st.write(
        result["answer"]
    )


    st.subheader("Sources")

    for source in result["sources"]:

        st.write(
            f'{source["source"]} - Page {source["page"]}'
        )