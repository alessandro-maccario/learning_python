"""
Given a list of people's names, automize the creation of N number of letters
where the name after "Dear [insert_name_here]" is taken from the list.
The output will be a file called "letter_for_[insert_name_here].txt".
This will be done in Python for the 100 Days of Code challenge from the Udemy course.

Reference
    - Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    - Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    - Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


Problem Breakdown:
    1. Create a letter using starting_letter.txt for each name in invited_names.txt
    3. Replace the [name] placeholder with the actual name.
    4. Save the letters in the folder "ReadyToSend".

"""

# CONSTANT
PLACEHOLDER = "[name]"

# open the starting letter file
with open(
    "day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r"
) as letter:
    letter = letter.read()

# open the names file
with open(
    "day_24/Mail Merge Project Start/Input/Names/invited_names.txt", "r"
) as names:
    names = names.readlines()

# create the .txt file with personalized names
for name in names:
    name = name.rstrip("\n")

    # Replace the target string
    filedata = letter.replace(PLACEHOLDER, name)
    with open(
        f"day_24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w"
    ) as personalized_letter:
        personalized_letter.write(filedata)
