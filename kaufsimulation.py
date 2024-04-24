
anzahlTestkaeufer = int(input("Wieviele Testkäufer soll es geben?"))
if anzahlTestkaeufer <= 0:
    print("Es müssen mehr als 0 sein!")
    exit()


durchschnitt = 0.0
bewertungen = []  # Eine Liste, um die Bewertungen aller Testkäufer zu speichern

for _ in range(anzahlTestkaeufer):  # Iteriere über die Anzahl der Testkäufer
    bewertung = int(input("Wie würden Sie bewerten? 1 - schlecht, 2 - OK, 3 - Sehr gut: "))
    bewertungen.append(bewertung)  # Füge die Bewertung zur Liste hinzu

print(bewertungen)

summe = sum(bewertungen)
durchschnitt = summe / anzahlTestkaeufer
print(durchschnitt)