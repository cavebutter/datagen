#  Functions used in the DataGen Application
import random
import csv

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

#  Process first names -- names then frequencies
def process_first_names(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        list_name = list(reader)
        gender_name = [row[0] for row in list_name]
        del gender_name[0]
    return gender_name

# Frequencies
def process_names_frequencies(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        list_name = list(reader)
        gender_frequency = [row[2] for row in list_name]
        del gender_frequency[0]
        gender_frequency = [int(i) for i in gender_frequency]
    return gender_frequency

# Process surnames
def process_surnames(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        surnamelist = list(reader)
        del surnamelist[0]
        surnames = [row[0].title() for row in surnamelist]
    return surnames

# Process surname cumulative Frequencies
def surname_cum_freq(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        surnamelist = list(reader)
        del surnamelist[0]
        surname_cum_freq = [float(row[4]) for row in surnamelist]
    return surname_cum_freq

# Generate Names
def create_people_first_name(size, pct_f, m_names, f_names, m_freq, f_freq):
    size = int(size)
    size_f = size * (int(pct_f) / 100)
    size_m = size * (1 - int(pct_f) / 100)
    m_first_names = [random.choices(m_names, weights = m_freq, k = size_m)]
    f_first_names = [random.choices(f_names, weights = f_freq, k = size_f)]
    all_first_names = list(zip(m_first_names, f_first_names))
    return all_first_names

def create_pople_surname(size):
    surnames = [random.choices(surnames, cum_weights = surname_cum_freq, k = size)]
    return surnames
