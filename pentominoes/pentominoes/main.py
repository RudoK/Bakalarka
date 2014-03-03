import math
import random
import unittest

__author__ = 'MeriMood'
#vsetky hracie moduly sa daju reprezentovat v poli 5x5
#x
Modul_x1 = [[0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
#i
Modul_i1 = [[1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_i2 = [[1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]

#z
Modul_z11 = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
Modul_z12 = [[0, 0, 1, 0, 0],
             [1, 1, 1, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
Modul_z21 = [[0, 1, 1, 0, 0],
             [0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
Modul_z22 = [[1, 0, 0, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
#v
Modul_v1 = [[1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
Modul_v2 = [[1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
Modul_v3 = [[1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
Modul_v4 = [[0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

#w
Modul_w1 = [[0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_w2 = [[1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_w3 = [[0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_w4 = [[1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_w = [Modul_w1, Modul_w2, Modul_w3, Modul_w4]

#t

Modul_t1 = [[1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_t2 = [[0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_t3 = [[0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_t4 = [[1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_t = [Modul_t1, Modul_t2, Modul_t3, Modul_t4]

#u

Modul_u1 = [[1, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_u2 = [[1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_u3 = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_u4 = [[1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

Modul_u = [Modul_u1, Modul_u2, Modul_u3, Modul_u4]

#f
Modul_f11 = [[1, 0, 0, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f12 = [[0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f13 = [[0, 1, 0, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f14 = [[0, 1, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f21 = [[1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f22 = [[0, 1, 0, 0, 0],
             [1, 1, 1, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f23 = [[0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f24 = [[0, 0, 1, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_f = [Modul_f11, Modul_f12, Modul_f13, Modul_f14,
           Modul_f21, Modul_f22, Modul_f23, Modul_f24]
#l
Modul_l11 = [[1, 1, 1, 1, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l12 = [[0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l13 = [[1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l14 = [[1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l21 = [[1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l22 = [[1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l23 = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l24 = [[0, 0, 0, 1, 0],
             [1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_l = [Modul_l11, Modul_l12, Modul_l13, Modul_l14,
           Modul_l21, Modul_l22, Modul_l23, Modul_l24]

#y

Modul_y11 = [[1, 1, 1, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y12 = [[1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y13 = [[0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y14 = [[0, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y21 = [[1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y22 = [[0, 0, 1, 0, 0],
             [1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y23 = [[0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y24 = [[1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_y = [Modul_y11, Modul_y12, Modul_y13, Modul_y14,
           Modul_y21, Modul_y22, Modul_y23, Modul_y24]

#n

Modul_n11 = [[1, 1, 1, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n12 = [[0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n13 = [[1, 1, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n14 = [[0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n21 = [[1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n22 = [[0, 0, 1, 1, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n23 = [[1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n24 = [[0, 1, 1, 1, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_n = [Modul_n11, Modul_n12, Modul_n13, Modul_n14,
           Modul_n21, Modul_n22, Modul_n23, Modul_n24]

#p

Modul_p11 = [[1, 1, 1, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p12 = [[0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p13 = [[1, 1, 0, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p14 = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p21 = [[1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p22 = [[0, 1, 1, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p23 = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p24 = [[1, 1, 1, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

Modul_p = [Modul_p11, Modul_p12, Modul_p13, Modul_p14,
           Modul_p21, Modul_p22, Modul_p23, Modul_p24]

Modul_i = [Modul_i1, Modul_i2]

Modul_z = [Modul_z11, Modul_z12, Modul_z21, Modul_z22]

Modul_v = [Modul_v1, Modul_v2, Modul_v3, Modul_v4]

Modul_x = [Modul_x1]

Moduly = [Modul_f, Modul_i, Modul_l, Modul_n, Modul_p, Modul_t,
          Modul_u, Modul_v, Modul_w, Modul_x, Modul_y, Modul_z]


def vypis_plochu(plocha):
    var = ""
    for x in range(4, 9):
        for y in range(4, 16):
            if plocha[x][y] > -1:
                var += " "
            var += " "
            var += str(plocha[x][y])
        print (var)
        var = ""
    print ("")


def zapis_modul(x, y, xModul, xOtocenie, plocha):
    x1 = 0
    y1 = 0
    for xtmp in range(x, x + 5):
        for ytmp in range(y, y + 5):
            plocha[xtmp][ytmp] += Moduly[xModul][xOtocenie][x1][y1]
            x1 += 1
        x1 = 0
        y1 += 1


def vymaz_modul(x, y, xModul, xOtocenie, plocha):
    x1 = 0
    y1 = 0
    for xtmp in range(x, x + 5):
        for ytmp in range(y, y + 5):
            plocha[xtmp][ytmp] -= Moduly[xModul][xOtocenie][x1][y1]
            x1 += 1
        x1 = 0
        y1 += 1


def finalenergy(plocha):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            hodnota += math.fabs(plocha[x][y])
    return hodnota


def energy(plocha):
    hodnota = 0
    for x in range(4, 9):
        for y in range(4, 16):
            if plocha[x][y] < 0:
                hodnota += math.fabs(plocha[x][y]) * 2
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


def energy2(plocha):
    velkost = 0
    pocet_ostrovov = 0
    new_plocha = [[-1 for x in range(0, 22)] for y in range(0, 15)]
    for x in range(4, 9):
        for y in range(4, 16):
            new_plocha[x][y] = plocha[x][y]

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


def prob(e1, e2, temp):
    delta_e = e2 - e1
    if delta_e < 0:
        return 1.1
    if round(temp, 3) <= 0:
        return 0.1
    return min(math.exp(-1 * (delta_e / temp)), 1)


def generuj(rozlozenie, plocha):
    xModul = random.randrange(0, 12)
    x = random.randrange(4, 9)
    y = random.randrange(4, 16)
    pocet_otoceni = len(Moduly[xModul])
    xOtocenie = random.randrange(0, pocet_otoceni)
    vymaz_modul(rozlozenie[xModul][0], rozlozenie[xModul][1], xModul, rozlozenie[xModul][2], plocha)
    rozlozenie[xModul][0] = x
    rozlozenie[xModul][1] = y
    rozlozenie[xModul][2] = xOtocenie
    zapis_modul(rozlozenie[xModul][0], rozlozenie[xModul][1], xModul, rozlozenie[xModul][2], plocha)


def test(eval):
    #1. stanovenie optimalnej teploty a poklesu
    temp = 500
    pokles = 0.05
    delta_temp = 0
    for i in range(0, 5):
        Hracia_plocha = [[-1 for x in range(0, 22)] for y in range(0, 15)]

        rozlozenie_cur = [[0 for x in range(0, 3)] for y in range(0, 12)]

        rozlozenie_best = [[0 for x in range(0, 3)] for y in range(0, 12)]
        for xModul in range(0, len(Moduly)):
            #generuj poziciu
            x = random.randrange(4, 10)
            y = random.randrange(4, 17)
            #generuj otocenie
            pocet_otoceni = len(Moduly[xModul])
            xOtocenie = random.randrange(0, pocet_otoceni)
            zapis_modul(x, y, xModul, xOtocenie, Hracia_plocha)
            rozlozenie_cur[xModul][0] = x
            rozlozenie_cur[xModul][1] = y
            rozlozenie_cur[xModul][2] = xOtocenie
            rozlozenie_best[xModul][0] = x
            rozlozenie_best[xModul][1] = y
            rozlozenie_best[xModul][2] = xOtocenie
        cur = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        for x in range(4, 9):
            for y in range(4, 16):
                cur[x][y] = Hracia_plocha[x][y]
        ecur = eval(cur)
        delta_e = 0
        while temp > 0:
            temp -= pokles
            new_plocha = [[-1 for x in range(0, 22)] for y in range(0, 15)]
            for x in range(4, 9):
                for y in range(4, 16):
                    new_plocha[x][y] = cur[x][y]
            rozlozenie_new = [[0 for x in range(0, 3)] for y in range(0, 12)]
            for x in range(0, 12):
                for y in range(0, 3):
                    rozlozenie_new[x][y] = rozlozenie_cur[x][y]
            generuj(rozlozenie_new, new_plocha)
            enew = eval(new_plocha)
            delta_e += math.fabs(enew - ecur)
            probability = prob(ecur, enew, temp)
            randomnumber = float(random.randrange(0, 10000000000)) / 10000000000
            if probability > randomnumber:
                for x in range(4, 9):
                    for y in range(4, 16):
                        cur[x][y] = new_plocha[x][y]
                for x in range(0, 12):
                    for y in range(0, 3):
                        rozlozenie_cur[x][y] = rozlozenie_new[x][y]
                ecur = eval(cur)
        temp = delta_e / 10000
        pokles = temp / 10000
        delta_temp += temp
    delta_temp /= 10
    temp = delta_temp
    pokles = temp / 10000
    print ("%f10" % delta_temp)
    #######################################################################################################
    #2 zbehnutie zihania + navrat priemernych hodnot
    priemerny_vysledok = 0
    for iterator in range(0, 1000):
        Hracia_plocha = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        rozlozenie_cur = [[0 for x in range(0, 3)] for y in range(0, 12)]

        rozlozenie_best = [[0 for x in range(0, 3)] for y in range(0, 12)]
        for xModul in range(0, len(Moduly)):
            #generuj poziciu
            y = random.randrange(4, 17)
            #generuj otocenie
            pocet_otoceni = len(Moduly[xModul])
            xOtocenie = random.randrange(0, pocet_otoceni)
            zapis_modul(x, y, xModul, xOtocenie, Hracia_plocha)
            rozlozenie_cur[xModul][0] = x
            rozlozenie_cur[xModul][1] = y
            rozlozenie_cur[xModul][2] = xOtocenie
            rozlozenie_best[xModul][0] = x
            rozlozenie_best[xModul][1] = y
            rozlozenie_best[xModul][2] = xOtocenie
        cur = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        for x in range(4, 9):
            for y in range(4, 16):
                cur[x][y] = Hracia_plocha[x][y]
                #    vypis_plochu(cur)
        best = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        for x in range(4, 9):
            for y in range(4, 16):
                best[x][y] = Hracia_plocha[x][y]
            #ebest = energy(best)
        ebest = energy2(best)
        #ecur = energy(cur)
        ecur = energy2(cur)
        emin = 0
        temp = 50
        halp = 0
        #    new_plocha = Hracia_plocha
        while temp > 0.001:
            temp -= 0.001
            new_plocha = [[-1 for x in range(0, 22)] for y in range(0, 15)]
            for x in range(4, 9):
                for y in range(4, 16):
                    new_plocha[x][y] = cur[x][y]
            rozlozenie_new = [[0 for x in range(0, 3)] for y in range(0, 12)]
            for x in range(0, 12):
                for y in range(0, 3):
                    rozlozenie_new[x][y] = rozlozenie_cur[x][y]
            generuj(rozlozenie_new, new_plocha)
            enew = eval(new_plocha)
            probability = prob(ecur, enew, temp)
            randomnumber = float(random.randrange(0, 10000000000)) / 10000000000
            if probability > randomnumber:
                for x in range(4, 9):
                    for y in range(4, 16):
                        cur[x][y] = new_plocha[x][y]
                for x in range(0, 12):
                    for y in range(0, 3):
                        rozlozenie_cur[x][y] = rozlozenie_new[x][y]
                ecur = eval(cur)
                if ecur < ebest:
                    for x in range(4, 9):
                        for y in range(4, 16):
                            best[x][y] = cur[x][y]
                    for x in range(0, 12):
                        for y in range(0, 3):
                            rozlozenie_best[x][y] = rozlozenie_cur[x][y]
                    ebest = eval(best)

        ebest = finalenergy(best)
        vypis_plochu(best)
        priemerny_vysledok += ebest
        print ("ebest: %d" % ebest)
    print("%f10" % priemerny_vysledok / 1000)


#test(energy)


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.hracia_plocha1 = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        self.hracia_plocha2 = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        self.hracia_plocha2[4][8] = 0
        self.hracia_plocha2[5][8] = 0
        self.hracia_plocha2[6][8] = 0
        self.hracia_plocha2[7][8] = 0
        self.hracia_plocha2[8][8] = 0
        self.hracia_plocha3 = [[-1 for x in range(0, 22)] for y in range(0, 15)]
        self.hracia_plocha3[4][8] = 0
        self.hracia_plocha3[5][8] = 0
        self.hracia_plocha3[6][8] = 0
        self.hracia_plocha3[7][8] = 0
        self.hracia_plocha3[8][8] = 0
        self.hracia_plocha3[6][4] = 0
        self.hracia_plocha3[6][5] = 0
        self.hracia_plocha3[6][6] = 0
        self.hracia_plocha3[6][7] = 0
        self.hracia_plocha4 = [[-1 for x in range(0, 22)] for y in range(0, 15)]
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
        self.hracia_plocha5 = [[-1 for x in range(0, 22)] for y in range(0, 15)]
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
            pocet_otoceni = len(Moduly[xModul])
            xOtocenie = random.randrange(0, pocet_otoceni)
            vyber = (xModul, xOtocenie, x, y)
            if vyber not in boli:
                boli.add(vyber)
        print (len(boli))
        self.assertEqual(len(boli), 3780)
        for x in range(0, 12):
            for y in range(0, len(Moduly[x])):
                for z in range (4, 9):
                    for w in range (4, 16):
                        vyber = (x, y, z, w)
                        if vyber not in boli:
                            print(vyber)
        print ("done")



if __name__ == '__main__':
    unittest.main()
