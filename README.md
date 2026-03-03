# ITER Archive - Automatisation de l'Archivage et du Tri des Documents

Application Python Flask pour automatiser l'archivage, l'extraction de texte (OCR) et la classification automatique des documents du Département ITER.

## 🎯 Objectifs

-Numérisation des documents
-Extraction automatique de texte (OCR) depuis images et PDF
- Classification intelligente des documents
- Stockage structuré dans une base de données
- Interface web conviviale
- Recherche et filtrage par catégorie

## Catégories de documents supportées

- Procès-verbaux
- Dossiers étudiants
- Demandes administratives
- Notes de service
- Rapports pédagogiques
- Autres

##  Installation

### Prérequis

- Python 3.8+
- Tesseract-OCR (pour l'extraction de texte)

### Installation de Tesseract-OCR

#### Windows
```bash
# Télécharger l'installeur depuis :
https://github.com/UB-Mannheim/tesseract/wiki

# Installer avec le chemin par défaut : C:\Program Files\Tesseract-OCR
```

### Installation du projet

1. Cloner ou télécharger le projet
```bash
cd ITER_ARCHIVE
```

2. Créer un environnement virtuel
```bash
python -m venv venv
```

3. Activer l'environnement virtuel

**Windows:**
```terminal

venv\Scripts\activate


4. Installer les dépendances
```terminal
pip install -r requirements.txt
```

##  Utilisation

### Démarrer l'application

```bash
python app.py
```

L'application sera accessible à : `http://localhost:5000`

### Accès à l'interface

- **Accueil** : Tableau de bord avec statistiques
- **Uploader** : Télécharger et classifier des documents
- **Documents** : Consulter tous les documents archivés
- **Statistiques** : Analyser la répartition par catégorie

## Structure du projet

```
ITER_ARCHIVE/
├── app.py                 # Application Flask principale
├── classifier.py          # Module de classification
├── database.py            # Gestion de la base de données SQLite
├── ocr.py                 # Module d'extraction de texte (OCR)
├── requirements.txt       # Dépendances Python
├── archive.db            # Base de données (créée automatiquement)
├── uploads/              # Dossier des fichiers uploadés
├── templates/            # Templates HTML
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── upload.html       # Page d'upload
│   ├── documents.html    # Liste des documents
│   ├── stats.html        # Statistiques
│   ├── 404.html          # Page d'erreur 404
│   └── 500.html          # Page d'erreur 500
├── static/               # Fichiers CSS, JS
├── data/                 # Données supplémentaires
└── venv/                 # Environnement virtuel
```

##  Dépendances principales

- **Flask** : Framework web
- **PyPDF2** : Extraction de texte depuis les PDF
- **pytesseract** : Wrapper Python pour Tesseract OCR
- **Pillow** : Traitement des images
- **scikit-learn** : (optionnel) Pour améliorations futures

##  Configuration

### Modifier le chemin de Tesseract

Si Tesseract est installé dans un dossier différent, modifier dans `ocr.py` :

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Chemin\Vers\tesseract.exe"
```

### Ajouter de nouvelles catégories

Modifier la fonction `classify_document()` dans `classifier.py` pour ajouter de nouvelles catégories.

### Limiter la taille des fichiers

Modifier dans `app.py` :

```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB
```

## 🐛 Dépannage

### Tesseract-OCR n'est pas trouvé
```
OSError: tesseract is not installed or it's not in your PATH
```
Solution : Installer Tesseract ou configurer le chemin dans `ocr.py`

### Erreur lors de l'upload
- Vérifier l'extension du fichier (PDF, PNG, JPG, etc.)
- Vérifier la taille du fichier (max 50 MB par défaut)
- Vérifier que le dossier `uploads/` existe

### Erreur de base de données
La base de données est initialisée automatiquement au premier démarrage. Si problème :
```bash
rm archive.db
python app.py
```

## 📚 Documentation API

### Routes principales

| Route | Méthode | Description |
|-------|---------|-------------|
| `/` | GET | Page d'accueil |
| `/upload` | GET, POST | Uploader un document |
| `/documents` | GET | Tous les documents |
| `/documents/<category>` | GET | Filtrer par catégorie |
| `/stats` | GET | Statistiques |

## 🔐 Sécurité

- Validation des extensions de fichier
- Limite de taille de fichier
- Nettoyage des noms de fichier
- Gestion des erreurs

## 📝 Logs

Les erreurs sont affichées dans la console lors du démarrage en mode debug.

## 🎓 Améliorations futures possibles

- [ ] Authentification utilisateur
- [ ] Recherche fulltext
- [ ] Export en Excel/CSV
- [ ] Reconnaissance de documents scannés améliorée
- [ ] API REST pour intégration tierce
- [ ] Notifications par email
- [ ] Support multilingue amélioré
- [ ] Machine learning pour classification améliorée

## 📄 Licence

Projet développé pour le Département ITER

## 📞 Support

Pour toute question ou problème, veuillez contacter l'administrateur système.
