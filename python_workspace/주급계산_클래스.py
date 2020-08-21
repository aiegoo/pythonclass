class WeekPay:
    name="홍길동"
    work_time = 40
    per_pay = 10000
    def process(self):
        self.pay = self.work_time * self.per_pay 
    def output(self):
        print(self.name, self.pay)
    def Input(self):
        self.name = input("이름 : ")
        self.work_time = int(input("근무시간 "))
        self.per_pay = int(input("시간당 급여액"))

wp = WeekPay()
wp.Input()
wp.process()
wp.output()




