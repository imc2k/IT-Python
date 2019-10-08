from banner import banner
from math import sqrt
banner("Pythagorean Calculator","By Isiah.c")

print("We will help you find the missing side of a right triangle.")
print("The lengths of two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print ("")
print ("please enter the length of each side, or leave it blank if you dont know.")
again = 'Y'
while again == 'Y':
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if a == "":
        b = float (b)
        c = float (c)
        a = sqrt(c*c-b*b)
        print(f"Your missing side is{a}")
    elif b == "":
        a = float (a)
        c = float (c)
        b = sqrt(c*c-a*a)
        print(f"Your missing side is{b}")

    elif c == "":
        a = float (a)
        b = float (b)
        c =sqrt(a*a+b*b)
        print(f"Your missing side is{c}")

    again = input("Would you like to enter another triangle?(Y/N) ")
print ("Thank you for using the Pythangrean Calculator")