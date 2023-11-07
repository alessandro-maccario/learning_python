# import packages
from pkgs.config import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# write down the Deep Jungle decision text
st.write(DEEP_JUNGLE_DECISION)
# st.write("-----")

# give the user an intro based on the next decision
emerald_door_col, sapphyre_door_col, ruby_door_col = st.columns(3)

with emerald_door_col:
    st.write(EMERALD_RIDDLE)
    st.image("../imgs/emerald_door-pixelicious-modified.png")

with sapphyre_door_col:
    st.write(SAPPHIRE_RIDDLE)
    st.image("../imgs/sapphyre_door-pixelicious-modified.png")

with ruby_door_col:
    st.write(RUBY_RIDDLE)
    st.image("../imgs/ruby_door-pixelicious-modified.png")


st.write("-----")

# second decision of the user (wait = continue adventure; swim = game over)
user_path_decision = st.text(USER_PATH_DECISION)

# hacking way of centering the buttons:
# https://discuss.streamlit.io/t/center-button-st-button/9751/3
# create seven fictitious columns and use column 5 and 6 for centering the buttons
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1, 2, 3, 4, 5, 6, 7, 8])

with col1:
    pass
with col2:
    pass
with col3:
    pass
with col4:
    pass
with col5:
    if st.button("Emerald door", key="emerald"):
        switch_page("emerald_door")
with col6:
    if st.button("Sapphire door", key="sapphire"):
        switch_page("sapphire_door")
with col7:
    if st.button("Ruby \n\ndoor", key="ruby"):
        switch_page("ruby_door")
with col8:
    pass
