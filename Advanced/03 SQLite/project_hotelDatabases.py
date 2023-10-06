# Import module 
import sqlite3


# Task 1: Create connection object
con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
one = cur.execute("SELECT * FROM booking_summary").fetchone()
#print(one)

# Task 4: View first ten rows of booking_summary 
ten = cur.execute("SELECT * FROM booking_summary").fetchmany(10)
#print(ten)

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country='BRA';''').fetchall()
#print(bra)

# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER, hotel TEXT, is_cancelled INTEGER, lead_time INTEGER, arrival_date_year INTEGER, arrival_date_month TEXT, arrival_date_day_of_month INTEGER, adults INTEGER, children INTEGER, country TEXT, adr REAL, special_requests INTEGER)
  ''')

# Task 7: Insert the object bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
ten = cur.execute("SELECT * FROM bra_customers").fetchmany(10)
#print(ten)

# Task 9: Retrieve lead_time rows where the bookings were canceled

# pandas method
#df = pandas.read_sql_query('''SELECT * FROM titanic;''', con)

leadTime_cancelled = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# Task 10: Find average lead time for those who canceled and print results
averageSum = 0
for item in leadTime_cancelled:
  averageSum += item[0]
av_leadtimeCancelled = averageSum / len(leadTime_cancelled)
print("Cancelled lead time: ", av_leadtimeCancelled)

# Task 11: Retrieve lead_time rows where the bookings were not cancelled
# lets do the pandas method this time
import pandas as pd
leadTime_notCancelled = pd.read_sql_query('''SELECT lead_time FROM bra_customers WHERE is_cancelled=0;''', con)

# Task 12: Find average lead time for those who did not cancel and print results
av_leadtimeNotCancelled = leadTime_notCancelled.mean()
#print(av_leadtimeNotCancelled.describe())
print("Not cancelled lead time: ", av_leadtimeNotCancelled['lead_time'])

print('---')
# Task 13: Retrieve special_requests rows where the bookings were cancelled
requests_Cancelled = pd.read_sql_query('''SELECT special_requests FROM bra_customers WHERE is_cancelled=1;''', con)

# Task 14: Find total speacial requests for those who canceled and print results
total_requests_Cancelled = requests_Cancelled.sum()
print("Total requests, cancelled: ", total_requests_Cancelled['special_requests'])

# Task 15: Retrieve special_requests rows where the bookings were not cancelled
requests_NotCancelled = pd.read_sql_query('''SELECT special_requests FROM bra_customers WHERE is_cancelled=0;''', con)

# Task 16: Find total speacial requests for those who did not cancel and print results
total_requests_NotCancelled = requests_NotCancelled.sum()
print("Total requests, Not cancelled: ", total_requests_NotCancelled['special_requests'])

# Task 17: Commit changes and close the connection
con.commit()
con.close()
