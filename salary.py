import pandas as pd

# Create a dataframe
df = pd.DataFrame({
    'Applicant_ID': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'Credit_Score': [700, 820, 600, 750, 680],
    'Age': [28, 35, 42, 30, 55],
    'Income': [60000, 80000, 40000, 75000, 90000],
    'Loan_Amount': [20000, 35000, 15000, 25000, 30000],
    'Loan_Term': [36, 60, 24, 48, 60],
    'Employment_Status': ['Full-time', 'Freelance', 'Unemployed', 'Full-time', 'Retired'],
    'Housing_Status': ['Rent', 'Own', 'Homeless', 'Rent', 'Own'],
    'Previous_Default': [0, 0, 1, 1, 0]
})

# Group the data starting with the letter "F" for the 'Employment_Status' column and calculate the average
df_employment_status = df[df['Employment_Status'].str.startswith('F')].groupby('Employment_Status').mean()

# Group the data for the 'Housing_Status' column and calculate the difference between the maximum value and the minimum value
#df_housing_status = df.groupby('Housing_Status').agg({'Loan_Amount': ['max', 'min']})
#df_housing_status['Difference'] = df_housing_status['max'] - df_housing_status['min']
df_housing_status = df.groupby('Housing_Status')['Loan_Amount'].agg(['max', 'min'])
df_housing_status['Difference'] = df_housing_status['max'] - df_housing_status['min']



# Obtain a list of non-unemployed applicants whose Loan Amount represents more than one-third of their income
df_non_unemployed = df[df['Employment_Status'] != 'Unemployed']
df_non_unemployed_high_loan = df_non_unemployed[df_non_unemployed['Loan_Amount'] > (df_non_unemployed['Income'] / 3)]

# Show the results obtained
print(df_employment_status)
print(df_housing_status)
print(df_non_unemployed_high_loan)

