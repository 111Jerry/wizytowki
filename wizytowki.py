"""
Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać
podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact)
rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.

Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci
“Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu,
a wizytówka bazowa prywatny.

Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.

Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa
parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
"""
import sys
import logging
#from faker import Faker
#fake = Faker()
class BaseContact:
    def __init__(self, imie, nazwisko, telefon, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.e_mail = e_mail

        #Variables
        self._label_lenght = len(imie) + len(nazwisko) +1
    
    def contact(self):
        print(f"Wybieram numer +48", self.telefon, "i dzwonię do ", self.imie, self.nazwisko)
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.telefon} {self.e_mail}"
    
    def __repr__(self):
        return f"BaseContact(imie={self.imie} nazwisko={self.nazwisko}, telefon={self.telefon}, e_mail={self.e_mail})"

    @property
    def label_lenght(self):
        return self._label_lenght
    
    
class BusinessContacts(BaseContact):
    def __init__(self, stanowisko, firma, telefon_firmowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_firmowy = telefon_firmowy
    
    def businesscontacts(self):
        print(f"Wybieram numer firmowy +48", self.telefon_firmowy, "i dzwonię do ", self.imie, self.nazwisko)

jnowak = BaseContact(imie="Jan", nazwisko="Nowak", telefon=728443113, e_mail = "jnowak@luxmed.pl")
akowalski = BusinessContacts(imie="Andrzej", nazwisko="Kowalski", telefon=723445773, stanowisko="senior specialist", firma="Luxmed", telefon_firmowy=727110234, e_mail="akowalski@luxmed.pl")

print(akowalski.label_lenght)
jnowak.contact()
akowalski.businesscontacts()
akowalski.contact()

def create_contacts(self):
        input(__name__)
"""
akowalski = VCard(imie="Andrzej", nazwisko="Kowalski", nazwa_firmy="Commarch", stanowisko="senior specialist", e_mail="akowalski@commarch.com")
print(jnowak.stanowisko)
akowalski = VCard(imie="Andrzej", nazwisko="Kowalski", nazwa_firmy="Commarch", stanowisko="senior specialist", e_mail="akowalski@commarch.com")
print(akowalski.stanowisko)
aklin = VCard(imie="Andrzej", nazwisko="Klin", nazwa_firmy="Merlin", stanowisko="junior specialist", e_mail = "aklin@merlin.pl")
print(aklin.stanowisko)
mstelmaszczyk = VCard(imie="Mirosław", nazwisko="Stelmaszczyk", nazwa_firmy="Stekop", stanowisko="manager", e_mail = "mstelmaszczyk@stekop.pl")
print(mstelmaszczyk.stanowisko)
bniewiadomski = VCard(imie="Bogdan", nazwisko="Niewiadomski", nazwa_firmy="Solid Security", stanowisko="specialist", e_mail = "bniewiadomski@solid.eu")
print(bniewiadomski.stanowisko)
"""