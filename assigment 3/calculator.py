# 1. Make a calculator using Python with addition , subtraction , multiplication ,
# division and power.
a =int(input("enter first value:"))
b =int(input("enter second value:"))
operator =input("enter operator:")
if operator=="+":
    print("answer=",a+b)
elif operator=="-":
    print("answer=",a-b)
elif operator=="*":
    print("answer=",a*b)
elif operator=="/":
    print("answer=",a/b)
elif operator=="**":
    print("answer=",a**b)    
else:
    ("enter correct operator")




