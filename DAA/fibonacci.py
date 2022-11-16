# Fibonacci series using recursion
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = 9
	print(fibonacci(n))



# Fibonacci Series using Dynamic Programming
def fibonacci(n):
	f = [0, 1]
	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	return f[n]
	
print(fibonacci(9))

