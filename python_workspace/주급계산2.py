#주급계산2.py

#4개의 list 
nameList=list()
workList=list()
perpayList=list()
payList=[]

for i in range(1,4):
    name = input("이름 : ")
    work_time = int(input("근무시간 : "))
    perpay = int(input("시간당급여액 : "))
    nameList.append(name)
    workList.append(work_time)
    perpayList.append( perpay )

for i in range(0, len(nameList)):
    pay = workList[i] * perpayList[i]
    payList.append(pay) 

totalPay = 0 
for i in range(0, len(payList)):
    totalPay = totalPay + payList[i]

print("이름\t근무시간\t시간당급여액\t급여")
print("-"*100)
for i in range(0, len(nameList)):
    print(nameList[i], end='\t')
    print(workList[i], end='\t')
    print(perpayList[i], end='\t')
    print(payList[i])
print("총지급액 : ", totalPay)
    
    
