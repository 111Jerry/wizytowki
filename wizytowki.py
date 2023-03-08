import sys
import logging

class VCard:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.e_mail = e_mail
nowak = VCard(imie="Jan", nazwisko="Nowak", nazwa_firmy="Luxmed", stanowisko="manager", e_mail = "jnowak@luxmed.pl")
print(nowak)