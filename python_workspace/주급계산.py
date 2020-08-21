"""
문제1. 주급계산 
이름, 근무시간, 시간당급여액, 주급을 계산하는데 
만일 근무시간이 40시간이 넘는다면 초과부분에 대해서는 
시간당급여액의  50%를 특별수당으로 계산하라
그리고 총 금액이 20만원 이하이면 3.3%로 세금을 계산하고 
20만원 초과 40만원 이하이면 4.4% 
40만운 초과이면 5.5%로 계산하라 

이름   근무시간 단가     총액   수당  세금  실수령액
홍길동  20    10000    200000   0  6600  199400 

1.입력작업 - 계산결과를 가져오는데 필요한 입력데이타가 뭔가 
  이름, 시간당급여액, 근무시간
2.계산
   총액 : 근무시간 * 시간당급여액 
   수당 : 근무시간이 40넘어갈때  
         초과분(근무시간-40)*시간당급여액* 0.5
   세금 : 20이하 0.033  20크고 40이하 0.044, 그밖에 0.055 
3.출력결과 

"""
name = input("이름 : ")
work_time = int(input("일한시간 : "))
per_pay = int( input("시간당 급여액 "))

pay = work_time * per_pay
over_pay =0 

if( work_time>40):
    over_pay = (work_time - 40) * per_pay * 0.5 

total_pay = pay + over_pay 

if total_pay <= 200000:
    tax = total_pay * 0.033
elif total_pay <=400000:
    tax = total_pay * 0.044
else:
    tax = total_pay * 0.055

real_pay = total_pay - tax 
result = "{} {} {} {} {} {} {} {}".format( 
    name, work_time, per_pay,pay, over_pay, total_pay, tax, 
    real_pay
)
print(result)

