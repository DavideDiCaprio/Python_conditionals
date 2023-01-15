'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

def grading():

    Marks = int(input("Enter marks:"))

    if Marks < 25 :
        print("F")
    elif Marks >= 25 and Marks <= 45:
        print("E")
    elif Marks >= 45 and Marks < 50:
        print("D")
    elif Marks >= 50 and Marks < 60:
        print("C")
    elif Marks >= 60 and Marks < 80:
        print("B")
    elif Marks >= 80 and Marks < 100:
        print("A")
    else :
        print("Wrong number")
