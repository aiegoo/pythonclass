s = input("아무키나 누르세요")
count=[]
for i in range(0, 26):
    count.append(0)

for c in s:
    if ord(c)>=ord('a') and ord(c)<=ord('z'):
        count[ ord(c) - ord('a')]+=1 
    elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
        count[ ord(c) - ord('A')]+=1 

for i in range(0, 26):
    print( chr(ord('A')+i), "===>", count[i])