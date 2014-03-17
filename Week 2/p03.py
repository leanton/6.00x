balance = 5000.0;
annualInterestRate = 0.18;

def remainBalance(balance, payment, annualInterestRate):
        for i in range(12):
                balance = round((balance - payment) * (1 + annualInterestRate / 12), 2)
        return balance;

loPayment = round(balance / 12.0, 2)
hiPayment = round(balance, 2)
remainbalance = balance
while (abs(remainbalance) > 0.1):
	payment = round((hiPayment + loPayment)/2, 2)
	remainbalance = remainBalance(balance, payment, annualInterestRate)
	if (remainbalance > 0):
		loPayment = payment
	else:
		hiPayment = payment 
	#print(remainbalance)

print('Lowest Payment: ' + str(payment))

