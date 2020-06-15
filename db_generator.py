import datagen_functions as dg
import random
import csv
from prettytable import from_csv, PrettyTable
import os
import shutil
from pathlib import Path

db_name = input('What is the name of your database? ')
cust_size = int(input('How many customers in your database? '))
cust_f_pct = int(input('What percentage of your customers are female? '))
sales_regions = int(input("How many sales regions in your database? "))
sales_reps = int(input('How many sales reps does each sales manager have? '))
total_reps = sales_regions * sales_reps
start_year = int(input('What is the start year for sales data? '))
end_year = int(input('What is the end year for sales data? '))
tx_year = int(input('What is the volume of sales transactions per year? '))
volume = tx_year * (end_year - start_year + 1)

# Make Directory of DB files
output_directory = Path.cwd() / 'output' / db_name
os.mkdir(output_directory)
data_dir = Path.cwd() / 'data'

#  Generate Customer List
f_names = dg.process_first_names(data_dir / 'first_names_f.csv')
f_freq = dg.process_names_frequencies(data_dir / 'first_names_f.csv')
m_names = dg.process_first_names(data_dir / 'first_names_m.csv')
m_freq = dg.process_names_frequencies(data_dir / 'first_names_m.csv')
surnames = dg.process_surnames(data_dir / 'Names_2010Census.csv')
surname_cum_freq = dg.surname_cum_freq(data_dir / 'Names_2010Census.csv')
# surname_cum_freq.pop()


# Determine proportion of f/m
size_f = int(round(cust_size * (cust_f_pct / 100),0))
size_m = int(round(cust_size * (1-(cust_f_pct / 100)),0))

# Choose first names
first_names = []
m_first_name = random.choices(m_names, weights = m_freq, k = size_m)
f_first_name = random.choices(f_names, weights = f_freq, k = size_f)
for name in m_first_name:
    first_names.append(name)
for name in f_first_name:
    first_names.append(name)

# Choose surnames
surnames = random.choices(surnames, cum_weights = surname_cum_freq, k = cust_size)

# Choose addresses
with open(data_dir / 'fake_addresses_3.csv') as f:
    reader=csv.reader(f)
    addresses = list(reader)
del addresses[0]

sample_addresses = dg.random_index(cust_size, addresses)
street_address = [row[0] for row in sample_addresses]
city = [row[1] for row in sample_addresses]
state = [row[2] for row in sample_addresses]
zipcode = [row[3] for row in sample_addresses]

# Add ID/Index
index = dg.add_index(cust_size)

# Build master customer list
customer_list = list(zip(index,first_names,surnames,street_address,city,state,zipcode))
customer_list.sort(key=lambda list: list[3]) # Sort by address to randomize a bit more

# Export Customers to csv and txt

headers = ['CustID', 'First_Name', 'Last_Name', 'Address', 'City', 'State', 'Zip']

with open(output_directory / 'customers.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerows(customer_list)

fp = open(output_directory / 'customers.csv', 'r')
pt = from_csv(fp)
fp.close()
with open(output_directory / 'customers.txt', 'w') as f:
    f.write(str(pt))

# Sales Managers and Sales Reps
sales_managers = dg.sales(sales_regions, sales_regions)
headers = ['Rep_ID', 'First Name', 'Last Name', 'Region']
with open(output_directory / 'sales_mgrs.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerows(sales_managers)

fp = open(output_directory / 'sales_mgrs.csv', 'r')
pt = from_csv(fp)
fp.close()
with open(output_directory / 'sales_mgrs.txt', 'w') as f:
    f.write(str(pt))

num_reps = sales_regions * sales_reps
reps = dg.sales(sales_regions, num_reps)
sales_reps = dg.sales(sales_regions, num_reps)
with open(output_directory / 'sales_reps.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerows(sales_reps)

fp = open(output_directory / 'sales_reps.csv', 'r')
pt = from_csv(fp)
fp.close()
with open(output_directory / 'sales_reps.txt', 'w') as f:
    f.write(str(pt))

sales_data = dg.g_sales(volume, start_year, end_year, db_name)
headers = ['tx_id', 'cust_id', 'rep_id', 'prod_id', 'price', 'qty', 'cost', 'tx_date']
with open(output_directory / 'transactions.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerows(sales_data)

regions = dg.regions(sales_regions,db_name)

shutil.copyfile(data_dir / 'products.csv', output_directory / 'products.csv')
shutil.copyfile(data_dir / 'manufacturers.csv', output_directory / 'manufacturers.csv')

