class CounterManager:
    __insCount=0 #변수앞에 __ 붙이면 접근권한이 
    #private 로 바뀐다. 외부에서 접근불가 

    def __init__(self):
        #self.insCount=self.insCount+1 
        #self가 붙은건 instance영역 이다 
        CounterManager.__insCount+=1 
        #클래스 영역의 변수 값을 증가시킨다 
    
    def staticPrintCount():
        print("현재 객체 숫자 ",
                CounterManager.__insCount)
    #위 함수를 static으로 쓰려면 반드시 등록을 해야
    SprintCount = staticmethod(staticPrintCount)

    #클래스메서드의경우 첫번째 인자로 클래스가 
    #전달된다. 
    def clsPrintCount(cls):
        print("현재 객체 숫자 ",
                cls.__insCount)

    ClsPrintCount = classmethod(clsPrintCount)

a=[CounterManager(), 
     CounterManager(), CounterManager()]
CounterManager.SprintCount()
a[0].SprintCount()

CounterManager.ClsPrintCount()
a[0].ClsPrintCount()

class Util:
    def isCapital(c):
        if ord('A')<=ord(c)<=ord('Z'):
            return True
        else:
            return False
    #전체문자열이 숫자로 구성되었는지 확인하기 
    def isDigit(s):
        for c in s:
            if ord('0')>ord(c) or ord(c)>ord('9'):
                return False 
        #for문을 다 빠져나오도록 return 이 
        #안되었다는 얘기는 다 숫자라는 
        return True 

    sPrint = staticmethod(isCapital)
    myIsDigit = staticmethod(isDigit)

print( Util.sPrint("A") )
print( Util.myIsDigit("1234"))
print( Util.myIsDigit("a1234"))

u = Util() 
print( u.sPrint("b")) 


