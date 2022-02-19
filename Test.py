print("Hello\" World!")

#walrus operator
print(ds := True)
ds = False
print(ds)

#High Order Functions
def upr(txt) : return txt.upper()
def hlo(f) :
    txt = f("Hello")
    print(txt, type(txt))
hlo(upr)

def dvsr(x):
    def dvdt(y) : return (y/x)
    return dvdt
dvd = dvsr(2)
print(dvd(2))

#lambda
lambda_double = lambda x:x *2
lambda_multply = lambda x, y: x*y
lambda_check = lambda adult:True if adult > 18 else False
print(lambda_double(4))
print(lambda_multply(2, 2))
print(lambda_check(19))

studens = ("Subham", "Pankaj", "Shivam", "Abhisek")
print()
for i in sorted(studens, reverse=True) : print(i, end=',')
studensRslt = [("Subham", 74, 'B'), ("Pankaj", 46, 'C'), ("Shivam", 44, 'C'), ("Abhisek", 61, 'B')]
print()
grade = lambda grades:grades[1]
studensRslt.sort(key=grade, reverse=True)
for i in studensRslt : print(i)

store = [("shirt", 7), ("jean",10), ("pant",8), ("t-shirt", 5)]
print()
to_rupee = lambda price:(price[0], price[1]*74.80)
for i in list(map(to_rupee,store)) : print(i)

friends = [("Mohan", 16), ("Rahul", 20), ("Kunal", 12), ("Ravi", 19)]
print()
adlt = lambda dta:dta[1] >= 19
for i in list(filter(adlt,friends)) : print(i)

import functools
ltrs = ['H', 'E', 'L', 'L', 'O']
print('\n')
print(functools.reduce(lambda x,y,:x+y, ltrs))

#comprehension
waterLevl = [10, 80, 60, 20, 120, 40, 180]
print()
print([tnk if tnk < 100 else "Fall" for tnk in waterLevl])
print("Fall:", list(filter(lambda x:x>100, waterLevl)))
print("Not-Fill:", [tnk for tnk in waterLevl if tnk < 100])

sqrs = []
print()
print([i*i for i in range(1, 11)])

cities_F = {"New York" : 32, "Boston" : 75, "Los Angeles" : 100, "Chicago" :50}
print()
print({key: round((value-32)*(5/9)) for (key, value) in cities_F.items()})
print({key: value for (key, value) in cities_F.items() if value > 40})
print({key: ("Warm" if value > 40 else "Cold") for (key, value) in cities_F.items()})

tuplNmbrs = (9, 0, 7, 8, 4)
print()
def addNumbr(n) : return n+n
toMap = map(addNumbr, tuplNmbrs)
print(list(toMap))
print(list(map(lambda x: x + x, tuplNmbrs)))
print(list(filter(lambda x: x%2==0, tuplNmbrs)))
tuplNam = ("Summit", "Nayan", "Abhisek", "Manoj", "Vinod")
lstScr = [1200, 800, 600, 200, 0]
print(list(zip(tuplNam, tuplNmbrs, lstScr)))
for i in zip(tuplNam, tuplNmbrs, lstScr) : print(i, end=',')
print()
print(dict(zip(tuplNam, tuplNmbrs)))
