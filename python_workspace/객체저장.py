import pickle
colors = {"red":"빨간색", "green":"초록색", "blue":"파란색"}
f = open("colors.bin", "wb")
pickle.dump(colors, f)#파일에 저장하기 - 직렬화 
f.close() 

del colors
f = open("colors.bin", "rb")
colors = pickle.load(f)#역직렬화 
f.close()

print( colors )