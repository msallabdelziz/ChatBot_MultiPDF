import streamlit as st

st.title("Chatbot pour PDF")

# Zone pour télécharger des fichiers PDF
uploaded_files = st.file_uploader("Téléchargez des fichiers PDF", type=["pdf"])

if uploaded_files:
    # Vous pouvez traiter les fichiers PDF ici
    for file in uploaded_files:
        # Insérez ici le code pour traiter les fichiers PDF
        pass
