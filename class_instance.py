class ElderBrother:  #parent class/base class/ super class
    salary=10000

class Ram(ElderBrother):  #child class/derived class/sub class
    pocket=500    
    def ramInfo(self): #child(parent class)
            print("ram function",self.pocket,self.salary)
r1=Ram()
print(r1.salary,r1.pocket)


     