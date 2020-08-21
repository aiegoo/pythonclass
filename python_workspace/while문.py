#while문.py 
"""
while 조건식:  조건식의 결과는 True, False이다 
    문장1      조건식이 True일때만 작동된다
    문장2 
"""
i=1
while i<=5:
    print(i)
    i = i + 1

"""
숫자를 입력받는데 양수가 입력되는동안 합을 구하고
음수들어오면 종료, 0은 안들어온다 
"""
s=0
num = int(input("정수 : " ))
while( num>0):
    s = s + num 
    num = int(input("정수 : " ))

print("합계 ", s )

"""
break - while, for문등을 중간에 빠져나가고자 할때 사용한다 
        break문은 자긴과 가장 가까운 루프를 종료한다 
"""
for i in range(1, 11):
    if i==5:
        break 
    print(i)

for i in range(1, 11):
    if i==5:
        continue  #continue문은 건너뛰기  
    print(i)
