# Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def feladat2():
    a = int(input("Kérem adjon meg egy számot!: "))
    i = 0
    szamlalo = 0
    while i < 10:
        a = int(input("Kérem adjon meg egy számot!: "))
        if a % 3 == 0:
            szamlalo += 1
        i += 1
    print(f"{szamlalo}db számnak osztója a 3! ")

# Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def feladat3():
    a = int(input("Kérem adjon meg egy számot!: "))
    while not (a % 10 == 0):
        print(f"{a} nem osztható 10-zel. Kérem próbálja újra. ")
        a = int(input("Kérem adjon meg egy számot!: "))
    print(f"{a} osztható 10-zel!")

# Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def feladat4():
    a = int(input("Adjon meg egy kétjegyű páros számot!: "))
    while not((a % 2 == 0) and 100 > a >= 10):
        a = int(input("Adjon meg egy kétjegyű páros számot!: "))
    print("Helyes!")

# Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
def feladat5():
    a = int(input("Adjon meg egy kétjegyű páratlan számot!: "))
    while not(a < 0 and (a % 2 != 0)):
        a = int(input("Adjon meg egy kétjegyű páratlan számot!: "))
    print("Helyes!")

# Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
def feladat6():
    a: int = int(input("Adj meg egy szämot!: "))
    gyok: float = a ** 0.5
    while not (gyok.is_integer() or (a%3==0)):
        print("3-al oszthato vagy nögyzet szämot adj meg!")
        a: int = int(input("Adj meg egy szämot!: "))
        gyok: float = a ** 0.5
    print(f"{a} 3-al osztato vagy negyzetszäm!")

# Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
def feladat7():
    a: int = int(input("Adj meg egy számot!"))
    b: int = int(input("Adj meg egy számot!"))
    c: int = int(input("Adj meg egy számot!"))
    while not ((a<b+c) and (b<a+c) and (c<a+b)):
        print("A megadott számok nem alkalmasak háromszög oldalalinak. Próbáld újra!")
        a: int = int(input("Adj meg egy számot!"))
        b: int = int(input("Adj meg egy számot!"))
        c: int = int(input("Adj meg egy számot!"))
    print("Ok.")

# Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
def felafat8():
    a: str = str(input("Írj valamit!: "))
    while len(a)<=3:
        print("Legyen hosszabb, mint 3 betű!")
        a: str = str(input("Írj egy szót!: "))
    print(a.upper())

# Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
def feladat9():
    a:str = str(input("Írj valamit!: "))
    while not (len(a)<=4 and a.islower()):
        print("Legyen kisbetűs és minimum 4 betű!")
        a: str = str(input("Írj valamit!: "))

'''Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), 
és írasd ki az átlagukat 2 tizedes jegy pontossággal 
(a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!'''
def feladat10():
    a:int = int(input("Adj meg egy számot!: "))
    i = 0
    gyujto = 0
    while a != 0:
        i += 1
        gyujto += a
        a: int = int(input("Adj meg egy számot!: "))
    print(gyujto/i)

