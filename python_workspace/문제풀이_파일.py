f = open("testdata1.txt", "r")
sList = f.readlines()
f.close()

s=0
cnt=0
for item in sList:
    number = int(item)
    s = s+ number
    cnt = cnt+1 

print(s, s/cnt)
