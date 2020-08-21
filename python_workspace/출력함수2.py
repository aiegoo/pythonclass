for x in range(1, 20):
    print( str(x).ljust(3), " X ", x, "=", str(x*x).rjust(5))

w = ["house", "dog", "cat", "hospital", "president"]
for word in w:
    print("*", word.center(20), "*")
    print("*", word.zfill(20), "*")

print( "{0} is {1} {0} {1} {1} {2}".format("apple", 
"red", "green"))

print( "{item} is {color}".format(item="banana",
                     color="yellow"))

dic = [{"item":"apple", "color":"red"},
       {"item":"banana", "color":"yellow"}]
print( "{0[item]} is {0[color]}".format(dic[1]))

for item in dic:
    print("{0} is {1}".format(item["item"], item["color"]))

"""
엔터키를 \r\n 또는 \n 바꾸면 text파일이다. 
파이썬 소스나, 메모장등으로 작성한 파일 
우리눈에 특별한 프로그램 없이 시각적으로 보이는것들은 
텍스트파일 
"""