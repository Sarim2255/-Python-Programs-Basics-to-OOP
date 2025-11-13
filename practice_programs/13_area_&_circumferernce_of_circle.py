import math
def circle(radius):
    # area = float(math.pi) * radius **2
    # circumference = 2 * float(math.pi) * radius
     
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius

    
    return f"Area: {area}\nCircumference: {circumference}"


r = int(input("Enter the radius of circle:"))
cir = circle(r)
print(cir)



# ---------------------------------------------------------------------
"""
Output->

    Enter the radius of circle: 3
    Area: 28.25999999998
    Circumference: 18.84
    
"""