#함수를 정의했다 만들었다. 
def myfunc1():
    print('='*50)

def myfunc2(mark, cnt):
    print(mark*cnt)

myfunc2("*", 20)
myfunc2("!", 50)
myfunc2("@", 70)
myfunc2("~", 50)
myfunc2("9", 70)

myfunc1() #함수를 호출한다 
print("정보1")
myfunc1() #함수를 호출한다 
print("정보2")
myfunc1() #함수를 호출한다 
print("정보3")

#1~n까지의 합계를 구하는 함수
def mysum(limit): #파라미터
    """
    함수안에서 만드는 변수는 모두 지역변수 
    함수내에서만 존재한다.
    """
    s=0
    for i in range(1, limit+1):
        s = s + i 
    return s #값 반환하기 

print( mysum(100) ) #100 - 인수(argument)
print( mysum(1000) )

#구구단을 출력하는 함수 
# mygugu(3,5)
def mygugu(start, end):
    #에러처리를 함수 앞쪽에서 진행하자
    #return 구문 - 값반환, 함수종료
    if start>end:
        print("앞에 숫자가 더 작은게 와야합니다.")
        return #함수가 종료된다. 

    for i in range(start, end+1):
        print("*** ", i, " 단 ***")
        for j in range(1,10):
            print("%3d X %3d = %3d" %(i,j,i*j))

mygugu(5,3)
mygugu(3,4)

def mycount(sentence, mark):
    count=0
    for c in sentence:
        if c ==mark:
            count +=1
    return count 

#함수만들기, 문자열, 문자 "I like star, red star", "s"
print( mycount("I like star, red star", "s"))
#s가 몇번 등장했는지 숫자 반환함수 





