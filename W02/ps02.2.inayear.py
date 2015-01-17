##PS02: Problem 2: Paying Debt Off In a Year

#Test Case 1:
#balance = 3329
#annualInterestRate = 0.2

#Test Case 2:
#balance = 4773
#annualInterestRate = 0.2

#Test Case 3:
balance = 3926
annualInterestRate = 0.2

# Code start
money_to_pay_each_month = 10

monthly_interest_rate= annualInterestRate / 12.0
has_payed_of_debt = False

if balance <= 0:
    has_payed_of_debt = True
    
while not has_payed_of_debt:
    previous_balance = balance
    
    for current_month in range(1, 13):        
        monthly_unpaid_balance = (previous_balance) - (money_to_pay_each_month)
        updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
        previous_balance = updated_balance_each_month
            
    if previous_balance <= 0:
        has_payed_of_debt = True
        break
    else:
        money_to_pay_each_month += 10

print "Lowest Payment: " + str(money_to_pay_each_month)