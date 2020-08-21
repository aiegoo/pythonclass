def times(a, b):
    return a*b

def times2(a, b):
    a = a*2
    b = b*2
    return a,b #파이썬은 - 알아서 tuple타입 반환으로 만든다 

print( times ) #괄호 없음 - 함수 호출한게 아니다 
print( times(4,5))

a=10
b=20
a, b = times2(a,b)
print(a, b)

a = times2
print( a(7, 9))

print( globals() )

print( dir(__builtins__))

print( sum([1,3,5,7,9]) )

def display():
    print("값 반환을 하지 않는 함수입니다.")
    #함수가 값을 반환하지 않으면 None 객체를 반환하도록 되어있다
print( display() ) 
