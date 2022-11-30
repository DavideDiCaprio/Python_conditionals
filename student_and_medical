'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
Percentage of class attended
Is student is allowed to sit in exam or not.'''

def student_attendence():
    held = int(input("enter classes held "))
    attended = int(input("enter classes attended "))
    attendence = (attended * held)/100
    
    if attendence < 75 :
        print("not allowed ")
    else :
        print("allowed")
        
'''Modify the above question to allow student to sit if he/she has medical cause. 
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.'''

def medical_cause():
    held = int(input("enter classes held "))
    attended = int(input("enter classes attended "))
    attendence = (attended * held)/100
    
    if attendence < 75 :
        print("not allowed, you have a medical cause?")
        medical_cause = input("print 'Y' or 'N' :")
        
        if medical_cause == "Y" :
            print("allowed")
            
        elif medical_cause == "N":
            print("not allowed")
    
    else :
        print("allowed")
