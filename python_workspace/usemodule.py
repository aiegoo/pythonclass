import mymodule1

print ( mymodule1.sigma(100) )

mymodule1.gugudan(7)

#as - ailasing:별명 - 다른이름으로 
import mymodule1 as mm 
print( mm.sigma(1000))
mm.gugudan(9)

#from mymodule1 import sigma
#from mymodule1 import gugudan 

from mymodule1 import * 

print( sigma(1000) )
gugudan(4)



