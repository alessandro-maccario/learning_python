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

# write down the Cliff decision text
st.write(CLIFF_DECISION)

# create two columns and add picture for each path
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    pass
with col2:
    st.image("../imgs/kraken-pixelicious-modified.png")
with col3:
    pass

st.write("Would you like to start again?")
if st.button("Start again", key="left"):
    switch_page("treasure_island")
