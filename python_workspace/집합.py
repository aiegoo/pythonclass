#집합.py

A = set( [1,2,3,4,5])
B = set( [1,3,6,7])
print( type(A))

#교집합 구하기 
C1 = A.intersection(B)
print( C1 )

#합집합 
C2 = A.union(B)
print(C2)

#차집합
C3 = A.difference(B)
print(C3)

A = set([1,2,3,4,5,1,2,3,6,7,8,9])
print(A)
#print( A[0] ) - 집합은 인덱싱을 지원하지 않는다 
AList = list(A) #집합을 list타입으로 전환하면 indexing 가능하다
print(AList)
print( type(AList))