def additive(num: int)->int:
	count = 0
	while num > 9:
		num = sumdigits(num)
		count +=1

	return count

def sumdigits(num: int)->int:
	tot = 0
	while num > 0:
		num, tot = num // 10, tot + (num % 10)

	return tot


num = int(input("Enter a number: "))
print("The sum of digits of number is", sumdigits(num), "and the additive persitence is", additive(num))