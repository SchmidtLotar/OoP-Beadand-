from datetime import datetime

# Absztrakt Járat osztály
class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaad(self, jarat):
        self.jaratok.append(jarat)

class JegyFoglalas:
    def __init__(self, jarat, datum, foglalo_neve):
        self.jarat = jarat
        self.datum = datum
        self.foglalo_neve = foglalo_neve

# Adatbázis szimuláció
legitarsasagok = []
foglalasok = []

def elokeszites():
    global legitarsasagok, foglalasok
    l1 = Legitarsasag("SkyshowTravel")
    j1 = BelfoldiJarat("B101", "Budapest", 15000)
    j2 = BelfoldiJarat("B202", "Prága", 22000)
    j3 = NemzetkoziJarat("N303", "London", 45000)
    l1.jarat_hozzaad(j1)
    l1.jarat_hozzaad(j2)
    l1.jarat_hozzaad(j3)
    legitarsasagok.append(l1)
    # Előfoglalások
    foglalasok.append(JegyFoglalas(j1, "2025-06-20", "Kiss Béla"))
    foglalasok.append(JegyFoglalas(j2, "2025-06-21", "Lakatos Péter"))
    foglalasok.append(JegyFoglalas(j3, "2025-06-22", "Smith Jonatán"))
    foglalasok.append(JegyFoglalas(j1, "2025-06-23", "Tóth Gábor"))
    foglalasok.append(JegyFoglalas(j2, "2025-06-24", "Kovács Éva"))
    foglalasok.append(JegyFoglalas(j3, "2025-06-25", "Müller Éva"))

def jegy_foglalasa():
    print("Elérhető járatok:")
    for idx, l in enumerate(legitarsasagok):
        print(f"Légitársaság: {l.nev}")
        for i, j in enumerate(l.jaratok):
            print(f"  [{i}] {j.jaratszam} - {j.celallomas} ({j.jegyar} Ft)")
    try:
        jarat_idx = int(input("Válassz járatot (0-2): "))
        datum = input("Add meg az utazás dátumát (YYYY-MM-DD): ")
        nev = input("Add meg a neved: ")
        jarat = legitarsasagok[0].jaratok[jarat_idx]
        # Adatvalidáció
        if not datum or datetime.strptime(datum, "%Y-%m-%d") < datetime.now():
            print("Érvénytelen dátum.")
            return
        foglalas = JegyFoglalas(jarat, datum, nev)
        foglalasok.append(foglalas)
        print(f"Sikeres foglalás! Ár: {jarat.jegyar} Ft")
    except Exception as e:
        print("Hiba a foglalás során.", e)

def foglalas_lemondasa():
    nev = input("Add meg a neved a lemondáshoz: ")
    aktiv_foglalasok = [f for f in foglalasok if f.foglalo_neve == nev]
    if not aktiv_foglalasok:
        print("Nincs ilyen néven foglalás.")
        return
    for idx, f in enumerate(aktiv_foglalasok):
        print(f"[{idx}] {f.jarat.jaratszam} - {f.jarat.celallomas} {f.datum}")
    idx = int(input("Melyik foglalást szeretnéd lemondani? (index): "))
    # Validáció: csak létező foglalás törölhető
    foglalasok.remove(aktiv_foglalasok[idx])
    print("Foglalás lemondva.")

def foglalasok_listazasa():
    if not foglalasok:
        print("Nincs aktív foglalás.")
        return
    for f in foglalasok:
        print(f"{f.foglalo_neve}: {f.jarat.jaratszam} - {f.jarat.celallomas} {f.datum}")

def main():
    elokeszites()
    while True:
        print("\n--- Repülőjegy-foglalási rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")
        valasz = input("Válassz műveletet: ")
        if valasz == "1":
            jegy_foglalasa()
        elif valasz == "2":
            foglalas_lemondasa()
        elif valasz == "3":
            foglalasok_listazasa()
        elif valasz == "0":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
