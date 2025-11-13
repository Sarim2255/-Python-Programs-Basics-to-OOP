
def c_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_temperature(fahrenheit):
    celsius = 5/9 *(fahrenheit - 32 )
    return celsius

# From celcius to Fahrenheit 
celsius = float(input("Enter the temperature in degree celcius: "))
c_temp = c_temperature(celsius)
print(f'The temperature in degree fahrenheit is {c_temp}')


# From Fahrenheit to celcius
# fahrenheit = float(input("Enter the temperature in degree celcius: "))
# f_temp = c_temperature(fahrenheit)
# print(f'The temperature in degree celcius is {f_temp}')


# -------------------------------------------------------------------------------------
"""
Output->

    Enter the temperature in degree celcius: 15
    The temperature in degree fahrenheit is 59.0
    
"""