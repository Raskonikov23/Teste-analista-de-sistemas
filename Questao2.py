# get input from user
n = int(input("Enter a number: "))

# calculate Fibonacci sequence
fibonacci = [0, 1]
while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# check if number is in Fibonacci sequence
if n in fibonacci:
    print("The number", n, "is in the Fibonacci sequence.")
else:
    print("The number", n, "is not in the Fibonacci sequence.")
          
