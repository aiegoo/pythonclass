"""
이름, 근무시간, 시간당급여액, 총액, 수당, 세금 
"""
dataList = list() #전역변수로 씀 

def append(dataList):
     
    while(True):
        temp = dict() #dict타입 객체 만들고 
        temp['name']=input("이름 : ")
        temp['worktime']=int(input("근무시간 : "))
        temp['perpay']=int(input("시간당급여액 : "))

        dataList.append(temp)
        again = input("계속?1.yes 2.no")
        if again!="1":
            break 

def output(dataList):   
    for data in dataList:
        print(data['name'], end='\t')
        print(data['worktime'], end='\t')
        print(data['perpay'], end='\t')
        print(data['pay'], end='\n')
        
def process(dataList): 
    for data in dataList:
        data['pay']= data['worktime'] * data['perpay']

def start(dataList):
    while(True):
        print("1.추가")
        print("2.출력")
        print("0.종료")
        menu = input("선택 : ")
        if menu=="1":
            append(dataList)
        elif menu=="2":
            process(dataList)
            output(dataList)
        else:
            print("프로그램을 종료합니다.")
            return

#테스트용 
#append()
#output() 
start(dataList)


