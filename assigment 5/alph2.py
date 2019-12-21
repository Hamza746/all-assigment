# Question:2
# Write a Python function that accepts a string and calculate the number of upper
# case letters and lower case letters.
def alphabet (letters):
    upper=0
    lower=0
    for i in letters:
        if i.isupper()== True:
            upper+=1
        else:
            lower+=1
    print(upper)           
    print(lower) 
alphabet("HAMZazaz.")    
