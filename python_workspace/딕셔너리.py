#딕셔너리.py

colors = {'red':'빨간색', 'green':'초록색', 'blue':'파란색'}
print( colors )

print ( colors['red'] )
print ( colors['green'] )
print ( colors['blue'] )

#새로운 키 추가하기 - 키가 존재하지 않으면 새로만들고,
#존재하면 덮어쓴다 
colors['brown']='갈색'
colors['red']='빨강색'
print( colors )

personInfo=dict() #처음에 데이터없이 객체만 만든다 
personInfo['name']="홍길동"
personInfo['phone']='010-0000-0000'
print( personInfo['name'] )
print( personInfo.get('name'))

#키리스트만 
print( colors.keys() )

#값 리스트만 
print( colors.values() )











