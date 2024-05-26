from hotel_main import *
from datetime import datetime, date

print(f"\nÜdvözöljük az {szallo.szallodaNev} szálloda CLI felületén!")

while True:
    print("\n***************************************")
    print("Válasszon a lehetséges műveletek közül!")
    print("\n1: Foglalások listázása.")
    print("2: Szoba foglalása.")
    print("3: Foglalás lemondása.")
    print("x: Kilépés.")

    valasztottMenu = input("\nVálasztott menüpontja: ")
    print("------------------------")
    
    # Foglalások listázássa
    if valasztottMenu == "1":
        szallo.foglalasListazas()
    
    # Foglalás
    elif valasztottMenu == "2":       
        nap = input("\nAdd meg a foglalni kívánt dátumot \"YYYY-MM-DD\" formátumban (pl.: 2024-08-16)")
        try:
            datum = datetime.strptime(nap, '%Y-%m-%d').date()
            if datum < datetime.now().date():
                print("\nTéves foglalási dátum! \nAdjon meg későbbi dátumot!")
            else:
                print("\nVálasszon szobáink közül: \n")
                for szoba in szallo.szobaLista:
                    print(szoba)
                szoba = int(input("\nVálassza ki a szoba számát: "))
                
                if nap in szallo.szobaLista[szoba - 1].foglalasok:
                    print(f"\nA választott szoba a {nap} dátumon sajnos már foglalt!")
                else:
                    szallo.foglal(Foglalas(szoba, nap))
                    print("\n*****************************************************************")
                    print("Sikeres fodglalas!")
                    print(f"A foglalás dátuma: {datum}")
                    print(f"A foglalt szoba száma: {szallo.szobaLista[szoba - 1].szobaSzam}")
                    print(f"A szoba  ára: {szallo.szobaLista[szoba - 1].szobaAr} forint")
                    print(f"A szobában az ágyak száma: {szallo.szobaLista[szoba - 1].szobaAgy}")
                    print("*****************************************************************")
        except ValueError:
            print("\nTéves dátum vagy szobaszám formátumot adott meg")
    
    # Foglalások törlése
    elif valasztottMenu == "3":
        print("\nVálassza ki melyik foglalást szeretné törölni!")
        szallo.foglalasListazas()
        nap = input("\nAdd meg a törölni kívánt dátumot \"YYYY-MM-DD\" formátumban (pl.: 2024-08-16)")
        
        try:            
            datum = datetime.strptime(nap, '%Y-%m-%d').date()       
            szoba = int(input("\nVálassza ki a szoba számát: "))
            # print(szallo.szobaLista[szoba - 1].foglalasok)
            if nap in szallo.szobaLista[szoba - 1].foglalasok:
                szallo.szobaLista[szoba - 1].foglalasok.remove(nap)
                # szallo.foglalasLista
                print("\nSikeres törölte a foglalást!")
                szallo.foglalasListazas()
            else:
                print(f"\nA választott Szoba_{szoba} a {datum} dátumon nem tartalmaz foglalást!")           
        except ValueError:
            print("\nTéves dátum vagy szobaszám formátumot adott meg!")
             
    # Kilépés
    elif valasztottMenu == "x":
        print("\nKöszönjük, viszontlátásra!\n")
        exit()

    # Téves menüpont választás
    else:
        print("\nTéves menüpont kiválasztás!")
