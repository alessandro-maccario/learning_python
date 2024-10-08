# import packages
from pkgs.config import *

###################################
###### TREASURE ISLAND GAME #######
###################################

if __name__ == "__main__":
    # print the title and the treasure chest variable
    print(START_TREASURE_ISLAND)

    # print the introduction story to the game
    print(INTRO_DESCRIPTION)

    # You should start with a loop so the user can start again whenever they want!
    is_loop_true = True
    # add a boolean variable to keep track of the fact that the user won or not
    isWinning = True

    while is_loop_true:
        print(INTRO_FIRST_DECISION)
        # give the user an intro based on the next decision
        print(FIRST_LEFT_PATH)
        print(FIRST_RIGHT_PATH)

        # let the user choose the first step
        user_path_decision = input(
            """ Which one do you chose? Insert left or right? """
        ).lower()

        # first decision of the user (left = continue adventure; right = game over)
        if user_path_decision == "left":
            print(JUNGLE_DECISION)

            # second decision of the user (wait = continue adventure; swim = game over)
            user_path_decision = input(
                """ Will you proceed to the jungle or to the cliff? Insert jungle or cliff:  """
            ).lower()

            if user_path_decision == "jungle":
                print(DEEP_JUNGLE_DECISION)

                # third decision of the user: here three
                user_path_decision = input(
                    """ Which door would you like to choose? Insert emerald, sapphire or ruby """
                ).lower()
                # if the user decide for the emerald door
                if user_path_decision == "emerald":
                    print(EMERALD_DOOR_DECISION)
                    is_loop_true = False
                # if the user decide for the sapphire door
                elif user_path_decision == "sapphire":
                    print(SAPPHIRE_DOOR_DECISION)
                    is_loop_true = False
                # if the user decide for the ruby door
                else:
                    print(RUBY_DOOR_DECISION)
                    is_loop_true = False

            else:
                # if the user decide for going towards the cliff
                print(CLIFF_DECISION)
                is_continue = input(
                    """ Do you want to start over again?  Insert Y of N: """
                ).lower()
                if is_continue == "y":
                    continue
                else:
                    is_loop_true = False
                    isWinning = False

        else:
            print(ROCKY_SHORELINE)
            is_continue = input(
                """ Do you want to start over again?  Insert Y of N: """
            ).lower()
            if is_continue == "y":
                continue
            else:
                is_loop_true = False
                isWinning = False

if isWinning == False:
    print(" Thank you for playing! Come back again to try your luck! ")
else:
    print(ENDING_GAME)
