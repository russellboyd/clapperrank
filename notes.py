if __name__ == "__main__":
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	list = []
	for x in a:
		if x < 5:
			print(x);
			list.append(x)
	
	for x in list:
		print(x)

	num = int(input("Please enter a number: "))
	
	for x in a:
		if x < num:
			print(x)
