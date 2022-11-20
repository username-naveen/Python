# multi-level inheritance

# class a:
#     def __init__(self, name_a):
#         self.name_a = name_a
        
# class b(a):
#     def __init__(self, name_b, name_a):
#         self.name_b = name_b
#         a.__init__(self,name_a)

# class c(b):
#     def __init__(self, name_c, name_b, name_a):
#         self.name_c = name_c
#         b.__init__(self,name_b, name_a)
        
        
# x = c('nav', 'har', 'anj')
# print(x.name_a)

# hierarchical inheritance

# Base class
class A:
     def a_func(self):
         print("I am from the parent class.")

# 1st Derived class
class B(A):
     def b_func(self):
         print("I am from the first child.")

# 2nd Derived class
class C(A):
     def c_func(self):
         print("I am from the second child.")
 
# Driver's code
obj1 = B()
obj2 = C()
print(obj1.a_func())
print(obj1.b_func())    #child 1 method
print(obj2.a_func())
print(obj2.c_func())  