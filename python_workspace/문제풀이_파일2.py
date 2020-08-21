f = open("data.txt", "r", encoding="utf-8")
sList = f.readlines()
f.close()

for item in sList:
    print(item)
    if item!="\n":
        data = item.split(",")
        name = data[0] 
        kor = int(data[1])
        eng = int(data[2])
        mat = int(data[3])
        total = kor + eng + mat 
        avg = total/3 

        print(name, kor,eng, mat, total, avg)

