from database import init_db, insert_document
from ocr import extract_text
from classifier import classifier

def main():

    init_db()

    image_path = input("Chemin du document image : ")

    texte = extract_text(image_path)

    type_doc = classifier(texte)

    titre = input("Titre du document : ")

    insert_document(titre, type_doc, texte)

    print("Document enregistré avec succès !")
    print("Type détecté :", type_doc)

if __name__ == "__main__":
    main()