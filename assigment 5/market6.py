# Question: 6
# Suppose a customer is shopping in a market and you need to print all the items
# which user bought from market.
# Write a function which accepts the multiple arguments of user shopping list and
# print all the items which user bought from market.
# (Hint: Arbitrary Argument concept can make this task ease)


def marketitem(*shoppinglist):
    for elements in shoppinglist:
        print("you brought:", elements)


shoppinglist = []
while True:
    a = input(shoppinglist)
    print(a, "you buy from market if you leave enter quit:")
    if shoppinglist == "quit":
        break
    shoppinglist.append(a)
marketitem(shoppinglist)
