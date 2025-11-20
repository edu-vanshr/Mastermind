import random as rand


print("""
Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
Du ska försöka gissa denna kods siffror på max 12 drag.
Efter respektive gissning så kommer du att få en respons:
✓  = rätt siffra på rätt plats
☐  = rätt siffra på fel plats
(ingen markering om siffran inte finns i koden)

Du får välja mellan två svårighetsnivåer:
1 = Lättare nivå (alla siffror olika)
2 = Svårare nivå (siffror kan upprepas)
""")


def välj_svårhetsgrad():
    while True:
        try:
            nivå = int(input("Ange önskad nivå: lättare (1), svårare (2) -> "))
        except ValueError:
            continue

        if nivå == 1:   # Alla siffror olika
            tal = list(range(1, 7))
            return [tal.pop(rand.randrange(len(tal))) for _ in range(4)]

        elif nivå == 2:  # Dubbletter tillåtna
            return [rand.randint(1, 6) for _ in range(4)]


def kontroll_av_gissning():
    while True:
        giss = input("Ange gissning (fyra siffror 1-6) -> ").replace(" ", "")

        if len(giss) != 4 or not giss.isdigit():
            continue

        gissning = [int(s) for s in giss]

        if all(1 <= s <= 6 for s in gissning):
            return gissning

def kopiera_tal(tal):
    return tal.copy()

def jämför_gissning(gissning, tal):
    resultat = ""

    g = gissning.copy()
    t = tal.copy()

    # Först: rätt siffra på rätt plats
    i = 0
    while i < len(g):
        if g[i] == t[i]:
            resultat += "✓"
            g.pop(i)
            t.pop(i)
        else:
            i += 1

    # Sedan: rätt siffra på fel plats
    i = 0
    while i < len(g):
        if g[i] in t:
            resultat += "☐"
            t.remove(g[i])
            g.pop(i)
        else:
            i += 1

    return resultat

# -------------------------------------------------------
# Funktion: visa gissningar och resultat
# -------------------------------------------------------
def visa_gissning(resultat_lst, gissningar_lst):
    print(f"""
 Drag #    Drag        Feedback
--------------------------------------
""")
    for i in range(12, 0, -1):
        print(f"{i:>2}", end="  ")
        try:
            print(f"{gissningar_lst[i-1]:^12}{resultat_lst[i-1]}")
        except IndexError:
            print("")

# -------------------------------------------------------
# Funktion: kontroll om spelet är klart
# -------------------------------------------------------
def klarade_spelet(resultat, försök):
    if resultat == "✓✓✓✓":
        print(f"Grattis! Du klarade spelet på {försök} gissningar!")
        return True

# -------------------------------------------------------
# Funktion: spelet förlorat
# -------------------------------------------------------
def klarade_inte_spelet(tal):
    print("Bättre lycka nästa gång! Rätt rad var:", " ".join(map(str, tal)))

# -------------------------------------------------------
# Funktion: fråga om man vill spela igen
# -------------------------------------------------------
def spela_igen():
    while True:
        val = input("Vill du spela igen? (j/n) -> ").lower()
        if val.startswith("j"):
            return True
        elif val.startswith("n"):
            return False

# -------------------------------------------------------
# Funktion: kör själva spelet
# -------------------------------------------------------
def kör_spel():
    while True:
        tal = välj_svårhetsgrad()

        resultat_lst = []
        gissningar_lst = []
        försök = 0

        while True:
            giss = kontroll_av_gissning()
            försök += 1

            giss_str = " ".join(str(s) for s in giss)
            gissningar_lst.append(giss_str)

            res = jämför_gissning(giss, kopiera_tal(tal))
            resultat_lst.append(res)

            visa_gissning(resultat_lst, gissningar_lst)

            if klarade_spelet(res, försök):
                break
            if försök == 12:
                klarade_inte_spelet(tal)
                break

        if not spela_igen():
            break

# -------------------------------------------------------
# Huvudprogram
# -------------------------------------------------------
kör_spel()
print("Programmet avslutades normalt.")
