import random


utente1=input("UTENTE 1 inserisci il tuo nome : ")
utente2=input("UTENTE 2 inserisci il tuo nome : ")
print("Perfetto", utente1 ,"e", utente2 ,"inziamo a buttare i dadi...")

max=101 #inserire qui quante volte vuoi che deve essere buttato il dado
ut11=0
ut22=0
for massimo in range(0, max):
    ut1 = random.randint(0,6)
    ut2 = random.randint(0,6)
    print(massimo)
    if (ut1==ut2):
        print("partita patta")
    elif (ut1>ut2):
        ut11+=1
        print("partita vinta da :", utente1, "punteggio parziale ",ut11)
    else:
        ut22+=1
        print("partita vinta da :", utente2, "punteggio parziale ",ut22)
if (ut11>ut22):
    print("partita vinta da ",utente1 )
else:
    print("partita vinta da ",utente2 )
print("punteggio finale è ", ut11 , "-" , ut22, "." )
