for i in range(1,11):
    for j in range(1, 11):
        print(i, j)
        if j==5: 
            break

for j in range(1, 11):
    if j==5: 
        break
    print( j)

for j in range(1, 11):
    if j==5: 
        continue
    print( j)
else:
    print("""
    break나 continue구문이 실행되지 않았습니다.
    """)

a = [1,2,3,5,8,12,13,54,66,77]
key = 666
for i in a:
    if key == i:
        print("찾음")
        break 
else:
    print("못찾음")

