# import packages
from pkgs.config import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# first decision of the user (left = continue adventure; right = game over)
st.write(SAPPHIRE_DOOR_DECISION)
st.write("-----")


# give the user an intro based on the next decision
col1, col2, col3 = st.columns(3)

with col1:
    pass

with col2:
    # create a clickable button
    st.link_button("CORSAIR HARPOON", "https://shorturl.at/cRU56")

with col3:
    pass
