balance = 5000.0;
annualInterestRate = 0.18;

def remainBalance(balance, payment, annualInterestRate):
        for i in range(12):
                balance = round((balance - payment) * (1 + annualInterestRate / 12), 2)
        return balance;

loPayment = round(balance / 12, 2)
hiPayment = round(balance, 2)
remainbalance = balance
while (remainbalance > 0.01):
	payment += 10
	remainbalance = remainBalance(balance, payment, annualInterestRate)
	#print(remainbalance)

print('Lowest Payment: ' + str(payment))


