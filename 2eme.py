#2éme programme python qui vas convertir des nombres decimaux en chiffre romain

#initialisation...

valeurSaisitatransformer =input("Choisit une valeur je vais la transformer en nombre romain ")
NombreRomain = ""
ConversionDecimale = 0 





#Traitement...

if(valeurSaisitatransformer==""):
    print("Tu dois choisir une valeur")

def ConversionEnRomain(Decimal):
  #Initialisation
    NobrequiStocke = ""

    #Traitement...
    if (Decimal<3999):
       
       nombrequistocke = "Conversion pas possible"
   
    if(Decimal==1): 
     nombrequistocke = "I" 

     for i in Decimal:

        nombrequistocke += "I"
       
    
    
