# Mastermind

Spelet Mastermind låter spelaren försöka lista ut en hemlig kod på fyra siffror (1–6) på max 12 försök. Datorn genererar koden slumpmässigt och ger feedback efter varje gissning.

## Kort beskrivning av programmet

Spelaren väljer svårighetsgrad 1 eller 2:

- (1) Alla siffror olika
- (2) Siffror kan upprepas

Spelaren gör gissningar och får feedback:

- ✓ = rätt siffra på rätt plats
- ☐ = rätt siffra på fel plats

Spelet visar tidigare gissningar och feedback
Spelet avslutas när spelaren lyckas eller når max antal drag
Spelaren kan välja att spela igen

## Hur programmet startas och körs

1.Navigera till filen mastermind.py
2.Klicka på "Run" knappen som ligger längst upp till höger
3.Programmet startas då med att introducera spelet och spelaren får välja svårighetsgrad
4.Njuta av spelet!

## Exempel på in- och utmatning

Datorn kommer att slumpa fram en kod på 4 siffror mellan 1 och 6.
Du ska försöka gissa denna kods siffror på max 12 drag.
Efter respektive gissning får du en respons:
✓  = rätt siffra på rätt plats
☐  = rätt siffra på fel plats
(ingen markering om siffran inte finns i koden)
Du får välja mellan två svårighetsnivåer:

1 = Lättare nivå (alla siffror olika)
2 = Svårare nivå (siffror kan upprepas)
Ange önskad nivå: lättare (1), svårare (2) -> 2
Ange gissning (4 siffror 1-6) -> 1234

Drag #    Gissning      Feedback
----------------------------------

1         1 2 3 4     ✓☐☐

Ange gissning (4 siffror 1-6) -> 1325
 Drag #    Gissning      Feedback
-----------------------------------

2         1 3 2 5     ☐☐
1         1 2 3 4     ✓☐☐

Ange gissning (4 siffror 1-6) -> 3125
 Drag #    Gissning      Feedback
-----------------------------------

3         3 1 2 5     ☐☐
2         1 3 2 5     ☐☐
1         1 2 3 4     ✓☐☐

Ange gissning (4 siffror 1-6) -> 3156
 Drag #    Gissning      Feedback
-----------------------------------
4         3 1 5 6     ☐
3         3 1 2 5     ☐☐
2         1 3 2 5     ☐☐
1         1 2 3 4     ✓☐☐

Ange gissning (4 siffror 1-6) -> 4211
 Drag #    Gissning      Feedback
-----------------------------------
5         4 2 1 1     ✓✓✓✓
4         3 1 5 6     ☐
3         3 1 2 5     ☐☐
2         1 3 2 5     ☐☐
1         1 2 3 4     ✓☐☐

Grattis! Du klarade spelet på 5 gissningar!
Vill du spela igen? (Ja/Nej) -> nej
Programmet avslutades normalt.

## Loggbok

Datum - 18/11/2025

Vad vi gjorde - Idag fick vi tyvärr ingen kodning gjort, eftersom vi hade en hemlig politiker som besökte oss. Istället så började vi diskutera hur kodningen för Mastermind skulle se ut.

Problem/Frågeställningar som uppstod - Inga problem än så länge, utan att Ulf Kristersson avbröt lektionen.

Lösning - Inga lösningar krävdes



Datum - 20/11/2025

Vad vi gjorde - Idag började vi med att importera random som rand, och sen skrev vi MAX_ANTAL = 4 (Max antal siffror är 4) och MAX_DRAG = 12 (Max 12 gissningar).
Efter det implementerade vi introduktionen och svårighetsgraden i Mastermind-spelet. Programmet visar först instruktioner för spelaren om hur spelet fungerar: spelaren ska gissa en kod på 4 siffror mellan 1 och 6 och får feedback efter varje gissning (✓ = rätt siffra på rätt plats, ☐ = rätt siffra på fel plats, ingen markering om siffran inte finns i koden).
Vi skapade även funktionen välj_svårhetsgrad(), som låter spelaren välja mellan två nivåer:

