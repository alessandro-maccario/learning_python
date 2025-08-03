[//]: <> This is a comment in Markdown
[//]: <> Calculator application developed in Python
[//]: <> Possible to use a class in this case

[//]: <> Define the four common operations

- 1.add()
- 2.subtract()
- 3.multiply()
- 4.divide()

first_operation = 0
current_operation = 0

decision_operation = input("Which operation do you want to perform? Insert the corresponding number for: 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division.")
[//]: <> possible to convert this if-else with a function and reduce the code
if decision_operation == 1:
first_operation += add(int(input("Insert the first number")), int(input("Insert the second number") ) )
elif decision_operation == 2:
first_operation += subtract(int(input("Insert the first number")), int(input("Insert the second number") ) )
elif decision_operation == 3:
first_operation += multiply(int(input("Insert the first number")), int(input("Insert the second number") ) )
elif decision_operation == 4:
first_operation += divide(int(input("Insert the first number")), int(input("Insert the second number") ) )

current_operation = first_operation

decision_continuation = input("Do you want to continue? Type 'y' to continue, type 'n' to start a new calculation, type 'close' to close the application entirely.)

if decision_continuation in ('y', 'n'):
[//]: <> do something in a function
elif decision_continuation == "close":
[//]: <> close the application
break
else:
print("Please, provide a valid choice between: 'y' to continue, 'n' to start a new calculation, 'close' to close the application.)
