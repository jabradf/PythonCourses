import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Pull the Age records from the titanic table using .fetchall() method and save as age
age = curs.execute("SELECT Age FROM titanic;").fetchall()

# for loop that calculates the average
sum = 0

for number in age:
  if number[0] < 18:
    sum += 1

print(sum)
