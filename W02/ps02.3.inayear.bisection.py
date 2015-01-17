# -*- coding: utf-8 -*-
##PS02: Problem 3: Paying Debt Off In a Year using Bisection

#Test Case 1:
#balance = 320000
#annualInterestRate = 0.2

#Test Case 2:
balance = 999999
annualInterestRate = 0.18

# Code Start
epsilon = 0.01
monthly_interest_rate= annualInterestRate / 12.0
monthly_payment_lower_bound = balance / 12.0
monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
ans = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2.0

def in_a_year(pay, myBalance):
    '''
    pay and myBalance are num
    Returns what is left of balance after one year
    with given payment (pay) and balance (myBalance)
    '''
    previous_balance = myBalance
    for current_month in range(1, 13):        
        monthly_unpaid_balance = (previous_balance) - (pay)
        updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
        previous_balance = updated_balance_each_month
        if previous_balance <= 0:
            break

    return previous_balance

b1 = in_a_year(ans, balance)

while abs(b1) > epsilon:   
    if b1 < 0:
       monthly_payment_upper_bound = ans
    else :
       monthly_payment_lower_bound = ans;

    ans = (monthly_payment_upper_bound+monthly_payment_lower_bound)/2.0;
    
    b1 = in_a_year(ans, balance)
    
print "Lowest Payment: " + str(round(ans, 2))