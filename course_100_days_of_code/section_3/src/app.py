# import packages
from pkgs.config import *
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# add a title to the main page
st.title(":blue[The Pirate Treasure Island Adventure]")
st.header("", divider="grey")


# add a subheader
st.text(
    """         Welcome to this text-based game adventure where you, mate, the adventurer, 
        will go through a Piraty adventure to found an amazing treasure at the end 
        of the quest... If you can survive the perils along the way! """
)


###################################
###### TREASURE ISLAND GAME #######
###################################


if __name__ == "__main__":
    # print the title and the treasure chest variable
    st.write(START_TREASURE_ISLAND)

    # print the introduction story to the game
    st.write(INTRO_DESCRIPTION)

    # You should start with a loop so the user can start again whenever they want!
    is_loop_true = True

    # give the user an intro based on the next decision
    st.write(FIRST_LEFT_PATH)
    print()
    st.write(FIRST_RIGHT_PATH)

    # hacking way of centering the buttons:
    # https://discuss.streamlit.io/t/center-button-st-button/9751/3
    # create three columns
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
        if st.button("Left", key="left"):
            switch_page("page_2")
    with col6:
        if st.button("Right", key="right"):
            switch_page("page_3")
    with col7:
        pass

    # # let the user choose the first step
    # if st.button("Left", key="left"):
    #     switch_page("page_2")

    # if st.button("Right", key="right"):
    #     switch_page("page_3")
    # if left_path_button == True:
    #     switch_page("page_2")

    # user_path_decision = st.radio(
    #     "Which one do you chose?",
    #     ["Left", "Right"],
    #     captions=["Deep Jungle", "Rocky shoreline"],
    # ).lower()
    # if user_path_decision == "left":
    #     # switch_page("page_2")
    #     print(user_path_decision)

    # # first decision of the user (left = continue adventure; right = game over)
    # if user_path_decision == "left":
    #     st.write(JUNGLE_DECISION)
    #     st.write("-----")

    #     # second decision of the user (wait = continue adventure; swim = game over)
    #     user_path_decision = st.text_input(
    #         """ Will you proceed to the jungle or to the cliff? Insert jungle or cliff:  """
    #     ).lower()

    #     if user_path_decision == "jungle":
    #         st.write(DEEP_JUNGLE_DECISION)
    #         st.write("-----")

    #         # third decision of the user: here three
    #         user_path_decision = st.text_input(
    #             """ Which door would you like to choose? Insert emerald, sapphire or ruby """
    #         ).lower()
    #         # if the user decide for the emerald door
    #         if user_path_decision == "emerald":
    #             st.write(EMERALD_DOOR_DECISION)
    #             is_loop_true = False
    #         # if the user decide for the sapphire door
    #         elif user_path_decision == "sapphire":
    #             st.write(SAPPHIRE_DOOR_DECISION)
    #             is_loop_true = False
    #         # if the user decide for the ruby door
    #         else:
    #             st.write(RUBY_DOOR_DECISION)
    #             is_loop_true = False

    #     else:
    #         # if the user decide for going towards the cliff
    #         st.write(CLIFF_DECISION)
    #         is_continue = input(
    #             """ Do you want to start over again?  Insert Y of N: """
    #         ).lower()
    #         if is_continue == "y":
    #             continue
    #         else:
    #             is_loop_true = False

    # else:
    #     st.write(ROCKY_SHORELINE)
    #     is_continue = input(
    #         """ Do you want to start over again?  Insert Y of N: """
    #     ).lower()
    #     if is_continue == "y":
    #         continue
    #     else:
    #         is_loop_true = False

# st.write(ENDING_GAME)
