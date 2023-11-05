# ASCII ART
# https://ascii.co.uk/art

###################################
###### TREASURE ISLAND GAME #######
###################################

print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      '''
)

print(
    """
      Ahoy, matey! 
      Welcome to the treacherous shores of Skull Island, 
      a haven for scallywags and for buried treasure. 
      As you step onto these sun-soaked sands, you become the protagonist of an epic pirate tale. 
      Your mission is to unravel the mysteries of this legendary island and lay your hands on the 
      long-lost pirate booty hidden beneath its rugged terrain.

      Once a bustling pirate haven, Skull Island now stands eerily deserted. 
      The reason? A ghostly curse, they say... 
      It is whispered in the darkest corners of the seven seas that 
      the island's treasure is guarded by vengeful spirits, 
      the restless souls of pirates who perished seeking their ill-gotten gains. 
      These tormented souls, unable to move on to the afterlife, have driven away all but the boldest of adventurers.

      You'll need to navigate treacherous waters, decipher cryptic maps, 
      and outsmart cunning pirates who guard the secrets of this island. 
      The winds of destiny are at your back, and the choice is yours, me heartie. 
      Will you seize the fortune that awaits, or will you be swallowed by the depths of the sea?

      Are you ready to embark on this swashbuckling quest?"

"""
)

# You should start with a loop so the user can start again whenever they want!
is_loop_true = True


# let the user choose the first step
user_path_decision = input(
    """
        As you stand on the sun-drenched beach of Skull Island, you see two winding paths ahead, each veiled in mystery.
        Wich one do you choose, left or right?
        """
).lower()

# first decision of the user (left = continue adventure; right = game over)
if user_path_decision == "left":
    print(
        """
        The path to the left leads into a dense jungle, where twisted vines and ancient trees cast eerie shadows. 
        Muffled sounds of unseen creatures echo from the foliage, and you catch a glint of something metallic hidden amidst the greenery.
        """
    )
else:
    print(
        """
        The right path takes you along the rocky shoreline, where the crashing waves sing a haunting tune. 
        You spot the remains of a weathered shipwreck, partially buried in the sand, hinting at forgotten tales of the sea.
        
        As you follow the path to the right, you tread upon the rocky shoreline, your senses filled with the salty scent of the sea. 
        The remains of a weathered shipwreck lie ahead, partially buried in the sand, a testament to the island's treacherous history.

        As you draw closer to the shipwreck, an enchanting melody begins to fill the air, a song so melodious and 
        magical that it seems to pull you closer, as if beckoning you to the ship's main deck.

        The tune grows stronger and more irresistible with each step. You can't resist the allure, and you find yourself stepping 
        onto the creaking deck of the wrecked vessel. But as you do, you suddenly realize the terrible truth – it was a trap!

        A beautiful and beguiling Siren emerges from the depths of the shipwreck, her voice still captivating but now laced with malevolence. 
        You are ensnared by her haunting song, unable to resist its charm. The Siren's eyes glow with an otherworldly light, 
        and you are drawn into her sinister clutches.

        With a haunting, knowing smile, she whispers, 'Welcome to your doom, brave adventurer.' And as her song lures you deeper 
        into her enchantment, the world around you fades to darkness.."
        """
    )

    print(
        """
                                                   ____
                                              / ,--\
                                             / (' a(
                                           ,'   \__/
                                          /   __/(_
                                          \  (  - -\
                                         ._)_| |_)_)\
                                      __..---|(  /  \\
                                _,--``       ||_/    \\__
                              ,'  ___________||_/     '--\
                             /  ,'   ___    _||
                             | (___,' ,-\  /,-/
                             \       /
                              \  `--<_
                               `.____ \
                                     )/
        """
    )
    print("Game over!")
