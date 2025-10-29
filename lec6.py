 
age = int(input("enter your age:"))

if age < 0 :
    print("age cant be zero or negative")
elif age >= 18 :
    print("can vote")
else :
    print("not eligible for vote")