import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def grade_captions(captions: list):
    text = " | ".join(captions[:5])
    prompt = f"""
    Analyze these Instagram captions for engagement, clarity, and emotional connection. Rate them out of 10 and suggest how to improve them:
    "{text}"
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]