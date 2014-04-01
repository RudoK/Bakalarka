from __future__ import division
import math
import random
import unittest
import moduly
import funkcie
__author__ = 'MeriMood'

def anneal(fun, init_temp, ticks, opt = 1):
    hracia_plocha = funkcie.plocha()
    rozlozenie_cur = funkcie.rozlozenie()
    funkcie.inicializuj(hracia_plocha, rozlozenie_cur)
    cur = funkcie.plocha(hracia_plocha)
    best = funkcie.plocha(hracia_plocha)
    ebest = fun(best, opt)
    ecur = fun(cur, opt)
    temp = init_temp
    delta_e = 0
    while temp > init_temp/ticks:
        temp -= init_temp/ticks
        new_plocha = funkcie.plocha(cur)
        rozlozenie_new = funkcie.rozlozenie(rozlozenie_cur)
        funkcie.generuj(rozlozenie_new, new_plocha)
        enew = fun(new_plocha, opt)
        delta_e += math.fabs(enew - ecur)
        probability = funkcie.prob(ecur, enew, temp)
        randomnumber = random.random()
        if probability > randomnumber:
#            print(ecur - enew, temp)
            cur = funkcie.plocha(new_plocha)
            rozlozenie_cur = funkcie.rozlozenie(rozlozenie_new)
            ecur = fun(cur, opt)
            if ecur < ebest:
                best = funkcie.plocha(cur)
                ebest = fun(best, opt)

    ebest = funkcie.finalenergy(best)
    funkcie.vypis_plochu(best)
    print ("ebest: %d" % ebest)
    return ebest, delta_e

ticks = 100000
_temp = 500
delta_temp = 0
for iterator in range(0, 5):
    _temp = anneal(funkcie.energyObvod, _temp, ticks)[1]/ticks
    delta_temp += _temp
delta_temp /= 5
print(delta_temp)
priemerny_vysledok = 0
for iterator in range(0, 10):
    priemerny_vysledok += anneal(funkcie.energyObvod, delta_temp, ticks)[0]
print(priemerny_vysledok/10)

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.hracia_plocha1 = funkcie.plocha()
        self.hracia_plocha2 = funkcie.plocha()
        self.hracia_plocha2[4][8] = 0
        self.hracia_plocha2[5][8] = 0
        self.hracia_plocha2[6][8] = 0
        self.hracia_plocha2[7][8] = 0
        self.hracia_plocha2[8][8] = 0
        self.hracia_plocha3 = funkcie.plocha()
        self.hracia_plocha3[4][8] = 0
        self.hracia_plocha3[5][8] = 0
        self.hracia_plocha3[6][8] = 0
        self.hracia_plocha3[7][8] = 0
        self.hracia_plocha3[8][8] = 0
        self.hracia_plocha3[6][4] = 0
        self.hracia_plocha3[6][5] = 0
        self.hracia_plocha3[6][6] = 0
        self.hracia_plocha3[6][7] = 0
        self.hracia_plocha4 = funkcie.plocha()
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
        self.hracia_plocha5 = funkcie.plocha()
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
        self.assertEqual(funkcie.energy2(self.hracia_plocha1), 63)
        self.assertEqual(funkcie.energy2(self.hracia_plocha2), 30.5)
        self.assertEqual(funkcie.energy2(self.hracia_plocha3), 20)
        self.assertEqual(funkcie.energy2(self.hracia_plocha4), 14)
        self.assertEqual(funkcie.energy2(self.hracia_plocha5), 9.5)

    def test2(self):
        self.assertEqual(funkcie.finalenergy(self.hracia_plocha1), 60)
        self.assertEqual(funkcie.finalenergy(self.hracia_plocha2), 55)
        self.assertEqual(funkcie.finalenergy(self.hracia_plocha3), 51)
        self.assertEqual(funkcie.finalenergy(self.hracia_plocha4), 44)
        self.assertEqual(funkcie.finalenergy(self.hracia_plocha5), 61)

    def test3(self):
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 4, 4), 4)
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 5, 7), 1)
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 5, 4), 0)
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 7, 4), 4)
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 4, 9), 14)
        self.assertEqual(funkcie.energy2rekurzia(self.hracia_plocha5, 7, 9), 14)

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


#if __name__ == '__main__':
#   unittest.main()