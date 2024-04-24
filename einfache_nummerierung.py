start = input("Geben Sie den Startpunkt in Ganzzahlen ein: ")
end = input("Geben SIe den Endpunkt in Ganzzahlen ein: ")
step = input("Geben Sie Schrittweite in Ganzzahlen ein (\"außer 1\")")



numberlist =[]

# Hier wird von jeder Zahl einmögliches (-) entfernt und geprüft ob die nun positive Zahl
# eine Ganzzahl ist.

if not start.lstrip("-").isdigit() or not end.lstrip("-").isdigit() or not step.lstrip("-").isdigit():
    print("Bitte Ganzzahlen eingeben!")
    exit()
#Hier wird start, end, step der eingegebene Wert zugewiesen bzw als integer konvertiert

start = int(start)
end = int(end)
step = int(step)


if step == 1:
    print("Die Schrittweite darf nicht 1 betragen!")
    exit()

if start <= end:
    newstep = step if step > 0 else -step
else:
    newstep = step if step < 0 else -step

for i in range(start, end+1, newstep):
    numberlist.append(i)
print(f"Die Zahlenreihe: {numberlist}")