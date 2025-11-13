
def compound_intrest(principal, rate, time, n):

    amount = principal * (1 + rate / n) ** (n * time)
    Ci = amount - principal
    return Ci

p = int(input("Enter the principal: "))     #1000
r = float(input("Enter the rate of interst: "))        #0.05
t = int(input("Enter the time period: "))    #2
n = int(input("Enter the number of times interest is compounded per year: "))   #4

c = compound_intrest(p,r,t,n)
print(f"The compound interst is as :{c}")     #Output-> 104.4861011814121