class Person:
    pass

class Bird:
    pass 

class Student(Person): #Person클래스 상속
    pass

p, s = Person(), Student() 
print( isinstance(p, Person))#True
print( isinstance(s, Person)) #True
print( isinstance(s, Student)) #True
print( isinstance(p, Student)) #False
#Student 클래스는 Person 클래스의 자식이다. 
#Student 클래스는 Person의 일종이다 - O
#Person 클래스는 Student의 일종이라 X 
print(isinstance(p, Bird)) #False
print(isinstance(p, object)) #True
print(isinstance(int, object)) #True

"""
object 를 상속받습니다. 
모든 타입이 object를 상속받는다 

list 타입-파이썬 
a = [Person(), Person(), Person()]
b = [Bird(), Bird(), Bird()]
c = [Student(), Student(), Student()]
d = [object(), object(), object()]

a = Person()  나한테 하나 연결되어있다
b = a         두개째 연결되었다 
b = Student() -1
a = Bird()
"""


