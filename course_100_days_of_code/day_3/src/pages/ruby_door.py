# import packages
from pkgs.config import *
from pkgs.utils import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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
st.write(RUBY_DOOR_DECISION)
st.write("-----")


# give the user an intro based on the next decision
col1, col2, col3 = st.columns(3)

with col1:
    pass

with col2:
    # create a clickable button
    st.image("../imgs/silent_monster-modified.png")

    # create another columns inside the other columns to center the link/text
    col4, col5, col6, col7, col8 = st.columns([1, 1, 15, 1, 1])
    with col4:
        pass
    with col5:
        pass
    with col6:
        st.link_button("SILENT MONSTER KEYBOARD MAT", "https://shorturl.at/syKQW")
    with col7:
        pass
    with col8:
        pass

with col3:
    pass
