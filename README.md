# Loan-Data-Analysis

One-line description: Python script for analyzing loan data with filters and aggregations using pandas.

Summary: This Python script utilizes pandas to analyze a dataset containing loan applicants' information. It starts by creating a DataFrame with fields like Applicant ID, Credit Score, Age, Income, Loan Amount, Employment and Housing Status, and Previous Default incidents. The script then performs various analyses:
1. **Employment Analysis**: Filters applicants with employment statuses starting with 'F' and calculates the mean values of numeric columns.
2. **Housing Analysis**: Aggregates loan amounts by housing status to find the maximum, minimum, and their difference.
3. **Loan-to-Income Analysis**: Identifies applicants who are not unemployed and have a loan amount exceeding one-third of their income.
The output displays these analyses, providing insights into the financial behaviors and conditions of the applicants.
