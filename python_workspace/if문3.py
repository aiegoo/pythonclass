#if문3.py
"""
90이상이면 수
90미만 80이상이면 우 
80미만 70이상이면 미 
70이상 60미만이면 양
60미만 가 
"""
score = int(input("점수 : "))
if score>=90:
    print("수")
elif score>=80:
    print("우")
elif score>=70:
    print("미")
elif score>=60:
    print("양")
else:
    print("가")

