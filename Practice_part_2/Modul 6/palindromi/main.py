NO_OF_CHARS = 256

def voiPalindromi(st):
    count = [0] * (NO_OF_CHARS)
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
    kumm = 0

    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            kumm += 1

        if (kumm > 1):
            return False
    return True

uusi_s = input('Syötä rivi: ')

if (voiPalindromi(uusi_s)):
    print('Kyllä, rivista on mahdollista tehdä palindromia')
else:
    print('Ei. Rivista ei voi tehdä palindromia.')

