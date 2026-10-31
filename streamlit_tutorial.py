import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit !")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets get started")

#Conditional Logic with widgets

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

#Displaying Data and Charts
df = pd.DataFrame(np.random.randn(20,2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

#File uploading and caching topics

upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*,`code`,[link](https://streamlit.io)")
st.code("for i in range(5): print(i)",language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number",min_value=0,max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple","banana","mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","olives"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree to the terms")

if st. checkbox("Show Details"):
    st.info("Hear are more details...")
else:
    st.write("Table would appear hear")

with st.form("login.form"):
    username=st.text_input("username")
    password=st.text_input("Password",type="password")
    submitted=st.form_submit_button("login")

    if submitted:
        st.success(f"Welcome,{username}!")

st.image("https://res.cloudinary.com/dhmxejzos/image/upload/v1785918602/icp7qnrra14endexo1ub.webp",
         caption="Sample Image",
         use_container_width=True
        )
st.video("https://www.youtube.com/watch?v=YwANe-1W8iU")

