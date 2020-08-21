class Person:
    def __init__(self, name="홍길동", age=24):
        self.name = name 
        self.age = age 

    def print(self):
        print(self.name, self.age)

    #== 비교연산자 : 서로 같은 객체를 참조중인가?
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
           return True 
        else:
           return False

    def __str__(self):
        return "{} {}".format(self.name, self.age)

p1 = Person() 
p2 = Person()
if p1 == p2:
    print("둘이 같다")
else:
    print("둘이 다르다")
print ( p1 )
    
