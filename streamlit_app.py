import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

data = 'hi~~!!!!!'

# 1. 버튼을 누르면 true라고 말하는 간단한 동작 구현
# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운 받기 동작 구현



# 입력
if st.button('Click the butten'):
        st.success('True, 잘했습니다.')
st.data_editor(df)
st.checkbox('Option 1')
country = st.radio('Pick Country:', ['France','Germany'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', ['김은수','김00'])
st.slider('Slide me', min_value=1, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
st.download_button('Download Source data', data)
st.camera_input('Click a Snap')
st.color_picker('Pick a color')

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write(country)
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True


