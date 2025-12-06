#!/bin/bash

# Create necessary directories
mkdir -p App/Uploaded_Resumes
mkdir -p .streamlit

# Download NLTK data
python3 -c "import nltk; nltk.download('stopwords', download_dir='/home/appuser/nltk_data')"
python3 -c "import nltk; nltk.download('punkt', download_dir='/home/appuser/nltk_data')"
python3 -c "import nltk; nltk.download('averaged_perceptron_tagger', download_dir='/home/appuser/nltk_data')"

# Download spaCy model (using spaCy 3.x model)
python3 -m spacy download en_core_web_sm

echo "Setup complete!"
