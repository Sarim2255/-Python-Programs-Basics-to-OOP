num = int(input("Enter the number:"))
flag = False

if num <=1:
    print(f"{num} is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    
    if flag:
        print(f"Sorry! Not Prime : {num}")
    else:
        print(f"Prime number : {num}")



# -----------------------------------------------------------
"""
Output->

    Enter the number: 56
    Sorry! Not Prime: 56
    
    Enter the number: 71
    Prime number: 71
"""