# Question:4
# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same
# backward as forward, e.g., madam
def checks(word):
    a=word[::-1]
    if a==word:
        print("True")
    else:
        print("False")
checks("rock")        

