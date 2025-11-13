def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter the number: "))
c = check(n)
print(f"The number entered is {c}")


# ------------------------------------------------

'''
Output->
    Enter the number:34
    The number entered is Even
    ----------------------------
    Enter the number:33
    The number entered is Odd
'''