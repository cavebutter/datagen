# datagen
Several small applications that exist to provide sample data sets for a variety of different purposes.
generator.py generates any number of random string and numeric data columns and rows via text interface.  Output is csv with an option for .txt output using PrettyTable formatting.

db_generator.py creates multiple tables for a sample database of customers, employees, products, categories, and sales transactions.

create_mysql.py takes all of the data files created in db_generator and creates and populates a MySQL database.  Hard configured for 'localhost', root, root - but prompts can change the configuration.

Data in the data directory mostly comes from data.world.
