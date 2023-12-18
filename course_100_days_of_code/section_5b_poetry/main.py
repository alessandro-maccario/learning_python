"""
    Password Generator.
    Main source:
        - https://www.youtube.com/watch?v=Mxm3l3uDpFA
"""

# --- PIP packages ---#
import streamlit as st
import requests

# --- built in python packages ---#
import secrets  # https://docs.python.org/3/library/secrets.html
import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase

# --- build the main logic ---#
# --- Streamlit settings --- #

page_title = "Password Generator"
page_icon = " :old_key: "
layout = "centered"

# --- page config --- #
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

"#"
st.title(f"{page_icon}{page_title}")
"#"

# --- Streamlit config hide --- #
# Hide some page settings of streamlit such as the burger menu

hide_st_style = """<style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                header {visibility:hidden;}
                </style>
                """

st.markdown(hide_st_style, unsafe_allow_html=True)
