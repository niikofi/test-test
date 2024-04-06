print("Welcome to Nii Kofi's Grading System")
print("You can check your grades here")

scores = 45
if scores >= 90:
    print ("A")
    print("excellent")
elif scores <= 89 and scores >= 80:
    print("B")
    print("Very Good")
elif scores <= 79 and scores >= 70:
    print("C")
    print("Good") 
elif scores <= 69 and scores >= 60:
    print ("D") 
    print ("Credit") 
elif scores <= 59 and scores >= 50:
    print ("E")
    print ("Pass")
else:
    print("F")
    print("Fail")       

