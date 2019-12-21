#Question:3
# # Write a Python function to print the even numbers from a given list.
def even(number):
    evenlist = []
    for i in number:
        if i%2==0:
            evenlist.append(i)
    print(evenlist)
            
even([1,2,4,6,7,9,0,6,3,1,1,9,9,8])          
