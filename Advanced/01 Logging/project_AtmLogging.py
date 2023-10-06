import logging
import sys
import random

from datetime import datetime

#####################
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
file_handler = logging.FileHandler("output.log")
logger.addHandler(file_handler)
#####################

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    authenticated = False
    attempts = 0
    # added code for number of authentication attempts before killing it
    while not authenticated and attempts<3:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        logger.log(logging.ERROR, "Invalid pin. Try again.")
        attempts += 1
        #print("Error! Invalid pin. Try again.")
      else:
        authenticated = True
        return authenticated
 
  def deposit(self):
    tx = random.randint(10000, 1000000)
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      print("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction {tx} successful".format(tx=tx))
      
    except ValueError:
      logger.error(f"Transaction {tx} failed. You entered a non-number value to deposit.")
 
  def withdraw(self):
    number=random.randint(10000, 1000000)
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info(f"Transaction {number} Successful. You withdrew {amount}")
        #print("You withdrew: ${amount}".format( amount=amount))
        #print("Transaction Info:")
        #print("Status: Successful")
        #print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error(f"Transaction {number} failed! Insufficient balance to complete withdraw.")
        #print("Error! Insufficient balance to complete withdraw.")
        #print("Transaction Info:")
        #print("Status: Failed")
        #print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error(f"Transaction {number} failed! You entered a non-number value to withdraw.")
      #print("Error! You entered a non-number value to withdraw.")
      #print("Transaction Info:")
      #print("Status: Failed")
      #print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      #print("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
auth = acct.authenticate()
if auth:
  acct.deposit()
  acct.withdraw()
  acct.display()
else:
  print("not authenticated, goodbye!")