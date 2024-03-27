import random

ens = ()
for _ in range(10):
    i = random.randint(0,5)
    ens += (i,)
print(ens)

kah = ()
for _ in range(10):
    j = random.randint(-5, 0)
    kah += (j,)
print(kah)

kolm = ens + kah
print(kolm)
print(kolm.count(0))
