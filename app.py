import streamlit as st
import time
from bs4 import BeautifulSoup

if 'chat_counter' not in st.session_state:
    st.session_state['chat_counter'] = 2

def split_html_sections(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    sections = soup.find_all(class_='section')
    return [str(section) for section in sections]

def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

with st.chat_message("assistant", avatar=":material/robot:"):
    html_content = load_html_file("html/1.html")
    st.html(html_content)

if prompt := st.chat_input("How can I help you?"):
    if st.session_state.chat_counter == 2:
        
        with st.chat_message("user", avatar=":material/person:"):
            html_content = load_html_file("html/2.html")
            st.html(html_content)
            time.sleep(0.5)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            html_content = load_html_file("html/3.html")
            sections = split_html_sections(html_content)
            for section in sections:
                st.html(section)
                time.sleep(1)
        
        st.session_state.chat_counter += 1
    elif st.session_state.chat_counter == 3:
        with st.chat_message("user", avatar=":material/person:"):
            st.write(prompt)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            html_content = load_html_file("html/4.html")
            sections = split_html_sections(html_content)
            for section in sections:
                st.html(section)
                time.sleep(1)
        
        st.session_state.chat_counter += 1
                
    elif st.session_state.chat_counter == 4:
        with st.chat_message("user", avatar=":material/person:"):
            st.write(prompt)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            html_content = load_html_file("html/5.html")
            sections = split_html_sections(html_content)
            for section in sections:
                st.html(section)
                time.sleep(1)
        st.session_state.chat_counter += 1
    elif st.session_state.chat_counter == 5:
        with st.chat_message("user", avatar=":material/person:"):
            st.write(prompt)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            html_content = load_html_file("html/6.html")
            sections = split_html_sections(html_content)
            for section in sections:
                st.html(section)
                time.sleep(1)
        st.session_state.chat_counter += 1
