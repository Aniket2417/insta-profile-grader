import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def grade_bio(bio: str):
    prompt = f"""
    Rate this Instagram bio for attractiveness, clarity, and uniqueness. Suggest a better version if needed:
    Bio: "{bio}"
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]