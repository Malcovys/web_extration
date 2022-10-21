import csv
import requests
from bs4 import BeautifulSoup

def addSreingInArray(block):
   arrayString = []
   for list in block:
      arrayString.append(list.string)
   return arrayString
         
        

url = ""

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page_get_article_titles = soup.find_all("", class_="")
page_get_decription = soup.find_all("", class_="")

string_titles = addSreingInArray(page_get_article_titles)
string_descriptions = addSreingInArray(page_get_decription)

# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for titre, description in zip(string_titles, string_descriptions):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [titre, description]
      writer.writerow(ligne)
