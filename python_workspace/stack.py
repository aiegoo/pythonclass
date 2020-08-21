#stack.py

class Stack:
    #변수들은 외부에서 접근못하게 전부 private 권한으로 
    __MAX=5 #스택의 최대크기 __  이 변수가 private 라서 
            #클래스 외부에서 접근 불가 
    __buffer=list()
    __top=-1  #가장 최신데이터의 index를 갖고 있는 변수 
            #-1이면 stack empty 상황을 얘기한다 
    def __init__(self):
        for i in range(0, self.__MAX):
            self.__buffer.append("")

    def isFull(self):      #스택이 꽉차면 True 
        if self.__top == self.__MAX-1:
            return True
        else:
            return False 
    
    def isEmpty(self): #스택이 empty이면 True아니면 False
        if self.__top == -1:
            return True 
        else:
            return False 

    def push(self, data): #스택에 데이터 넣기 
        if (self.isFull()):
            print("Stack overflow")
            return 
        self.__top += 1
        self.__buffer[ self.__top ] = data 

    def pop(self): #스택에서 데이터 하나 제거 
        if self.isEmpty():
            print("Stack underflow")
            return None 
        r = self.__buffer[self.__top]
        self.__top -= 1
        return r 

    def peek(self): #스택의 최상위 데이터 확인용 함수 
        if self.isEmpty():
            print("Stack underflow")
            return None 
        r = self.__buffer[self.__top]
        return r 
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.push("F")

while(not s.isEmpty()):
    print( s.pop() )




