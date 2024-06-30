import streamlit as st
import requests, time

def text_generator(text):
    # Yield each character with a delay
    for char in text:
        yield char
        time.sleep(0.002)


st.title("Internal-AI")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"], unsafe_allow_html=True)
        

with st.chat_message("assistant", avatar=":material/robot:"):
    response =  requests.get("http://127.0.0.1:8000/html/1.html")
    st.html(response.text)
    # st.session_state.messages.append({"role": "assistant", "content": response})

chat_counter = 2

if prompt := st.chat_input("How can I help you?"):
    # st.session_state.messages.append({"role": "user", "content": prompt})
    if chat_counter == 2:
        
        with st.chat_message("user", avatar=":material/person:"):
            response =  requests.get("http://127.0.0.1:8000/html/2.html")
            st.html(response.text)
            time.sleep(5)
            
        with st.chat_message("assistant", avatar=":material/robot:"):
            response =  requests.get("http://127.0.0.1:8000/html/3.html")
            st.html(response.text)
        
        
        
        chat_counter += 1
        

    # with st.chat_message("assistant", avatar="👨‍💻"):
    #     message_placeholder = st.empty()
    #     full_response = ""
        
    #     for chunk in requests.get("http://localhost:8000/markdown/ongoing-projects.md", stream=True).iter_content(chunk_size=None):
    #         if chunk:
    #             full_response += chunk.decode('utf-8')
    #             message_placeholder.html(full_response + "▌")
        
    #     message_placeholder.markdown(full_response)
    
    # st.session_state.messages.append({"role": "assistant", "content": full_response})