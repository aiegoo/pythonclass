s = "Life is too short, You need Python"
print("문자열의 길이 : ", len(s))

#list 타입 
a = [1,2,3,4]
print("a의 길이 : ", len(a))

#인덱싱 
print("첫번째 문자 ", s[0] )
print("마지막 문자 ", s[len(s)-1] )
print( s[-1]) 
print( s[-2]) 
print( s[-3]) 

#슬라이싱 - 문자열을 잘라낸다.   s[ 시작위치:종료위치]
print(s[0:4]) #0,1,2,3 마지막은 빠진다. 

print(s[:12]) # 0,1,2,3,4,5,6,7,8,9,10,11
print(s[12:]) # 12 이후로 끝까지 

#s[0]='l' #값 바꾸기 불가능함 
s2 = 'l' + s[1:]
print(s2)

# %d - decimal(10진수)
s = "I eat %d apples." % 3
print(s)

s = "I eat %d apples and %d peach." % (3, 5)
print(s)
s = "I eat {} apples and {} peach.".format(3,5)
print(s)

s = "문자열 : %s 정수:%05d %o %X 실수:%.2f%%" % ('test',
              15,15,15, 4.5)
print(s)

s = "0:{} 1:{} 2:{} ".format(3,4,5)
print(s)

s = "0:{2} 1:{1} 2:{0}  {1}".format(3,4,5)
print(s)

s="%-20s*" % ('korea')
print(s)
s="%20s*" % ('korea')
print(s)

s = "I ate {number} apples".format(number=3) 

print(  "{:<10}".format(15) )
print(  "{:>010}".format(15) )
print(  "{:^10}".format(15) )

