import streamlit as st
import re
#from firebase import firebase

st.set_page_config(
    page_title="QPM",
    page_icon="",
)

st.title("Question Paper Maker")

cont1 = st.container()

cont1.subheader("Make your selections:-")

sel_sub = cont1.selectbox('Select the subject for the paper: ',('AI', 'OS', 'SQL', 'DS', 'Other'))


marks = cont1.number_input('Enter your previous marks: ', max_value = 100)
cont1.caption('Marks out of 100')
