[//]: <> This is a comment in Markdown
[//]: <> Blackjack application developed in Python

### Rules

The main goal of Blackjack is to get the highest value based on the cards that you get from the _dealer_, but without going over 21.
You are the playes and your counterpart are other _players_ or the _dealer_.

- Cards from 2 to 10 count with their _face_ value: that means, that a 2 is counted as a 2, a 3 as a 3, and so on.
- The _Jack_, _King_ and _Queen_ count as 10
- The _Ace_ can either count as a 1 or 11: depending if you are going under or over 21, you can decide the value represented by the _ACE_. (for this simplified Blackjack version, the _ACE_ counts as 11)

### Terminology

- BUST: if the user goes over 21, it's called a BUST and you lose

### Mechanics of the game

**BUST CONDITION**
E.g.: the playe and the dealer starts with 2 cards each, but one of the cards from the dealer is hidden.
The player has:

- A Queen
- A Three

The dealer has:

- A 10
- A hidden card

The player do not know what the dealer has, therefore, based on what the user can see as their cards, they have to decide if they want another card from the dealer's deck or not. If yes, and the card that the player receives gives them, in total, more than 21, than the user BUST and they lose, no matter what the dealer has in their hands. Therefore, if the hidden card of the dealer would have trigger the dealer to lose, the player lose first.

If the dealer scores more than the player, e.g. by getting 21 in total, then the dealer WINS and the player loses.

**DRAW CONDITION**
In case, both the playes and the dealer end up with the same values (e.g.: both have 20 as the value of their hands), the game ends up with a DRAW.

**SPECIAL RULES**

If the dealer ends up with a value < 17, then they MUST withdraw another card from the deck.

**ASSUMPTIONS FOR THIS PROJECT**

- We assume that the cards the dealer and the player are starting with will come from this list:
  - cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] (the last three 10s are for Jack, King and Queen). Notice that the _ACE_ will be represented as 11.
- we assume we have an infinite deck: that means, when a card is drawn from the deck it is not removed from it. We consider that the cards in the deck have equal chances of occurring.

## Flowchart

1. Start with the simplified list of cards
2. Draw two random cards for the user and two random cards for the dealer
   2a. Show to the user both of the cards that they got and only one that the dealer got.
   Use an "\*" to show the hidden card of the dealer.
3. Sums up what is the user's current card value.
   3a. If the user's card value is above 21, then the user BUST and lose.
   3b. If not Ask the user if they want another card.
   a. If yes, then the user and the dealer receive each another card.
   b. If the user sums of the card values is > 21, the user goes BUST
   c. The dealer's cards will be shown and if the dealer has a value < 17, then they MUST draw another card. If the sums of the card value is > 21, they BUST and the user wins.
4. If the user's card value is still < 21, ask the user again to draw another card (possible usage of recursion). Otherwise, the user wins.
5. Ask the user if they want to continue to play or not.
