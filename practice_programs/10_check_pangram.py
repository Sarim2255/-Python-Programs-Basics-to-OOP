# pangram means that a string should contain all the alphabets in it.


def check_pangram(str):
    string = str.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVYXYZ"

    for words in string:
        if words in alphabets:
            return "Wow all alphabets are present"
        else:
            return "Ohh-no not all alphabets are present"
        
str = input("Enter the string: ")
a = check_pangram(str)
print(a)


# ---------------------------------------------------------------------
"""
Output->

        Enter the string: good morning
        Ohh-no not all alphabets are present
      ---------------------------------------------------------------
        Enter the string: a quick brown fox jumps over the lazy dog.
        Wow all alphabets are present


"""