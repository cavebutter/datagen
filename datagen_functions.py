# Functions used in the DataGen Application
import random
import csv
import datetime


#  Generates a random subset of the referenced list of strings.  Number
#  of rows is determined by the passed row_count variable.
def random_index(row_count, str_list):
    i = 0
    randomized_list = []
    while i < row_count:
        index = random.randint(0, len(str_list) - 1)
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
#  This function is not used - it is re-created in db_generator
def create_people_first_name(size, pct_f, m_names, f_names, m_freq, f_freq):
    size = int(size)
    size_f = size * (int(pct_f) / 100)
    size_m = size * (1 - int(pct_f) / 100)
    m_first_names = [random.choices(m_names, weights=m_freq, k=size_m)]
    f_first_names = [random.choices(f_names, weights=f_freq, k=size_f)]
    all_first_names = list(zip(m_first_names, f_first_names))
    return all_first_names


def create_people_surname(size):
    surnames = [random.choices(surnames, cum_weights=surname_cum_freq, k=size)]
    return surnames


# create a list of 300 names to build a sales force from
def sales(sales_regions, reps, f_file, m_file, s_file):
    f_names = process_first_names(f_file)
    f_freq = process_names_frequencies(f_file)
    m_names = process_first_names(m_file)
    m_freq = process_names_frequencies(m_file)
    # Create list of 300 names to choose from
    size = 150
    first_names = []
    m_first_name = random.choices(m_names, weights=m_freq, k=size)
    f_first_name = random.choices(f_names, weights=f_freq, k=size)
    for name in m_first_name:
        first_names.append(name)
    for name in f_first_name:
        first_names.append(name)
    surnames = process_surnames(s_file)
    sname_cum_freq = surname_cum_freq(s_file)
    surnames = random.choices(surnames, cum_weights=sname_cum_freq, k=size * 2)

    # Select random entries from big list
    f_names_list = random_index(reps, first_names)
    l_names_list = random_index(reps, surnames)
    # create index
    rep_id = add_index(reps)
    # Assign regions
    new_sales_regions = sales_regions
    if new_sales_regions == 1:
        region_list = ['USA']
    elif new_sales_regions == 2:
        region_list = ['West', 'East']
    elif new_sales_regions == 3:
        region_list = ['West', 'East', 'South']
    elif new_sales_regions == 4:
        region_list = ['West', 'Midwest', 'South', 'Northeast']
    elif new_sales_regions == 5:
        region_list = ['West', 'Midwest', 'Southeast', 'Southwest', 'Rocky Mountain']
    elif new_sales_regions == 6:
        region_list = ['Pacific', 'Rocky Mountain', 'Midwest', 'Northeast', 'Southwest', 'Southeast']
    elif new_sales_regions == 7:
        region_list = ['Mid-Atlantic', 'Midwest', 'Northeast', 'Northwest', 'Southeast', 'Southwest', 'West']
    elif new_sales_regions == 8:
        region_list = ['Great Lakes', 'Mid South', 'Mid West', 'New England', 'Northeast', 'Northwest', 'South Central',
                       'Southeast', 'West']
    elif new_sales_regions == 9:
        region_list = ['Far West', 'Great Lakes', 'Mid South', 'Mid West', 'Mountain West', 'New England', 'Northeast',
                       'Northwest', 'South Central', 'Southeast']
    regions_list = region_list * ((int(reps) // len(region_list)) + 1)
    sales = list(zip(rep_id, f_names_list, l_names_list, regions_list))

    return sales


# Generate Generic Sales - a single line item for each sale.
# Not invoices, rather a list of tx_id, cust_id, product_id, sales_rep,
# date, qty, unit_price, order_total
def g_sales(volume, start_year, end_year, data_directory):
    with open('data\\products.csv', 'r') as f:
        reader = csv.reader(f)
        products = list(reader)
    with open('output\\' + data_directory + '\\customers.csv', 'r') as f:
        reader = csv.reader(f)
        customers = list(reader)
    with open('output\\' + data_directory + '\\sales_reps.csv', 'r') as f:
        reader = csv.reader(f)
        sales_reps = list(reader)
    generic_sales = []  # List to hold all transactions
    i = 0
    tx_id = 1
    qty = [1, 2, 3, 4, 5]  # List of possible order quantities
    qty_cum_wts = [40, 50, 55, 56, 57]  # Cumulative weights for above quantities
    #  Determine start and end dates and setup random date chooser
    start_date = datetime.date(int(start_year), 1, 1)
    end_date = datetime.date(int(end_year), 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    while i < volume:
        tx = []
        tx.append(tx_id)
        choose_cust = random.randint(1, len(customers) - 1)
        cust_choice = customers[choose_cust][0]
        tx.append(cust_choice)  # index 1
        choose_rep = random.randint(1, len(sales_reps) - 1)
        rep_choice = sales_reps[choose_rep][0]
        tx.append(rep_choice)  # index 2
        choose_product = random.randint(1, len(products) - 1)
        prod_id_choice = products[choose_product][5]
        tx.append(prod_id_choice)  # Product ID  # index 3
        unit_price_choice = float(products[choose_product][3])
        tx.append(unit_price_choice)
        order_qty_list = random.choices(qty, cum_weights=qty_cum_wts, k=1)
        order_qty = int(' '.join([str(elem) for elem in order_qty_list]))
        tx.append(order_qty)
        order_price = round(tx[4] * tx[5], 2)
        tx.append(order_price)
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        tx_date = random_date.strftime('%Y-%m-%d')
        tx.append(tx_date)  # index 7
        generic_sales.append(tx)
        i += 1
        tx_id += 1

    return generic_sales


# Create a regions.csv that matches the regions in the db
def regions(sales_regions, output_directory):
    with open('data\\regions.csv', 'r') as f:
        reader = csv.reader(f)
        full_list = list(reader)
    states = [item[0] for item in full_list]
    col = int(sales_regions)
    region_column = [item[col] for item in full_list]
    new_list = list(zip(states, region_column))
    header = ['state', 'region']
    with open('output\\' + output_directory + '\\regions.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(new_list)


