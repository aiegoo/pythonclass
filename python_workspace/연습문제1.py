"""
name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))
total =kor + eng + mat 
avg = total/3 

print("{} {} {}".format(name, total, avg))
"""
print ( 13 % 2==0)

s ="881120-1068234"
print( s[:6], s[7:])
print(s[7])

a = "a:b:c:d"
b = a.replace(":", "#") #string-readonly 
print(b)

#파이썬은 모든 변수가 참조형태이다.
#대상을 직접 저장하지 않고 대상에 대한 주소(참조)를 저장한다. 

a = [1,3,5,4,2] 
b = a #데이터가 아니라 참조가 복사된다 .

a.sort()
a.reverse()
print("가공된값 : ", a)
print("원본 : ", b)
print( id(a), id(b))

print ( a is b)  #둘이 같은 객체를 참조하느냐 

print("하드카피이후")
b = a[:] #실제로 대상을 다시 만들어서 복사(하드카피)
print( id(a), id(b))
print ( a is b)  #둘이 같은 객체를 참조하느냐 

b[0] = 100
print(a, b)

#외부에서 파이썬 모듈을 들고올수있다
#패키지 - 라이브러리 묶음 
#from 패키지명 import 라이브명 
#특정패키지로부터 해당 라이브러만 메모리로 가지고 와라 
from copy import copy
a = [1,2,3,4,5]
b = copy(a)

a[0] = 10
print(a, b)

#join : 문자열 결합함수 

s2 = " ".join(['Life', 'is', 'too', 'short'])
print(s2)

s2 = ",".join(['Life', 'is', 'too', 'short'])
print(s2)

a = (1,2,3,4)
a = a+ (5,) 
#그냥 괄호만 하면 튜플인지 int 에 () 친건지 알수 없어서
print(a)

a={}
a['name'] = 'python'
a[('a','b')] = 'python'
#a[[1]] = 'python' -error
a[250] = 'python'
#키값에 - 튜플은 쓰지말자
#키값 - 상수만, 값이 변하는거 - 변수X 
#list객체-값변환이 되서 안되고, tuple은 readonly라서 된다. 
#별로 안중요 
print( a[('a', 'b')])

a = {'A':90, 'B':80, 'C':70}
print(a.pop('B')) #dictionary에서 키값 제거할때  



a = [1,2,3,4,5]
b = a
print( id(a), id(b))

