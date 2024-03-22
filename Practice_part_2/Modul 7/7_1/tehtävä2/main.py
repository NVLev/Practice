import math

def side_full (r, h):
    side = round(float(2 * 3.14 * r * h), 2)
    s = float(math.pi * r * 2)
    full = round(side + 2 * s, 2)
    return (side, full)

uus_r = float(input('Syötä radius: '))
uus_h = float(input('Syötä pituus: '))
tuple = side_full (uus_r, uus_h)
print(tuple)

