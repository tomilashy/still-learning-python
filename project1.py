'''
Created on May 2, 2018

@author: o_olasub
'''

print("*****************************************");
print("Input 2 numbers");
a=float(input());
b=float(input());
print("*****************************************");
print("The results are: \n")

print(f" Sum is: {a+b} \n Difference is: {a-b} \n Product is {a*b} \n Average is: {(a+b)/2}")



age=input("\nInput your age\n");

if age:
    age=int(age)    
    if age>17 and not age<17:
        print("You are an adult");
    elif age<18:
        print("You are a minor");
else:
    print("you did not input anything")