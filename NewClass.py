class newClass :

    newVar = None

    def __init__(self, model, length) :
        self.model = model
        self.length = length

    def newFunc(self) :
        print("__init__ model: ", self.model)
        return self

    def addFunc(self) : print("new_class addFunc")


class inheritanceNewClass(newClass) :
    def __init__(self, model, length) :
        super().__init__(model, length)

    def inheritanceFunc(self) :
        print("model", self.model)
        print("length", self.length)

incls = inheritanceNewClass("jk", 4)
print(incls.newFunc())
incls.inheritanceFunc()

class myClass :
    myVar = 6

class deriveInheritanceClass(inheritanceNewClass, myClass) :
    print("The Parents of deriveInheritanceClass ", end = ':')
    print(inheritanceNewClass,myClass)
