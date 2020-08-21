class Parent:
    def funcationA(self):
        print("----- A ------")
    def funcationB(self):
        print("----- B ------")
    def funcationC(self):
        print("----- C ------")
    def process(self):
        self.funcationA()
        self.funcationB() #다시 만들어써라
        self.funcationC()

class Child(Parent):
    def funcationB(self):
        print("-------------")
        print("@@@@@@@@@@@@@")
        print("-------------")

c = Child() 
c.process()