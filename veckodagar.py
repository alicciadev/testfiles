months = ["jan", "feb", "mar", "apr", "jun", "jul", "jun", "aug", "sep", "okt", "nov", "dec"]
weekdays = ["mån", "tis", "ons", "tor", "fre", "lör", "sön"]
maxdays = [31,28,31,30,31,30, 31, 31, 30, 31, 30, 31]


wdaystring = input("Ange veckodag den 1a januari? ").lower()
while wdaystring not in weekdays:
    print("Ska vara en av veckans dagar.")
    wdaystring = input("Ange veckodag den 1a januari? ").lower()

wnr = weekdays.index(wdaystring)

answer = input("Är det skottår? ").lower()
while answer not in ["ja", "nej"]:
    print("Fel, svaret ska vara ja eller nej")
    answer = input("Är det skottår? ").lower()

if answer == "ja":
    maxdays[1] = 29
    
for mnr in range (0,12):
    print(months[mnr])
    for dnr in range(0,maxdays[mnr]):
        print(dnr + 1, "\t", weekdays[wnr])
        wnr = (wnr + 1) % 7
