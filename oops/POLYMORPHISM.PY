# class bank:
#     def __init__(self):
#         print('''
#         SBI
#         branch:ekm
#         ifsc:sbi00002
#         location:mg road ekm      
#         ''')
#     def depo(self):
#         print('amt added')

# class users(bank):
#     def __init__(self):
#         super().__init__()
#         self.name=input("name")
#         self.email=input("email")     
#     def user_dtls(self):
#         print(self.name,self.email)     
        
# manu=users()             


from abc import ABC,abstractmethod

class clg(ABC):
    @abstractmethod
    def register(self):
        print('reg')
    def class_rooms(self):
        print('class rooms')    
    def ground(self):
        print("ground")    

class std(clg):
    def register(self):
        name=input(" enter name")     
        phno=input("enter phno")
        email=input("enter email")
    def notes(self):
        print("notes in std")    
        
class staff(clg):
    def register(self):
        name=input(" enter name")     
        exp=input("enter exp")
        sub=input("enter sub")
    def exam_papers(self):
        print("exam papers")    
        
std1=std()
std1.register()

s1=staff()
s1.register()
        
                  