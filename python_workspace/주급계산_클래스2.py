class WeekPay:
    name="홍길동"
    week_time=40
    per_pay=10000
    def setValue(self, name, week_time, per_pay):
        self.name = name 
        self.week_time=week_time 
        self.per_pay = per_pay 
    #생성자 - 객체가 생성될때 자동으로 호출된다. 
    #시스템이 호출자라 이름이 정해져 있다 
    #__init__(self) 정해져 
    #한개만(파이썬 오버로딩 지원안한다)
    def __init__(self, name="", 
           week_time=0, per_pay=0):
        self.name = name
        self.week_time=week_time
        self.per_pay = per_pay 
    def output(self):
        print(self.name , self.week_time, 
        self.per_pay)  

work1 = WeekPay("김영아", 50, 2000)
work1.output()

wList = [WeekPay("a", 40, 10000), 
         WeekPay("b", 20, 30000),
         WeekPay("c", 50, 15000)]

for work in wList:
    work.output()          

