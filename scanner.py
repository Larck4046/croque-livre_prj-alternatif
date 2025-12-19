import requests as r
from bs4 import BeautifulSoup
# Aucune idée pourquoi j'ai décidé de faire une class btw
class Scan:
    def __init__(self,code):
        self.code = code


    def googleapi(self):
        info = r.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{self.code}").json()
        titre = info['items'][0]['volumeInfo']['title']
        auteur = info['items'][0]['volumeInfo']['authors'][0]
        while True:
            correct = input(f"{titre} par {auteur}\nOui/Non (O/N)?\n").strip().lower()
            if correct == "o":
                return True
            elif correct == "n":
                return False
            else:
                print("Invalid Input")
                continue
    def bookfinder(self):
        info = r.get(f"https://www.bookfinder.com/isbn/{self.code}/")
        magnifique_soupe = BeautifulSoup(info.content, 'html.parser')
        titre = magnifique_soupe.find("h1", class_="text-xl font-bold text-blue-800 mb-2")
        aut = magnifique_soupe.find("a", class_="text-blue-700 underline font-medium").text
        space = aut.find(",")
        auteur = f"{aut[space + 2:]} {aut[:space]}"
        input(f"{titre.text} par {auteur}")
S = Scan(input("Wsp scan le livre twin\n"))
if S.googleapi():
    print("Cool bravo tu peux payer juste ici")


else:
    S.bookfinder()
    print("bookfinder time")


    # Test ISBN: 9782072947407
