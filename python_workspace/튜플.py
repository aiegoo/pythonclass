#튜플.py

a = (1,2,3)
print(type(a))
print(a)

a,b,c = (1,2,3)
print(type(a))
print(a)
print(b)
print(c)

a=10
b=7 

"""
temp = a
a = b
b = temp 
"""
a,b = b, a 
print("a=", a)
print("b=", b)

#함수는 반환값이 하나만 있다 
def myfunc(a,b,c):
    a = a*2
    b = b*2 
    c = c*2
    return (a,b,c)

x,y,z = myfunc(10,20,30)
print(x,y,z) 
