# ASCII ART
# https://ascii.co.uk/art

# import packages
from pkgs.config import START_TREASURE_ISLAND, INTRO

###################################
###### TREASURE ISLAND GAME #######
###################################

if __name__ == "__main__":
    # print the title and the treasure chest variable
    print(START_TREASURE_ISLAND)

    # print the introduction story to the game
    print(INTRO)

    # You should start with a loop so the user can start again whenever they want!
    is_loop_true = True

    while is_loop_true:
        # let the user choose the first step
        user_path_decision = input(""" Left or right? """).lower()
        print("-----")

        # first decision of the user (left = continue adventure; right = game over)
        if user_path_decision == "left":
            print(""" Your first decision was left. """)
            print("-----")

            # second decision of the user (wait = continue adventure; swim = game over)
            user_path_decision = input(""" Wait or swim? """).lower()

            if user_path_decision == "wait":
                print(""" Your second decision was wait. """)
                print("-----")

                # third decision of the user
                user_path_decision = input(""" Which door? """).lower()
                if user_path_decision == "yellow":
                    print(""" You found the Pirate Treasure! Congrats! """)
                    is_loop_true = False
                else:
                    print(""" Game over! """)
                    is_continue = input(
                        """ Do you want to start over again?  Insert Y of N: """
                    ).lower()
                    if is_continue == "y":
                        continue
                    else:
                        is_loop_true = False

            else:
                print(""" Game over! """)
                is_continue = input(
                    """ Do you want to start over again?  Insert Y of N: """
                ).lower()
                if is_continue == "y":
                    continue
                else:
                    is_loop_true = False

        else:
            print(""" Game over! """)
            is_continue = input(
                """ Do you want to start over again?  Insert Y of N: """
            ).lower()
            if is_continue == "y":
                continue
            else:
                is_loop_true = False
