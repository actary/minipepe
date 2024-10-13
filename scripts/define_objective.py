# define_objective.py
def define_objective(axis):
    if axis == "innovation_tradition":
        print("Explorons la dialectique de l’innovation et de la tradition.")
        question = "Comment pensez-vous que l’innovation peut transformer votre environnement sans trahir vos racines ?"
        print(f"Question : {question}")
    
    elif axis == "artist_entrepreneur":
        print("Explorons le conflit d’identité entre l’artiste et l’entrepreneur.")
        question = "Pensez-vous qu’il est possible de concilier créativité artistique et impératifs commerciaux ?"
        print(f"Question : {question}")
    
    else:
        print("Axe inconnu. Réessayez.")
        return None

    # Récupérer la réponse de l'utilisateur
    response = input("Entrez votre réponse : ")
    
    # Concaténer la question avec la réponse pour une meilleure analyse
    objective_data = {
        "axis": axis,
        "question": question,
        "response": response
    }
    return objective_data

# Appel de la fonction
if __name__ == "__main__":
    from start_conversation import start_conversation
    axis = start_conversation()
    if axis:
        objective = define_objective(axis)
        if objective:
            print(f"Votre objectif défini : {objective}")