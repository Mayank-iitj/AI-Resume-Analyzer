# Installation Script for AI Resume Analyzer
# Run this to install all dependencies

Write-Host "Installing AI Resume Analyzer Dependencies..." -ForegroundColor Green
Write-Host "=" * 60

# Install Python packages
Write-Host "`nInstalling Python packages..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt

# Download spaCy model
Write-Host "`nDownloading spaCy language model..." -ForegroundColor Yellow
python -m spacy download en_core_web_sm

# Download NLTK data
Write-Host "`nDownloading NLTK data..." -ForegroundColor Yellow
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"

Write-Host "`n" + "=" * 60
Write-Host "✅ Installation Complete!" -ForegroundColor Green
Write-Host "`nTo run the app:" -ForegroundColor Cyan
Write-Host "  `$env:DB_ENABLED='false'" -ForegroundColor White
Write-Host "  streamlit run App/App.py" -ForegroundColor White
Write-Host "=" * 60
