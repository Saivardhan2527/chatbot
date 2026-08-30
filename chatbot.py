import streamlit as st
import requests

st.set_page_config(page_title="chatbot",page_icon="🤖",layout="centered")

st.header("my chatbot")

# list to store and display the conversation
if "conversation" not in st.session_state:
    st.session_state["conversation"]=[]

for value in st.session_state["conversation"]:
    with st.chat_message(value["role"]):
         st.write(value["data"])


# to get input from user st.chat_input to get chatgpt type design

prompt = st.chat_input("write your prompt here..")

if prompt:
    
    st.session_state["conversation"].append({"role":"user","data":prompt})

    with st.chat_message("user"):
        st.write(prompt)


    res = requests.post("https://saivardhan2527.app.n8n.cloud/webhook-test/7bf42c88-ef4b-470f-808c-f9066515f11c",json={"message":prompt})

    ai_message = res.json()[0]["output"]
    
    
    st.session_state["conversation"].append({"role":"assistant","data":ai_message})
    with st.chat_message("assistant"):
            st.write(ai_message)