mwst = float(1.16)
cont = ("j")
print("Willkommen beim Deutschen Mehrwertsteuer Rechner v 0.1")
print("von RE IT Dienstleistungen")
print("https://github.com/R4W3/VATCALC_German")
print("______________________________________\n")

while cont == 'j':
    netto = input("Nettobetrag: ")
    float(netto)
    print(netto , "exkl. 16% MwSt.")
    print(float(netto) * float(mwst) , "inkl. 16% MwSt.")
    print("Weiterrechnen? (j/n)")
    cont = input()

print("Vielen Dank!")
exit()