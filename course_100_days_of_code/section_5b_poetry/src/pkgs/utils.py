# --- PIP packages ---#
import streamlit as st

# --- built in python packages ---#
import secrets  # https://docs.python.org/3/library/secrets.html
import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase
import clipboard


# --- Password generator function --- #
def generate_password() -> None:
    """
    It uses the string module to get the letters and digits thath make up
    the alphabet used to generate the random characters. These
    characters are appended to the pwd string which is then assigned
    to the session_state variable [pw].

    Parameter
    ---------
    None

    Returns
    -------
    session_state: str
        Password string with the latest password created.
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
    Return the copied password generated text to clipboard.

    Parameter
    ---------
    text: str
        Password generated text

    Returns
    -------
    str
        Copied password

    References
    ----------
        - https://discuss.streamlit.io/t/copy-to-clipboard-using-st-markdown/50415/2
    """
    st.session_state.copied.append(text)
    clipboard.copy(text)
