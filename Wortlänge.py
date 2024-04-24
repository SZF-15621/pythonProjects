def longest_word(path):
    max_word = 0
    with open(path, "r") as f:
        for line in f:
            words =line.split()
            for word in words:
                w_length = len(word)
                if w_length > max_word:
                    max_word = w_length
    return max_word


def main():
    path = input("Geben Sie bitte den Dateipfad an: ")

    try:
        max_word = longest_word(path)
        print(f"Das längste Wort ist: {max_word}")
    except:
        print("Fehler. Datei existiert nicht.")



if __name__ == "__main__":
    main()