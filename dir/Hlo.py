

class hlo :
    def __init__(self, *ds) :
        print("Self Init")
        print("ds Init :", ds)
        self._ad = "ad is public var"
        self.__ads = 'ads is private var'
    def hlo__ads(self) : return self.__ads
    def _hlo_ad(self) : return self._ad

hloVar = hlo("ds", 5, 0, True, 7.2)
print(hloVar)
print(hloVar._ad)
print(hloVar.hlo__ads())
