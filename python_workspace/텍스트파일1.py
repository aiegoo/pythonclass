f = open("test2.txt", "w") #파일을 쓰기모드로 연다 
f.write("file write test 111111\n")
f.write("file write test 222222\n")
f.write("file write test 333333\n")
f.close() 

f = open("test2.txt", "r")
s = f.read()
print(s)
print(type(s))
f.close()

f = open("test2.txt", "r")
sList = f.readlines()
print(type(sList))
for line in sList:
    print(line, end="")
f.close()