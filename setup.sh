#!/bin/bash

# Create necessary directories
mkdir -p App/Uploaded_Resumes
mkdir -p .streamlit

# Download NLTK data
python -c "import nltk; nltk.download('stopwords')"

# Download spaCy model (using spaCy 3.x model)
python -m spacy download en_core_web_sm

echo "Setup complete!"
