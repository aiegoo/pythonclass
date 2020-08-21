def devide(x, y):
    return x/y 
try:
    print( devide(5,6))
    #print(devide("5", "0"))
    print(devide(5,0)) 
except Exception as e:
    print(e.args[0])
finally:
    print("종료합니다.")
