# Import module sqlite3
import sqlite3

# Create connection object
con = sqlite3.connect("titanic.db")

# Create cursor object
curs = con.cursor()

# Retrieve the row where username = 'stephB423'; from new_table
n_row = curs.execute('''SELECT * FROM new_table WHERE username = 'stephB423';''').fetchall()
print(n_row)

# Close the connection
con.close()