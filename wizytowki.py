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
#from faker import Faker
class VCard:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.e_mail = e_mail

        self._lenght_name = 0
    
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.nazwa_firmy} {self.stanowisko}'
    
    def __repr__(self):
        return f"VCard(imie={self.imie} nazwisko={self.nazwisko}, nazwa_firmy={self.nazwa_firmy}, stanowisko={self.stanowisko}, e_mail={self.e_mail})"

    def contact(self):
        print(f"Wybieram kontakt:  ")
"""
jnowak = VCard(imie="Jan", nazwisko="Nowak", nazwa_firmy="Luxmed", stanowisko="manager", e_mail = "jnowak@luxmed.pl")
print(jnowak.stanowisko)
akowalski = VCard(imie="Andrzej", nazwisko="Kowalski", nazwa_firmy="Commarch", stanowisko="senior specialist", e_mail="akowalski@commarch.com")
print(akowalski.stanowisko)
aklin = VCard(imie="Andrzej", nazwisko="Klin", nazwa_firmy="Merlin", stanowisko="junior specialist", e_mail = "aklin@merlin.pl")
print(aklin.stanowisko)
mstelmaszczyk = VCard(imie="Mirosław", nazwisko="Stelmaszczyk", nazwa_firmy="Stekop", stanowisko="manager", e_mail = "mstelmaszczyk@stekop.pl")
print(mstelmaszczyk.stanowisko)
bniewiadomski = VCard(imie="Bogdan", nazwisko="Niewiadomski", nazwa_firmy="Solid Security", stanowisko="specialist", e_mail = "bniewiadomski@solid.eu")
print(bniewiadomski.stanowisko)


print(jnowak)
"""