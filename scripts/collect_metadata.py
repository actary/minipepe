# collect_metadata.py
def collect_metadata(response):
    print("Analyse des métadonnées basées sur votre réponse...")

    # Exemple d'extraction plus avancée de métadonnées avec analyse de sentiment et ajout de catégories pertinentes
    keywords = ["créativité", "innovation", "tradition", "commerce", "authenticité", "solidarité", "digital", "art"]
    
    # Extraction des mots-clés pertinents
    extracted_keywords = [word for word in response.split() if word.lower() in keywords]
    
    # Analyse du sentiment : ajouter plus de termes positifs/négatifs pour une analyse plus précise
    positive_terms = ["possible", "réussi", "succès", "positif", "amélioration"]
    negative_terms = ["impossible", "difficile", "échec", "problème", "négatif"]
    
    if any(term in response.lower() for term in positive_terms):
        sentiment = "positive"
    elif any(term in response.lower() for term in negative_terms):
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Calcul de la longueur du texte
    response_length = len(response.split())

    # Ajout de catégories basées sur les mots-clés
    categories = {
        "creativity": "créativité" in extracted_keywords,
        "innovation": "innovation" in extracted_keywords,
        "tradition": "tradition" in extracted_keywords,
        "commerce": "commerce" in extracted_keywords,
        "authenticity": "authenticité" in extracted_keywords,
        "solidarity": "solidarité" in extracted_keywords,
        "digital": "digital" in extracted_keywords,
        "art": "art" in extracted_keywords
    }

    # Assemblage des métadonnées
    metadata = {
        "length": response_length,
        "keywords": extracted_keywords,
        "sentiment": sentiment,
        "categories": categories
    }

    # Affichage des métadonnées extraites
    print(f"Métadonnées collectées : {metadata}")
    return metadata

# Appel de la fonction
if __name__ == "__main__":
    from define_objective import define_objective
    from start_conversation import start_conversation
    
    axis = start_conversation()
    objective = define_objective(axis)
    metadata = collect_metadata(objective)