- Lättare nivå – alla siffror i koden är olika.
- Svårare nivå – siffror kan upprepas.

Funktionen genererar sedan en slumpmässig kod baserat på vald nivå.

Problem/Frågeställningar som uppstod - Spelaren kunde skriva in ogiltig inmatning, t.ex. text eller siffror utanför 1–2 när svårighetsgrad skulle väljas.
Att slumpa koden utan att upprepa siffror på lättare nivå krävde också extra logik.

Lösning -

- Vi använde en try/except-sats för att hantera ogiltig inmatning och skrev ut ett felmeddelande om något annat än 1 eller 2 anges.
- För att generera koden utan upprepning skapade vi först en lista med siffrorna 1–6, och tog sedan slumpmässigt ut siffror utan att återanvända dem med hjälp av pop() och rand.randrange().
- För svårare nivå använde vi rand.randint(1, 6) som tillåter att siffror kan upprepas.



Datum - 25/11/2025

Vad vi gjorde - Idag implementerade vi funktionerna som kontrollerar spelarens gissning och ger feedback.

1.kontroll_av_gissning()

- Kontrollerar att spelaren matar in exakt fyra siffror mellan 1 och 6.
- Tar bort eventuella mellanslag och säkerställer att inmatningen är giltig innan den används i spelet.
- Returnerar en lista med siffror som används för att jämföra med den hemliga koden.

2.jämför_gissning(gissning, kod)

- Jämför spelarens gissning med den hemliga koden.
- Returnerar en sträng med symboler:

✓ = rätt siffra på rätt plats

☐ = rätt siffra på fel plats

- Först markeras rätt siffra på rätt plats, sedan rätt siffra på fel plats.

Problem/Frågeställningar som uppstod -

- Spelaren kunde skriva in färre eller fler siffror än 4, eller använda siffror utanför 1–6.
- Att korrekt jämföra gissningen med koden och ge feedback med både ✓ och ☐ var lite klurigt, särskilt när siffror upprepas.

- Idag glömde vi också att göra git commit på kodningen

Lösning - Vi använde replace(" ", "") för att ta bort eventuella mellanslag och isdigit() + längdkontroll för att säkerställa att spelaren bara matar in giltiga siffror.
I jämför_gissning() kopierade vi gissningen och koden (copy()) för att kunna ta bort siffror allteftersom de matchades.

Vi använde två steg för feedback:

- Först markerades siffror som var på rätt plats med ✓.
- Sedan markerades siffror som fanns i koden men på fel plats med ☐.



Datum - 27/11/2025

Vad vi gjorde - Idag gjorde vi nästan klart Mastermind men flera funktioner som:


1.visa_gissning():

- Visar historik över alla gissningar

Den här funktionen skriver ut en tabell där spelaren kan se:

- Alla tidigare gissningar
- Feedback till varje gissning (✓ och ☐)
- Dragnummer

Tabellen är dynamisk och visar tomma rader om spelaren inte gjort max antal drag.

2.klarade_spelet() – Kontroll av vinst

- Funktionen kontrollerar om feedback består av exakt fyra ✓.
- Om ja → skriver ut att spelaren klarat spelet och på hur många försök.

3.klarade_inte_spelet() – Förlustmeddelande

Om spelaren misslyckas efter 12 drag visas:

- ”Bättre lycka nästa gång!”
- Den hemliga koden _ _ _ _

4.spela_igen() – Frågar spelaren om ny omgång

Funktionen accepterar svar:

- j / ja
- n / nej

Och säkerställer att spelaren inte skriver något ogiltigt.

5.kör_spel() – Huvudloopen för hela spelet
Detta är alltså programmets hjärta som:

