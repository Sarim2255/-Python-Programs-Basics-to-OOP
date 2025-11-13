def palindrome(text):
    word = text.lower()
    left = 0
    right = len(word)-1

    while left < right:
        if word[left] != word[right]:
            return "Not a Palindrome"
        else:
            return "Palindrome"
        
str = input("Enter the string: ")
p = palindrome(str)
print(p)


# --------------------------------------------------------
'''
Output->

    Enter the string: Madam
    Palindrome
    --------------------------
    Enter the string: teacher
    Not a Palindrome
'''