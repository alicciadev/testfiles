
import random

gissning = input("Vad väljer du? ")
val = random.choice(["sten","sax","påse"])

playcount = 0
pythcount = 0

a = "sten"
b = "sax"
c = "påse"

a > b
b > c
c > a

while gissning == "sten" or gissning == "sax" or gissning == "påse":
        if gissning > val:
            print("Grattis, du fick poäng. Datorn valde ", val, ".", sep="")
            playcount += 1
            input("Vad väljer du? ")
            val = random.choice(["sten","sax","påse"])
            continue

        elif gissning < val:
            print("Tyvärr du frlorade. Datorn valde ", val, ".", sep="")
            playcount += 1
            input("Vad väljer du? ")
            val = random.choice(["sten","sax","påse"])
            continue

        elif gissning == val:
            print("Oavgjort. testa igen. datorn valde", val)
            input("Vad väljer du? ")
            val = random.choice(["sten","sax","påse"])
            continue

        elif gissning == "sluta":
            print("Tack för en god match, ditt poäng är:", playcount, "pyhtons poäng är", pythcount)



