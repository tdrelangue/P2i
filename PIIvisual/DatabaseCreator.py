# DLC, contrat date, (jours de quarantaine, delai de surremballage, délai de livraison)+,  production, livraison
# entrée = [DLC(15 - 300), contractDate(15 - 300), Retard(0-20), production(0-1 * 7), Livraison(0-1 * 7), RetardMin(0-20), changements(0-1 * 5)
# sortie = [DLC(15 - 300), contractDate(15 - 300), Retard(0-20), production(0-1 * 7), Livraison(0-1 * 7)

changements = {
    "DLC": True,
    "Contract Date": False,
    "delai de surremballage": True,
    "delai de livraison" : False,
    "jours de quarantaine": True,

}

#Réseaux baésiens
# avantage et inconvénients des IAs possibles