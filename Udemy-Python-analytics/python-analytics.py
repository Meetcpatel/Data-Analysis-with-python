import pandas as pd

df = pd.read_csv('original1.csv', sep=',', header=0)

# print(df)

def cleanup_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary

df['clean_salary'] = df.apply(cleanup_salary, axis=1)

print('Average salary par gender')
print(df.groupby('gender')['clean_salary'].mean())


def female_salary(row):
    if row['gender'] == 'Female':
        return row['clean_salary']

df['female_sallry_avg'] = df.apply(female_salary, axis=1)

def male_salary(row):
    if row['gender'] == 'Male':
        return row['clean_salary']

df['male_sallry_avg'] = df.apply(male_salary, axis=1)

print(df.groupby('Job Title')['clean_salary', 'male_sallry_avg', 'female_sallry_avg'].mean())

print(df)
