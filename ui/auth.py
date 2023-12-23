"""
Auth in user, to proxy ui. 

Uses supabase passwordless auth: https://supabase.com/docs/reference/python/auth-signinwithotp

Remember to set your redirect url to 8501 (streamlit default).
"""
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client

# Set up Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def sign_in_with_otp(email: str):
    data = supabase.auth.sign_in_with_otp({"email": email})
    # Redirect to Supabase UI with the return data
    st.write(f"Please check your email for a login link!")
    

# Create the Streamlit app
def main():
    st.title("User Authentication")

    # User email input
    email = st.text_input("Enter your email")

    # Sign in button
    if st.button("Sign In"):
        sign_in_with_otp(email)


if __name__ == "__main__":
    main()