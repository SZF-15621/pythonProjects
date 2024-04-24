from fuzzywuzzy import fuzz

standard = input("Geben Sie den Standardsatz ein: ")
vergleichssatz = input("Geben Sie bitte einen Satz, der verglichen werden soll: ")

score = fuzz.ratio(standard, vergleichssatz)

print(f"Die Sätze gleichen sich zu {score} %.")