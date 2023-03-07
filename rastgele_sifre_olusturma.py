import random
import string

def rastgelesifre(uzunluk):
    harfler = string.ascii_uppercase
    sonuc = "".join(random.choice(harfler) for i in range(uzunluk))
    print("Rastgele sayı uzunluğu", uzunluk,"ve rastgele şifre:", sonuc)

rastgelesifre(15)
