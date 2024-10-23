class college:
    def course(s):
        print("course")
    def staff(s):
        print("staff") 
class sports(college):
    def indoor(s):
        print("indoor")
    def outdoor(s):
        print("outdoor")
class arts(college):
    def drawing(s):
        print("drawing")
class cricket(sports):
    def c_tournament(s):
        print("c_tournament")
class football(sports):            
    def f_tournament(s):
        print("f_tournament")
        
        
        
std1=football()
std1.f_tournament()
std2=cricket()
std2.c_tournament()        
std3=sports()
std3.course()
std4=arts()
std4.staff()