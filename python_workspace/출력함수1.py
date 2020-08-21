import sys 

print("출력", "연습", "print", sep="$", end="@")
print("두번째줄 ", file=sys.stderr) 

#엑셀:cp949 
f = open("파일출력.txt", "w", encoding="utf-8")
print("여기에 내보내는건 다 파일로 나감", file=f)
f.close()