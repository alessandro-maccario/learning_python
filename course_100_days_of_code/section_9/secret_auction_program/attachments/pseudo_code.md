dictionary -> key:value based on key = person's name; value: persons's bid

bids = {}
name => What is your name? -> James
bid => What is your bid? -> 140
bids.update({name: bid})

clear_screen()
another_player => Is there another bidder? If yes, continue, if no stop the program.

bids = {"James": 140, "John": 100, "Jack": 2000}

Sort the dictionary:
[//]: <> NO --> sorted_dict = [mydict[k] for k in sorted(mydict.keys())]
[//]: <> sort and get the first value
highest_bidder = {key:value for key,value in list(sorted(mydict.keys()))[0]}
highest_bidder_name = highest_bidder[0]
highest_bidder_bid = highest_bidder[1]

---

Flowchart

1. ask for the name
2. ask for the bid
3. clear_screen()
4. ask for another bidder.
   4a.: If yes, clearn_screen() and ask again about the name, the bid and add it to the previous dictionary
   4b.: If no, sort the dictionary by value and then return the following string: "The highest bidder was {highest_bidder_name } with a bid of {highest_bidder_bid}
