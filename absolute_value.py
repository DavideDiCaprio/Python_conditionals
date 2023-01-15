'''Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1'''

def absolute_value():
    number = int(input("enter number:" ))
    print(abs(number))

#con i condizionali 

def absolute_value():
    number = int(input("enter number:" ))

    if number < 0:
        print(number * (-1))
    else :
        print(number)
