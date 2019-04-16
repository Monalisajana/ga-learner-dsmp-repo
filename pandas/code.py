# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)




# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
null = bank.isnull().sum()
bank_mode = banks.mode()
banks = banks.fillna('bank_mode')


#code ends here


# --------------
# Code starts here





avg_loan_amount = pd.pivot_table(banks,index = ['Gender','Married','Self_Employed'],values ='LoanAmount',aggfunc = np.mean)
print(avg_loan_amount)



# code ends here



# --------------
# code starts here




cond1=banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se = len(cond1)
print(loan_approved_se)
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)
percentage_se = (loan_approved_se / 614 ) * 100
percentage_nse = (loan_approved_nse /614) * 100
print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here



count = 0
loan_term = banks['Loan_Amount_Term'].apply(lambda x :int(x)/ 12)
for i in loan_term:
  if i >=25:
    count = count + 1
print(count)
big_loan_term = count    


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


