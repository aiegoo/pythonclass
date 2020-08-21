a = [1,3,5,7,9]
print( "크기 : ", len(a))
print( a[0] )
print( a[1] )
print( a[2] )
print( a[3] )
print( a[4] )
print( a[-1])
print( a[-2])

print ( a[0:3])
print ( a[:3] )
print ( a[3:] )

word = ["파이썬", "딥러닝", "머신러닝", "인공지능", "MYSQL"]
print( word )
print( word[0])
print( word[0][0], word[0][1], word[0][2])
print( len(word[0]))
print( len(word[3]))
print( len(word[4]))

#바꿔치기 
word[2] = "machine learning"
print( word )

#요소추가할때 
word.append("nodejs")
word.append("javascript")

print( word )

word = word + ["장고"]
print(word)

#확장 -  append 와 달리 요소 하나씩이 아니리 
# list + list
word.extend(["Django"]) #string->list 로 전환시켜서 
print(word)

print("0번째 요소 삭제하기 ")
del word[0]
print(word)

#정렬하기 
word.sort()
print(word)

#뒤집기
word.reverse()
print(word)

#검색기능 
print( "위치값 : ", word.index('nodejs'))

print( word.count("python") ) #존재하는 데이터개수
print( "python" in word ) #true 또는 false로 대답한다

#print( "위치값 : ", word.index('python'))

#append : 맨뒤에 , insert :중간에 
word.insert(4, "java")
print(word)

word.remove("MYSQL")
print(word)

#pop함수 - 맨 마지막 요소를 삭제한다 
word.pop()
print(word)








