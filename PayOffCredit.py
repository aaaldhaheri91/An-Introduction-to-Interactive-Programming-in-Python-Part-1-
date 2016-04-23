##Credit Card balance program
balance = float(input("Please Enter the outstanding balance: "))
annual_interest = float(input("Please enter the annual credit card interest rate as a decimal: "))
minimum_monthly = float(input("Please enter the minimum monthly payment rate as a decimal: "))
amount_paid = 0
remaining_balance = None

def calculate(balance, annual_interest, minimum_monthly):
    global remaining_balance, amount_paid
    i = 0
    for i in range(12):
        print ("\nMonth: " + str(i +1))
        minimum_payment = minimum_monthly * balance

        amount_paid += minimum_payment
        print ("Minimum monthly payment: $", round(minimum_payment, 2))

        interest_paid = (annual_interest / 12) * balance
        principal_paid = minimum_payment - interest_paid
        print ("Principal paid: $", round(principal_paid, 2)) 

        remaining_balance = balance - principal_paid
        print ("Remaining balance: $", round(remaining_balance, 2))
        i += 1
        balance -= principal_paid

    return remaining_balance, amount_paid


function = calculate(balance, annual_interest, minimum_monthly)
print ("\nReslult")
print ("Total amount paid: $", round(amount_paid, 2))
print ("Remaining balance: $", round(remaining_balance, 2))


# Determines remaining credit card balance after a year of making the minimum payment each month

balance = float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
minMonthlyPaymentRate = float(input("Enter the minimum monthly payment rate as a decimal: "))

# Monthly Interest Rate
monthlyInterestRate = annualInterestRate/12

# Initialize state variables
numMonths = 1
totalAmtPaid = 0

while numMonths <= 12:
    # Minimum monthly payment of balance at start of the month
    minPayment = round(minMonthlyPaymentRate * balance,2)
    totalAmtPaid += minPayment
    
    # Amt of monthly payment that goes to interest
    interestPaid = round(monthlyInterestRate * balance,2)
    
    # Amt of principal paid off
    principalPaid = minPayment - interestPaid
    
    # Subtract monthly payment from outstanding balance
    balance -= principalPaid
    
    print ("Month:", numMonths)
    print ("Minimum monthly payment:", minPayment)
    print ("Remaining balance:", balance)
    
    # Count this as a new month     
    numMonths += 1

print ("RESULT")
print ("Total amount paid:",totalAmtPaid)
print ("Remaining balance:",balance)
