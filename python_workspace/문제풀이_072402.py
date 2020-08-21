#ABCDEFGHIJKLMNOPQRSTUVWXYZ 

"""
    *            행 : 5, i, 0,1,2,3,4,
   ***           공백개수:4            별:1
  *****                  3               3
 *******                 2               5
*********                1               7
                         0               9
                공백개수 + i = 4        2*i-1
                        = 4-i
"""
for i in range(0, 6):
    #공백그리기
    for j in range(0,  6-i):
        print(' ', end='')
    for j in range(0,  2*i-1):
        print('*', end='')
    print() #라인하나 바꿈
    