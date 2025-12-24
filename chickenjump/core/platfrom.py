import random
from data.konstanta import *

def init_platform():
    return [
        [175,480,70,10,0,True],
        [85,370,70,10,0,True],
        [265,370,70,10,0,True],
        [175,260,70,10,0,True],
        [85,150,70,10,0,True],
        [265,150,70,10,0,True],
        [175,40,70,10,0,True]
    ]

def platform_acak(y):
    return [
        random.randint(20, LEBAR - LEBAR_PLATFORM - 20),
        y,
        70,
        10,
        random.choice([-1, 1]),
        False
    ]

def gerak_platform(platforms, skor):
    if 150 <= skor < 350:
        for p in platforms:
            if p[4] != 0:
                p[0] += p[4] * 2
                if p[0] <= 0 or p[0] >= LEBAR - 70:
                    p[4] *= -1
