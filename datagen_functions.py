#  Functions used in the DataGen Application
import random

#  Generates a random subset of the referenced list of strings.  Number
#  of rows is determined by the passed row_count variable.
def random_index(row_count, str_list):
    i = 0
    randomized_list = []
    while i < row_count:
        index = random.randint (0,len(str_list)-1)
        item = str_list[index]
        randomized_list.append(item)
        i += 1
    return randomized_list

#  Generates a column of numbers from the random lists defined in
#  generator.py  Row numbers determined by the passed row_count variable
def generate_num_col(row_count, num_list):
    output = num_list[0:row_count]
    return output

#  Generate in index column with row numbers determined by passed row_count
def add_index(row_count):
    i = 1
    index = []
    while i <= row_count:
        index.append(i)
        i += 1
    return index

#  Flattens a list of lists
def flatten_lol(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        for item in sublist:
            flat_list.append(item)
    return flat_list

### Functions to support MySQL Terminal-Like table formatting
def longest_value(input_list):
    if isinstance(input_list[1], int):
        converted_list = (str(w) for w in input_list)
        longest_value = len(max(converted_list, key=len))
    else:
        longest_value = len(max(input_list, key=len))
    return longest_value



