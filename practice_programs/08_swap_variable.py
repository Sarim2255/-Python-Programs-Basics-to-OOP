a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

# method 1
a = a + b
b = a - b
a = a - b
print(a,b)          #3  2

# method 2
a,b = b,a
print(a,b)          #2  3