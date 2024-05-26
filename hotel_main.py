from abc import ABC, abstractmethod
from datetime import datetime, date

# Absztrakt Szoba osztály
class Szoba(ABC):
    szobaLista = []
    szobaAr = 5000
    
    def __init__(self,szobaSzam: int) -> None:
        # assert szobaAr >= 0, "Téves ár!"
        self.szobaSzam = szobaSzam
        self.szobaAr = Szoba.szobaAr
        self.extrak = []
        self.foglalasok = []
        self.szobaAgy = None
        Szoba.szobaLista.append(self)

    def __repr__(self):
        return f"Szoba_{self.szobaSzam}: Ágyak száma: {self.szobaAgy}, Ár: {self.szobaAr}, Extrák: {self.extrak}, Foglalások: {self.foglalasok}"

    @abstractmethod
    def ujszobaAr(self, szobaAr):
        self.szobaAr = szobaAr

    @abstractmethod
    def szobaExtra(self, extra: str, felar: int):
        self.extrak.append(extra)    
        self.szobaAr += felar

# Egy ágyas szoba osztály
class EgyagyasSzoba(Szoba):
    szobaAr = 10000
    
    def __init__(self, szobaSzam: int):
        super().__init__(szobaSzam)
        self.szobaAr = EgyagyasSzoba.szobaAr
        self.szobaAgy = 1
       
    def ujszobaAr(self, szobaAr):
        super().szobaAr(self, szobaAr)

    def szobaExtra(self, extra: str, felar: int):
        super().szobaExtra(extra, felar)    

# Két ágyas szoba osztály
class KetagyasSzoba(Szoba):
    szobaAr = 16000
    
    def __init__(self, szobaSzam: int):
        super().__init__(szobaSzam)
        self.szobaAr = KetagyasSzoba.szobaAr
        self.szobaAgy = 2
    
    def ujszobaAr(self, szobaAr):
        super().szobaAr(self, szobaAr)

    def szobaExtra(self, extra: str, felar: int):
        super().szobaExtra(extra, felar) 
    
#Foglalás osztály
class Foglalas:
    
    def __init__(self, szobaSzam, datum):
        self.datum = datum
        datum = datetime.strptime(datum, '%Y-%m-%d').date()
        self.szobaSzam = szobaSzam
                
#Szálloda osztály
class Szalloda(EgyagyasSzoba,KetagyasSzoba):
    
    def __init__(self, szallodaNev):
        self.szallodaNev = szallodaNev
        self.szobakSzama = 0
        self.szobaLista = []
        
    # Szoba létrehozás
    def ujSzoba(self, szoba):
        self.szobaLista.append(szoba)
        self.szobakSzama += 1   
    
    # Szobafoglalás 
    def foglal(self, foglalas):              
        if foglalas.datum not in self.szobaLista[foglalas.szobaSzam - 1].foglalasok:
            self.szobaLista[foglalas.szobaSzam - 1].foglalasok.append(foglalas.datum)            
            if __name__ == "__main__":
                print(f"Sikeres foglalás!")
                print(f"A foglalás dátuma: {foglalas.datum}")
                print(f"A szoba  ára: {self.szobaLista[foglalas.szobaSzam - 1].szobaAr}")
                print(f"A szobában az ágyak száma: {self.szobaLista[foglalas.szobaSzam - 1].szobaAgy}")
                print(f"A foglalt szoba: {self.szobaLista[foglalas.szobaSzam - 1].szobaSzam}")            
        else:
            if __name__ == "__main__":
                print("A dátumra a szoba már foglalt!")   
    
    # Foglalások listázása
    def foglalasListazas(self):        
        print(f"\nAz {self.szallodaNev} szálloda aktuális foglalásai:")
        for szoba in self.szobaLista:
            for foglalas in szoba.foglalasok:
                print(f"Szoba_{szoba.szobaSzam} foglalt: {foglalas}")
    
    # Foglalások törlése
    def foglalasTorles(self, szoba, datum):
        datum = datetime.strptime(datum, '%Y-%m-%d').date()
        if str(datum) in self.szobaLista[szoba - 1].foglalasok:
            self.szobaLista[szoba - 1].foglalasok.remove(str(datum))           
            if __name__ == "__main__":
                print("Sikeres foglalás törlés")
            self.foglalasListazas()
        else:
            if __name__ == "__main__":
                print("A törölni kívánt foglalás dátumán a szoba nem foglalt!")

# Futtatás előtti feltöltés: Szálloda 
szallo = Szalloda("Objektum")

# Futtatás előtti feltöltés: Szobák 
szallo.ujSzoba(EgyagyasSzoba(1))
szallo.ujSzoba(EgyagyasSzoba(2))
szallo.ujSzoba(KetagyasSzoba(3))

szallo.szobaLista[1].szobaExtra("Minibár", 500)
szallo.szobaLista[2].szobaExtra("Erkély", 1000)

# Futtatás előtti feltöltés: Foglalások
szallo.foglal(Foglalas(1, '2024-06-16'))
szallo.foglal(Foglalas(1, '2024-06-17'))
szallo.foglal(Foglalas(2, '2024-06-20'))
szallo.foglal(Foglalas(3, '2024-07-20'))
szallo.foglal(Foglalas(3, '2024-07-21'))

# print(szallo.foglalasListazas)
print(szallo.szobaLista)

# szallo.foglalasTorles(1,"2024-06-16")
# print(szallo.szobaLista)
# szallo.foglalasTorles(1,"2024-06-17")
# print(szallo.szobaLista)
szallo.foglalasListazas()