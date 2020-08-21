#클래스의 정의 
class Person:
    name="홍길동"
    age=18 
    def Print(self):
        print(self.name, self.age)
#객체, 인스턴스를 만듦
p1 = Person()
print(p1.name, p1.age)
p1.Print()

#멤버들을 클래스명으로 접근 가능하다. 
print(Person.name, Person.age)
Person.phone = "010-0000-0000"

print(p1.phone)


