# app4_quiz.py
import os
import streamlit as st
import teacher_quiz
from config import DB_PATH

st.set_page_config(page_title="Quiz Generator", page_icon="❓")
st.title("❓ საგამოცდო კითხვების გენერატორი")

st.write("დააჭირეთ ღილაკს დოკუმენტის მიხედვით 5 სასწავლო კითხვის მისაღებად.")

if st.button("5 კითხვის გენერირება"):
    if os.path.exists(DB_PATH):
        with st.spinner("კითხვები გენერირდება..."):
            questions = teacher_quiz.generate_questions()
            st.text_area("გენერირებული კითხვები:", value=questions, height=200)
    else:
        st.error("ჯერ შექმენით ბაზა ბრძანებით: python ingest.py")
