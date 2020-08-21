class MyClass:
    def __init__(self, value=""):
        self.value = value 
        print("객체 생성 ")
    def __del__(self):
        print("객체 소멸")

#함수를 부르면, 스택이라는 메모리공간에 필요로하는
#변수와 기타 코드들을 놓는데 함수사용이 종료하면 
#다 지워진다. 

def myfunc():
    m1 = MyClass("Hello") #지역변수, 함수호출될때 참조
    #가 시작되고, 함수 종료하면 참조가 없어진다.
    m2 = m1
myfunc() 
