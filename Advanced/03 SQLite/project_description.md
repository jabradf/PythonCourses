# Analyzing Hotel Databases with Python
Sleep Away Inc., a hotel corporation, has just hired you as a data analyst. They would like you to analyze their most recent data about customers who cancelled their booking and customers who did not cancel.

It is your job to connect to Sleep Away’s SQLite database so you can edit and analyze the hotel_booking.db database. The company wants to learn about the BRA customers (Brazilian customers) who cancelled their bookings compared to the BRA customers who did not.

To do this, you will create a new data table in their database that only has the Brazilian customer hotel bookings. Once you create this new table and fill it with the BRA data, you will analyze it and report back to Sleep Away Inc. Lastly, don’t forget to commit these changes to the database and close the connection.

The hotel_booking.db database has a data table called booking_summary, which consists of their booking information from the year 2017. Here is a field description from the booking_summary data table:
```
Field	Description
hotel	Type of hotel (Resort or City)
is_cancelled	1=cancelled, 0= not cancelled
lead_time	Number of days that elapsed between the entering date of the booking and the arrival date
arrival_date_year	Year they arrived
arrival_date_month	Month they arrived
arrival_date_day_of_month	Day of month they arrived
adults	Number of adults
children	Number of children
adr	Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of staying nights
special_requests	Number of special requests made by the customer (e.g. twin bed or high floor)
```
Mark the tasks as complete by checking them off
Creating Connection and Cursor Objects
1. Connect to the hotel_booking.db database and name the connection object con.


2. Next, you must create your cursor object with .cursor(). Name your cursor object cur for convenience with the following tasks.

## Explore and Understand the Data
3. Now that you have connected to the database, let’s look at some of the actual rows of data.
   
Using the .fetchone() method, view the first row from the booking_summary table. Be sure to print this line of code to view the output.


4. To better understand the data, pull more than one row with the .fetchmany() method. Be sure to specify how many rows to pull and print this line of code to view the output.


Pull `BRA` Data and Save as SQLite Table
5. Now that you’ve looked at some records from booking_summary, pull all records with BRA (Brazil) as country of origin.

Create a SQL statement with the `.fetchall()` method to retrieve the BRA records, and save this tuple as bra. You may print the first five rows of bra to double-check your work.

6. Create a new table named bra_customers that has the following field names and field types:
```
num INTEGER, hotel TEXT, is_cancelled INTEGER, lead_time INTEGER, arrival_date_year INTEGER, arrival_date_month TEXT, arrival_date_day_of_month INTEGER, adults INTEGER, children INTEGER, country TEXT, adr REAL, special_requests INTEGER
```
Note use `CREATE TABLE IF NOT EXISTS` instead of `CREATE` TABLE. This way you won’t run into the following error:
```
sqlite3.OperationalError: table bra_customers already exists
```
In the next task, you will insert the BRA records into this table.


7. Insert the object BRA into the table bra_customers using `.executemany()` and use question marks as field placeholders. Remember, the object BRA is a tuple list of all the rows of data that have BRA for the field country.

8. Great Job! To ensure you correctly inserted bra into bra_customers, print the first ten rows.


## Find the Average Lead Time
9. Sleep Away Inc. would like to compare the average lead time (number of days that elapsed between the entering date of the booking and the arrival date) of those who cancelled and those who did not cancel (from the BRA data).

Retrieve the rows of the column lead_time where the customer cancelled their booking. Pull this data from the bra_customers table using the .fetchall() method. You will also use the SQL commands SELECT, FROM, and WHERE.

Remember, the field is_cancelled is 1 if cancelled and a 0 if they did not cancel.

Be sure to save these rows as a new object such as `lead_time_can`.

Check out the Advanced Tip in the hint below to learn more about pulling and analyzing SQLite data!

10. Now that you retrieved the desired rows of data, create a for loop that iterates through and calculates the average lead time. This will be much easier if you saved the data retrieved in task #9 in a variable.

11. Create an object made up of the lead_time field, but this time for those who did NOT cancel their booking.

12. Calculate the average lead time of those who did NOT cancel their booking. You may use the same for loop as task #10 but make sure it iterates through the new data retrieved.

After you find the average lead time of both those who cancelled and those who did not cancel, compare them. Which group has a higher average lead time, and by how much? How could this knowledge help Sleep Away to have fewer cancellations?


## Find the Total Special Requests
13. Sleep Away Inc. also wants you to calculate the total amount of special requests for cancelled vs. not cancelled.

First, retrieve the special_requests field from the bra_customers data table for those who cancelled. You can use the `.fetchall()` method or a for loop.

Be sure to save this data as an object.

14. With the data you retrieved, use a for loop to find the total amount of special requests for cancelled bookings.

15. Pull the total special requests column from the bra_customers data table for those who did NOT cancel. You can use the `.fetchall()` method or a for loop.

Be sure to save this data to an object.

16. Now find the total amount of special requests for those who did not cancel. Compare this to the total amount of special requests for those who cancelled.

Does it surprise you which group is higher? What can you tell Sleep Away to help them have fewer cancellations?

## Committing Changes and Closing Connection
17. Great Job! You have finished working in this database. Commit all the changes using `.commit()`. This ensures that any changes to the database are not lost.

Once you have committed the changes, you may close the connection with `.close()`.