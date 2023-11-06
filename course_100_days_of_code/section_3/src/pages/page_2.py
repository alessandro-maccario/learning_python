# import packages
from pkgs.config import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# first decision of the user (left = continue adventure; right = game over)
st.write(JUNGLE_DECISION)
st.write("-----")

# second decision of the user (wait = continue adventure; swim = game over)
user_path_decision = st.text_input(
    """ Will you proceed to the jungle or to the cliff? Insert jungle or cliff:  """
).lower()

# navigate through different pages:
# https://discuss.streamlit.io/t/navigate-multipage-app-with-buttons-instead-of-sidebar/27986/19
# DOCS:
# https://docs.streamlit.io/library/get-started/multipage-apps

# Streamlit extras:
# https://arnaudmiribel.github.io/streamlit-extras/
