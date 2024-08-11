"""
    Password Generator.
    Main source:
        - https://www.youtube.com/watch?v=Mxm3l3uDpFA
        Minute 4:51

    Other possible source:
        - https://hackernoon.com/how-to-create-a-random-password-generator-using-python

    Emojii:
        - https://emojipedia.org/old-key#technical
"""

# --- PIP packages ---#
import streamlit as st

# --- built in python packages ---#
# import secrets  # https://docs.python.org/3/library/secrets.html
# import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase
# import clipboard
from pkgs.utils import *


# --- build the main logic ---#
# --- Streamlit settings --- #

page_title = "Password Generator"
page_icon = " :old_key: "
layout = "centered"

# --- page config --- #
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(f"{page_icon}{page_title}")

# --- Streamlit config hide --- #
# Hide some page settings of streamlit such as the burger menu

hide_st_style = """<style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                header {visibility:hidden;}
                </style>
                """

st.markdown(hide_st_style, unsafe_allow_html=True)


if "copied" not in st.session_state:
    st.session_state.copied = []

# --- Main page --- #
# Streamlit will be looking for the password variable session state
# at the beginning of the session and, as long as we do not call any function
# it will throw an error because it does not have any at the beginning
# of the call.
if "pw" not in st.session_state:
    st.session_state["pw"] = ""

# Stramlit magic to create horizontal divider
"---"

# Generate two columns
ocol1, ocol2 = st.columns([4, 1])  # 4 = 4 space; 1 = 4 spaces


# define text for the password
with ocol1:
    # add a caption with a grey color
    st.caption(
        ":grey[Secure password length is set at 14 chars.]"
    )  # display text used as hint
    st.button(
        "Generate secure password", key="pw_button", on_click=generate_password
    )  # the key must be unique
with ocol2:
    """"""

# Generate two columns
col1, col2 = st.columns([4, 3])  # 4 = 4 space; 3 = 3 spaces

with col1:
    # "---"
    # st.caption("Generated secure password")
    st.subheader(st.session_state["pw"])
with col2:
    st.button(
        "Copy to Clipboard 📋", on_click=on_copy_click, args=(st.session_state["pw"],)
    )

# show when the password has been copied
for text in st.session_state.copied:
    st.toast(f"Copied to clipboard: {text}", icon="✅")
