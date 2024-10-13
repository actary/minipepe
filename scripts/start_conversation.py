# start_conversation.py
def start_conversation():
    print("Bienvenue dans cette nouvelle exploration avec Mini-Pepe !")
    print("Choisissez un axe narratif pour commencer votre parcours :")
    print("1. La dialectique de l’innovation et de la tradition")
    print("2. L’artiste et l’entrepreneur : un conflit d’identité")
    
    # Boucle pour s'assurer que l'utilisateur fait un choix valide
    while True:
        choice = input("Entrez le numéro de votre choix (1 ou 2) : ")
        
        if choice == "1":
            print("\nVous avez choisi 'La dialectique de l’innovation et de la tradition'.")
            return "innovation_tradition"
        elif choice == "2":
            print("\nVous avez choisi 'L’artiste et l’entrepreneur : un conflit d’identité'.")
            return "artist_entrepreneur"
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

# Appel initial du script
if __name__ == "__main__":
    axis = start_conversation()