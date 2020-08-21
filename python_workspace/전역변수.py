"""
전역변수 -함수들이 같이 쓸 수 있는 공유변수 
지역변수 -함수내부에 선언되는 모든 변수들
         함수 사용이 종료하면 사라진다. 
"""
x = 10 
def myfunc1():
    global x
    print(id(x))
    x = x+5
    #UnboundLocalError: local variable 'x' referenced before assignment
    return x

print(id(x))
print("함수호출 후 ")
print (myfunc1())

