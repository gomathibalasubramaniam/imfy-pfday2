def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    #write your logic here
    if(current_currency_name=="Euro"):
        current_currency_amount=round(amount_needed_inr/70.5717)
    elif(current_currency_name=="BritishPound"):
        current_currency_amount=round(amount_needed_inr/100)
    elif(current_currency_name=="AustrailianDollar"):
        current_currency_amount=round(amount_needed_inr/46.729)
    elif(current_currency_name=="CanadianDollar"):
        current_currency_amount=round(amount_needed_inr/49.334)
    else:
        current_currency_amount=-1
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"CanadianDollar")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
