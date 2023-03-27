"""
Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa
parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
"""
import sys
import logging
from faker import Faker
fake = Faker()
class BaseContact:
    def __init__(self, imie, nazwisko, telefon, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.e_mail = e_mail

        #Variables
        self._label_lenght = 0
    
    def contact(self):
        print(f"Wybieram numer +48", self.telefon, "i dzwonię do ", self.imie, self.nazwisko)
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.telefon} {self.e_mail}"
    
    def __repr__(self):
        return f"BaseContact(imie={self.imie} nazwisko={self.nazwisko}, telefon={self.telefon}, e_mail={self.e_mail})"

    @property
    def label_lenght(self):
        self._label_lenght = len(self.imie) + len(self.nazwisko) +1
        print(self._label_lenght)
        return self._label_lenght
    
    
class BusinessContacts(BaseContact):
    def __init__(self, stanowisko, firma, telefon_firmowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_firmowy = telefon_firmowy
    
    def businesscontacts(self):
        print(f"Wybieram numer firmowy +48", self.telefon_firmowy, "i dzwonię do ", self.imie, self.nazwisko)
"""
Baza kontaktów z danymi pryw.
jnowak = BaseContact(imie="Jan", nazwisko="Nowak", telefon=728443113, e_mail = "jnowak@luxmed.pl")
kraczek = BaseContact(imie="Krzysztof", nazwisko="Raczek", telefon=600443113, e_mail = "kraczek@o2.pl")
rdabrowski = BaseContact(imie="Rafał", nazwisko="Dąbrowski", telefon=606221213, e_mail = "rdabrowski@wp.pl")
jkrolik = BaseContact(imie="Jrosław", nazwisko="Królik", telefon=723515234, e_mail = "jkrolik@tlen.pl")
mzabielny = BaseContact(imie="Maciek", nazwisko="Zabielny", telefon=503234765, e_mail = "mzabielny@gmail.com")

Baza kontaktów firmowych
akowalski = BusinessContacts(imie="Andrzej", nazwisko="Kowalski", telefon=723445773, stanowisko="senior specialist", firma="Luxmed", telefon_firmowy=727110234, e_mail="akowalski@luxmed.pl")
rmucha = BusinessContacts(imie="Robert", nazwisko="Mucha", telefon=602773443, stanowisko="dyspozytor", firma="STEKOP", telefon_firmowy=722443567, e_mail="rmucha@stekop.pl")
amaciazek = BusinessContacts(imie="Andrzej", nazwisko="Maciążek", telefon=600713234, stanowisko="main specialist", firma="Commarch", telefon_firmowy=728443562, e_mail="amaciazek@commarch.eu")
wmieszko = BusinessContacts(imie="Wojciech", nazwisko="Mieszko", telefon=500789234, stanowisko="senior specialist", firma="Urząd Dozoru Technicznego", telefon_firmowy=727500276, e_mail="wmieszko@udt.pl")
wmitura = BusinessContacts(imie="Wojciech", nazwisko="Mitura", telefon=723446227, stanowisko="kierowca", firma="CCC", telefon_firmowy=723221364, e_mail="wmitura@ccc.eu")
sbierdzi = BusinessContacts(imie="Sławomir", nazwisko="Bierdzi", telefon=504998737, stanowisko="specialist", firma="Urząd Lotnictwa Cywilnego", telefon_firmowy=690270576, e_mail="sbierdzi@ulc.com")

akowalski.label_lenght
jnowak.contact()
akowalski.businesscontacts()
akowalski.contact()
"""
private_contact = []
business_contact = []

def create_contacts(typ_of_contact, number):
        if typ_of_contact == 1:
            for i in range(number):
                imie = fake.first_name()
                nazwisko = fake.last_name()
                telefon = fake.phone_number()
                e_mail = fake.email()

                customer_prv = BaseContact(imie, nazwisko, telefon, e_mail)
                private_contact.append(customer_prv)
                print(customer_prv)
                #print(private_contact)
                print(f"{imie} {nazwisko}, {telefon}, {e_mail}")
        elif typ_of_contact == 2:
            for i in range(number):  
                imie = fake.first_name()
                nazwisko = fake.last_name()
                telefon = fake.phone_number()
                e_mail = fake.email()
                stanowisko = fake.job()
                firma = fake.company()
                telefon_firmowy = fake.phone_number()

                customer_business = BusinessContacts(imie, nazwisko, telefon, stanowisko, firma, telefon_firmowy, e_mail)
                business_contact.append(customer_business)
                print(customer_business)
                #print(business_contact)
                print(f"{imie} {nazwisko}, {telefon}, {e_mail}, {stanowisko}, {firma}, {telefon_firmowy}")
        return

if __name__ == "__main__":
    typ_of_contact = int(input("Wciśnij 1, aby wygenerować wizytówki z danymi prywatnymi lub 2, aby wygenerować wizytówki firmowe: "))
    number = int(input("Podaj liczbę wizytówek: "))
    create_contacts(typ_of_contact, number)
    #print(end)
