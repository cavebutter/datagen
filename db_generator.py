import datagen_functions as dg
import random
import csv
from prettytable import from_csv, PrettyTable
import os

db_name = input('What is the name of your database? ')
cust_size = int(input('How many customers in your database? '))
cust_f_pct = int(input('What percentage of your customers are female? '))

# Make Directory of DB files
os.mkdir('output\\' + db_name)

#  Generate Customer List
f_names = dg.process_first_names('data\\first_names_f.csv')
f_freq = dg.process_names_frequencies('data\\first_names_f.csv')
m_names = dg.process_first_names('data\\first_names_m.csv')
m_freq = dg.process_names_frequencies('data\\first_names_m.csv')
surnames = dg.process_surnames('data\\Names_2010Census.csv')
surname_cum_freq = dg.surname_cum_freq('data\\Names_2010Census.csv')
#surname_cum_freq.pop()


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
with open('data\\fake_addresses_3.csv') as f:
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
headers = ['CustID', 'First_Name', 'Last_Name', 'Address', 'City', 'State', 'Zip' ]

with open('output\\' + db_name + '\\customers.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerows(customer_list)

fp = open('output\\customers.csv', 'r')
pt = from_csv(fp)
fp.close()
with open('output\\customers.txt', 'w') as f:
    f.write(str(pt))
