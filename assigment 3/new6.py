# Write a Python script to check if a given key already exists in a dictionary
adict={1:"Hamza",2:"Hussain",3:"Haris",4:"kamran"}
b=int(input("key:"))
print(adict.keys())
for i in adict.keys():
    if i==b:
        print("key exist")
        break
else:
    print("key doesnt exist")    




