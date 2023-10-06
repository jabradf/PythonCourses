def helper():
  import sqlite3
  con = sqlite3.connect("titanic.db")
  curs = con.cursor()
  curs.execute('''DROP TABLE IF EXISTS new_table''')