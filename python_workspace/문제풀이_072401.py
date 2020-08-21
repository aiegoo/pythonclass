#ABCDEFGHIJKLMNOPQRSTUVWXYZ 

for i in range(0, 26):
    k=ord('A')+i
    for j in range(0, 26):
        print( chr(k), end='')
        k=k+1 
        if k>ord('Z'):
            k=ord('A')
    print()