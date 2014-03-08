import math
import random
import unittest
import moduly
__author__ = 'MeriMood'


def prob(e1, e2, temp):
    delta_e = e2 - e1
    if delta_e < 0:
        return 1.1
    if round(temp, 3) <= 0:
        return 0.1
    return min(math.exp(-1 * (delta_e / temp)), 1)


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


def finalenergy(p):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            hodnota += math.fabs(p[x][y])
    return hodnota


def energy(p):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            if p[x][y] < 0:
                hodnota += math.fabs(p[x][y]) * 2
    return hodnota


def rec(new_plocha, x, y):
    hodnota = math.fabs(new_plocha[x][y])
    new_plocha[x][y] = 0
    if (new_plocha[x + 1][y] == -1) & (x < 8):
        hodnota += rec(new_plocha, x + 1, y)
    if (new_plocha[x - 1][y] == -1) & (x > 4):
        hodnota += rec(new_plocha, x - 1, y)
    if (new_plocha[x][y + 1] == -1) & (y < 15):
        hodnota += rec(new_plocha, x, y + 1)
    if (new_plocha[x][y - 1] == -1) & (y > 4):
        hodnota += rec(new_plocha, x, y - 1)
    return hodnota


def energy2(p):
    velkost = 0
    pocet_ostrovov = 0
    new_plocha = plocha(p)
    for x in range(4, 9):
        for y in range(4, 16):
            if new_plocha[x][y] == -1:
                velkost += 3 + rec(new_plocha, x, y)
                pocet_ostrovov += 1
            #                print("ostrov: %d" % pocet_ostrovov)
            #                print("velkost: %d" % velkost)
            #                velkost = 0
            #    print("%.10f" % float(velkost*2/pocet_ostrovov))
    if pocet_ostrovov == 0:
        pocet_ostrovov = 1
    return float(velkost / pocet_ostrovov)


def setanneal(eval):
    #1. stanovenie optimalnej teploty a poklesu
    temp = 500
    pokles = 0.05
    delta_temp = 0
    for i in range(0, 5):
        hracia_plocha = plocha()
        rozlozenie_cur = rozlozenie()
        inicializuj(hracia_plocha, rozlozenie_cur)
        cur = plocha(hracia_plocha)
        ecur = eval(cur)
        delta_e = 0
        while temp > 0:
            temp -= pokles
            new_plocha = plocha(cur)
            rozlozenie_new = rozlozenie(rozlozenie_cur)
            generuj(rozlozenie_new, new_plocha)
            enew = eval(new_plocha)
            delta_e += math.fabs(enew - ecur)
            probability = prob(ecur, enew, temp)
            randomnumber = random.random()
            if probability > randomnumber:
                cur = plocha(new_plocha)
                rozlozenie_cur = rozlozenie(rozlozenie_new)
                ecur = eval(cur)
        temp = delta_e / 1000
        pokles = temp / 1000
        delta_temp += temp
    delta_temp /= 5
    temp = delta_temp
    pokles = temp / 10000
    print ("%f10" % delta_temp)
    return delta_temp


def anneal(eval, delta_temp, pokles):
    hracia_plocha = plocha()
    rozlozenie_cur = rozlozenie()
    inicializuj(hracia_plocha, rozlozenie_cur)
    cur = plocha(hracia_plocha)
    best = plocha(hracia_plocha)
    ebest = eval(best)
    ecur = eval(cur)
    temp = delta_temp
    delta_e = 0
    while temp > pokles:
        temp -= pokles
        new_plocha = plocha(cur)
        rozlozenie_new = rozlozenie(rozlozenie_cur)
        generuj(rozlozenie_new, new_plocha)
        enew = eval(new_plocha)
        delta_e += math.fabs(enew - ecur)
        probability = prob(ecur, enew, temp)
        randomnumber = random.random()
        if probability > randomnumber:
            print(ecur, enew, ecur - enew)
            cur = plocha(new_plocha)
            rozlozenie_cur = rozlozenie(rozlozenie_new)
            ecur = eval(cur)
            if ecur < ebest:
                best = plocha(cur)
                ebest = eval(best)

    ebest = finalenergy(best)
    result = eval(best)
    vypis_plochu(best)
    print ("ebest: %d" % ebest)
    return result


delta_temp = setanneal(energy2)

priemerny_vysledok = 0
for iterator in range(0, 1000):
    priemerny_vysledok += anneal(energy2, delta_temp, delta_temp/1000)
