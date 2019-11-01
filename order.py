warmup = [str(i) for i in input('Enter a sequecne of numbers: ')]
warmup1 = []

for num in warmup:
	if '0' not in warmup:
		warmup1.append(num)
	print(warmup1)