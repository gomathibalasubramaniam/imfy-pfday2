def find_new_salary(current_salary,job_level):
    if(job_level==3):
        new_salary=(current_salary*0.15)+current_salary
    elif(job_level==4):
        new_salary=(current_salary*0.07)+current_salary
    elif(job_level==5):
        new_salary=(current_salary*0.05)+current_salary
    else:
        new_salary=invalid
    return new_salary
# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(25000,4)
print(new_salary)
