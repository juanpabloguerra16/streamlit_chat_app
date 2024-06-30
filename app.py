import streamlit as st
import requests, time

with st.chat_message("assistant", avatar=":material/robot:"):
    response =  requests.get("http://127.0.0.1:8000/html/1.html")
    st.html(response.text)

chat_counter = 2

if prompt := st.chat_input("How can I help you?"):
    if chat_counter == 2:
        
        with st.chat_message("user", avatar=":material/person:"):
            response =  requests.get("http://127.0.0.1:8000/html/2.html")
            st.html(response.text)
            time.sleep(5)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            response =  requests.get("http://127.0.0.1:8000/html/3.html")
            # your task is to parse and split the response by html section by section and write each chunk to st.html
            # refactor here
            st.html(response.text)
        
        
        
        chat_counter += 1
        