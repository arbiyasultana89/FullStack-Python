# class student:
#     name="Arbiya"
#     def study(self):
#         print("Arbiya is studying")
# s1 = student()
# print(s1.name)
# s1.study()


# class student():
#     def details(self):
#         print("Had breakfast")
# s1 = student()
# s1.details()

# student.details(s1)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1=student("Arbiya",20)
# s2=student("sara",23)
# s3=student("ram",25)
# print(s1.name,s2.name,s3.name)
# print(s1.age,s2.age,s3.age)


# class bank:
#     def __init__(self,balance):
#         self.balance = balance

#         def check_balance(self):
#             print(self.balance)

# account = bank(5000)
# account.check_balance()

# class user:
#     def __init__(self,name):
#         self.name = name

#     def login(self):
#         print(self.name,"logged in")

# u1=user("raj")
# u2=user("sara")
# u1.login()
# u2.login()


# class Animal:
#     def wild(self):
#          print("Wild Animal")

# class dog(Animal):
#      def domestic(self):
#         print("Dog is a domestic animal")
# s=dog()
# s.wild()
# s.domestic()


# class thatha:
#     def land(self):
#         print("thatha's land")


# class appa(thatha):
#     def house(self):
#         print("appa's land")


# class maga(appa):
#     def bike(self):
#         print("son has a bike")
# obj=maga()
# obj.land()
# obj.house()
# obj.bike()

# class father:
#     def property(self):
#         print("Father's land")
# class mother:
#     def property(self):
#         print("Mother's land")


# class son(father,mother):
#     def property(self):
#         print("son gets both mother's and fathers's property")

# s1=son()
# s1.house()
# s1.land()
# s1.property()


# class Father:
#     def land(self):
#         print("Father's land")


# class daughter(Father) :
#     def gift(self):
#         print("Father's gift")


# class son(Father):
#     def house(self):
#         print("Fathers's house")

# s1=son()
# s2=daughter()
# s1.land()
# s1.house()
# s2.land()
# s2.gift()


# class student:
#     def __init__(self,name):
#         self.name = name


#     def __str__(self):
#         return self.name

# s=student("Queen")
# print(s)

def login(func):
    def wrapper():
        print("checking login")
        func()
        return wrapper
#login
def dashboard():
    print("Dashboard page")
dashboard()


def login(func):
    def wrapper():
        print("Function ended")
        func()
    return wrapper

def hello():
    print("Hello python")
hello()

def hii():
    print("hii")
hii()

import json
student={
    "name":"jhon",
    "age":20
}
data=json.dumps(student)
print(data)










