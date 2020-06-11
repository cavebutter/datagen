# RPM Datagen

## Summary

Several small applications that exist to provide sample data sets for a variety of different purposes. 

generator.py generates any number of random string and numeric data columns and rows via text interface. Output is csv with an option for .txt output using PrettyTable formatting.  This is perfect for creating small tables to use when asking questions on Stack Overflow or similar.  The formatted .txt output saves you a lot of time and makes your questions look better.

db_generator.py creates multiple tables for a sample database of customers, employees, products, categories, and sales transactions.

create_mysql.py takes all of the data files created in db_generator and creates and populates a MySQL database. Hard configured for 'localhost', root, root - but prompts can change the configuration.

All applications run in IDLE or command line.

## To Create a Database or Database Table CSVs (Quick Summary)
0.  If creating a database, ensure you have access to a MySQL server.  If not, you will have all the csvs you need to create one manually.
1.  Run db_generator.py and remember the name of your database
2.  Run create_mysql.py and enter the name of your database
3.  Enjoy your data

## To Generate Random Data
1.  Run generator.py
2.  Enter the name of your table.  This will be the name of the output files.
3.  Choosing Index will add an ID column in column A.
4.  Enjoy your data

## Detailed Walkthrough of db_generator
1.  "What is the name of your database?" This question establishes the output directory (output/db_name) and is used to run create_mysql
2.  "How many customers in your database?" The length of the customers table.  Effectively no max.
3.  "What percentage of your customers are female?" Enter an integer.  This sets the percentage of female and male names generated.
4.  "How many sales regions in your database?" Enter an integer 1-9.  Each region will generate 1 sales manager of random name and gender.  Regions cover the USA with each state assigned to a region.
5.  "How many sales reps does each sales manager have?"  Random names and genders.
6.  "What is the start year for sales data?" Establishes the lower boundary for transaction dates starting on 1/1 of the input year.
7.  "What is the end year for sales data?" Establishes the upper boundary for transaction dates ending on 12/31 of the input year.
8.  "What is the volume of sales transactions per year?" Used to determine the length of the transactions table.  Transaction dates are selected randomly from the date range.
9.  All required tables will be generated and saved in 'output/$db_name'.
10.  If you'd like a MySQL database generated from this data, run create_mysql_db  *You must have create db rights on your server*
11.  "Use 'localhost', root, root?"  This is the default configuration for MySQL instances in MAMP.  Enter 'y' to use these credentials.  Any other entry will prompt you to enter host, user and pass for your database.
12.  "Enter your database name."  This tells the application where to look for the data as well as provides the name for the new db.  
13.  Enjoy your database

### I hope you find this application useful!

I welcome feedback!

Pleae consider a donation to support more development work.  (Venmo: @JayCo613)
