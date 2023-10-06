ATM Logging
You are developing a mobile ATM application that will handle bank transactions such as deposits and withdrawals. With the original design of this application, you used print statements to print helpful information to the console, such as amounts entered for each transaction, transaction status, and date and timestamps to see when each transaction occurred.

The goal of this project is to modify the existing BankAccount methods to utilize the logging module instead of print statements. Using the logging module over print statements will help make the project code more readable and maintainable after these modifications are made.

A solution.py file is also loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers when you’re done!

Tasks
8/9 Complete
Mark the tasks as complete by checking them off
Replacing Print Statements
1.
Start off by looking over the starting code in script.py. To try it out yourself, type python3 script.py in the console and click Enter.

Note that if you make any edits to the code, you must click Save before running the code again.

2.
Create a logger object that directs logged messages to the console. Do this above the BankAccount class.

You will also need to import two libraries.


Stuck? Get a hint
3.
Set your log level to INFO.


Stuck? Get a hint
4.
Determine which print statements should be replaced by logged messages. Depending on the content of the message, select the appropriate logging level to use for each statement.

Note that this will be the most important and time-consuming part of the project. If you feel stuck at all, click the hint below or look at solution.py for some inspiration.


Stuck? Get a hint
5.
Reduce repetitive code within the Transaction Info sections by including a date timestamp in each log message.


Stuck? Get a hint
Executing Logged Messages
6.
Add an additional handler to also direct the logged messages to a log file called formatted.log.


Stuck? Get a hint
7.
Execute the code and supply the following inputs:

Deposit: $50

Withdraw: $200

View the saved log file or the console and verify that an error was logged for insufficient funds for the withdrawal transaction.

8.
Re-execute the code and supply the following inputs:

Deposit: $50
Withdraw: $10
View the saved log file to see the successful deposit and withdrawal transactions.