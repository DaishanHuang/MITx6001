##PS02: Problem 1: Paying the Minimum

#Test Case 1:
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#Test Case 2:
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Code start
previous_balance = balance
total_paid = 0.0

monthly_interest_rate= annualInterestRate / 12.0

for current_month in range(1, 13):
    print "Month: " + str(current_month)
    
    minimum_monthly_payment = (monthlyPaymentRate) * (previous_balance)
    monthly_unpaid_balance = (previous_balance) - (minimum_monthly_payment)
    updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
    
    print "Minimum monthly payment: " + str(round(minimum_monthly_payment, 2))
    print "Remaining balance: " + str(round(updated_balance_each_month, 2))
    
    total_paid += minimum_monthly_payment
    previous_balance = updated_balance_each_month
    


print "Total paid: " + str(round(total_paid, 2))
print "Remaining balance: " + str(round(previous_balance, 2))
