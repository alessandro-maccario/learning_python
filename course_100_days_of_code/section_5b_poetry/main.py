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
import secrets  # https://docs.python.org/3/library/secrets.html
import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase
import clipboard


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

# hide_st_style = """<style>
#                 #MainMenu {visibility:hidden;}
#                 footer {visibility:hidden;}
#                 header {visibility:hidden;}
#                 </style>
#                 """

# st.markdown(hide_st_style, unsafe_allow_html=True)


# --- Password generator function --- #
def generate_password() -> None:
    """
    It uses the string module to get the letters and digits thath make up
    the alphabet used to generate the random characters. These
    characters are appended to the pwd string which is then assigned
    to the session_state variable [pw].
    """
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    pwd_length = 14  # you can change it with your own decision
    pwd = ""  # empty string to start with

    for i in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))

    st.session_state[
        "pw"
    ] = pwd  # explanation about state_session: https://docs.streamlit.io/library/api-reference/session-state


def on_copy_click(text):
    """
    https://discuss.streamlit.io/t/copy-to-clipboard-using-st-markdown/50415/2
    """
    st.session_state.copied.append(text)
    clipboard.copy(text)


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

# Generate three columns
ocol1, ocol2, ocol3 = st.columns([1, 4, 1])  # 1 = 1 space; 4 = 4 spaces


# define text for the password
with ocol1:
    """"""
with ocol2:
    st.caption(
        "Secure password length is set at 14 chars."
    )  # display text used as hint
    st.button(
        "Generate secure password", key="pw_button", on_click=generate_password
    )  # the key must be unique
with ocol3:
    """"""

# "#"  # needed to display empty space. It is still streamlit magic

# Generate three columns
col1, col2, col3 = st.columns([1, 4, 1])  # 1 = 1 space; 4 = 4 spaces

with col1:
    """"""
with col2:
    # "---"
    # st.caption("Generated secure password")
    "---"
    st.subheader(st.session_state["pw"])
    st.button(
        "Copy to Clipboard 📋", on_click=on_copy_click, args=(st.session_state["pw"])
    )
with col3:
    """"""
