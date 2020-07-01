#from array import *
class sandip:
    def inp(self):
    name = str(input("enter the name:"))
    salary = int(input("enter the salary :"))
    def get(self):
        print("name is :",self.name)
        print("salary is :",self.salary)
class company:
    empid = int(input("enter the employee id "))
    def get1(self1):
        print("the employee id is :",self1.empid)

s = sandip()
s1 = company()

for i in range(0,5):
    s.inp()

s.get()
s1.get1()