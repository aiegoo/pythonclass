class Person:
    def __init__(self, name="홍길동", 
                phoneNumber="010-0000-0000"):
        self.name = name
        self.phoneNumber = phoneNumber 
        print("Person 생성자")

    def printInfo(self):
        print("--- Person printInfo---")
        print(self.name, self.phoneNumber)

    def callPrint(self):
        self.printInfo()

    def getName(self):
        return self.name 
    
    def getPhoneNumber(self):
        return self.phoneNumber

class Student(Person):
    def __init__(self, name="학생", 
        phoneNumber="010-1111-1111",
        subject="컴퓨터과학과", 
        studentID="111111"):
        print("Student 생성자")

        #부모생성자 강제호출하기 
        Person.__init__(self, name, phoneNumber)

        #self.name = name
        #self.phoneNumber = phoneNumber
        self.subject=subject 
        self.studentID=studentID
 
    #부모메서드인 printInfo 메서드를 재정의한다 
    def printInfo(self):
        print("-----------------")
        print(self.name)
        print(self.phoneNumber)
        print(self.subject)
        print(self.studentID)
        
p, s = Person(), Student()

#각자 자기 객체꺼 호출한다 
p.callPrint() #Person 클래스의 printInfo 함수 호출
#---- printinfo호출하기 
s.callPrint() #Student 클래스의 printInfo함수호출
s2 = Student()
print( s2.getName() )
print( s2.getPhoneNumber())



