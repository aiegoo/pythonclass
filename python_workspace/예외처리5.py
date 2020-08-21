def myfunc(a, b):
    try:
        return a/b
    except TypeError as t:
        print(t.args[0])
    except Exception as e:
        print(e.args[0])

def add(a, b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요") 
    return a+b

def sub(a, b):
    assert type(a)==int and type(b)==int, "정수만 넣으세요"
    return a-b   

def mul(a, b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요")
    return a*b 

def div(a, b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요")
    if b == 0 :
        raise ZeroDivisionError("0으로 나눌수없습니다")
    return a/b 

try:
    print( add(4,4) )
    print( sub(4,"3") )
    print( mul(4,3) )
    print( div(4,0) )
except TypeError as e:
    print("type error", e.args[0])
except ZeroDivisionError as e2:
    print(e2.args[0])


