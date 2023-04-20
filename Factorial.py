number = int(input("Choose a number to calculate its factorial:\n"))
factorial = number

while number > 1:
    factorial = factorial * (number - 1)
    number -= 1

print(F"The result is {factorial}")
