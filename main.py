print("How many copies would you like:\n")
copies = input()
copies = int(copies)
ppc = 0
float(ppc)
tot = 0
float(tot)

if copies >= 0 and copies <= 99:
  ppc = .30
elif copies >= 100 and copies <= 499:
  ppc = .28
elif copies >= 500 and copies <= 749:
  ppc = .27
elif copies >= 750 and copies <= 1000:
  ppc = .26
elif copies > 1000:
  ppc = .25

tot = ppc * copies
print ("Price per copy is:",ppc)
print ("Toal cost is:",tot)