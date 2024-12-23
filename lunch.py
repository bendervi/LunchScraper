import requests
from colorama import Fore
from bs4 import BeautifulSoup


meny = 'https://chalmerskonferens.se/sv/lunchmenyer-johanneberg-2/'

response = requests.get(meny)

soup = BeautifulSoup(response.text, 'html.parser')
kres = soup.find('div', class_='siteorigin-widget-tinymce textwidget')

text = kres.get_text()

# Splits the menus from the text (very ugly!!!)
prices = text.split("GREENS:")[0]
# Greens menu is all the text from greens to street food
greens = text.split("GREENS:")[1].split("STREET FOOD:", 1)[0].replace(".", "")
street = text.split("STREET FOOD:")[1].split("NORDIC:", 1)[0].replace(".", "")
nordic = text.split("NORDIC:")[1].replace(".", "")

# List comprehension to remove emissions, as they were not 
# interesting to me (sorry!!!)
greens = ''.join([i for i in greens if not i.isdigit()])
street = ''.join([i for i in street if not i.isdigit()])
nordic = ''.join([i for i in nordic if not i.isdigit()])

# Removes the left over emissionstext
greensMenu = greens.split("COe", 1)[0]
streetMenu = street.split("COe", 1)[0]
nordicMenu = nordic.split("COe", 1)[0]

# ALLERGIES
allergies = {
    'milk': 'https://stvmplateimpact.blob.core.windows.net/allergens/milk.svg',
    'gluten': 'https://stvmplateimpact.blob.core.windows.net/allergens/gluten.svg',
    'eggs': 'https://stvmplateimpact.blob.core.windows.net/allergens/eggs.svg',
    'sulphites': 'https://stvmplateimpact.blob.core.windows.net/allergens/sulphites.svg',
    'celery': 'https://stvmplateimpact.blob.core.windows.net/allergens/sulphites.svg',
}

#print(kres)
allergyDivs = kres.find_all('td')
gDiv = allergyDivs[3]
sDiv = allergyDivs[8]
nDiv = allergyDivs[13] 


gDivImgs = gDiv.find_all("img", src=True)
sDivImgs = sDiv.find_all("img", src=True)
nDivImgs = nDiv.find_all("img", src=True)

greenAllergies = ""

# check if any image matches to the allergy list
for img in gDivImgs:
    img_src = img['src']  # Get the src attribute
    for allergy, link in allergies.items():
        if img_src == link:
            greenAllergies += allergy.capitalize() + " "

streetAllergies = ""


for img in sDivImgs:
    img_src = img['src']  
    for allergy, link in allergies.items():
        if img_src == link:
            streetAllergies += allergy.capitalize() + " "

nordicAllergies = ""


for img in nDivImgs:
    img_src = img['src']  
    for allergy, link in allergies.items():
        if img_src == link:
            nordicAllergies += allergy.capitalize() + " "
            

print()
print(Fore.GREEN + "Greens: " +  Fore.BLACK + greensMenu)
print(Fore.GREEN + "Allergies: " +  Fore.BLACK + greenAllergies.strip())
print(Fore.RED + "Street: " +  Fore.BLACK + streetMenu)
print(Fore.RED + "Allergies: " + Fore.BLACK + streetAllergies.strip())
print(Fore.BLUE + "Nordic: " +  Fore.BLACK + nordicMenu)
print(Fore.BLUE + "Allergies: " +  Fore.BLACK + nordicAllergies.strip())
print()

print("Enter the allergen to filter by allergies (milk/gluten/eggs/sulphites/celery) : ")
allergen = input()
allergen = allergen.strip().lower()

print()

counter = 0
if allergen not in greenAllergies.lower().split():
    print(Fore.GREEN + "Greens: " + Fore.BLACK + greensMenu)
    counter += 1
if allergen not in streetAllergies.lower().split():
    print(Fore.RED + "Street: " + Fore.BLACK + streetMenu)
    counter += 1
if allergen not in nordicAllergies.lower().split():
    print(Fore.BLUE + "Nordic: " + Fore.BLACK + nordicMenu)
    counter += 1

if counter == 0:
    print("No available food for you today :( Try your luck at Store!")

print()