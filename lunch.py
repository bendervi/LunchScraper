import requests
import json
from bs4 import BeautifulSoup


meny = 'https://chalmerskonferens.se/sv/lunchmenyer-johanneberg-2/'

response = requests.get(meny)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify)

kres = soup.find('div', class_='siteorigin-widget-tinymce textwidget')

text = kres.get_text();

prices = text.split("GREENS:")[0]
greens = text.split("GREENS:")[1].split("STREET FOOD:", 1)[0].replace(".", "")
street = text.split("STREET FOOD:")[1].split("NORDIC:", 1)[0].replace(".", "")
nordic = text.split("NORDIC:")[1].replace(".", "")

greens = ''.join([i for i in greens if not i.isdigit()])
street = ''.join([i for i in street if not i.isdigit()])
nordic = ''.join([i for i in nordic if not i.isdigit()])

greensMenu = greens.split("COe", 1)[0]
streetMenu = street.split("COe", 1)[0]
nordicMenu = nordic.split("COe", 1)[0]

# ALLERGIES
milk = 'https://stvmplateimpact.blob.core.windows.net/allergens/milk.svg'
gluten = 'https://stvmplateimpact.blob.core.windows.net/allergens/gluten.svg'
eggs = 'https://stvmplateimpact.blob.core.windows.net/allergens/eggs.svg'
suplhites = 'https://stvmplateimpact.blob.core.windows.net/allergens/sulphites.svg'
celery = 'https://stvmplateimpact.blob.core.windows.net/allergens/sulphites.svg'

print("Greens: " + greensMenu)
print("Street: " + streetMenu)
print("Nordic: " + nordicMenu)
