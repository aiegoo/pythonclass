"""
dataList = [
    {"name":"홍길동", "phone":"010-0000-0000"},
    {"name":"고길동", "phone":"010-0000-0000"},
    {"name":"길창덕", "phone":"010-0000-0000"},   
]

#list 타입에 요소로 dict타입이 
for data in dataList:
    print( data['name'], data['phone'])
"""

dataList =[] #리스트 객체 만들기 
count = int(input("몇명?"))
for i in range(0, count):
    data = dict()
    data['name'] = input("이름 : ")
    data['work_time'] = int(input("근무시간 : "))
    data['per_pay'] = int(input('시간당급여액 :'))
    dataList.append( data )

#print(dataList)

for data in dataList:
    data['pay'] = data['work_time'] * data['per_pay']

for data in dataList:
    print(data)
