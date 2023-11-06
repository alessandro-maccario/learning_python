"""
    This Section 3 of 100 days of code is meant to hold Day 3 Project: Treasure Island.

    References:
        - For ASCII text art: 
            https://patorjk.com/software/taag/#p=display&f=Bulbhead&t=The%20Pirate%20Treasure%20Island 

        - For ASCII picture art:
            https://ascii.co.uk/art
"""

# main ASCII intro picture

START_TREASURE_ISLAND = '''
                        
                        

 ____  _   _  ____    ____  ____  ____    __   ____  ____    ____  ____  ____    __    ___  __  __  ____  ____    ____  ___  __      __    _  _  ____  
(_  _)( )_( )( ___)  (  _ \(_  _)(  _ \  /__\ (_  _)( ___)  (_  _)(  _ \( ___)  /__\  / __)(  )(  )(  _ \( ___)  (_  _)/ __)(  )    /__\  ( \( )(  _ \ 
  )(   ) _ (  )__)    )___/ _)(_  )   / /(__)\  )(   )__)     )(   )   / )__)  /(__)\ \__ \ )(__)(  )   / )__)    _)(_ \__ \ )(__  /(__)\  )  (  )(_) )
 (__) (_) (_)(____)  (__)  (____)(_)\_)(__)(__)(__) (____)   (__) (_)\_)(____)(__)(__)(___/(______)(_)\_)(____)  (____)(___/(____)(__)(__)(_)\_)(____/ 

                        
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
                        /______/______/______/______/______/______/______/______/______/______/______/_
                        *******************************************************************************
                        '''

INTRO_DESCRIPTION = """
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

INTRO_FIRST_DECISION = """
                        As you stand on the sun-drenched beach of Skull Island, 
                        you see two winding paths ahead, each veiled in mystery.
              
                        Which one would you choose, LEFT or RIGHT?
                        """

FIRST_LEFT_PATH = """
                  The path to the left leads into a dense jungle, where twisted vines and ancient 
                  trees cast eerie shadows. Muffled sounds of unseen creatures echo from the foliage, 
                  and you catch a glint of something metallic hidden amidst the greenery.
                  """

FIRST_RIGHT_PATH = """
                    The right path takes you along the rocky shoreline, where the crashing waves sing a haunting tune. 
                    You spot the remains of a weathered shipwreck, partially buried in the sand, hinting at forgotten tales of the sea.
                    """

ROCKY_SHORELINE = """
                                As you follow the path to the right, you tread upon the rocky shoreline, 
                                your senses filled with the salty scent of the sea. The remains of a weathered
                                shipwreck lie ahead, partially buried in the sand, a testament to the island's 
                                treacherous history. As you draw closer to the shipwreck, an enchanting melody 
                                begins to fill the air, a song so melodious and magical that it seems to pull 
                                you closer, as if beckoning you to the ship's main deck. 
                                The tune grows stronger and more irresistible with each step. 
                                You can't resist the allure, and you find yourself stepping onto the creaking 
                                deck of the wrecked vessel. 
                                But as you do, you suddenly realize the terrible truth – it was a trap! 
                                A beautiful and beguiling Siren emerges from the depths of the shipwreck, 
                                her voice still captivating but now laced with malevolence. 
                                You are ensnared by her haunting song, unable to resist its charm. 
                                The Siren's eyes glow with an otherworldly light, and you are drawn into her sinister clutches. 
                                With a haunting, knowing smile, she whispers, 'Welcome to your doom, brave adventurer.' 
                                And as her song lures you deeper into her enchantment, the world around you fades to darkness. 
                                
                                Game over!
                                """

JUNGLE_DECISION = """
                                As you make your way through the tangled undergrowth of the dense jungle on the left, 
                                the world around you transforms into a lush, mysterious landscape. 
                                Ancient trees with gnarled roots tower above, their leaves creating a natural canopy 
                                that filters the sunlight into an enchanting green glow. 
                                
                                The air is thick with humidity and the calls of exotic birds.
                                With each step, you uncover remnants of a forgotten civilization – overgrown statues, 
                                moss-covered ruins, and cryptic symbols etched into stone. 
                                
                                The atmosphere is rich with the scent of adventure, and you sense that something of 
                                great significance may lie hidden within this jungle's depths.
                                
                                Deeper into the jungle, you stumble upon a massive stone doorway, half-covered by creeping vines.
                                Moonstones, radiant and otherworldly, are embedded in the door, creating an intricate mosaic that 
                                seems impossible to obtain. Each stone emits an eerie, soft glow. 
                                Each moonstone is intricately embedded in the door's surface, creating a mesmerizing pattern.

                                But as you study the moonstone mosaic, you notice something amiss: 
                                there's a conspicuous gap in the pattern where one moonstone should be. 
                                It's as if one of the precious gems has been removed, leaving a void in the mosaic.
                                Below the missing moonstone, there's an inscription that appears to be a riddle: 
                                'The path to riches lies beyond the guardian's gaze, beneath the watchful eye of the moon.'
                                
                                Before you stretches a fork in the path – one leading deeper into the jungle, 
                                the other winding upward toward a rocky cliff. The choice is yours, intrepid explorer. 
                                
                                Will you seek to find the missing moonstone to complete the door's mosaic, 
                                thereby solving the riddle, or will you ascend the rocky cliff to seek a vantage point? 
                                Your decision will shape the course of your pirate legend. Which path shall it be?
                                
                                """
DEEP_JUNGLE_DECISION = """
                  As you venture deeper into the dense jungle, the intertwined branches create a maze of intricate paths. 
                  However, your keen eye catches a glint of metal amidst the foliage. 
                  With the rusty saber you discovered earlier, you carefully clear the way, and the path becomes more defined.
                  After a few more steps, the saber reveals a hidden treasure - a very old and ancient statue, 
                  nearly lost to time, obscured by creeping branches. As you diligently cut away the last of the 
                  encroaching foliage, you uncover a moon-like shape beneath the overgrowth.
                
                  Intrigued, you reach out to touch the mysterious shape, and as you turn it, 
                  a wrenching sound echoes through the jungle. With a sudden shift, the statue reveals a 
                  hidden gemstone underneath, glistening like a captured fragment of the night's sky.

                  You carefully pocket the gemstone, sensing its significance. 
                  Your journey leads you back to the massive stone doorway, where you gently place the 
                  gemstone into the gap in the moonstone mosaic. 
                  With a soft click, the missing piece falls into place.

                  The door creaks open, revealing an eerie darkness beyond. 
                  You take a deep breath and step inside. After a few seconds, dim light gradually fills the room, 
                  revealing three very different doors, each with its distinct color and an 
                  enigmatic riddle etched into its surface.

                  You also notice that for each door, there is no keyhole to be found. 
                  Instead, all you need to do is turn the handle to open it.

                  The first door, with an emerald hue, bears a riddle that asks, 
                    
                    "I hold keys but can't unlock a box,
                    A realm with space, yet lacks a chamber's locks.
                    You can enter but can't go inside. 
                    What am I?"
                  
                  The second door, a deep sapphire blue, presents a riddle:
                  
                    "I have no tail, no paws, just clicks and rays,
                    Yet through the maze, I'll guide your way.
                    With fingertip, palm, or claw, it's all a breeze,
                    The choice is yours, how gentle your touch can appease.
                    What am I, you'll ponder, for hours and days?"

                  The third door, painted in a rich ruby red, challenges you with the riddle: 
                    
                    "I'm spread beneath your keys, but I'm no secret treasure map,
                    Soft as a pirate's touch, yet I offer a quiet lap.
                    I guard the deck from stains, where your crew likes to chat,
                    What am I, in this pirate life, keeping your sizes snug and flat?"
                  
                  Your heart races with anticipation as you stand before these three enigmatic choices. 
                  Each door holds a different mystery. 
                  Which one will you choose to unlock?"
