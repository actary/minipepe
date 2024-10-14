# preliminary_questions.py

def ask_preliminary_questions():
    print("Nous allons poser quelques questions pour mieux comprendre vos besoins.")

    # Poser des questions ouvertes sur le contexte
    context = input("Quel est le contexte ou le projet sur lequel vous travaillez actuellement ? ")
    
    # Demander des précisions sur les défis rencontrés
    challenges = input("Quels sont les principaux défis ou problèmes que vous rencontrez dans ce projet ? ")

    # Demander des attentes sur le type de contenu ou d'accompagnement
    expectations = input("Quel type de contenu ou d'aide attendez-vous de cet outil (ex. : blog, article, stratégie, etc.) ? ")

    # Créer un dictionnaire pour stocker les réponses
    preliminary_data = {
        "context": context,
        "challenges": challenges,
        "expectations": expectations
    }

    # Afficher un résumé des réponses
    print("\nRésumé des réponses :")
    for key, value in preliminary_data.items():
        print(f"{key.capitalize()} : {value}")

    return preliminary_data

# Appel initial du script
if __name__ == "__main__":
    preliminary_data = ask_preliminary_questions()
    print(f"Vos données préliminaires : {preliminary_data}")
