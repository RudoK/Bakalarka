from __future__ import division
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


def nulaplocha(p=[[0 for x in range(0, 22)] for y in range(0, 15)]):
    result = [[0 for x in range(0, 22)] for y in range(0, 15)]
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
def energy(p, opt = 1):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            if p[x][y] < 0:
                hodnota += math.fabs(p[x][y]) * 2
    return hodnota


#ohodnocovacia funkcia, ktora berie do uvahy velkosti a pocet ostrovov, vyuziva pomocnu funkciu
def energy2(p, opt = 0.5):
    velkost = 0
    pocet_ostrovov = 0
    vaha_pocet_ostrovov = 1-opt
    vaha_velkost = 1-vaha_pocet_ostrovov
#    print(vaha_pocet_ostrovov, vaha_velkost)
    new_plocha = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if new_plocha[x][y] == -1:
                velkost += vaha_pocet_ostrovov + vaha_velkost*energy2rekurzia(new_plocha, x, y)
                pocet_ostrovov += 1
            #                print("ostrov: %d" % pocet_ostrovov)
            #                print("velkost: %d" % velkost)
            #                velkost = 0
            #    print("%.10f" % float(velkost*2/pocet_ostrovov))
    if pocet_ostrovov == 0:
        pocet_ostrovov = 1
    #print(velkost / pocet_ostrovov)
    return float(velkost + pocet_ostrovov)


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
def finalenergy(p, opt = 1):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            hodnota += math.fabs(p[x][y])
    return hodnota


#hracia plocha ma 2 stredy a to na poziciach 3,6 a 3,7 ( pre moju rozsirenu plochu ku kazdej suradnici treba pripocitat
# 4)
def distance(xpos, ypos):
    if ypos > 9:
        dist = math.sqrt(math.pow(math.fabs(ypos - 10), 2) + math.pow(math.fabs(xpos - 6), 2))
    else:
        dist = math.sqrt(math.pow(math.fabs(ypos - 9), 2) + math.pow(math.fabs(xpos - 6), 2))
    return dist


def energy3rekurzia(new_plocha, x, y):
    hodnota = math.fabs(new_plocha[x][y])
    hodnota += distance(x, y)
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


def energy3(p, opt = 1):
    velkost = 0
    pocet_ostrovov = 0
    new_plocha = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if new_plocha[x][y] == -1:
                velkost += 3 + energy3rekurzia(new_plocha, x, y)
                pocet_ostrovov += 1
    if pocet_ostrovov == 0:
        pocet_ostrovov = 1
#    print(velkost / pocet_ostrovov)
    return float(velkost / pocet_ostrovov)


def najdiKladneOstrovy(new_plocha, x, y, N):
    new_plocha[x][y] = N
    if (new_plocha[x + 1][y] > 0) & (x < 8):
        najdiKladneOstrovy(new_plocha, x + 1, y, N)
    if (new_plocha[x - 1][y] > 0) & (x > 4):
        najdiKladneOstrovy(new_plocha, x - 1, y, N)
    if (new_plocha[x][y + 1] > 0) & (y < 15):
        najdiKladneOstrovy(new_plocha, x, y + 1, N)
    if (new_plocha[x][y - 1] > 0) & (y > 4):
        najdiKladneOstrovy(new_plocha, x, y - 1, N)
    return new_plocha


def kladneObvody(p):
    N = -2
    tmp = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if tmp[x][y] == -1:
                tmp[x][y] = 0
            if tmp[x][y] > 0:
                tmp = najdiKladneOstrovy(tmp, x, y, N)
                N -= 1
    coasts = []
    coast = 0
    for i in range(N, 0):
        coasts.append(coast)

    for x in range(4, 9):
        for y in range(4, 16):
            if tmp[x][y] < 0:
                if (tmp[x - 1][y] >= 0) | (x == 4):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x + 1][y] >= 0) | (x == 8):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x][y - 1] >= 0) | (y == 4):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x][y + 1] >= 0) | (y == 15):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
    return coasts


