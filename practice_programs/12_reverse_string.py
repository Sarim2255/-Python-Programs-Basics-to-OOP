def reverse_string(str):
    return str[::-1]
# slicing helps in reversing the string [start:stop:step]

s = input("Enter the string: ")
str = reverse_string(s)
print(f"The reverse string is as {str}")


# ------------------------------------------------------
"""
Output->

        Enter the string: snow
        The reverse string is as wons
        
"""