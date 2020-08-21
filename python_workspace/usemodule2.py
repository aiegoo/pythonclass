#from . import simplemodule 
import simplemodule

print( simplemodule.add(1,2,3))
print( simplemodule.evenAdd(1,2,3))
print( simplemodule.isEven(5))

import simplemodule as sm 
print( sm.add(1,2,3))
print( sm.evenAdd(1,2,3))
print( sm.isEven(5))

from simplemodule import * 
print( add(1,2,3,4,5))
print( evenAdd(1,2,4,6,8,9))
print( isEven(4))