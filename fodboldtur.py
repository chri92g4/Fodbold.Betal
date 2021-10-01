import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut(): #giver afslut en funktion som man kan køre i koden
    outfile = open(filename, 'wb') #python åbner filen
    pickle.dump(fodboldtur, outfile) #python gemmer filen
    outfile.close() #python lukker filen
    print("Programmet er afsluttet!")

def printliste(): #giver print liste en funktion som gør det nemmere at bruge deti koden
    for item in fodboldtur.items():
        print(item)

def menu(): #definerer menuen så jeg kan køre den altid Vha menu()
    print("MENU")
    print("1: Print liste")
    print("2: rediger beløb")
    print("3: Afslut program")
    print("4: Hvor meget mangler folk")
    print("5: Tilføj en ekstra person til listen")
    print("6: Slet en person fra listen")
    print("7: Se hvor meget der mangler i alt")
    print("8: Se de 3 personer der mangler at betale mest")
    #her printer jeg de forskellige valg

    valg = input("Indtast dit valg:") #ændrer input til valg da det gør det mere overskueligt


    if (valg == '1'): #jeg laver et "if" statement for hver valg som checker hvad bruger input er.
        printliste() #printer altid dicten som det første men har valgt at kalde den liste da flere vil forstå det
        menu()


    if (valg =='2'):
        print("Hvilket beløb skal redigeres?")
        printliste()
        navn = input("indtast navn") #ændrer input til navn så den kan finde navnet i listen.
        if navn in fodboldtur: #får python til at checke om navnet er i listen så man ikke kan ødelægge programmet.
            beløb = int(input("hvor meget vil du ændre beløbet med"))#sætter beløb til en int og som input da brugeren formegentlig gerne vil ændre problemet.
            if beløb == 0: #får python til at checke om beløbet er 0 da dette er et ugyldigt beløb
                valg = input("dette er ikke et gyldigt beløb vil du prøve igen?") #hvis brugeres skriver 0 kan personen vælge ja eller nej for at prøve nyt beløb eller ende programmet
                if (valg =='ja'):
                    menu()
                else:
                    print("Det iorden have en god dag!")
                    afslut()
            else:
                fodboldtur[navn]+=beløb #hvis alt stemmer både navn og beløb er gyldig så tilføjer den eller trækker fra alt efter hva man har skrevet.
                menu()

        else:
            print("dette navn er ikke i listen skriv venligst fulde navn og tjek at det er gyldigt")# hvis navnet ikke er gyldigt starter den forfra så man kan prøve igen.
            menu()


    if (valg == '3'):
        afslut()


    if (valg =='4'):
        printliste()
        print("Hvem vil du gerne kigge på?")
        navn = input("indtast navn")
        if navn in fodboldtur:
            print(navn,"mangler",fodboldtur[navn]-4500/len(fodboldtur),"kroner") #da hver person skal betale 4500 ber jeg python om at printe navnet og beløbet i int-4500kr

            Valg=input("vil du lukke programmet?") #derefter spørger jeg om brugeren vil lukke programmet eller fortsætte med andre funktioner.
            if Valg == 'ja':
                afslut() # hvis "ja" kører den afslut funktion og alutter programmet samt gemmer ændringer.
            else:
                menu() #kører menu funktionen uden at gemme ændringer før man kører afslut.

        else:
            print("dette navn er ikke i listen skriv venligst fulde navn og tjek at det er gyldigt")
            menu()

    if (valg =='5'):
        navn = input("skriv venligst det navn du vil tilføje")
        fodboldtur[navn]=0 #sætter beløbet som personen starter med samt fortæller programmet hvad brugeren skriver.
        printliste() #printer listen så brugeren kan se at navnet er tilføjet.
        Valg=input("så er personen tilføjet vil du lukke programmet?")
        if Valg == 'ja':
            afslut()
        else:
            menu()

    if (valg =='6'):
        printliste()
        navn = input("skriv venligst det navn du vil slette") #man kan ikke tilføje et navn uden at kunne slette et navn også.
        if navn in fodboldtur: #python checker for navnet i listen.
            fodboldtur.pop(navn)#hvis navnet er i listen bruger python "pop" funktion og fjerner navnet
        else:
            print("dette navn findes ikke sørg for at tjekke det findes")#findes navnet ik kan man prøve igen
            menu()

        Valg=input("så er personen fjernet vil du lukke programmet")
        if Valg == 'ja':
            afslut()
        else:
            menu()

    if (valg =='7'):
        Sum = 0 # definerer sum som en int
        for key in fodboldtur.keys(): #ber programmet om at sætte beløb som en key som jeg kan definerer senere
            Sum += fodboldtur[key]#tilføjer beløbne en efter en og ber programmet tjekke om der er nyt beløb
        print(Sum - 4500, "kroner")#ber programmet printe den fulde sum -4500 så brugeren ved hvor meget der mangler i alt
        Valg = input("vil du lukke programmet?")  # derefter spørger jeg om brugeren vil lukke programmet eller fortsætte med andre funktioner.
        if Valg == 'ja':
            afslut()
        else:
            menu()

    if (valg =='8'):
        from operator import itemgetter #python importere "itemgetter" fra operator som er den sorterede dict
        sidsteplads = sorted(fodboldtur.items(), key=itemgetter(1)) #giver "sidsteplads" en defination som jeg kan kalde når det skal printes.
        print(sidsteplads[0:3])#printer "sidsteplads" fra tal 0-3 som er de 3 der mangler at betale mest.

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

menu()
