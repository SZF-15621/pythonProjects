

eingabe = input("Bitte geben Sie Ihre Liste mit \",\" getrennt ein: ").split(",")
eingabe = [word.strip() for word in eingabe]

fertige_liste = list(set(eingabe))

fertige_liste.sort()
print(len(eingabe))
print(len(fertige_liste))
print(eingabe)
print(fertige_liste)