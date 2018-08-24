'''
Created on Jun 18, 2018

@author: kripa
'''
'''first_name = "Rohit"
print("first_name")
print('first_name')
print(first_name)

#var_1-2 = 900
#$_var = 1300
var_124 = 9000
print(var_124)
#A_B_^4 = 505
_NAME = 'RAHUL'
print(_NAME)
_name = "rohit"
print(_name)
____ = 600
print(____)
name = "ram"
print(name)
'''

'''num = -2
print(type(num))
var1 = 7.8
print(type(var1))
var2 = 2+9j
print(type(var2))
'''
'''num1 = 34
num2 = 12.6
result = num1 * num2
print(type(result))
print(result)
num3 = 2+3j
data = num1 + num3
print(type(data))
print(data)
num4 = 8j
data1 = data + num4
print(data1)
expr = [(6*5)+4-(8/2)*9]
print(expr)
'''
'''import math
print(math.factorial(41))
print(math.fabs(6.5000))
print(math.log(5))
print(math.log10(2))
r = 10
print(2*math.pi*r)
print(math.pi)
print(2*3.141*r)
print(math.sqrt(16))
#print(math.sqrt(-9))
import cmath
print(cmath.sqrt(-9))
'''


'''name = 'rohan123'
print(type(name))
address = "blr"
print(type(address))
'''
para = " *Author: W3layouts \
Author URL: http://w3layouts.com \
License: Creative Commons Attribution 3.0 Unported \
License URL: http://creativecommons.org/licenses/by/3.0/"
'''print(para)



print(name[2])
print(name[-1])
#print(name[8])
print(len(name))
'''

#para = "ram goes to market."
'''print(len(para))
print(para[1:6])
print(para[:6])
print(para[2:])
print(para[:])
print(para[-16:-4])
print(para[::-1])
'''
#print(para[1:6][1:4])

'''first_name = "rohan"
last_name = "mohan"
result = first_name / last_name
print(result)'''
'''
num = 123
data = result + str(num)
print(data)'''

'''name = "rohan"
data = name*(-4)
print(data)'''

'''data1 = data*'hi'
print(data1)'''

'''name = "rohithhhhhhhhhhh"
print(name.capitalize())
print(name.count('h'))
print(name.find('ro'))
print(name.index('t'))
'''
'''
l1 = [1,2,3,'a','b','c']
print(type(l1))
print(l1[-2])
print(len(l1)) 
'''
'''name = 'rohan'
print(name.join('abcd'))
'''
'''l1 = [1,2,3,4,5,'a','b','c']
print(l1[-6:-2])
print(l1[2:5])
print(l1[:])
print(l1[2:80])
l2 = l1
print(l2)
l2[1] = 1000
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l3 = l1[:]
print(l3)
print(id(l3))
l3[1] = 4000
print(l3)
print(l1)
print(l1[::-1])
'''
'''l1 = [1,2,3,4,5,'a','b','c']
l1.append(123)
print(l1)
l1.append('e')
print(l1)
l2 = [100,200,300,'hello']
l1.append(l2)
print(l1)
print(l1[10][3][1])
'''
'''l1  = [1,2,3,4]
l2 = [5,6,7]
l3 = []
l4 = []
l3.append(l1)
print(l3)
print(len(l3))
l3.append(l2)
print(l3)
print(len(l3))
l4.extend(l1)
print(l4)
print(len(l4))
l4.extend(l2)
print(l4)
print(len(l4))
'''
'''l1 = [1,2,3,4]
l2 = [5,6,7]
l3 = l1 + l2 
print(l3)
l3.extend('hello')
print(l3)
l3.extend(123)
print(l3)
'''
'''l1 = [1,2,3,4]
l2 = [5,6,7]
l3 = l1*4 
print(l3)
'''
'''l1 = [1,2,3,4,'delhi',5,6,2,4,4,4,4]
print(l1.count(40))
var = l1.index(4, )
var1 = l1[var+1:].index(4,)
print(var + var1+1)
'''
'''l1 = [1,2,3,4,'delhi',5,6,2,4,4,4,4]
l1.insert(1, 1000)
print(l1)
l1[2] = 700
print(l1)
l1.pop()
print(l1)
l1.pop(3)
print(l1)
'''
'''t1 = ()
print(id(t1))
print(type(t1))
t1 = (1,2,3,'india','army',3,3)
print(id(t1))
#t1[1] = 6000
l1 = [1,2,3,'india','army']
l1[1] = 6000
print(l1)
l2 = []
print(id(l2))
l2= [200,300]
print(id(l2))

print(t1.count(300))
print(t1.index('army', ))
print( 'army' in t1)
'''
'''name = 'rohan'
var = name.replace('h', 'kl')
print(name)
print(var)
l1  = ['r','o','h','a','n']
l1.insert(2, 'kl')
print(l1)
name[2] = 'kl'
'''
'''t1 = (1,2,3,4)
t2 = (100,200,300)
result = t1 + t2
print(result)
print(t1*4)
print(t1/2)'''

