import streamlit as st

st.title("🎈 My new app")
st.write("StreamLit приложение🎈 ")


import pandas as pd
st.title("Пример Streamlit - развертывание в Web приложение")
name = st.text_input("Введите ваше имя", "")
st.write(f"Hello {name}!")
x = st.slider("Select an integer x", 0, 100, 1)
y = st.slider("Select an integer y", 0, 100, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)
df = pd.DataFrame({"x": [x], "y": [y] , "x * y": [x * y]}, index = ["addition row"])
st.write(df)
df = pd.DataFrame({"x": [x], "y": [y] , "x - y": [x - y]}, index = ["addition row"])
st.write(df)
df = pd.DataFrame({"x": [x], "y": [y] , "x / y": [x / y]}, index = ["addition row"])
st.write(df)