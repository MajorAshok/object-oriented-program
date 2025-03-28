# Creating Class and accessing it 
#1. class classname:
#2.   variable
#3.  methode 
#4. object=classname()
#5. object.var    
# Example
class A:
    x=1
    y=2
    def Add(self,x,y):
        print(x+y)
obj1=A()
obj1.Add(5,7)

   



# 01.Calculator 
class calculator:
    def Add(self,a,b):
        print(a+b)
    def Subtract(self,a,b):
        print(a-b)
    def Devision(self,a,b):
        print(a/b)
    def multiplication(self,a,b):
        print(a*b)
calculate=calculator()
calculate.Add(2,3)
calculate.Subtract(4,6)            
calculate.Devision(4,8)
calculate.multiplication(6,8)

# Storing class object in variable 
class A :
    def Add(self,a,b):
        return(a+b)
obj=A()
c=obj.Add(int(input("No.1 ")),int(input("No.2 ")))
print(c)

# Que; Write a program to calculate the following formula: F=a**2+b**2+2*a*b
class formula:
    def calcu(self,a,b):
        return(a**2+b**2+2*a*b)
obj=formula()
FORMULA=obj.calcu(int(input("No.1 ")),int(input("No.2 ")))
print(FORMULA)

#02. Calculating simple intrest ;
class Account:
    def account(self,p,r,t):
        SI=p*r*t/100
        print(f'Simple intrest is:{SI}') 
obj=Account()
obj.account(10000,0.4,2)

#03. Calculating Parimeter and area :
class rectangle :
    def area(self,length,width):
        Area=length*width
        print(f'Area of Rectangle: {Area}')
    def peri(self,length,width):
        perimeter=2*(length+width)
        print(f'Perimeter of rectangle: {perimeter}')
obj=rectangle()
calculation=obj.area(int(input("Enter length: ")),int(input("Enter width: ")))
print(calculation)

