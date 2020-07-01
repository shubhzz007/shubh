class person:
#    def __init__(self):
    pay = int(input("enter the salary :"))
    first = input("Enter first name :")
    last = input("enter the last name :")
    email = input("enter the email :")


    def full_name(self):
        print("full name is :")
        print(self.first + self.last)

e = person()
e.full_name()