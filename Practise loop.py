"""#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = last - 10
if last > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif last == 0:
    print("Last digit of", number, "is", last, "and is 0")
else:
    print("Last digit of", number, "is", last, "and is less than 6 and not 0")
"""
"""
for i in range(97, 123):
    print("{}".format(chr(i)),end="")
"""
"""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print("{:s}".format(chr(i)), end="")
"""

"""
for i in range(1, 90):
    if i<10:
        print('0'+str(i), end=", ")
    else:
        print(i, end=", ")"""


'''for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")'''


"""
a=20;
b=10;
print(a+b)
print(a-b)"""
        
'''def calculate(a, b):
    print(a+b)
    print(a-b)
    print(a*b)

calculate(20,10)
calculate(40,30)
calculate(50,40)'''

'''def my_function(a,b):
    print("Arguments and parameters")
    print()
    print()
my_function(5,10)'''

'''a=10
b=20
print(a<=b)
'''

'''def my_function():
    passI()'''


'''l=[10,20,30,40,50]
a=0
for value in l:
    a=a+value
print(a)'''

'''lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper-1):
    if(i%5)==0:
        print(i)'''
'''
def pri(my_list=[1,2,3,4,5]):
    for i in my_list:
        print('{:d}'.format(i))

pri() '''

'''def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None
    return my_list[idx]'''

'''class user:
    user1 = user()
    user1.first_name="sandeep"
    user1.last_name="kumar"
    print()'''

class User():
    def __init__(self, full_name, place):
        self.name=full_name
        self.place=place

user=User("Sandeep","Hyderabad")
print(user.name)
print(user.place)

    





            
        








    
