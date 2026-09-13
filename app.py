import re
import streamlit as st

st.title("Auto-Scrub: Digital Footprint Cleaner")
st.write("Paste your text below to automatically redact emails and phone numbers.")

user_input = st.text_area("Input Text", placeholder="Paste text here...")

if st.button("Scrub Text"):
    if user_input:
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        
        redacted = re.sub(email_pattern, '[EMAIL REDACTED]', user_input)
        redacted = re.sub(phone_pattern, '[PHONE REDACTED]', redacted)
        
        st.subheader("Scrubbed Output:")
        st.write(redacted)
    else:
        st.warning("Please enter some text first.")
