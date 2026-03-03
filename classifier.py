def classify_document(text):
    text = text.lower()

    if any(word in text for word in ["facture", "montant", "total", "tva"]):
        return "Facture"

    elif any(word in text for word in ["contrat", "accord", "signature"]):
        return "Contrat"

    elif any(word in text for word in ["cv", "curriculum", "experience"]):
        return "CV"

    elif any(word in text for word in ["rapport", "analyse", "projet"]):
        return "Rapport"

    else:
        return "Autre"