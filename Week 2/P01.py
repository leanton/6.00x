balance = 5000.0;
annualInterestRate = 0.18;
monthlyPaymentRate = 0.02;

sumPayment = 0.0;
for i in range(12):
	payment = round(monthlyPaymentRate * balance, 2)
	balance = round((balance - payment) * (1 + annualInterestRate / 12), 2)
	print("Month: " + str(i+1))
	print("Minimum monthly payment: " + str(payment))
	print("Remaining balance: " + str(balance))
	sumPayment += payment

print("Total paid: " + str(sumPayment))
print("Remaining balance: " + str(balance))
