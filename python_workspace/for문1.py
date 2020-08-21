#리스트
for item in ['일', '이', '삼', '사', '오']:
    print(item)

#튜플
for item in ('하루', '이틀', '사흘', '나흘', '닷새'):
    print(item)

#dictionay 를 모조리 출력하고자 할때 
colors = {'red':'빨간색', 'green':'초록색', 'blue':'파란색'}
for key in colors:
    print(key, "===>", colors[key])

#배열의 인덱스와  내용을 동시에 
flowers=["작약", "백일홍", "철쭉", "장미", "튤립"]
for index, value in enumerate(flowers):
    print(index, value)

score = [60, 55, 40, 70, 95, 80, 54, 65, 35]
result = [] #list타입 객체 만들기 
for item in score:
    if item>=60:
        result.append("합격")
    else:
        result.append("불합격")

print(score)
print(result)

#zip 여러개의 리스트를 각각의 요소별로 결합시켜서 하나의 
#tuple로 조합하여 전달하는 함수이다          
for item in zip(score, result):
    print(item)

for item1, item2 in zip(score, result):
    print(item1, "===>", item2)

a = [1,2,3,4,5,6,7,8,9,10]
for item in a:
    print(item)

#숫자리스트 생성 : range 함수- generator -> list로 형전환 
a = list(range(1, 10, 2))  #시작값, 종료값, 증감치 
print(a)

a = list(range(2, 10, 2))  #시작값, 종료값, 증감치 
print(a)

#list, tuple, dict,
#generator(일종의 데이터를 계속 생성하는 함수)

for i in range(1, 101):
    print("{:3}".format(i), end=' ')
    if i%10==0:
        print()
print() #마지막에 for문 다 종료하고 줄바꿈하기 

# 100 90 80 70 60 .... 10
for i in range(100, 1, -10):
    print("{:3}".format(i), end='')
print()

computer = ["python", "인공지능", "머신러닝", 
            "딥러닝","퍼셉트론", "시그모이드", 
            "최소제곱법", "분산", "표준편차"]
for index in range(0, len(computer), 2):
    print( computer[index] )

a = [1,3,5,7,9,11,13,15,17]
b = ['일', '이', '삼', '사', '오']
c = ['가', '나', '다', '라', '마']

for a1, b1, c1  in zip(a, b, c):
    print(a1, b1, c1)

#합계구하기
a = [9,2,5,8,11]
#반복구조   s = a[0] + a[1] + a[2] + a[3] + a[4]
# s =    a[0]
# s = s + a[1]
# s = s + a[2]
# s = 0
# s = s + a[n] - 공통식 
# 
a = [10, 11,45, 33,2,44,5,6,9]
s = 0 
for i in range(0, len(a)):
    s = s + a[i] 
print("합계 : ", s)

s = 0 
for i in a:
    s = s + i 
print("합계 : ", s)

"""
1.
정수를 10개 입력받아서 합과 평균 구하여 출력하기

2.정수를 10개 입력받아서 각각 짝수와 홀수의 
개수와 평균 구하기 
"""




