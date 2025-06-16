import streamlit as st
from grader.profile_scraper import scrape_user_profile
from grader.bio_grader import grade_bio
from grader.caption_grader import grade_captions
from grader.photo_grader import score_profile_image

st.title("📸 Instagram Profile Grader for Personal Growth")

username = st.text_input("Enter your Instagram username (public only):")

if st.button("Analyze My Profile"):
    with st.spinner("Scraping and analyzing..."):
       profile = scrape_user_profile(username)


        st.subheader("1. Your Bio")
        st.write(profile["bio"])
        st.markdown("**AI Suggestions:**")
        st.write(grade_bio(profile["bio"]))

        st.subheader("2. Profile Image Analysis")
        st.image(profile["images"][0], width=300)
        st.write(score_profile_image(profile["images"][0]))

        st.subheader("3. Caption Quality")
        st.write(grade_captions(profile["captions"]))
