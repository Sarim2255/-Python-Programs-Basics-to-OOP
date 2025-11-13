def count_vowel(str):
    word  = str.lower()
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels:
            count +=1
    return count


str = input("Enter your string: ")
s = count_vowel(str)
print(f"The number of vowels in the {str} is {s}")


# ---------------------------------------------------------------------
"""
Output
        Enter your  string: John Snow
        The number of vowels in the John Snow is 2
"""