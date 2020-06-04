# Program to generate sample data tables
import random
import csv
import datagen_functions as dg
from prettytable import from_csv, PrettyTable

# Generate string lists from included csv's

with open('data/animals.csv', newline='') as f:
    reader = csv.reader(f, delimiter = ',')
    foo = list(reader)
    animals = foo[0]

with open('data/flowers.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    flowers = foo[0]

with open('data/trees.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    trees = foo[0]

with open('data/countries.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    countries = foo[0]

with open('data/dogs.csv', newline='') as f:
    reader = csv.reader(f)
    dogs = list(reader)
         

with open('data/colors.csv', newline='') as f:
    reader = csv.reader(f, delimiter = ",")
    colors = list(reader)
    
# Flatten the lists of lists
dogs = dg.flatten_lol(dogs)  
colors = dg.flatten_lol(colors)

del foo


# Number Lists
num_list_1 = [random.randint(1, 500) for x in range(500)]

num_list_2 = [random.randint(501, 10000) for x in range(500)]

num_list_3 = [random.randint(10000, 900000) for x in range(500)]

num_list_4 = [random.randint(1, 10) for x in range(500)]


# Get information about the table
col_list = [] # Stores the list of values for each column
col_headers = [] # Stores the names of the headers for each column

table_name = input('What is the name of your table? ')
include_index = input('Do you want your table to be indexed? (y/n) ')
row_count = int(input('How many rows of data in your table? '))
if include_index == "y":  # Creates index
    index = dg.add_index(row_count)
    col_list.append(index)
    col_headers.append('ID')  # Hard-coded header
    
# Routine to determine number and type of columns
num_columns = int(input('How many columns in your table? (Max 8) '))
i = 0
while i < num_columns:
    i += 1
    item = input("""What type of data would you like?
(1)  Animals
(2)  Flowers
(3)  Trees
(4)  Countries
(5)  Colors
(6)  Dogs
(7)  Numbers in range 1-500
(8)  Numbers in range 501-10000
(9)  Numbers in range 10000-900000
(10) Numbers in range 1-10
Enter the number of your choice: """)

#  Pretty primitive error handling, but it seems to work    
    while item not in ['1','2','3','4','5','6','7','8','9','10']:
        item = input('Make a better choice.  Please enter a number: ')    
    header = input("What is the name of this column? ")
    col_headers.append(header)

#  There must be a more elegant way to handle this...    
    if item == '1':
        animals_list = dg.random_index(row_count, animals)
        col_list.append(animals_list)
    elif item == '2':
        flowers_list = dg.random_index(row_count, flowers)
        col_list.append(flowers_list)
    elif item == '3':
        trees_list = dg.random_index(row_count, trees)
        col_list.append(trees_list)
    elif item == '4':
        countries_list = dg.random_index(row_count, countries)
        col_list.append(countries_list)
    elif item == '5':
        colors_list = dg.random_index(row_count, colors)
        col_list.append(colors_list)
    elif item == '6':
        dogs_list = dg.random_index(row_count, dogs)
        col_list.append(dogs_list)
    elif item == '7':
        num_1 = dg.generate_num_col(row_count,num_list_1)
        col_list.append(num_1)
    elif item == '8':
        num_2 = dg.generate_num_col(row_count,num_list_2)
        col_list.append(num_2)
    elif item == '9':
        num_3 = dg.generate_num_col(row_count,num_list_3)
        col_list.append(num_3)
    elif item == '10':
        num_4 = dg.generate_num_col(row_count,num_list_4)
        col_list.append(num_4)
    
 # Commbined list of generated lists


master = list(zip(*col_list))

# Output as csv
with open('output\\' + table_name + ".csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(col_headers)
    writer.writerows(master)


# Completion Message
print("Your sample data CSV file is ready.  You can find it in the Output directory.")
as_text = input('Would you like the output as formatted text too? (y/n) ')

# Formatting text with PrettyTable
if as_text == 'y':
    fp = open('output\\' + table_name + ".csv", "r")
    pt = from_csv(fp)
    fp.close()
    with open('output\\' + table_name + ".txt", "w") as f:
        f.write(str(pt))
    print("Your txt file is ready.  It is in the Output directory")
        
    