def Obvody(p):
    N = -2
    tmp = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if tmp[x][y] == -1:
                tmp = najdiOstrovy(tmp, x, y, N)
                N -= 1
    coasts = []
    coast = 0
    for i in range(N, 0):
        coasts.append(coast)

    for x in range(4, 9):
        for y in range(4, 16):
            if tmp[x][y] < 0:
                if (tmp[x - 1][y] >= 0) | (x == 4):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x + 1][y] >= 0) | (x == 8):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x][y - 1] >= 0) | (y == 4):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
                if (tmp[x][y + 1] >= 0) | (y == 15):
                    coast += 1
                    coasts[int(math.fabs(tmp[x][y]))] += 1
    return coasts


def energyKladnyObvod(p, opt = 0.5):
    vaha_zvysok = 1-opt
    vaha_obvod = 1-vaha_zvysok
    new_plocha = plocha(p)
    obvody = []
    obvody = kladneObvody(new_plocha)
    celkovy_obvod = 0
    for i in range(0, len(obvody)):
        celkovy_obvod += obvody[i]
    celkova_velkost = energy(p)

    return celkovy_obvod*vaha_obvod + celkova_velkost*vaha_zvysok


def najdiOstrovy(new_plocha, x, y, N):
    new_plocha[x][y] = N
    if (new_plocha[x + 1][y] == -1) & (x < 8):
        najdiOstrovy(new_plocha, x + 1, y, N)
    if (new_plocha[x - 1][y] == -1) & (x > 4):
        najdiOstrovy(new_plocha, x - 1, y, N)
    if (new_plocha[x][y + 1] == -1) & (y < 15):
        najdiOstrovy(new_plocha, x, y + 1, N)
    if (new_plocha[x][y - 1] == -1) & (y > 4):
        najdiOstrovy(new_plocha, x, y - 1, N)
    return new_plocha


def energyObvod(p, opt = 0.5):
    vaha_zvysok = 1-opt
    vaha_obvod = 1-vaha_zvysok
    new_plocha = plocha(p)
    obvody = []
    obvody = Obvody(new_plocha)
    celkovy_obvod = 0
    for i in range(0, len(obvody)):
        celkovy_obvod += obvody[i]
    celkova_velkost = energy(p)

    return celkovy_obvod*vaha_obvod + celkova_velkost*vaha_zvysok


def energyCelyObvod(p, opt = 0.5):
    vaha_zvysok = 1-opt
    vaha_obvod = 1-vaha_zvysok
    new_plocha = plocha(p)
    zaporne_obvody = []
    zaporne_obvody = Obvody(new_plocha)
    kladne_obvody = []
    kladne_obvody = kladneObvody(new_plocha)
    celkovy_obvod = 0
    for i in range(0, len(zaporne_obvody)):
        celkovy_obvod += zaporne_obvody[i]
    for i in range(0, len(kladne_obvody)):
        celkovy_obvod += kladne_obvody[i]
    celkova_velkost = energy(p)
    return celkovy_obvod*vaha_obvod + celkova_velkost*vaha_zvysok

def energy2CelyObvod(p, opt = 0.5):
    vaha_zvysok = 1-opt
    vaha_obvod = 1-vaha_zvysok
    new_plocha = plocha(p)
    zaporne_obvody = []
    zaporne_obvody = Obvody(new_plocha)
    kladne_obvody = []
    kladne_obvody = kladneObvody(new_plocha)
    celkovy_obvod = 0
    for i in range(0, len(zaporne_obvody)):
        celkovy_obvod += zaporne_obvody[i]
    for i in range(0, len(kladne_obvody)):
        celkovy_obvod += kladne_obvody[i]
    celkova_velkost = energy2(p)
    return celkovy_obvod*vaha_obvod + celkova_velkost*vaha_zvysok
