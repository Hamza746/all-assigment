# Write a Python program to sum all the numeric items in a dictionary
a={1:100,2:200,3:300,4:400,5:500}
b = sum(a[item] for item in a)
print(b)
