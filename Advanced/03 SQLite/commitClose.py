from start import helper
helper()
import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# insert a row in new_table table
curs.execute('''INSERT INTO new_table VALUES ('Stephanie Bready', 37, 'stephB423', 30.00)''')

# commit this change
con.commit()

# close the connection
con.close()
curs.execute()  # this will fail as the connection is closed. Error handling would be good to implement here. tye, catch, etc.