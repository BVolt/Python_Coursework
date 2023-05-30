"""
Author: Brenden Johnson
Assignment: Project 3 - Task 1
Date: 3-2-2023
Course: 2520.01
"""
from cryptography.fernet import Fernet


# Task 1
# Returns number of character in string
def get_num_of_characters(strng):
    n = 0
    for char in strng:
        n += 1
    return n


# Removes white spaces from string
def output_without_whitespace(strng):
    newStr = strng.replace(" ", "")
    # newStr = newStr.replace("\t", "")
    return newStr


# Encrypts String using Fernet
def get_safe(strng, key):
    fern = Fernet(key)
    encrypted = fern.encrypt(strng.encode())
    return encrypted


# Decrypt string using Fernet
def go_recover(strng, key):
    fern = Fernet(key)
    decrypted = fern.decrypt(strng).decode()
    return decrypted


# Prompts for input and execute all 4 functions
def main():
    sentence = input("Please enter a sentence or phrase: ")
    print("You have entered: " + sentence)
    print("Number of characters = ", get_num_of_characters(sentence))
    print("Whitespaces removed: " + output_without_whitespace(sentence))
    key = Fernet.generate_key()
    encryptedMsg = get_safe(sentence, key)
    print("Encrypted Message: ",  encryptedMsg)
    print("Decrypted Message: " + go_recover(encryptedMsg, key))


if __name__ == "__main__":
    main()


'''
Output

Test Case 1
Please enter a sentence or phrase: The only thing we have to fear is fear itself.
You have entered: The only thing we have to fear is fear itself.
Number of characters =  46
Whitespaces removed: Theonlythingwehavetofearisfearitself.
Encrypted Message:  b'gAAAAABkANP12DV8ZHzquzgU7CsgTXBUePp8ing4nBPoUkkHYIqkJIrz8u8jjnLmeHoWQRrbI3yVfAI332Ninp5wbMYYFfnA1yvw2JMhdZxO8RlzgPAk-HQ-eHPtu2iWrju7taCkCCcW'
Decrypted Message: The only thing we have to fear is fear itself.

Test Case 2
Please enter a sentence or phrase: my grandpa went to the bathroom and it smells
You have entered: my grandpa went to the bathroom and it smells
Number of characters =  45
Whitespaces removed: mygrandpawenttothebathroomanditsmells
Encrypted Message:  b'gAAAAABkANUMVVxGv8g4CS6rLnAGlllGVnZZirZlBw4PMEHJouT0VYDRzl-Ae0NbeVKHzAivwR_-W3wRUMw5J6kwctcP8Q1jHYZteu1u0EhxgbKjZG1Emqju_NGO1kNj9f4O-i4HHnTp'
Decrypted Message: my grandpa went to the bathroom and it smells

Test Case 3
Please enter a sentence or phrase: I like chocolate.
You have entered: I like chocolate.
Number of characters =  17
Whitespaces removed: Ilikechocolate.
Encrypted Message:  b'gAAAAABkANVUrPhtvOzmYKli_JR884zmNWHV7TIU7bc0j3S-DZQk6l5G41nBjf68SVDcrYy1LR1QAhGs8J3loqYcrrpEZiZ3hV08AfPYmfU_7Fz3lPRK2w0='
Decrypted Message: I like chocolate.
'''