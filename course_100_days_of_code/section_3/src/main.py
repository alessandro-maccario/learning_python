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

    while is_loop_true:
        # give the user an intro based on the next decision
        print(FIRST_LEFT_PATH)
        print()
        print(FIRST_RIGHT_PATH)

        # let the user choose the first step
        user_path_decision = input(
            """ Which one do you chose? Insert left or right? """
        ).lower()
        print("-----")

        # first decision of the user (left = continue adventure; right = game over)
        if user_path_decision == "left":
            print(DEEP_JUNGLE_DECISION)
            print("-----")

            # second decision of the user (wait = continue adventure; swim = game over)
            user_path_decision = input(
                """ Will you proceed to the jungle or to the cliff? Insert jungle or cliff:  """
            ).lower()

            if user_path_decision == "jungle":
                print(DEEP_JUNGLE_DECISION)
                print("-----")

                # third decision of the user: here three
                user_path_decision = input(
                    """ Which door would you like to choose? Insert emerald, sapphire or ruby """
                ).lower()
                if user_path_decision == "emerald":
                    print(""" You found the Pirate Treasure! Congrats! """)
                    is_loop_true = False
                elif user_path_decision == "sapphire":
                    print("")
                else:
                    print("")

                # else:
                #     print(""" Game over! """)
                #     is_continue = input(
                #         """ Do you want to start over again?  Insert Y of N: """
                #     ).lower()
                #     if is_continue == "y":
                #         continue
                #     else:
                #         is_loop_true = False

            else:
                print(CLIFF_DEFICION)
                is_continue = input(
                    """ Do you want to start over again?  Insert Y of N: """
                ).lower()
                if is_continue == "y":
                    continue
                else:
                    is_loop_true = False

        else:
            print(ROCKY_SHORELINE)
            is_continue = input(
                """ Do you want to start over again?  Insert Y of N: """
            ).lower()
            if is_continue == "y":
                continue
            else:
                is_loop_true = False
