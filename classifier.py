def classifier(texte):

    texte = texte.lower()

    if "réunion" in texte:
        return "Procès-verbal"

    elif "étudiant" in texte or "relevé de notes" in texte:
        return "Dossier étudiant"

    elif "demande" in texte:
        return "Demande administrative"

    else:
        return "Autre"