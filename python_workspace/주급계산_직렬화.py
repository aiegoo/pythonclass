import pickle 

class WeekPayData:
    name=""
    week_time=0
    per_pay=0
    payment=0
    #생성자 
    def __init__(self, name="", week_time=0, 
              per_pay=0):
        self.name = name 
        self.week_time = week_time 
        self.per_pay = per_pay 

    def process(self):
        self.payment= self.week_time * self.per_pay
    
    def print(self):
        print(self.name, self.per_pay, 
              self.week_time, self.payment)


class WeekPayMgr:
    dataList = list()

    def __init__(self):
        # self.dataList.append(
        #     WeekPayData("Tonylee", 40, 10000))
        # self.dataList.append(
        #     WeekPayData("Ruhulamin", 40, 40000))
        # self.dataList.append(
        #     WeekPayData("James", 30, 15000))
        self.load()
        
    def output(self):
        for item in self.dataList:
            item.process() 
            item.print() 

    def menuDisplay(self):
        print("1.Add")
        print("2.Print")
        print("3.Beautify")
        print("4.Import")
        print("5.Save")
        print("0.Exit")
        
    def start(self):
        while(True):
            self.menuDisplay()
            sel = input("Select : ")
            if sel=="1":
                self.append() 
            elif sel=="2":
                self.output()
            elif sel=="3":
                self.sort()
            elif sel=="4":
                self.load()
            elif sel=="5":
                self.save()
            else:
                break

    def append(self):
        data = WeekPayData()#새로운객체만들고 
        data.name=input("Name : ")
        data.week_time=int(input("Work Hours : "))
        data.per_pay=int(input("Hourly Wage"))
        
        self.dataList.append(data)

    def sort(self):
        tempList = sorted(self.dataList, 
            key=lambda data:data.name)
        for item in tempList:
            item.process()
            item.print()

    def load(self):
        try:
            f = open("Weeklypay.bin", "rb")
            self.dataList = pickle.load(f)
            f.close()
        except IOError:
            print("DB entry yet to be made")

    def save(self):
        f = open("주급.bin", "wb")
        pickle.dump(self.dataList, f)
        f.close()

mgr = WeekPayMgr()
mgr.start()

