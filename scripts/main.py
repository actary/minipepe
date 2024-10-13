import json
from start_conversation import start_conversation
from define_objective import define_objective
from collect_metadata import collect_metadata

# Charger les fichiers JSON
def load_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Demander des précisions sur l'histoire avec des questions ouvertes
def ask_story_details():
    story = {}
    story["accroche"] = input("\nAccroche : Parlez-moi de l'idée principale ou d'un moment clé de votre histoire : ")
    story["exposition"] = input("Exposition : Comment pourriez-vous décrire l'univers et les personnages de cette histoire ? ")
    story["personnages_funny_hat"] = input("Personnages : Décrivez les traits distinctifs ou symboliques de vos personnages (leur 'Funny Hat', par exemple). ")
    story["peripeties"] = input("Péripéties : Quelles situations mettraient vos personnages à l'épreuve ? ")
    story["denouement"] = input("Dénouement : Comment votre histoire se termine-t-elle ou pourrait-elle se terminer ? ")
    return story

# Demander le type de contenu à produire avec plus de liberté
def ask_content_type():
    return input("\nQuel type de contenu pensez-vous produire (ex. essai, post Instagram, article de blog, thread Twitter/X, etc.) ? : ")

# Générer un contenu personnalisé avec liberté et intégration des fichiers JSON
def generate_content(story_details, content_type):
    # Créer le contenu personnalisé de manière plus libre
    content = f"""
    **Type de contenu :** {content_type.upper()}
    
    **Accroche :** {story_details['accroche']}
    
    **Exposition :** {story_details['exposition']}
    
    **Personnages et traits distinctifs :** {story_details['personnages_funny_hat']}
    
    **Péripéties :** {story_details['peripeties']}
    
    **Dénouement :** {story_details['denouement']}
    """
    
    return content

# Fonction principale
def main():
    print("Bienvenue dans l'outil de création de contenu personnalisé avec Mini-Pepe !")

    # Charger les fichiers JSON pour personnaliser les réponses
    juliana_data = load_json_file('juliana.json')
    marmande_data = load_json_file('marmande_universe.json')

    # 1. Demander de préciser un axe narratif
    axis = start_conversation()

    if axis:
        # 2. Demander des précisions sur l'histoire
        objective_data = define_objective(axis)
        if objective_data:
            # 3. Collecter les métadonnées basées sur la réponse de l'utilisateur
            metadata = collect_metadata(objective_data["response"])

            # 4. Demander le type de contenu
            content_type = ask_content_type()

            # 5. Demander des détails sur l'histoire
            story_details = ask_story_details()

            # 6. Générer un contenu personnalisé
            generated_content = generate_content(story_details, content_type)

            # Afficher le contenu généré
            print("\nContenu généré :")
            print(generated_content)

        else:
            print("Erreur lors de la définition de l'objectif.")
    else:
        print("Aucun axe narratif sélectionné.")

if __name__ == "__main__":
    main()