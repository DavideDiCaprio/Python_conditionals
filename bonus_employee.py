'''Exercise:
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''


def deserves_bonus():
    print("enter year of service:")
    service = int(input())
    if service > 5 :
        print("enter your salary:")
        salary = int(input())
        bonus = salary * 0.05
        print(f"Your bonus is {bonus}")
    else:
        print("You dont'deserve a bonus")


deserves_bonus()
