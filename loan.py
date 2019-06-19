def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    a=account_number//1000
    if(a==1 and account_balance>=100000):
        if(salary>25000 and loan_type=="Car"):
            eligible_loan_amount=500000
            bank_emi_expected=36
        elif(salary>50000 and load_type=="House"):
            eligible_loan_amount=6000000
            bank_emi_expected=60
        elif(salary>75000 and load_type=="Business"):
            eligible_loan_amount=7500000
            bank_emi_expected=84
        elif(salary<25000 or salary<50000 or salary<75000):
            print("The customer is not eligibble for loan")
        elif(load_type!="Car" or load_type!="House" or load_type!="Business"):
            print("Invalid load")
        if(loan_amount_expected<eligible_loan_amount and customer_emi_expected<bank_emi_expected):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
        elif(loan_amount_expected>eligible_loan_amount and customer_emi_expected>bank_emi_expected):
            print("The customer is not eligible for the loan")
        

    #Use the below given print statements to display the output, in case of invalid data.
    else:
        if(a!=1):
            print("Invalid account number")
        if(account_balance<100000):
            print("Insufficient account balance")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
