"""
Comprehensive Test Script for AI Resume Analyzer
Tests all imports, syntax, and critical functionality
"""

import sys
import os

print("="*60)
print("AI RESUME ANALYZER - COMPREHENSIVE TEST")
print("="*60)

# Test 1: Python Version
print("\n[TEST 1] Python Version")
print(f"✅ Python {sys.version}")

# Test 2: Critical Imports
print("\n[TEST 2] Testing Critical Imports...")
errors = []

try:
    import streamlit
    print("✅ streamlit")
except ImportError as e:
    errors.append(f"❌ streamlit: {e}")
    print(f"❌ streamlit - NOT INSTALLED")

try:
    import pandas
    print("✅ pandas")
except ImportError as e:
    errors.append(f"❌ pandas: {e}")
    print(f"❌ pandas - NOT INSTALLED")

try:
    import pymysql
    print("✅ pymysql")
except ImportError as e:
    errors.append(f"❌ pymysql: {e}")
    print(f"❌ pymysql - NOT INSTALLED")

try:
    import plotly
    print("✅ plotly")
except ImportError as e:
    errors.append(f"❌ plotly: {e}")
    print(f"❌ plotly - NOT INSTALLED")

try:
    from PIL import Image
    print("✅ PIL (Pillow)")
except ImportError as e:
    errors.append(f"❌ PIL: {e}")
    print(f"❌ PIL - NOT INSTALLED")

try:
    import nltk
    print("✅ nltk")
except ImportError as e:
    errors.append(f"❌ nltk: {e}")
    print(f"❌ nltk - NOT INSTALLED")

try:
    import spacy
    print("✅ spacy")
except ImportError as e:
    errors.append(f"❌ spacy: {e}")
    print(f"❌ spacy - NOT INSTALLED")

try:
    from pyresparser import ResumeParser
    print("✅ pyresparser")
except ImportError as e:
    errors.append(f"❌ pyresparser: {e}")
    print(f"❌ pyresparser - NOT INSTALLED")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv")
except ImportError as e:
    errors.append(f"❌ python-dotenv: {e}")
    print(f"❌ python-dotenv - NOT INSTALLED")

try:
    from streamlit_tags import st_tags
    print("✅ streamlit-tags")
except ImportError as e:
    errors.append(f"❌ streamlit-tags: {e}")
    print(f"❌ streamlit-tags - NOT INSTALLED")

try:
    from pdfminer3.layout import LAParams
    print("✅ pdfminer3")
except ImportError as e:
    errors.append(f"❌ pdfminer3: {e}")
    print(f"❌ pdfminer3 - NOT INSTALLED")

try:
    import geocoder
    print("✅ geocoder")
except ImportError as e:
    errors.append(f"❌ geocoder: {e}")
    print(f"❌ geocoder - NOT INSTALLED")

try:
    from geopy.geocoders import Nominatim
    print("✅ geopy")
except ImportError as e:
    errors.append(f"❌ geopy: {e}")
    print(f"❌ geopy - NOT INSTALLED")

# Test 3: File Structure
print("\n[TEST 3] Testing File Structure...")
required_files = [
    'App/App.py',
    'App/Courses.py',
    'App/Logo/RESUM.png',
    'App/Logo/recommend.png',
    'requirements.txt',
    'Procfile',
    'railway.json',
    '.gitignore'
]

for file in required_files:
    if os.path.exists(file):
        print(f"✅ {file}")
    else:
        errors.append(f"❌ Missing file: {file}")
        print(f"❌ {file} - MISSING")

# Test 4: Directory Structure
print("\n[TEST 4] Testing Directory Structure...")
required_dirs = [
    'App',
    'App/Logo',
    'App/Uploaded_Resumes'
]

for dir_path in required_dirs:
    if os.path.exists(dir_path):
        print(f"✅ {dir_path}/")
    else:
        errors.append(f"❌ Missing directory: {dir_path}")
        print(f"❌ {dir_path}/ - MISSING")

# Test 5: Syntax Check
print("\n[TEST 5] Testing Python Syntax...")
try:
    import ast
    with open('App/App.py', 'r', encoding='utf-8') as f:
        ast.parse(f.read())
    print("✅ App/App.py - Syntax Valid")
except SyntaxError as e:
    errors.append(f"❌ Syntax Error in App.py: {e}")
    print(f"❌ App/App.py - SYNTAX ERROR: {e}")

try:
    with open('App/Courses.py', 'r', encoding='utf-8') as f:
        ast.parse(f.read())
    print("✅ App/Courses.py - Syntax Valid")
except SyntaxError as e:
    errors.append(f"❌ Syntax Error in Courses.py: {e}")
    print(f"❌ App/Courses.py - SYNTAX ERROR: {e}")

# Test 6: Environment Variables
print("\n[TEST 6] Testing Environment Configuration...")
from dotenv import load_dotenv
load_dotenv()

db_enabled = os.getenv('DB_ENABLED', 'false')
print(f"✅ DB_ENABLED = {db_enabled}")

# Summary
print("\n" + "="*60)
print("TEST SUMMARY")
print("="*60)

if errors:
    print(f"\n❌ FAILED - {len(errors)} error(s) found:\n")
    for error in errors:
        print(f"  {error}")
    print("\n📦 Missing packages can be installed with:")
    print("  pip install -r requirements.txt")
    print("  python -m spacy download en_core_web_sm")
else:
    print("\n✅ ALL TESTS PASSED!")
    print("\n🚀 Your app is ready to run:")
    print("  set DB_ENABLED=false")
    print("  streamlit run App/App.py")

print("\n" + "="*60)
