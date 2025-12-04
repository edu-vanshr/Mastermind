import random as rand


ANTAL_SIFFROR = 4  # Antal siffror i koden
MAX_DRAG = 12      # Max antal gissningar

# --------------------------- Introduktion ---------------------------
print(f"""
Datorn kommer att slumpa fram en kod på {ANTAL_SIFFROR} siffror mellan 1 och 6.
Du ska försöka gissa denna kods siffror på max {MAX_DRAG} drag.
Efter respektive gissning får du en respons:
✓  = rätt siffra på rätt plats
☐  = rätt siffra på fel plats
(ingen markering om siffran inte finns i koden)

Du får välja mellan två svårighetsnivåer:
1 = Lättare nivå (alla siffror olika)
2 = Svårare nivå (siffror kan upprepas)
""")

# --------------------------- Funktioner ---------------------------

def välj_svårhetsgrad():
    """
    Låter spelaren välja svårighetsgrad och genererar en kod.
    Nivå 1: alla siffror olika
    Nivå 2: siffror kan upprepas
    Returnerar: lista med siffror
    """
    while True:
        try:
            nivå = int(input("Ange önskad nivå: lättare (1), svårare (2) -> "))
        except ValueError:
            print("Felaktig inmatning. Ange 1 eller 2.")
            continue

        if nivå == 1:   # Alla siffror olika
            siffror = list(range(1, 7))
            return [siffror.pop(rand.randrange(len(siffror))) for _ in range(ANTAL_SIFFROR)]
        elif nivå == 2:  # Dubbletter tillåtna
            return [rand.randint(1, 6) for _ in range(ANTAL_SIFFROR)]
        else:
            print("Felaktig nivå. Ange 1 eller 2.")

def kontroll_av_gissning():
    """
    Kontrollerar spelarens gissning:
    - Fyra siffror (ANTAL_SIFFROR)
    - Alla siffror mellan 1 och 6
    Returnerar: lista med siffror
    """
    while True:
        giss = input(f"Ange gissning ({ANTAL_SIFFROR} siffror 1-6) -> ").replace(" ", "")

        if len(giss) != ANTAL_SIFFROR or not giss.isdigit():
            print(f"Ogiltig gissning. Ange exakt {ANTAL_SIFFROR} siffror mellan 1 och 6.")
            continue

        gissning = [int(s) for s in giss]
        if all(1 <= s <= 6 for s in gissning):
            return gissning
        else:
            print("Siffrorna måste vara mellan 1 och 6.")

def jämför_gissning(gissning, kod):
    """
    Jämför spelarens gissning med den hemliga koden.
    Returnerar en sträng med symboler:
    ✓ = rätt siffra på rätt plats
    ☐ = rätt siffra på fel plats
    """
    feedback = ""
    giss_kopia = gissning.copy()
    kod_kopia = kod.copy()

    # Först: rätt siffra på rätt plats
    i = 0
    while i < len(giss_kopia):
        if giss_kopia[i] == kod_kopia[i]:
            feedback += "✓"
            giss_kopia.pop(i)
            kod_kopia.pop(i)
        else:
            i += 1

    # Sedan: rätt siffra på fel plats
    i = 0
    while i < len(giss_kopia):
        if giss_kopia[i] in kod_kopia:
            feedback += "☐"
            kod_kopia.remove(giss_kopia[i])
            giss_kopia.pop(i)
        else:
            i += 1

    return feedback

def visa_gissning(feedback_lista, gissningar_lista):
    """Visar alla tidigare gissningar och deras feedback på samma rad."""
    print(f"""
 Drag #    Gissning      Feedback
-----------------------------------
""")
    for i in range(MAX_DRAG, 0, -1):
        try:
            giss = gissningar_lista[i-1]
            feedback = feedback_lista[i-1]
            # Skriv dragnummer, gissning och feedback på samma rad
            print(f"{i:>2}       {giss:^12}  {feedback}")
        except IndexError:
            # Om färre gissningar än drag, skriv tom rad
            print("")

def klarade_spelet(feedback, försök):
    """Kontrollerar om spelaren har vunnit spelet."""
    if feedback == "✓" * ANTAL_SIFFROR:
        print(f"Grattis! Du klarade spelet på {försök} gissningar!")
        return True

def klarade_inte_spelet(kod):
    """Skriver ut meddelande om spelaren förlorade spelet och visar rätt kod."""
    print("Bättre lycka nästa gång! Rätt kod var:", " ".join(map(str, kod)))

def spela_igen():
    """Frågar spelaren om de vill spela igen. Returnerar True/False."""
    while True:
        val = input("Vill du spela igen? (Ja/Nej) -> ").strip().lower()
        if val in ("j", "ja"):
            return True
        elif val in ("n", "nej"):
            return False
        else:
            print("Ogiltigt svar. Skriv 'Ja' eller 'Nej'.")

def kör_spel():
    """Huvudloop för spelet, hanterar hela spelomgången."""
    while True:
        kod = välj_svårhetsgrad()

        feedback_lista = []
        gissningar_lista = []
        försök = 0

        while True:
            giss = kontroll_av_gissning()
            försök += 1

            giss_str = " ".join(str(s) for s in giss)
            gissningar_lista.append(giss_str)

            feedback = jämför_gissning(giss, kod)
            feedback_lista.append(feedback)

            visa_gissning(feedback_lista, gissningar_lista)

            if klarade_spelet(feedback, försök):
                break
            if försök == MAX_DRAG:
                klarade_inte_spelet(kod)
                break

        if not spela_igen():
            break

# --------------------------- Huvudprogram ---------------------------
kör_spel()
print("Programmet avslutades normalt.")

