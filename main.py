import os
import PyPDF2
import docx2txt

def extract_text_from_pdf(pdf_path):
    """
    Extrait le texte d'un fichier PDF et retourne le texte sous forme de chaîne de caractères.
    """
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Parcours chaque page du PDF et extrait le texte
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    """
    Extrait le texte d'un fichier DOCX et retourne le texte sous forme de chaîne de caractères.
    """
    # Utilise docx2txt pour extraire le texte
    text = docx2txt.process(docx_path)
    return text

def save_text_to_file(text, output_file_path):
    """
    Sauvegarde le texte extrait dans un fichier texte.
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def extract_and_save_text(input_path, output_path):
    """
    Détecte le type de fichier (PDF ou DOCX), extrait le texte et le sauvegarde dans un fichier texte.
    """
    file_extension = os.path.splitext(input_path)[1].lower()

    if file_extension == '.pdf':
        # Appelle la fonction d'extraction pour les fichiers PDF
        extracted_text = extract_text_from_pdf(input_path)
    elif file_extension == '.docx':
        # Appelle la fonction d'extraction pour les fichiers DOCX
        extracted_text = extract_text_from_docx(input_path)
    else:
        raise ValueError(f"Format de fichier non pris en charge : {file_extension}")

    # Sauvegarde le texte extrait dans le fichier de sortie
    save_text_to_file(extracted_text, output_path)
    print(f"Texte extrait et sauvegardé dans {output_path}")

if __name__ == "__main__":
    # Chemin du fichier d'entrée (PDF ou DOCX)
    input_file_path = 'chemin/vers/votre/fichier.pdf'  # ou fichier.docx
    # Chemin du fichier de sortie (fichier texte)
    output_file_path = 'chemin/vers/votre/sortie.txt'

    # Exécute l'extraction et la sauvegarde
    extract_and_save_text(input_file_path, output_file_path)
