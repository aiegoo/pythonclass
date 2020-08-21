g = lambda x, y : x*y 
print( g(2,3))

#print 함수가 lambda호출 안해줌 
print ((lambda x, y : x*y)(3,4) )

def sqrt(x):
    x = x*x 
    return x

a = map(sqrt, [1,2,3,4,5,6,7,8,9,10])
print(type(a))
print(a)

for item in map(sqrt, [1,2,3,4,5,6,7,8,9,10]):
    print(item)

for item in map(lambda x:x*x, [1,2,3,4,5,6]):
    print(item)

a = list(map(lambda x:x*x, [1,2,3,4,5,6]) )
print( a )

#list 정렬함수- 자기순서가 바뀜,
#내장함수 sorted- 정렬된 데이터를 반환

a = [5,4,-8,9,1,2,-3,6,7,-10]
b = a[:]#하드카피, 새로운 객체 만들고 a값 복사 
a.sort(key=sqrt)
print(a)
print(b)
c = sorted( b, key=sqrt)
c = sorted( b, key=lambda item:item*item)
print("original : ", b)
print("sorted : ", c)

students=[
    {"name":"강만수", "kor":90, "eng":80},
    {"name":"김정하", "kor":80, "eng":60},
    {"name":"이민호", "kor":70, "eng":70},
    {"name":"김성훈", "kor":99, "eng":90},
    {"name":"강기정", "kor":95, "eng":750}
]

a = sorted(students, 
       key=lambda item:item['name'],
       reverse=True)#내림차순 정렬 
print(a)

a = ["flowers", "school", "like", "hope",
     "hospital"]
#filter(조건식, 리스트) 리스트에서 조건을 만족하는
#요소만 추출한다 
for item in filter(lambda x:len(x)>=5, a):
    print(item)

