# Question:5
# Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def prime(number):
    if number==2:
        print("This number is prime")
    elif number!=2:
        if (number%2==0) or (number%3==0) or (number%5==0):
            print("this number isnt prime")
        else:
            print("this number is prime")
prime(81)