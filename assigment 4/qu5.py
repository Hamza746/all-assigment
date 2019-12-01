# Question5:
# Guess the number game
# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to
# guess the correct number. Give three chances to user guess the number and also give hint to user if
# hidden number is greater or smaller than the number he given to input field.
import random as random
a = random.randint(1, 30)
print(a)
b = int(input("Enter number"))
if a == b:
    print("contagtulations!, your answer is correct")
else:
    if a > b:
        print("your answer is wrong, hidden number is greater than the entered number")
        c = int(input("enter another number"))
        if c == a:
            print("contagtulations!, your answer is correct")
        else:
            if c > a:
                print(
                    "your answer is wrong, hidden number is less than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d > a:
                        print(
                            "your answer is wrong, hidden number is less than the entered number")

                    elif d < a:
                        print(
                            "your answer is wrong, hidden number is greater than the entered number")
            elif c < a:
                print(
                    "your answer is wrong, hidden number is greater than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d > a:
                        print(
                            "your answer is wrong, hidden number is less than the entered number")

                    elif d < a:
                        print(
                            "your answer is wrong, hidden number is greater than the entered number")

    elif a < b:
        print("your answer is wrong, hidden number is less than the entered number")
        c = int(input("enter another number"))
        if c == a:
            print("contagtulations!, your answer is correct")
        else:
            if c > a:
                print(
                    "your answer is wrong, hidden number is less than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d > a:
                        print(
                            "your answer is wrong, hidden number is less than the entered number")

                    elif d < a:
                        print(
                            "your answer is wrong, hidden number is greater than the entered number")
            elif c < a:
                print(
                    "your answer is wrong, hidden number is greater than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d > a:
                        print(
                            "your answer is wrong, hidden number is less than the entered number")

                    elif d < a:
                        print(
                            "your answer is wrong, hidden number is greater than the entered number")
