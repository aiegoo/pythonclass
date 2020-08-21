"""
for문 안에 for문이 들어간다 
"""
for i in range(1,6):
    for j in range(1,6):
        print( "i=", i, "j=", j)

#i가 1일때 j=1,2,3,4,5
#i가 2일때 j=1,2,3,4,5
#i가 3일때 j=1,2,3,4,5
#i가 4일때 j=1,2,3,4,5
#i가 5일때 j=1,2,3,4,5  전부 25번 수행한다 

#구구단을 3,5단까지 
for i in range(3, 6):
    print("*** ", i , "단 ***")
    for j in range(1, 10):
        print("%3d X %3d = %3d" % (i, j, i*j))
    print() 

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='')
    print()

for i in range(1, 6):
    for j in range(1, 6-i+1):
        print("*", end='')
    print()    
"""
i=1   j= 1, 6
i=2   j= 1, 5
i=3   j= 1, 3
"""

"""
for, if 
1 2 3 4 5 6 7 8 9 10
11 12 ....        20

이중for문으로 
"""


k=1 
for i in range(0, 10):
    for j in range(0, 10):
        print("{:4}".format(k), end='')
        k=k+1 
    print()

#A~Z: 65 66 67 68 
print( ord('A') ) #ord-코드를 반환
print( ord('B') )
print( ord('C') )
print( ord('a') )
print( ord('b') )
print( ord('0') )
print( ord('1') )
print( chr(100))
print( chr(101))
print( chr(102))
print( chr(103))

"""
"45" -> 52 53  문자저장이 파이썬 2byte(unicode)
45          45
"""

base_a = ord('A')
for i in range(0,26):
    print( chr(base_a + i))


"""
문제1:
ABCDEFGIJKLMNOPQRSTUVWXYZ
BCDEFGIJKLMNOPQRSTUVWXYZA
CDEFGIJKLMNOPQRSTUVWXYZAB
DEFGIJKLMNOPQRSTUVWXYZABC
...
ZABCDEFGIJKLMNOPQRSTUVWXY

문제2:
     *
    ***
   *****
  *******
 *********
"""

print()
for i in range(0,26):
    k= ord('A')+i #시작값 놓기 
    for j in range(0,26):
        print( chr(k), end='')
        k=k+1
        if k>ord('Z'):
            k = ord('A')
    print()


for i in range(1, 6):
    for j in range(1,6-i+1):
        print(' ', end='')
    for j in range(1,2*i):
        print('*', end='')
    print()

print("역으로")
for i in range(6, 0, -1):
    for j in range(1,6-i+1):
        print(' ', end='')
    for j in range(1,2*i):
        print('*', end='')
    print()

    