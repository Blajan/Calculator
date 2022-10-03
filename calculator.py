from math import pow, floor, log
from datetime import *

while True:
    try:
        optiune = int(input("Alege una dintre optiuni: \n1. Adunare\n2. Scadere\n3. Impartire\n4. Inmultire\n5. Ridicare la putere\n6. Rest\n7. Logaritm\n"))
    except ValueError:
        print("Va rugam sa introduceti una dintre optiunile valabile")
    # Adunare
    if optiune == int(1):
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        rezultat = numar1 + numar2
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Scadere
    elif optiune == 2:
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        rezultat = numar1 - numar2
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Impartire
    elif optiune == 3:
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        rezultat = numar1 / numar2
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Inmultire
    elif optiune == 4:
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        rezultat = numar1 * numar2
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Ridicare la putere
    elif optiune == 5:
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        rezultat = pow(numar1, numar2)
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Rest
    elif optiune == 6:
        numar1 = int(input("Introduceti primul numar: "))
        numar2 = int(input("Introduceti al doilea numar: "))
        faraFloat = floor(numar1 / numar2)
        rezultat = numar1 % numar2
        print(f"Rezultatul este {faraFloat} rest {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Logaritm
    elif optiune == 7:
        numar1 = int(input("Introduceti numarul: "))
        rezultat = log(numar1, 2)
        print(f"Rezultatul este {int(rezultat)}")
        maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))
        if maiIncerci == "y":
            continue
        elif maiIncerci == "n":
            break
        while maiIncerci != "y" and maiIncerci != "n":
            maiIncerci = str(input("Doresti sa incerci si alta operatiune (y/n)?"))

    # Alta optiune
    else:
        print("Va rugam sa introduceti una dintre optiunile valabile")
        with open("C:\\Users\\40747\\PycharmProjects\\pythonProject6\\memorie.txt", "a") as adaugare:
            print(adaugare.write(f"\nAi ales optiunea {optiune} in data {datetime.now()}"))
        adaugare.close()
        listaMemorie = []
        with open("C:\\Users\\40747\\PycharmProjects\\pythonProject6\\memorie.txt", "r") as citire:
            for i in citire.readlines():
                listaMemorie.append(i)
            print(listaMemorie[-1])
        continue