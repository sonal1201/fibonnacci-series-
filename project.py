'''
In this project user will enter single or multiple numbers and your system will predict that the
entered number or number's is/are valid number(s) in a Fibonacci series or not.

For example, if user inputs 2 numbers
(0 and 7)

0 is valid and 7 is invalid.

Because if we plot Fibonacci series 0 1 1 2 3 5 8 13...... In this series 0 is their but 7 is not present.

(Student is free to decide the nput and output layout for this mini project)
'''
import math
a=input("Enter a number or numbers: ").split(",")
l1=[]
for i in a:
    l1.append(int(i))
# l1=sorted(l1)

def isfibonacci(n):
    return perfectsquare(5*n*n+4) or perfectsquare(5*n*n-4)

def perfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x

for i in l1:
    if (isfibonacci(i)==True):
        print(i,"is a Fibonacci Number")
    else:
        print(i,"is not a Fibonacci Number")