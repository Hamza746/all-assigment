# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def fact(number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial*i
    print(factorial)

fact(4)        

    







#         # Python program to find the factorial of a number provided by the user.

# # change the value for a different result
# num = 3

# # To take input from the user
# #num = int(input("Enter a number: "))

# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)