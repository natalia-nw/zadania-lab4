# zad 1
import random

rand = []
i = 0
while i != 10:
    r = random.randint(0, 100)
    if r % 4 == 0:
        rand.append(r)
        i += 1
podzielne = open('zad1.txt', 'a')
for elem in rand:
    podzielne.write(str(elem) + ' ')
podzielne.close()

# zad 2
with open('zad1.txt', 'r') as podzielne:
    liczby = podzielne.readlines()
    liczby = [elem[:-1] for elem in liczby]
    print(liczby)

# zad 3
with open('plik.txt', 'a') as plik:
    for elem in 'cokolwiek':
        plik.write(elem + ' ')

with open('plik.txt', 'r') as x:
    for elem in x:
        print(elem[:-1])

# zad 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return f'{self.ilosc} {self.jednostka_miary}'

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

cl = NaZakupy('kurczak', 0.5, 'kg', 23)

print(cl.wyswietl_produkt())
print(cl.ile_produktu())
print(cl.ile_kosztuje())

# zad 5
class CiagiArytmetyczne:
    ciag = []
    ilosc = 0
    a1 = 0
    r = 0
    def wyswietl_dane(self):
        return f'Lista elementów: {self.ciag}'

    def pobierz_parametry(self):
        self.a1 = int(input("Podaj pierwszy element ciągu: "))
        self.r = int(input("Podaj różnicę ciągu: "))
        self.ilosc = int(input("Podaj ilość elementów ciągu do wygenerowania: "))

    def policz_sume(self):
        return f'Suma elementów: {sum(self.ciag)}'

    def policz_elementy(self):
        self.ciag.append(self.a1)
        for x in range(1, self.ilosc):
            self.ciag.append(self.ciag[x - 1] + self.r)


kl = CiagiArytmetyczne()

kl.pobierz_parametry()
kl.policz_elementy()
print(kl.wyswietl_dane())
print(kl.policz_sume())

# zad 6
class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        return f'({self.x}, {self.y})'


robaczek = robaczek(0, 0, 1)

robaczek.idz_w_lewo(5)
robaczek.idz_w_prawo(18)
robaczek.idz_w_gore(1)
robaczek.idz_w_dol(8)
print(robaczek.pokaz_gdzie_jestes())