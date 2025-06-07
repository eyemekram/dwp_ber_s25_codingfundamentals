# Welcome intro of the program
print ("Hello, this is the final project of Ekram and Amna") #TODO: adding something more interesting

# Importing the data and library
import pandas as pd

path = 'Project_Ekram_Amna/data.csv'
df = pd.read_csv(path)

# Column names
print(f'Name of columns:{ df.columns}')


# Rows it has
print(f'Number of Rows: {df.shape [0]}')
print(f'Number of columns: {df.shape [1]}')

# Calculating average salary of all employees

print ('Average salary of all employees is:',df["Salary"].mean())

