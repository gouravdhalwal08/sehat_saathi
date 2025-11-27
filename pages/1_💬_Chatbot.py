import streamlit as st
from core.ai_helper import get_gemini_response
from core.language import TEXT

# Ensure language is set in session state
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

T = TEXT[st.session_state.lang]

st.header(T["chat_header"])

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": T["chat_welcome_message"]}
    ]

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input(T["chat_input_placeholder"]):
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(prompt)
            st.markdown(response)
    
    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response})