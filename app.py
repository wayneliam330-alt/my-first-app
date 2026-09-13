import re
import streamlit as st

st.set_page_config(page_title="SafePaste", page_icon="🔒")

st.title("🔒 SafePaste")
st.caption("Automatically redact emails, phone numbers, and sensitive keys before sharing.")

user_input = st.text_area("Paste text or code snippet below:", placeholder="e.g., Email me at john@example.com or call 555-0199...")

if st.button("Scrub Data", type="primary"):
    if user_input:
        # Patterns for sensitive data
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        card_pattern = r'\b(?:\d[ -]*?){13,16}\b'
        
        # Redact matches
        redacted = re.sub(email_pattern, '[EMAIL REDACTED]', user_input)
        redacted = re.sub(phone_pattern, '[PHONE REDACTED]', redacted)
        redacted = re.sub(card_pattern, '[CARD REDACTED]', redacted)
        
        st.subheader("Scrubbed Output:")
        st.code(redacted, language="text")
        st.success("Sensitive data hidden successfully!")
    else:
        st.warning("Please enter some text first.")
