import random

pole = [] #Prázné pole

skore = 0 #Počáteční skóre hráče
skore = int(skore)

zivoty = 2
zivoty = int(zivoty)

#animace
import time
import sys

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\rNačítání.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
print("\nNačteno!")

#Hlavní smyčka hry, počet kol je náhodně vybrán mezi 1 a 15
for i in range(random.randint(1, 15)):

    print("-------------------------------------------")
    print("◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌ ROUND",i+1, "◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌") # Výpis čísla kola
    print("-------------------------------------------")

    #Smyčka pro generování náhodných čísel do pole
    for j in range(random.randint(1, 10)):
        pole.append(random.randint(1, 10))

    print("Jaká je délka pole ?\n",pole) #Výpis pole a otázka na jeho délku
    print("-------------------------------------------")

    delka = int(len(pole)) #Výpočet délky pole

    odpoved = input("۞ ")
    odpoved = int(odpoved)
    print("-------------------------------------------")

    #Kontrola
    if odpoved == delka:
       skore = skore + 1
       print("Správně !!\nTvé skore: ", skore, "\nTvé životy: ", zivoty)
    else:
       zivoty = zivoty - 1
       print("Špatně! \nTvé skore:", skore, "\nTvé životy: ", zivoty)
    
    if zivoty == 0:
        break

print("Konec hry, tvé skore:",skore) #End
