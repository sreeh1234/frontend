print("RESULT")
n=str(input("Enter your Name"))
scr=float(input("Enter Your Score"))
if scr<=100 and scr>=90:
    print("Excellent\n your score is",scr," grade is A you Passed")
elif scr<=89 and scr>=80:
    print("Good\n your score is",scr," grade is B you Passed")
elif scr<=79 and scr>=70:
    print("Satisfactory\n your score is",scr,"grade is C you Passed")
elif scr<=69 and scr>=60:
    print("Needs Improvement\n your score is",scr,"grade is D you Passed")
elif scr<=59 and scr>=0:
    print("Needs Improvement\n your score is",scr,"grade is F you Failed")
else:
    print("Please enter a valid score between 0 and 100")    