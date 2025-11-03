# use exception handling

age = int(input("enter the age "))

try:
    if(age>0):
        if(age>18):
            print("you  are elg")
        else :
            print("not elg")
    else:
      raise Exception("Age less than 18 and No Negative Values")

# except age<18==401:
#     print("Success")

# except age<18==402:
#     print("402 Err0r")

# except age<18==403:
#     print("403 Err0r")

# except age<18==404:
#     print("Path Not Found And Page Not Found") 

except ValueError as age:
    print(age)

except Exception as e:
    print(e)


finally:
    print