'''Ask user to enter age, sex ( M or F ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".'''

def employee():

    user_age,user_sex = int(input("Enter age:")),input("Enter sex:")

    if user_sex == "F":
        print("You will work only in urban areas")    
    
    elif user_sex == "M" :

        if user_age >= 20 and user_age < 40:
                print("You can work anywhere")
            
        elif user_age >40 and user_age <=60:
                print("You will work in urban areas only")

        else :
            if user_age <20:
                print("Too young")
                                   
    else :
        print("ERROR")
