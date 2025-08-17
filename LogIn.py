import streamlit as st
import members as member


def login_restriction(email: str)-> bool:
    email.lower() in [m.lower() for m in member.ALLOWED_MEMBERS]


if "login" not in st.session_state:
    st.session_state.login = False

st.title("Chat Assistant LogIn")

if st.session_state["login"]:
    st.success("LogIn Successfull")
else:
    email = st.text_input("Please enter the email")
    password = st.text_input("Please enter the password")

    if st.button("LogIn"):
        if not email or not password:
            st.error("Please Enter Your E-mail and the Password")
        elif not login_restriction(email):
            st.error("Only members are allowed !!!", icon="🚨")
        else:
            if password == st.secrets["PASSWORD"]:
                st.session_state.login = True
                st.toast("Login Successful 🤩")
                st.success("LogIn Successfull")
                st.subheader('Please visit the ROBOREAD!')
            else:
                st.toast("Incoreect Password 😶")
                st.error('Incorrect Password', icon = "🚨")