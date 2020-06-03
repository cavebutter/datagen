# Program to generate sample data tables
import random
import csv

# Functions

def random_index(row_count, str_list):
    i = 0
    randomized_list = []
    while i < row_count:
        index = random.randint (0,len(str_list)-1)
        item = str_list[index]
        randomized_list.append(item)
        i += 1
    return randomized_list

def flatten_lol(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def generate_num_col_1(row_count):
    num_col_1 = num_list_1[0:row_count]
    return num_col_1

def generate_num_col_2(row_count):
    num_col_2 = num_list_2[0:row_count]
    return num_col_2

def generate_num_col_3(row_count):
    num_col_3 = num_list_3[0:row_count]
    return num_col_3

def generate_num_col_4(row_count):
    num_col_4 = num_list_4[0:row_count]
    return num_col_4

# Generate string lists from included csv's

with open('animals.csv', newline='') as f:
    reader = csv.reader(f, delimiter = ',')
    foo = list(reader)
    animals = foo[0]

with open('flowers.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    flowers = foo[0]

with open('trees.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    trees = foo[0]

with open('countries.csv', newline='') as f:
    reader = csv.reader(f)
    foo = list(reader)
    countries = foo[0]

with open('dogs.csv', newline='') as f:
    reader = csv.reader(f)
    dogs = list(reader)
         

with open('colors.csv', newline='') as f:
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
dogs = flatten_lol(dogs)  
colors = flatten_lol(colors)

# Generate the lists based on row_count
animals_list = random_index(row_count,animals)
flowers_list = random_index(row_count,flowers)
trees_list = random_index(row_count,trees)
countries_list = random_index(row_count,countries)
colors_list = random_index(row_count,colors)
dogs_list = random_index(row_count,dogs)
num_1 = generate_num_col_1(row_count)
num_2 = generate_num_col_2(row_count)
num_3 = generate_num_col_3(row_count)
num_4 = generate_num_col_4(row_count)

# Commbined list of generated lists
master = list(zip(animals_list,colors_list,flowers_list,trees_list,dogs_list,countries_list,num_1,num_2,num_3,num_4))

# Output as csv
with open(table_name + ".csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['animal', 'color', 'flower', 'tree', 'dog', 'country', 'num1', 'num2', 'num3', 'num4'])
    writer.writerows(master)

# Completion Message
print("Your sample data is ready")
