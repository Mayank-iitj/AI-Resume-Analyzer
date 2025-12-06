# AI Resume Analyzer - Deployment Guide

## 🚀 Quick Deploy to Streamlit Cloud

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))

### Steps

1. **Fork or Clone the Repository**
   ```bash
   git clone https://github.com/Mayank-iitj/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository: `Mayank-iitj/AI-Resume-Analyzer`
   - Main file path: `App/App.py`
   - Click "Deploy"

3. **Configure Secrets** (Optional - for database)
   - In Streamlit Cloud dashboard, go to your app settings
   - Click "Secrets"
   - Add your database credentials:
   ```toml
   [database]
   host = "your-db-host"
   user = "your-db-user"
   password = "your-db-password"
   name = "cv"
   ```

---

## 💻 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Mayank-iitj/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venvapp
venvapp\Scripts\activate

# Linux/Mac
python3 -m venv venvapp
source venvapp/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Setup Database
Create a MySQL database named `cv`:
```sql
CREATE DATABASE cv;
```

Update database credentials in `App/App.py` (line 95) or use environment variables (see below).

### 5. Run the Application
```bash
cd App
streamlit run App.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🔐 Environment Variables (Recommended)

For better security, use environment variables instead of hardcoding credentials.

### 1. Create `.env` file
Copy the example file:
```bash
cp .env.example .env
```

### 2. Edit `.env` with your credentials
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=cv
ENVIRONMENT=development
```

### 3. Update `App.py` to use environment variables
Add at the top of `App/App.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

# Replace line 95 with:
connection = pymysql.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', 'root@MySQL4admin'),
    db=os.getenv('DB_NAME', 'cv')
)
```

---

## 📦 Project Structure

```
AI-Resume-Analyzer/
├── App/
│   ├── App.py                 # Main application file
│   ├── Courses.py             # Course recommendations data
│   ├── requirements.txt       # Python dependencies (legacy)
│   ├── Logo/                  # Application logos
│   └── Uploaded_Resumes/      # Uploaded resume storage
├── pyresparser/
│   └── resume_parser.py       # Custom resume parser
├── screenshots/               # Application screenshots
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── .gitignore                # Git ignore rules
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies (root)
├── setup.sh                  # Deployment setup script
├── packages.txt              # System dependencies
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## 🔧 Configuration Files

### `.streamlit/config.toml`
Streamlit app configuration (theme, server settings)

### `setup.sh`
Automatically runs on Streamlit Cloud deployment to:
- Create necessary directories
- Download NLTK stopwords
- Install spaCy language model

### `packages.txt`
System-level dependencies for Streamlit Cloud

---

## 🐛 Troubleshooting

### Issue: "GeocoderUnavailable" error
**Solution**: Check your internet connection. The app uses geocoding to fetch location data.

### Issue: Database connection failed
**Solutions**:
1. Verify MySQL is running
2. Check database credentials
3. Ensure database `cv` exists
4. For Streamlit Cloud, configure secrets properly

### Issue: NLTK data not found
**Solution**: Run in Python:
```python
import nltk
nltk.download('stopwords')
```

### Issue: spaCy model not found
**Solution**: 
```bash
python -m spacy download en_core_web_sm
```

### Issue: File upload not working
**Solution**: Ensure `App/Uploaded_Resumes/` directory exists and has write permissions

---

## 🌐 Deployment Platforms

### Streamlit Cloud (Recommended)
- **Pros**: Free, easy setup, automatic deployments
- **Cons**: Limited resources, public apps only (free tier)
- **Best for**: Demos, portfolios, small projects

### Heroku
```bash
# Add Procfile
echo "web: sh setup.sh && streamlit run App/App.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

EXPOSE 8501

CMD ["streamlit", "run", "App/App.py"]
```

---

## 📝 Admin Access

**Default Credentials:**
- Username: `admin`
- Password: `admin@resume-analyzer`

**⚠️ Important**: Change these credentials before deploying to production!

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**MAYANK SHARMA**

---

## 🙏 Acknowledgments

- Dr Bright - (The Full Stack Data Scientist BootCamp)
- pyresparser library
- Streamlit framework
