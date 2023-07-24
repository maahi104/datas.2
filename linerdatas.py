# QUESTION 3
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if str2 in temp:
        return True
    else:
        return False

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")


# QUESTION 4

def first_non_repeated_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string = input("Enter a string: ")

result = first_non_repeated_character(string)

if result is None:
    print("There are no non-repeated characters in the string.")
else:
    print("The first non-repeated character in the string is:", result)