"""

# here the user must choose between three doors. You have to give the user a description for each of the door
# once chosen: what's inside? with a possible link to a keyboard, mouse and keyboard/mouse mat
EMERALD_DOOR_DECISION = """ Congrats, mate, you found the mistycal KEYCHRON K3 mechanical keyboard!!! Shop it here, and get the Pirate discount that you deserve 
                                for finishing this quest: https://shorturl.at/xBH38 """

SAPPHIRE_DOOR_DECISION = """ Congrats, mate, you found the mistycal CORSAIR HARPOON gaming mouse!!! Shop it here, and get the Pirate discount that you deserve 
                                for finishing this quest: https://shorturl.at/cRU56 """

RUBY_DOOR_DECISION = """ Congrats, mate, you found the mistycal Silent Monster Keyboard Mat!!! Shop it here, and get the Pirate discount that you deserve 
                                for finishing this quest: https://shorturl.at/fDJZ9"""

CLIFF_DECISION = """
            As you ascend the rocky cliff, the journey is strenuous but promising. 
            The view from above must be incredible, you think. 
            You conquer the rugged terrain, step by step, until finally, 
            you stand atop the cliff, peering out at the vast expanse of the ocean below.

            The horizon stretches infinitely, a breathtaking panorama, and you feel like a master of the world. 
            But just as you begin to relish this moment, a deafening crack splits the sky above. 
            A brilliant bolt of lightning illuminates the dark clouds, revealing a colossal, shadowy silhouette. 
            For a heart-stopping moment, the shape evokes an eerie, otherworldly presence.

            Terrified, you try to escape the impending tempest, but it's then that the sky opens up, 
            and a torrential rain pours down with relentless force. 
            The ground beneath your feet, once solid, transforms into a slippery, treacherous slope. 
            Panicked, you scramble to find your footing, but it's too late.

            The rain-soaked soil gives way, and you tumble down the cliffside, helpless to resist. 
            As you descend, the monster emerges from the turbulent sea, his immense form dominating the horizon. 
            The last thing your wide eyes can discern through the rain and mist are two hollow, yellow voids, 
            and a nightmarish tangle of inky tentacles.

            You suddenly realize that you focused on the finger and not at the moon, and that your journey 
            has come to a chilling, and untimely end, falling victim to the indomitable
            forces of nature and the eldritch horror that lies beneath the sea...

            Game over!
            """

ENDING_GAME = """ 
                You've navigated through treacherous waters, unraveled cryptic riddles, and braved the unknown, 
                like a true swashbuckler of the digital realm.
                You've found the treasure, not just of gold and gems, but of the journey itself. 
                In the heart of the digital world, you've become a legendary pirate, a master of code, and a seeker of adventure.
                With the treasure in hand, you return to the real world, but the memories of your 
                exploits in the digital realm will forever shine in your heart. 
                As a pirate of the digital seas, your legend lives on, and the treasures you've 
                discovered are a testament to the explorer's spirit that beats within every true adventurer.
                
                Congratulations, matey, you've emerged victorious in the grand tale of the Pirate's Treasure Island Adventure!!!
                """
