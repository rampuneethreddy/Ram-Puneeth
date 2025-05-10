import streamlit as st 
from langchain_groq import ChatGroq
apikey="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"
st.title("chat with Groq")
st.write("This is a simple app to chat with Groq using the Langchain ")

llm = ChatGroq(
    model="llama-3.1-8b-instant", api_key=apikey
)


user = st.chat_input("what do you want to ask?")

if user:
    with st.spinner("Thinking... "):
        response = llm.invoke(user)
        st.write(response.content)
    