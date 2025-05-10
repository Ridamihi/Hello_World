print("Avant erreur")
raise Exception("Erreur volontaire pour test")
print("Après erreur")  # Cette ligne ne sera jamais atteinte
