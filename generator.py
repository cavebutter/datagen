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
    

del foo


# Number Lists
num_list_1 = [random.randint(1, 500) for x in range(500)]

num_list_2 = [random.randint(501, 10000) for x in range(500)]

num_list_3 = [random.randint(10000, 900000) for x in range(500)]

num_list_4 = [random.randint(1, 10) for x in range(500)]


# Get information about the table
table_name = input('What is the name of your table? ')
include_index = input('Do you want your table to be indexed? (y/n) ')
num_str_columns = int(input('How many text columns in your table? (Max 4) ')) 
num_num_columns = int(input('How many numeric columns in your table? (Max 4)'))
row_count = int(input('How many rows of data in your table? '))

# Flatten the lists of lists
dogs = dg.flatten_lol(dogs)  
colors = dg.flatten_lol(colors)

# Generate the lists based on row_count
if include_index == "y":
    index = dg.add_index(row_count)
else:
    index = False
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

# Field length calcs for text output formatting
animal_length = dg.longest_value(animals_list)
flower_length = dg.longest_value(flowers_list)
tree_length = dg.longest_value(trees_list)
country_length = dg.longest_value(countries_list)
color_length = dg.longest_value(colors_list)
dog_length = dg.longest_value(dogs_list)
num_1_length = dg.longest_value(num_list_1)
num_2_length = dg.longest_value(num_list_2)
num_3_length = dg.longest_value(num_list_3)
num_4_length = dg.longest_value(num_list_4)

# Commbined list of generated lists

# If no index
if index == False:
    master = list(zip(animals_list,colors_list,flowers_list,trees_list,dogs_list,countries_list,num_1,num_2,num_3,num_4))

# Output as csv
    with open('output\\' + table_name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['animal', 'color', 'flower', 'tree', 'dog', 'country', 'num1', 'num2', 'num3', 'num4'])
        writer.writerows(master)

# If yes index
else:
    master = list(zip(index,animals_list,colors_list,flowers_list,trees_list,dogs_list,countries_list,num_1,num_2,num_3,num_4))

# Output as csv
    with open('output\\' + table_name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['ID','animal', 'color', 'flower', 'tree', 'dog', 'country', 'num1', 'num2', 'num3', 'num4'])
        writer.writerows(master)

# Completion Message
print("Your sample data CSV file is ready")
as_text = input('Would you like the output as formatted text too? (y/n) ')

if as_text == 'y':
    fp = open('output\\' + table_name + ".csv", "r")
    pt = from_csv(fp)
    fp.close()
    with open('output\\' + table_name + ".txt", "w") as f:
        f.write(str(pt))
    print("txt file is ready")
        
    
