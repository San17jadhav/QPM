import streamlit as st
import re
#from firebase import firebase

st.set_page_config(
    page_title="QPM",
    page_icon="",
)

st.title("Question Paper Maker")

form = st.form(key='regis_form')
uname = form.text_input('Enter Name!',)
email = form.text_input('Enter Email')
passwd = form.text_input('Enter Password!',type='password')
cnpasswd = form.text_input('Confirm Password!',type='password')

form.markdown('***')

submit = form.form_submit_button('Register')
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

if submit:
    if uname=="" or email=="" or passwd=="" or cnpasswd=="":
        st.error('Enter all the Details!!')
    elif re.fullmatch(regex, email)==None:
        st.error('Invalid Email')
    elif passwd != cnpasswd:
        st.error('Password Does not matches!!')
    else:
        st.success('Registerated Successfully!!')


          
        '''firebase = firebase.FirebaseApplication('https://xxxxx.firebaseio.com/', None)  
        data =  { 'UserName': uname,  
          'Email': email,  
          'Password': passwd 
          }  
        result = firebase.post('/python-sample-ed7f7/Students/',data)
        st.success('Registered!')'''