'''data = t1 - t2
print(data)'''

'''d1 = {}
print(type(d1))
d2 = dict()
print(type(d2))


d1 = {'name':'rohan',
      'age':40,
      'address':'blr'
      }
print(len(d1))
print(d1)
print(d1['name'])
d1['salary'] = 70000
print(d1)
'''
'''info = {300:'a',
        'name':'b',
        (4,5,6):'d',
        }
print(info)
'''
'''info = {'age':45,
        'name':'rohan',
        'phone_number':[1233,3444],
        'address':('bsr','blr'),
        'emp_data':{'salary':20000}
        }
print(info)
print(info['phone_number'][1])
print(info['emp_data']['salary'])
'''
'''emp_info = {'101':{'name':'rohan',
                                'age':40,
                                'salary':10000
                   }}
print(len(emp_info))
print(len(emp_info['101']))
emp_info['102'] = {'name':'rohan',
                                'age':45,
                                'salary':20000
                   }
print(emp_info)
emp_info['101']['address'] = 'blr'
print(emp_info)
'''

d1 = {'name':'rohit','address':'blr'}
d2 = {'age':20}
'''
result = d1*2
print(result)
'''
'''d1.clear()
print(d1)
'''
'''print(d1.get('name'))
print(d1.get('age'))
print(d1['name'])
print(d1['age'])
'''
'''print(d1.has_key('name'))
print(d1.has_key('age'))
print('name' in d1)
print('age' in d1)
'''
'''print(d1.keys())
print(d1.values())
'''
'''S1 = set()
print(type(S1))
S2 = set({1,2,3})
print(type(S2))

U = set({1,2,3,4,5,6,7,8,9,10,11,12})
C = set({1,2,3,4,5})
B = set({6,7,8,4})
H = set({4,5,10,11})

print(C.intersection(B))
print(C.intersection(H))
print(H.intersection(B))

print(C.union(B))
print(B.union(H))

print(C - B)
print(U - B - H - C)

print(U.issuperset(C))
print(B.issuperset(C))

print(C.issubset(U))
'''
'''print(bool(100))
num  = 0
print(bool(num))
str1 = "rohan"
print(bool(str1))
str2 = ''
print(bool(str2))
l1 = []
print(bool(l1))
l2 = [1,2,3,4]
print(bool(l2))
t1 = ()
print(bool(t1))
t = (100,200,300)
print(bool(t))
d1 = {}
print(bool(d1))
d2 = {'name':'rohan'}
print(bool(d2))
'''

'''num = int(input("enter any number:"))

if num == (9+1)*10:
    print("yes")
print("Bye")
'''

'''uname = input("enter your username:")
if uname == "rohit":
    print("valid user!")
else:
    print("invalid user!")
'''

'''marks = 7

if marks <=100 and marks >= 80:
    print("Grade is A")
elif marks<=79 and marks >= 70:
    print("grade is A")
elif marks <=69 and marks >= 60:
    print("grade C")
else:
    print("Fail")
'''

'''l1 = [1,2,3]
if bool(l1):
    print("data is available!")


if 90:
    print("hello")

if True:
    print("ok")'''

'''num = 10
while num > 5:
    print("welcome india!")
    print(num)
    num = num -1

var = 1
while var < 250:
    if var %2 == 0:
        print(var)
    var = var +1'''
'''index = 0
name = "rohan"
l1 = []
while index < len(name):
    print(name[index])
    l1.append(name[index])
    print(l1)
    index = index + 1
print(l1)
    '''
