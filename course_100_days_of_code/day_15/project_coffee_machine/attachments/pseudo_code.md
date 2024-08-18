# Coffee Machine Project

In this _Coffee Machine_ project I am going to build a simple replica of the software needed to run a coffee machine.

# Basic information

1. The coffee machine makes 3 hot flavours:
   1a. Espresso -> €1.50
   I. 50ml water
   II. 18g Coffee
   2b. Latte -> €2.50
   I. 200ml water
   II. 24g Coffee
   III. 150ml milk
   3c. Cappuccino -> €3
   I. 250ml water
   II. 24g Coffee
   III. 100ml milk
2. The coffee machine has some resources needed:
   2a. 300ml water
   2b. 200ml milk
   2c. 100g coffee
3. Coin operated: four types of american coins
   3a. penny: 1 cent ($0.01)
   3b. nickel: 5 cents ($0.05)
   3c. dime: 10 cents ($0.10)
   3d. quarter: 25 cents ($0.25)

# Program requirements

1. Print report: the coffee machine should be able to tell us how much resources are left. For instance, one of the first statement that the user should see is the following: "What would you like to have? (espresso/latte/cappuccino).". If the user types "report", a report of the available resources should be shown. For instance:
   1a. water: 300ml
   1b. milk: 200ml
   1c. coffee: 100g
   1d. money: $0
2. The coffee machine should be able to check if the resources are sufficient when the user orders a drink. For instance, the user sees: "What would you like to have? (espresso/latte/cappuccino).". After the user type "latte", for instance, the machine says "Please, insert coins." Then, the machine should ask:
   2a. "How many quarters?"
   2b. "How many dimes?"
   2c. "How many nickles?"
   2d. "How many pennies?"
   After inserting all of the money, the machine says "Here is $x.xx in change". Therefore, the machine accept those money and then calculates the amount of money that it has to give in return to the user. Then, a print statement that says "Here is your {coffee}, enjoy it!".
   If the coins are not sufficient, the machine should say something like "Sorry, that is not enough money. Money refunded."
3. Then, it starts again. If the user checks the report again, then they should see a lower amount of resources in it. In case, the user selects an option and there are not enough resources, then the machine should say something like "Sorry, there is not enough water.". Therefore, the machine should be able to go through all the resources and check them against the recipes.
