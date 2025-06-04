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

# Option 1: 
print ('Average salary of all employees is:',df["Salary"].mean())

# Option 2: 
for salaries in df["Salary"]: 
    sum_salaries= sum (df["Salary"])

print(sum_salaries)
average_salaries= sum_salaries/df.shape [0]
print(average_salaries)

# Calculating average age for all employees:
average_age =round (df["Age"].mean())
print ('Average age of all employees is:',average_age, "years old")

# Years of experience range among all employees: 
min_years_experience= min(df["YearsOfExperience"])
max_years_experience= max(df["YearsOfExperience"])
print("The years of experience among all employees ranges between", min_years_experience, " and ", max_years_experience)

# How many departments are there and what are these departments?:
name_department=set(df["Department"])
print("The name of the deparments are", name_department)
print("The company has", len(name_department), "departments")


 

