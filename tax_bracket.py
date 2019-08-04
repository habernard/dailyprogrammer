incomeCap = [0,10000,30000,100000,9999999]
taxRates = [0.00,0.10,0.25,0.40]

def tax(income):
	tax = 0.0
	for i in range(len(incomeCap)-1):
		tax = (max(income - incomeCap[i],0) - max(income - incomeCap[i+1],0)) * taxRates[i] + tax

	return int(tax)

income = int(input('Enter your income: '))
tax = tax(income)
print('You have to pay:', str(tax))