def changeValue(xList):
    for i in range(0, len(xList)):
        xList[i] = xList[i]*2
    """
    for x in xList:
        x = x * 2  이때 x는 xList의 값 하나만 읽어와서 사용할뿐
                본래의 xList와는 상관없다. 
    """
a = [1,2,3,4,5]
changeValue(a)
print( a )

def myfunc1(a=10, b=20, c=30):
    return a+b+c

print( myfunc1() )
print( myfunc1(1) )
print( myfunc1(1,2) )
print( myfunc1(1,2,3) )

def myfunc2(x, a=10, b=20, c=30):
    return x+a+b+c

print( myfunc2(10))

z = myfunc2(10, b=2, a=11)
print(z)

print("***", end='\t')

def myfunc3(*arg):
    #각 요소들의 합계 구해서 반환하기 
    s=0
    for item in arg:
        s = s+item 
    return s 

print ( myfunc3( 1 ))
print ( myfunc3( 10, 20, 30, 40,50 ))

#정의되지 않은 인자처리하기 - dict타입으로 전달
#argument 앞에 ** (아스테리스크 2개 붙인다)

def myfunc4(**info):
    print( info.keys())
    print( info.values())
    print( info['userid'])
    print( info['password'])
    print( info['username'])
    
myfunc4(userid='user01', password='1234', 
        username='홍길동')

