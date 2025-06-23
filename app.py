import streamlit as st
from pyngrok import ngrok

# Streamlit App
st.title('Hello Pri!')
st.write('This is your first Streamlit Web App!')

name = st.text_input('Enter your name:')
if st.button('Say Hello'):
    st.write(f'Hello {name}!')

# Ngrok Auth
ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")  # Yahan apna token dalna

# Start ngrok tunnel
public_url = ngrok.connect(8501)
print('Your Web App is Live at:', public_url)
