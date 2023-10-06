import sqlite3

# Create connection object
con = sqlite3.connect("titanic.db")

# Create cursor object
curs = con.cursor()

