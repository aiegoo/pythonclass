# *num 정수를 가변인자로 주겠다 
# 1, (1,2,3)
def add(*num):
    s = 0
    for i in num:
        s = s+i 
    return s 

def evenAdd(*num):
    s = 0
    for i in num:
        if i%2==0:
            s = s+i 
    return s 

def isEven(num):
    if num%2==0:
        return True 
    else:
        return False


if __name__ =="__main__":
    print( add(1,2) )
    print( add(120,2,1,5) )
    print( add(6,6,6,6,7,6) )
    print( evenAdd(2,3,4,5,6))
    print(isEven(4))
    print(isEven(5))