

agestring = input("Vilken är din ålder? ").strip()
summa = 0
count = 0
while agestring != "":
    age = int(agestring)
    if (age < 16 or age > 65) and age > 0:
        print("Fel ålder ska vara mellan 16 och 65 år")
        agestring = input("Ålder: ").strip()
        continue
    if age < 0:
        break

    summa += age
    count += 1
    agestring = input("Ålder: ").strip()

if count > 0:
    print("Medelålder: ", summa / count)
    
