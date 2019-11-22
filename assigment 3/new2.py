# Write a program to check if there is any numeric value in list using for loop
a =[12,5,5,78,5,"hamza","ali","pakistan"]
lst = []
for b in a:
    if type(b)==int:
        lst.append(b)
print("numeric values in list are:",lst)
