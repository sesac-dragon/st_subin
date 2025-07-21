import streamlit as st
import os
import pymysql

st.write('배포 테스트')
st.write('배포 테스트용 앱입니다.')

st.write('추가 커밋')

api_key = os.environ.get("API_SECRET_KEY")

st.write(f'api key = {api_key}')

if not os.environ.get('DB_HOST'):
    st.write('디비 접속정보가 없습니다.')
else:
    conn = pymysql.connect(host=os.environ.get('DB_HOST'))