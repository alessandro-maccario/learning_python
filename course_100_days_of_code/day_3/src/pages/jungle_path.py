# import packages
from pkgs.config import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pkgs.utils import *


############################################
################# SIDEBAR ##################
############################################
# collapsed and the disable the Sidebar
st.set_page_config(
    layout="centered",  # set the content centered on the page
    initial_sidebar_state="collapsed",  # set the sidebar as collapsed
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# to hide the sidebar button use CSS
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# import the css to change style to the buttons
local_css("style.css")
############################################

# first decision of the user (left = continue adventure; right = game over)
st.write(JUNGLE_DECISION)

# create two columns and add picture for each path
col1, col2 = st.columns(2)

with col1:
    st.image("../imgs/deeper_jungle-pixelicious-modified.png")

with col2:
    st.image("../imgs/cliff-pixelicious-modified.png")

st.write("-----")

# second decision of the user (wait = continue adventure; swim = game over)
user_path_decision = st.text(USER_PATH_DECISION)

# hacking way of centering the buttons:
# https://discuss.streamlit.io/t/center-button-st-button/9751/3
# create seven fictitious columns and use column 5 and 6 for centering the buttons
col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])

with col1:
    pass
with col2:
    pass
with col3:
    if st.button("Deep Jungle", key="left"):
        switch_page("deep_jungle")
with col4:
    pass
with col5:
    if st.button("Cliff", key="right"):
        switch_page("cliff_path")
with col6:
    pass
with col7:
    pass


# navigate through different pages:
# https://discuss.streamlit.io/t/navigate-multipage-app-with-buttons-instead-of-sidebar/27986/19
# DOCS:
# https://docs.streamlit.io/library/get-started/multipage-apps

# Streamlit extras:
# https://arnaudmiribel.github.io/streamlit-extras/
