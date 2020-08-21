"""
1.
정수를 10개 입력받아서 합과 평균 구하여 출력하기

2.정수를 10개 입력받아서 각각 짝수와 홀수의 
개수와 평균 구하기 
"""
numList = []
for i in range(1, 11):
    num = int(input("정수 "))
    numList.append(num)

s=0
for i in numList:
    s = s+i 
print("합계 : ", s)

even_cnt=0
odd_cnt=0
even_sum=0
odd_sum=0

for i in numList:
    if i%2==0:
        even_cnt = even_cnt + 1
        even_sum = even_sum + i 
    else:
        odd_cnt = odd_cnt + 1
        odd_sum = odd_sum + i 

print("짝수 개수 {}  짝수평균 {} ".format( even_cnt,
         even_sum/even_cnt))
print("홀수 개수 {}  홀수평균 {} ".format( odd_cnt,
         odd_sum/odd_cnt))

"""
이름  근무시간 시간당급여액  주급
-------------------------------
홍길동  15     10000        150000
장길산 40      10000        400000
임꺽정 30      12000        360000
---------------------------------
총지불액                    850000

"""