# import packages
from pkgs.config import *
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

############################################
################# SIDEBAR ##################
############################################
# Sidebar
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

############################################

# add a title to the main page
# st.title(":blue[The Pirate Treasure Island Adventure]")
# set the title to the center overriding the streamlit html
st.markdown(
    "<h1 style='text-align: center; color: #990000;'>The Pirate Treasure Island Adventure</h1>",
    unsafe_allow_html=True,
)
# add a grey divider for better separation
st.header("", divider="grey")


############################################
################## IMAGE ###################
############################################

print(START_TREASURE_ISLAND)
# add the treasure chest image
image = Image.open("../imgs/treasure_chest_pixel_cropped.png")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(" ")

with col2:
    st.image(image)

with col3:
    st.write(" ")


############################################

# add another division line
# st.header("", divider="green")
st.write("-----")

###################################
###### TREASURE ISLAND GAME #######
###################################


if __name__ == "__main__":
    # print the introduction story to the game
    st.write(INTRO_DESCRIPTION)

    # give the user an intro based on the next decision
    col1, col2 = st.columns(2)

    with col1:
        st.write(FIRST_LEFT_PATH)
        st.image("../imgs/dense_jungle-pixelicious-modified.png")

    with col2:
        st.write(FIRST_RIGHT_PATH)
        st.image("../imgs/wrecked_ship-pixelicious-modified.png")

    st.write("-----")
    # second decision of the user (wait = continue adventure; swim = game over)
    user_path_decision = st.text(USER_PATH_DECISION)

    # hacking way of centering the buttons:
    # https://discuss.streamlit.io/t/center-button-st-button/9751/3
    # create seven fictitious columns and use column 5 and 6 for centering the buttons
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 3, 4, 5, 6, 7])

    with col1:
        pass
    with col2:
        pass
    with col3:
        pass
    with col4:
        pass
    with col5:
        if st.button("Jungle", key="left"):
            switch_page("jungle_path")
    with col6:
        if st.button("Rocky shoreline", key="right"):
            switch_page("rocky_shoreline_path")
    with col7:
        pass
