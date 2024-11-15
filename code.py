import streamlit as st
import pandas as pd
import numpy as np

st.title('This is my first streamlit app!')
st.header('Header', divider='red')
st.write('Hello World!')

with st.sidebar:
    st.header("About App")
    st.write("Created on 8/23/2024")

st.markdown('Welcome')

x = st.slider("Choose the value of x", 1, 10)
st. write("The value of :blue[***x***] is", x)

st.subheader('Columns', divider='red')
col1, col2 = st.columns(2)

with col1:
    y = st.selectbox(
    "What number is y?",
    ("1", "2", "3"),
)
with col2:
    st. write("The value of :blue[***y***] is", y)

st.subheader('Area Chart', divider='red')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)