# Guess The Number

In this _Guess The Number_ game the player has a certain number of attempts (based on the difficulty level that they decide) to guess what the number is that the opponent (the computer) will randomly pick up.
There are two level of difficulties:

- normal: you have 10 guesses
- hard: you have 7 guesses

# Flowchart

1. Ask the user the level of difficulties they want to play: tell them how many guesses they have. Any fail attempt will result in a lower count of the attempts
2. The script will chose a random number between 0 and 100 (for example)
3. Ask the user to guess the number chosen by the script: **Make a guess: **.
   3a. If the number inserted by the player is > random number, then _Too high_. Otherwise, _Too low_.
4. If the number guessed is correct, output that number saying _You got it! The answer is {number_inserted by the user}_.
