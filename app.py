from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
import os
from werkzeug.utils import secure_filename
from classifier import classify_document
from database import init_db, add_document, get_all_documents, get_documents_by_type, get_document_stats
from ocr import extract_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max
app.secret_key = 'your-secret-key-change-in-production'

# Extensions autorisées
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'txt'}

def allowed_file(filename):
    """Vérifie si le fichier a une extension autorisée"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Créer les dossiers nécessaires
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# 
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Initialiser la base de données
init_db()

@app.route('/')
def index():
    """Page d'accueil"""
    stats = get_document_stats()
    total_docs = sum([count for _, count in stats])
    return render_template('index.html', stats=stats, total_docs=total_docs)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload et classification de documents"""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Pas de fichier sélectionné', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('Pas de fichier sélectionné', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            try:
                # Sauvegarder le fichier
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Extraire le texte
                texte = extract_text(filepath)
                
                # Classifier le document
                categorie = classify_document(texte)
                
                # Ajouter à la base de données
                if add_document(filename, categorie, texte, filepath):
                    flash(f'Document classifié comme: {categorie}', 'success')
                else:
                    flash('Erreur lors de l\'ajout du document', 'error')
                
                return redirect(url_for('documents'))
            except Exception as e:
                flash(f'Erreur: {str(e)}', 'error')
                return redirect(request.url)
        else:
            flash('Format de fichier non autorisé', 'error')
            return redirect(request.url)
    
    return render_template('upload.html')

@app.route('/documents')
def documents():
    """Affiche tous les documents archivés"""
    docs = get_all_documents()
    return render_template('documents.html', documents=docs)

@app.route('/documents/<category>')
def documents_by_category(category):
    """Affiche les documents par catégorie"""
    docs = get_documents_by_type(category)
    return render_template('documents.html', documents=docs, category=category)

@app.route('/stats')
def stats():
    """Affiche les statistiques"""
    stats_data = get_document_stats()
    total_docs = sum([count for _, count in stats_data])
    return render_template('stats.html', stats=stats_data, total_docs=total_docs)

@app.errorhandler(404)
def page_not_found(e):
    """Gère les erreurs 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Gère les erreurs 500"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)