'''
l1 = [1,2,3,4,5]
index =  0
while index  < len(l1):
    print(l1[index])
    index +=1
'''
"""l1 = []
name = 'rohan'
for i in name:
    print(i)
    print(type(i))
    l1.append(i)
    print(l1)
print(l1)
"""
'''my_list = [1,2,3,4,'hi','hello']
for var in my_list:
    print(var)
    print(type(var))
'''

'''my_tup = (100,200,300)
t1 = []
for i in my_tup:
    print(i)
    t1.append(i+10)
''''''t1 = tuple(t1)
print(t1)
print(type(t1))
'''
'''print(tuple(t1))
print(type(t1))
'''

'''info = {'name':'rohan',
        'age':45,
        'address':'blr'}
print(info.keys())
l1 = []
print(info.values())
l2 = []
for i in info:
    l1.append(i)
    l2.append(info[i])
print(l1)
print(l2)
'''

'''my_list = [['a','b','c','d'],
           ['e','f','g','h'],
           ['i','j','k','l']]

for i in my_list:
    print(i)
    for j in i:
        print(j)
'''

l1 = [100,200,'a','b','c',4,7,3,9]
#new_list = [0,1,2,3,4]
#new_list = [0,2,4]
'''new_list = []
i = 0
while i < len(l1):
    new_list.append(i)
    i +=1'''
'''new_list = range(len(l1))
print(new_list)
for i in new_list:
    print(l1[i])
print(range(2,40,5))
print(range(1,5))


for i in range(0,len(l1),2):
    print(l1[i])
'''
'''
name = "rohan" 

for i in range(len(name)):
    print(name[i])

t1 = (300,5,3,5,1)

for i in range(len(t1)):
    print(t1[i])
    
info = {'name':'rohan',
        'age':56,
        'address':'blr'}

'''
'''l1 = [1,2,3,4,5,6,7,8,9]
result=[]
for i in l1:
    var = 1
    temp = []
    while var <=10:
        temp.append(i*var)
        var +=1
    result.append(temp)
print(result)'''

'''l1 = [1,2,3.5,4.9,5.6]
result = map(int, l1)
print(result)
def f1(var):
    print(var)
map(f1,l1)

l2 = [200,300,400,500]
result = zip(l1,l2)
print(result)

def f2(var):
    return var>4
l1 = [1,2,3,4,5,6,7,8,9]
result=filter(f2, l1)
print(result)
'''
'''l1 = [1,2,3,4,5]
result = [i*i for i in l1]
print(result)'''

'''i = 1
while i <=10:
    print("block1")
    i +=1
    continue
    print("block2")
''''''for i in range(10):
    print(i)
    if i ==3:
        break
'''
'''
i = 90
if i ==100:
    pass
while i <=100:
    var = 1
    print(var)
    i +=5
    var = var +10
    print(var)
print(i)
'''
'''result = []
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[10,11,12],[13,14,15],[16,17,18]]
for i in range(len(a)):
    print(a[i])
    temp = []
    for j in range(len(a[i])):
        print(a[i][j]+b[i][j])
        temp.append(a[i][j]+b[i][j])
    result.append(temp)
print(result)
'''
'''def print_msg(msg):
    print(msg)
    print(id(msg))
    print("hello india!")
''''''print_msg()
print_msg()
print_msg()
print_msg()
print_msg()
'''
'''print_msg('hi')

name  = 'rahul'
print(id(name))
print_msg(name)
'''
'''def add(a,b):
    c = a + b
    print(c)
add(4,7)
'''    
'''    
def add(var1,var2):
    return var1+var2

result = add
print(add)
print(result)
print(result(34, 56))
data = add(62, 78)
print(data)

data1 = result(23, 30)
print(data1)
'''
'''print(num)
def f1():
    global num
    num = 800
    print(num)
  
def f2():
    print(num)
f1()  
f2()
'''
'''def modify_data(var):
    print(var)
    var = 1000
    print(var)
    
num = 9000
modify_data(num)
'''
'''l1 = [1,2,3,4]
def modify_data(var):
    print(var)
    var[2] = 1000
    print(var)
    
def set_data(var):
    print(var)

modify_data(l1)
set_data(l1)
'''
'''def emp_info(name,salary,age=0,dpt='emp'):
    print(name)
    print(age)
    print(salary)
    print(dpt)
    
emp_info('raju', 23, 10000, 'security')
emp_info('ram', 34, 23000)
emp_info(age=56, name='rohit', salary=10000, dpt="it")
'''
'''
def f1(var):
    print(var)
    print("this is f1 function.")
    if var == 8:
        return 0
    else:
        var = var +1
    f1(var)
f1(4)    

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
result = fact(5)
print(result)

def a_p(var):
    if var == 1:
        return 1
    else:
        return var+a_p(var-5)
data = a_p(51)
print(data)
'''    
'''    
def outer_function(var1):
    var2 = var1 + 10
    def inner_function(num):
        return num*100
    data = inner_function(var1)
    return data
result = outer_function(15)
print(result)
'''
'''
class Fruit:
    pass

obj1 = Fruit()
obj2  = Fruit()
obj3 = Fruit()
obj1.var1 = 'sofa'
obj1.var2 = 'bed'
obj2.var3 = 'fan'
obj2.var4 = 'tv'
obj3.var5='window'
obj3.var6 = 'fridge'

print(obj1.var1)
print(obj1.var2)
print(obj3.var5)
print(obj3.var6)
print(obj2.var3)
print(obj2.var4)

obj4 = obj1
print(obj4.var1)
print(obj4)
print(obj1)

obj4.var2 = "light"
print(obj1.var2)

import copy
obj5=copy.copy(obj1)
print(obj1)
print(obj5)
print(obj5.var1)
print(obj5.var2)
obj5.var1 = "gate"
print(obj1.var1)
print(obj5.var1)
del obj1
del obj4
print(obj5.var1)
'''

