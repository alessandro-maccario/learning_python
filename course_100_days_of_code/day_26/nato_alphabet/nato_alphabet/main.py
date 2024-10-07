"""
Script to create the NATO Phonetic Alphabet by using Python for the 100 Days of Code challenge from the Udemy course.

Problem Breakdown:
    1. Create a dictionary in this format: {"A": "Alfa", "B":"Bravo", ...}.
    2. Create a list of the phonetic code words from a word that the user inputs.
    Example: user_input = "Thomas" -> result => ["Tango", "Hotel", "Oscar", "Mike", "Alfa", "Sierra"]


Requirements:
    - To use dictionary comprehension: {new_key:new_value for (index, row) in df.iterrows()}

"""

# --- IMPORT PACKAGES --- #
import pandas as pd

# read the nato_phonetic_alphabet
df = pd.read_csv("day_26/nato_alphabet/data/nato_phonetic_alphabet.csv")

# ask for the user input
user_input = input("Enter the word to be converted to NATO Phonetic Alphabet:").upper()

# create dictionary from the pandas dataframe
dict_nato = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

# grab the NATO Phonetic Alphabet from the dictionary and store the conversion into the list
list_nato_phonetic_alphabet = [dict_nato[each_letter] for each_letter in user_input]

# print the NATO Phonetic Alphabet for the user
print("The NATO Phonetic Alphabet is: ", list_nato_phonetic_alphabet)
