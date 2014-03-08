import math
import random
import moduly
__author__ = 'MeriMood'


def prob(e1, e2, temp):
    delta_e = e2 - e1
    if delta_e < 0:
        return 1.1
    if round(temp, 3) <= 0:
        return 0.1
    return min(math.exp(-1 * (delta_e / temp)), 1)


def zapis_modul(x, y, xModul, xOtocenie, p):
    x1 = 0
    y1 = 0
    for xtmp in range(x, x + 5):
        for ytmp in range(y, y + 5):
            p[xtmp][ytmp] += moduly.Moduly[xModul][xOtocenie][x1][y1]
            x1 += 1
        x1 = 0
        y1 += 1


def vymaz_modul(x, y, xModul, xOtocenie, p):
    x1 = 0
    y1 = 0
    for xtmp in range(x, x + 5):
        for ytmp in range(y, y + 5):
            p[xtmp][ytmp] -= moduly.Moduly[xModul][xOtocenie][x1][y1]
            x1 += 1
        x1 = 0
        y1 += 1


def generuj(rozlozenie, p):
    xModul = random.randrange(0, 12)
    x = random.randrange(4, 9)
    y = random.randrange(4, 16)
    pocet_otoceni = len(moduly.Moduly[xModul])
    xOtocenie = random.randrange(0, pocet_otoceni)
    vymaz_modul(rozlozenie[xModul][0], rozlozenie[xModul][1], xModul, rozlozenie[xModul][2], p)
    rozlozenie[xModul][0] = x
    rozlozenie[xModul][1] = y
    rozlozenie[xModul][2] = xOtocenie
    zapis_modul(rozlozenie[xModul][0], rozlozenie[xModul][1], xModul, rozlozenie[xModul][2], p)


def inicializuj(hracia_plocha, rozlozenie_cur):
    for xModul in range(0, len(moduly.Moduly)):
        #generuj poziciu
        x = random.randrange(4, 10)
        y = random.randrange(4, 17)
        #generuj otocenie
        pocet_otoceni = len(moduly.Moduly[xModul])
        xOtocenie = random.randrange(0, pocet_otoceni)
        zapis_modul(x, y, xModul, xOtocenie, hracia_plocha)
        rozlozenie_cur[xModul][0] = x
        rozlozenie_cur[xModul][1] = y
        rozlozenie_cur[xModul][2] = xOtocenie


def plocha(p=[[-1 for x in range(0, 22)] for y in range(0, 15)]):
    result = [[-1 for x in range(0, 22)] for y in range(0, 15)]
    for x in range(0, 15):
        for y in range(0, 22):
            result[x][y] = p[x][y]
    return result


def rozlozenie(r=[[0 for x in range(0, 3)] for y in range(0, 12)]):
    result = [[0 for x in range(0, 3)] for y in range(0, 12)]
    for x in range(0, 12):
        for y in range(0, 3):
            result[x][y] = r[x][y]
    return result


def vypis_plochu(p):
    var = ""
    for x in range(4, 9):
        for y in range(4, 16):
            if p[x][y] > -1:
                var += " "
            var += " "
            var += str(p[x][y])
        print (var)
        var = ""
    print ("")


#ohodnocovacia funkcia, ktora berie do uvahy iba policka s -1, vracia pocet takychto policok na ploche
def energy(p):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            if p[x][y] < 0:
                hodnota += math.fabs(p[x][y]) * 2
    return hodnota


#ohodnocovacia funkcia, ktora berie do uvahy velkosti a pocet ostrovov, vyuziva pomocnu funkciu
def energy2(p):
    velkost = 0
    pocet_ostrovov = 0
    new_plocha = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if new_plocha[x][y] == -1:
                velkost += 3 + energy2rekurzia(new_plocha, x, y)
                pocet_ostrovov += 1
            #                print("ostrov: %d" % pocet_ostrovov)
            #                print("velkost: %d" % velkost)
            #                velkost = 0
            #    print("%.10f" % float(velkost*2/pocet_ostrovov))
    if pocet_ostrovov == 0:
        pocet_ostrovov = 1
    return float(velkost / pocet_ostrovov)


#na danej pozicii x a y sa nachadza -1, zisti na aky velky ostrov zlozeny z -1 som narazil
def energy2rekurzia(new_plocha, x, y):
    hodnota = math.fabs(new_plocha[x][y])
    new_plocha[x][y] = 0
    if (new_plocha[x + 1][y] == -1) & (x < 8):
        hodnota += energy2rekurzia(new_plocha, x + 1, y)
    if (new_plocha[x - 1][y] == -1) & (x > 4):
        hodnota += energy2rekurzia(new_plocha, x - 1, y)
    if (new_plocha[x][y + 1] == -1) & (y < 15):
        hodnota += energy2rekurzia(new_plocha, x, y + 1)
    if (new_plocha[x][y - 1] == -1) & (y > 4):
        hodnota += energy2rekurzia(new_plocha, x, y - 1)
    return hodnota


#objektivna ohodnocovacia funkcia, vrati realnu hodnotu ktora sa na chadza dokopy na ploche (optimum je 0)
def finalenergy(p):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            hodnota += math.fabs(p[x][y])
    return hodnota
