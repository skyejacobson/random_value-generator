import random
import pandas as pd

# set up the table dimensions
num_rows = '''number of rows'''
num_cols = '''number of columns'''

# calculate the average value
avg_val = '''Your average value here'''

# calculate the range of random values based on the average value
rand_range = 2 * (avg_val - '''the whole number value of your average value''')

# create a list of random numbers with 2 decimal places
rand_list = [round(random.uniform('''x''', '''y''' + rand_range), 2) for i in range(num_rows)]

# create a pandas DataFrame from the data and print it
df = pd.DataFrame(rand_list, columns=['''name'''])
print(df)