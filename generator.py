# Program to generate sample data tables
import random
import csv
import datagen_functions as dg

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
    

del foo


# Number Lists
num_list_1 = [random.randint(1, 500) for x in range(500)]

num_list_2 = [random.randint(501, 10000) for x in range(500)]

num_list_3 = [random.randint(10000, 900000) for x in range(500)]

num_list_4 = [random.randint(1, 10) for x in range(500)]


# Get information about the table
table_name = input('What is the name of your table? ')
num_str_columns = int(input('How many text columns in your table? (Max 4) ')) 
num_num_columns = int(input('How many numeric columns in your table? (Max 4)'))
row_count = int(input('How many rows of data in your table? '))

# Flatten the lists of lists
dogs = dg.flatten_lol(dogs)  
colors = dg.flatten_lol(colors)

# Generate the lists based on row_count
animals_list = dg.random_index(row_count,animals)
flowers_list = dg.random_index(row_count,flowers)
trees_list = dg.random_index(row_count,trees)
countries_list = dg.random_index(row_count,countries)
colors_list = dg.random_index(row_count,colors)
dogs_list = dg.random_index(row_count,dogs)
num_1 = dg.generate_num_col(row_count,num_list_1)
num_2 = dg.generate_num_col(row_count,num_list_2)
num_3 = dg.generate_num_col(row_count,num_list_3)
num_4 = dg.generate_num_col(row_count,num_list_4)

# Commbined list of generated lists
master = list(zip(animals_list,colors_list,flowers_list,trees_list,dogs_list,countries_list,num_1,num_2,num_3,num_4))

# Output as csv
with open(table_name + ".csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['animal', 'color', 'flower', 'tree', 'dog', 'country', 'num1', 'num2', 'num3', 'num4'])
    writer.writerows(master)

# Completion Message
print("Your sample data is ready")
