class university:
    def exams(self):
        print("exams")
    def syllabus(self):
        print("syllabus")  
class college(university):
    def library(self):
        print("libraries")
    def staff(self):
        print("staff")   
class students(college):
    def uniform(self):
        print("uniform")        
                   
                   
student1=students()
student1.syllabus()
student2=college()
student2.library()
student3=university()
student3.exams()