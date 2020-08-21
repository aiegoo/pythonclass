#mylist.py 

class Node:
    def __init__(self, data=""):
        self.data = data
        self.next = None #다음번 요소 없음 
    #생성자만 있어도 변수 만들어진다. 

class MyList:
    def __init__(self):
        self.head = Node() 
        self.tail = Node() 
        self.head.next = self.tail 
        self.tail.next= self.tail   

        # head->() -> () -> tail 

    #head ->() -> A -> B -> C -> ()-> tail 
    """
    1.처음에 데이터 한건도 없을때 
    2.중간에 끼워넣을때 
    3.맨앞에 끼워넣을때
    4.맨뒤에 끼워넣을때 
    """
    def insertHead(self, data):
        #1.새로운 데이터 들어오면 Node객체 추가, 객체 
        #에 데이터 전달
        newNode = Node(data)
        #2.head.next 가 newNode를 가르키도록 해야한다 
        newNode.next = self.head.next 
        self.head.next = newNode

    def print(self):
        #시작->다음번노드-> 끝날때까지
        start = self.head.next 
        while(start!=self.tail):
            print( start.data )
            #다음번 요소로 이동하기 
            start = start.next 

    def append(self, data=""):
        trace1 = self.head.next 
        trace2 = self.head #한발짝뒤에서 
        while( trace1!=self.tail): #맨뒤쪽 추적 
            trace1 = trace1.next 
            trace2 = trace2.next 
        
        newNode = Node(data)
        newNode.next = self.tail 
        trace2.next = newNode 
        
        

m = MyList()
m.append("A")
m.append("B")
m.append("C")
m.append("D")
m.append("E")
m.print()

m2 = MyList()
m2.append(1)
m2.append(2)
m2.append(3)
m2.print() 


    
        
        