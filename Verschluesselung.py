sentence = input("Geben Sie einen Satz ein: ")
toremove = input("Geben Sie folgende Zeichen oder Wörter ein, die entfernt werden sollen: ")
clean_sentence = ""

positions = []

for i, char in enumerate(sentence):
    if char in toremove:
        positions.append(i)
    else:
        clean_sentence += char

print(f"Sie wollen {toremove} entfernen")
if len(positions) > 0:
    print(f"Die entsprechenden Positionen der entfernten Zeichen sind: {positions}")
else:
    print(f"{toremove} befindet sich nicht im Satz.")

print(f"Der bearbeitete Satz lautet: {clean_sentence}")

original_sentence = ""

for i, char in enumerate(sentence):
    if i in positions:
        original_sentence += char
    else:
        original_sentence += clean_sentence[0]
        clean_sentence = clean_sentence[1:]

        print(f"Der ursprüngliche Satz lautet: {original_sentence}")