'''class A:
    def __init__(self,var):
        print("object created!")
        print(var)
        
    def __del__(self):
        print("object deleted!")
        
obj = A(200)
obj1 = A(400)
del obj
obj3 = A(90)
obj4 = A(80)
'''

'''class Employee:
    def show_details(self,name,age,salary):
        print("name is {} , age is {} and salary is {}".format(name,age,salary))
    def add(self,a,b):
        return a+b
    def print_msg(var):
        print("welcome to india!")'''
'''obj = Employee()
obj.show_details('rahul', 20, 10000)
data = obj.add(50,60)
print(data)
obj.print_msg()'''
'''obj = Employee()
result  = Employee.add(obj,50,60)
print(result)
'''







'''class Fruits:
   @classmethod
    def print_msg(cls,name):
        print("this is a class method!")
'''    

'''Fruits.print_msg('rohit')
obj = Fruits()
obj.print_msg("rohan")
'''


'''class Fruits:
    @staticmethod
    def add(var1,var2):
        return var1+var2

result = Fruits.add(56,12)
print(result)
obj = Fruits()
result = obj.add(41, 12)
print(result)
'''
l1 = [100,200,[1,2,3],500]
'''l2 = l1
l2[1] = 3000
print(l1)
print(l2)
'''
'''import copy 
l2 = copy.copy(l1)
l2[1] = 3000
l2[2][1] = 4500
print(l1)
print(l2)

l3 = copy.deepcopy(l1)
l3[2][1] = 9000
print(l1)
print(l3)
'''
'''
class Employee:
    name = 'rohan'
    age = 30
    @classmethod
    def print_data(cls):
        print(Employee.name)
        print(Employee.age)
        
    def  show_data(self):
        print(self.name)    
print(Employee.name)
print(Employee.age)
Employee.print_data()

obj = Employee()
print(obj.name)
obj.show_data()
'''
'''class Fruits:
    def __init__(self):
        self.name = 'rohan'
    
    def show_data(self):
        print(self.name)    

obj = Fruits()
obj.show_data()
print(obj.name)
'''    
'''
class First:
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_data(self):
        print(self.name,self.age,self.salary)

obj = First('rahul',67,200000)
obj.get_data()
'''    
'''class First:
    address = 'blr'
print(First.address)
obj = First()
print(obj.address)
obj1 = First()
obj2 = First()
print(obj2.address)
print(obj1.address)
obj.address = "delhi"
print(obj.address)
print(obj1.address)
First.address = "Delhi"
print(obj1.address)
print(obj2.address)
'''
'''class A:
    name="a"
    def __init__(self):
        print("class A object created!")
    def a_m1(self):
        print("this method belongs to A class!")
        
class B(A):
    age = 45
    def __init__(self):
        A.__init__(self)
        print("class B object created!")
    def b_m1(self):
        print("this method belongs to B class!")

obj_B = B()
'''
'''obj_B =  B()
print(obj_B.age)
print(obj_B.name)
obj_B.a_m1()
obj_A = A()
print(obj_A.name)
print(obj_A.age)
'''
'''
class A:
    name = 'A'
    def __init__(self):
        print("const. of A!")
    def a_m1(self):
        print("Aclass method!")
class B(A):
    age = 45
    def __init__(self):
        A.__init__(self)
        print("const. of B!")
    def b_m1(self):
        print("Bclass method!")
class C(B):
    address = "blr"
    def __init__(self):
        B.__init__(self)
        print("const. of C!")
    def c_m1(self):
        print("Cclass method!")
class D(C):
    salary = 300000
    def __init__(self):
        C.__init__(self)
        print("const. of D!")
    def c_m1(self):
        print("D class method!")


obj_c = C()'''
#obj_a =A()
#obj_b = B()
#obj_c = C()
'''obj_d = D()
print(obj_d.name)
print(obj_d.age)
print(obj_d.address)
print(obj_d.salary)'''
#print(obj_c.salary)
'''class A:
    name = 'a'
    def __init__(self):
        print("const. of class A!")
    def a_m1(self):
        print("method belongs to A!")
    def m(self):
        print("A")
class B:
    age = 45
    def __init__(self):
        print("const. of class B!")
    def b_m1(self):
        print("method belongs to B!")
    def m(self):
        print("B")
class C:
    address = 'a'
    def __init__(self):
        print("const. of class C!")
    def c_m1(self):
        print("method belongs to C!")
    def m(self):
        print("C")
class D(B,A,C):
    salary = 450000
    def __init__(self):
        C.__init__(self)
        A.__init__(self)
        B.__init__(self)
        print("const. of class D!")
    def d_m1(self):
        print("method belongs to D!")
obj_d = D()
print(obj_d.name)
print(obj_d.age)
print(obj_d.address)
obj_d.m()

'''
"""
class A:
    pass
    '''def m(self):
        print("A")'''
class B:
    def m(self):
        print("B")
class C(A):
    pass
    '''def m(self):
        print("C")'''
class D(C,B):
    pass
    '''def m(self):
        print("D")'''
obj_d = D()
obj_d.m()
"""
'''class A:
    __name = "rohit"
    def get_name(self):
        return self.__name
    
obj = A()
print(obj.get_name())
'''
'''class First:
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

obj = First()
obj.set_name("rohan")
#print(obj.__name)
print(obj.get_name())
'''
'''class Fruits:
    def show_info(self,name,age,salary=0,address=None):
        print(name)
        print(age)
        print(salary)
        print(address)
        if salary == 0:
            print("give some money!")

obj = Fruits()
obj.show_info('rohit',45,30000,'blr')
obj.show_info('rohan',60,45000)
obj.show_info('mohan',30)
#obj.show_info('rahul')
obj.show_info(salary=8000,age=90,name='rahul',address='delhi')
'''
'''class one:
    def show_result(self,str1):
        index=0
        var=1
        result=" "
        while (index<len(str1)):
            result=result+str1[index]*var
            index=index+1
            var=var+1
        print(result)
        
obj=one()
obj.show_result("rahul")
obj.show_result("ram")
'''

'''class Fruits():
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name
    
    def __radd__(self,ins):
        return self.price + ins
        
obj = Fruits('apple',300)
print(obj)
obj1 = Fruits('mango',60)
print(obj1)
print( obj + obj1 )
obj2 = Fruits('banana',60)
print(sum([obj1,obj2,obj]))
print(sum([50,67,56,90]))
'''

'''def add_minirals(myfunc):
    def add_boost():
        print("boost added!")
        myfunc()
    return add_boost

@add_minirals
def make_boost():
    print("add milk")

make_boost()
'''
'''result = add_minirals(make_boost)
print(result)
result()
'''    





























    
            

































    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    










































    
    
    
    

    
    
    
    
    
    
    
    
    
    
    


























    
    
    
    
    
    
    
    
    
















    
    
    
    
    
    
    
    





















































   











































 










































































