print(priemerny_vysledok/1000)


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.hracia_plocha1 = plocha()
        self.hracia_plocha2 = plocha()
        self.hracia_plocha2[4][8] = 0
        self.hracia_plocha2[5][8] = 0
        self.hracia_plocha2[6][8] = 0
        self.hracia_plocha2[7][8] = 0
        self.hracia_plocha2[8][8] = 0
        self.hracia_plocha3 = plocha()
        self.hracia_plocha3[4][8] = 0
        self.hracia_plocha3[5][8] = 0
        self.hracia_plocha3[6][8] = 0
        self.hracia_plocha3[7][8] = 0
        self.hracia_plocha3[8][8] = 0
        self.hracia_plocha3[6][4] = 0
        self.hracia_plocha3[6][5] = 0
        self.hracia_plocha3[6][6] = 0
        self.hracia_plocha3[6][7] = 0
        self.hracia_plocha4 = plocha()
        self.hracia_plocha4[4][8] = 0
        self.hracia_plocha4[5][8] = 0
        self.hracia_plocha4[6][8] = 0
        self.hracia_plocha4[7][8] = 0
        self.hracia_plocha4[8][8] = 0
        self.hracia_plocha4[6][4] = 0
        self.hracia_plocha4[6][5] = 0
        self.hracia_plocha4[6][6] = 0
        self.hracia_plocha4[6][7] = 0
        self.hracia_plocha4[6][9] = 0
        self.hracia_plocha4[6][10] = 0
        self.hracia_plocha4[6][11] = 0
        self.hracia_plocha4[6][12] = 0
        self.hracia_plocha4[6][13] = 0
        self.hracia_plocha4[6][14] = 0
        self.hracia_plocha4[6][15] = 0
        self.hracia_plocha5 = plocha()
        self.hracia_plocha5[4][8] = 1
        self.hracia_plocha5[5][8] = 1
        self.hracia_plocha5[6][8] = 2
        self.hracia_plocha5[7][8] = 3
        self.hracia_plocha5[8][8] = 1
        self.hracia_plocha5[4][6] = 1
        self.hracia_plocha5[5][6] = 1
        self.hracia_plocha5[6][6] = 7
        self.hracia_plocha5[7][6] = 4
        self.hracia_plocha5[4][7] = 2
        self.hracia_plocha5[8][6] = 1
        self.hracia_plocha5[6][4] = 1
        self.hracia_plocha5[6][5] = 1
        self.hracia_plocha5[6][6] = 1
        self.hracia_plocha5[6][7] = 1
        self.hracia_plocha5[6][9] = 0
        self.hracia_plocha5[6][10] = 0
        self.hracia_plocha5[6][11] = 0
        self.hracia_plocha5[6][12] = 0
        self.hracia_plocha5[6][13] = 0
        self.hracia_plocha5[6][14] = 0
        self.hracia_plocha5[6][15] = 1

    def test1(self):
        self.assertEqual(energy2(self.hracia_plocha1), 63)
        self.assertEqual(energy2(self.hracia_plocha2), 30.5)
        self.assertEqual(energy2(self.hracia_plocha3), 20)
        self.assertEqual(energy2(self.hracia_plocha4), 14)
        self.assertEqual(energy2(self.hracia_plocha5), 9.5)

    def test2(self):
        self.assertEqual(finalenergy(self.hracia_plocha1), 60)
        self.assertEqual(finalenergy(self.hracia_plocha2), 55)
        self.assertEqual(finalenergy(self.hracia_plocha3), 51)
        self.assertEqual(finalenergy(self.hracia_plocha4), 44)
        self.assertEqual(finalenergy(self.hracia_plocha5), 61)

    def test3(self):
        self.assertEqual(rec(self.hracia_plocha5, 4, 4), 4)
        self.assertEqual(rec(self.hracia_plocha5, 5, 7), 1)
        self.assertEqual(rec(self.hracia_plocha5, 5, 4), 0)
        self.assertEqual(rec(self.hracia_plocha5, 7, 4), 4)
        self.assertEqual(rec(self.hracia_plocha5, 4, 9), 14)
        self.assertEqual(rec(self.hracia_plocha5, 7, 9), 14)

    def test4(self):
        boli = set()
        for x in range (0, 100000):
            xModul = random.randrange(0, 12)
            x = random.randrange(4, 9)
            y = random.randrange(4, 16)
            pocet_otoceni = len(moduly.Moduly[xModul])
            xOtocenie = random.randrange(0, pocet_otoceni)
            vyber = (xModul, xOtocenie, x, y)
            if vyber not in boli:
                boli.add(vyber)
        print (len(boli))
        self.assertEqual(len(boli), 3780)
        for x in range(0, 12):
            for y in range(0, len(moduly.Moduly[x])):
                for z in range (4, 9):
                    for w in range (4, 16):
                        vyber = (x, y, z, w)
                        if vyber not in boli:
                            print(vyber)
        print ("done")



if __name__ == '__main__':
    unittest.main()