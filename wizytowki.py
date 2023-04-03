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
    
    
def contact(self):
        print(f"Wybieram numer +48", self.telefon, "i dzwonię do ", self.imie, self.nazwisko)

def create_contacts(typ_of_contact, number):
        if typ_of_contact == 1:
            for i in range(number):
                imie = fake.first_name()
                nazwisko = fake.last_name()
                telefon = fake.phone_number()
                e_mail = fake.email()

                customer_prv = BaseContact(imie, nazwisko, telefon, e_mail)
                contact(customer_prv)
                #print(customer_prv)
                #print(f"{imie} {nazwisko}, {telefon}, {e_mail}")
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
                contact(customer_business)
                #print(customer_business)
                #print(f"{imie} {nazwisko}, {telefon}, {e_mail}, {stanowisko}, {firma}, {telefon_firmowy}")
        return

if __name__ == "__main__":
    typ_of_contact = int(input("Wciśnij 1, aby wygenerować wizytówki z danymi prywatnymi lub 2, aby wygenerować wizytówki firmowe: "))
    number = int(input("Podaj liczbę wizytówek: "))
    create_contacts(typ_of_contact, number)
    
