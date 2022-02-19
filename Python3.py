from NewClass import newClass
from dir import Hlo
import module

#NewClass
nwcls = newClass("sdf", 4)
print(nwcls.model)
print(nwcls.length)
print(nwcls.newFunc())
nwcls.newVar = 8
print(nwcls.newVar)

nwcls.newFunc().addFunc()

#modul
print()
print(module)
print(module.__name__)