- Genererar ny kod baserat på vald svårighetsgrad
- Loopar igenom alla gissningar
- Samlar och sparar gissningar och feedback
- Visar tabellen efter varje drag
- Stoppar spelet vid vinst eller förlust
- Frågar om spelaren vill fortsätta

6.Huvudprogrammet

kör_spel() startas automatiskt och när spelaren avslutar spelet skrivs:

"Programmet avslutades normalt."


Problem/Frågeställningar som uppstod - Det var lite svårt att få tabellen för gissningar att alltid se snygg ut, särskilt när spelaren gjort färre än 12 gissningar.
Vi behövde se till att spelet inte fortsatte efter att spelaren vunnit eller förlorat, utan bröt loopen korrekt.
Vi behövde också skapa en tydlig huvudloop som hanterar flera spelomgångar utan att programmet kraschar.

Lösning -

- Vi använde try/except i visa_gissning() så att tomma rader skrivs ut när inga värden finns på en viss rad, vilket gjorde tabellen stabil.

Vi lade in två tydliga kontroller i huvudloopen:

- if klarade_spelet(...): break

- if försök == MAX_DRAG: ... break

För flera spel i rad använde vi en while-loop runt hela spelet i kör_spel(), kombinerat med spela_igen() som returnerar True/False.
På så sätt blir loopen kontrollerad och lätt att följa.



Datum - 2/12/2025

Vad vi gjorde - Idag kodade vi klart Mastermind genom att lägga till kommentarer på varje funktion. Vi dubbelkollade även på Sten-Sax-Påse kodningen och märkte att inte fanns lika många kommentarer.
Vi började även skriva i vår README.md (både för StenSaxPåse och Mastermind) för att dokumentera.

Problem/Frågeställningar som uppstod - Vi märkte att StenSaxPåse koden hade inte så många kommentarer

Lösning - Vi kommer att fixa kommentarer på den nästkommande lektionen, så att allt kod kan pushas till GitHub.



Datum - 4/12/2025 (Sista lektionen innan redovisningen den 9/12/2025)

Vad vi gjorde - Idag skrev vi klart kommentarer på Sten-Sax-Påse och Mastermind programmet och även README-filen, som då kunde pushas till GitHub.
Samtidigt skapade vi en Google-Presentation inför redovisningen

Problem/frågeställningar som uppstod - Vår README-fil och kod kunde inte pushas till GitHub.

Lösning - Vi fick  hjälp från vår lärare Nikodemus som fixade allt.


## Buggar, Begränsningar och Framtida Förbättringar

Buggar:

- Just nu finns inga kända kritiska buggar, men programmet förutsätter att användaren skriver in siffror korrekt. Felaktiga eller oväntade tecken kan i vissa fall ge oväntat beteende vid inmatning.
- Om terminalfönstret är väldigt smalt kan tabellen med gissningar och feedback visas felplacerat eller utan korrekt radbrytning.

Begränsningar:

- Spelet spelas helt i terminalen och har ingen grafisk version.

- Enbart siffrorna 1–6 kan användas i koden och gissningarna.
-
- Feedbacken visar inte ordningen av träffar — den visar endast antal ✓ och ☐, inte vilka positioner som är rätt.
-
- Spelet är gjort för en spelare (ingen multiplayer-funktionalitet).

- Svårighetsgraden styr bara antal siffror och drag, inte komplexitet i koden.

Framtida förbättringar:

- Färgkodning i terminalen, t.ex. ✓ i grönt och ☐ i gult.

- Bättre validering av användarinmatning för att hantera fler typer av feltryck.

- Möjlighet att välja större talintervall, t.ex. 1–8 eller 1–9.

- Inbyggd hjälpmeny som förklarar regler och symboler.

- Statistiklogg (antal vinster, genomsnittliga försök, snabbaste lösning osv.)

- Hintsystem där spelaren kan få en ledtråd mot en kostnad av 1 extra drag.

- Multiplayer-läge där en spelare skriver koden och den andra gissar.









