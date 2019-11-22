 # Write a program to identify duplicate values from list
list = ['1','2','3','4','5','2','4','3','2','6']
list2 = []
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)