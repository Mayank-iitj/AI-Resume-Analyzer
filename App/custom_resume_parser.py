"""
Custom Resume Parser - Replacement for pyresparser
This module provides resume parsing functionality without config file dependencies
"""

import re
import spacy
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from io import StringIO
import os


class CustomResumeParser:
    """
    Custom resume parser that doesn't require config files.
    Extracts: name, email, phone, skills, degree, page count
    """
    
    def __init__(self, resume_path):
        self.resume_path = resume_path
        self.text = self._extract_text_from_pdf()
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except:
            # Fallback if spaCy model not available
            self.nlp = None
        
    def _extract_text_from_pdf(self):
        """Extract text from PDF file"""
        try:
            resource_manager = PDFResourceManager()
            fake_file_handle = StringIO()
            converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            
            with open(self.resume_path, 'rb') as fh:
                for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)
                
                text = fake_file_handle.getvalue()
            
            converter.close()
            fake_file_handle.close()
            return text
        except Exception as e:
            return ""
    
    def _extract_email(self):
        """Extract email using regex"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, self.text)
        return emails[0] if emails else None
    
    def _extract_phone(self):
        """Extract phone number using regex"""
        # Patterns for various phone formats
        patterns = [
            r'(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # US format
            r'(\+\d{1,3}[-.\s]?)?\d{10}',  # 10 digit
            r'(\+\d{1,3}[-.\s]?)?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # With separators
        ]
        
        for pattern in patterns:
            phones = re.findall(pattern, self.text)
            if phones:
                # Clean up the phone number
                phone = ''.join(filter(str.isdigit, str(phones[0])))
                if len(phone) >= 10:
                    return phone
        return None
    
    def _extract_name(self):
        """Extract name using spaCy NER"""
        if not self.nlp:
            # Fallback: get first line that looks like a name
            lines = self.text.split('\n')
            for line in lines[:5]:  # Check first 5 lines
                line = line.strip()
                if line and len(line.split()) <= 4 and len(line) < 50:
                    # Likely a name if it's short and at the top
                    return line
            return None
        
        doc = self.nlp(self.text[:1000])  # Process first 1000 chars
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                return ent.text
        
        # Fallback to first capitalized words
        lines = self.text.split('\n')
        for line in lines[:5]:
            words = line.strip().split()
            if len(words) >= 2 and all(w[0].isupper() for w in words[:2] if w):
                return ' '.join(words[:3])
        return None
    
    def _extract_skills(self):
        """Extract skills from resume"""
        # Common technical skills
        skills_db = [
            'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin',
            'react', 'angular', 'vue', 'node', 'django', 'flask', 'spring', 'express',
            'html', 'css', 'sql', 'nosql', 'mongodb', 'postgresql', 'mysql', 'redis',
            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git', 'ci/cd',
            'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
            'data analysis', 'pandas', 'numpy', 'matplotlib', 'tableau', 'power bi',
            'agile', 'scrum', 'jira', 'rest api', 'graphql', 'microservices',
            'linux', 'unix', 'bash', 'shell scripting', 'devops', 'testing', 'selenium'
        ]
        
        text_lower = self.text.lower()
        found_skills = []
        
        for skill in skills_db:
            if skill in text_lower:
                found_skills.append(skill.title())
        
        return list(set(found_skills))  # Remove duplicates
    
    def _extract_degree(self):
        """Extract education degree"""
        degrees = [
            'B.Tech', 'B.E.', 'M.Tech', 'M.E.', 'PhD', 'MBA', 'BBA', 'MCA', 'BCA',
            'Bachelor', 'Master', 'Doctorate', 'B.Sc', 'M.Sc', 'B.A.', 'M.A.',
            'Engineering', 'Computer Science', 'Information Technology'
        ]
        
        found_degrees = []
        for degree in degrees:
            if degree.lower() in self.text.lower():
                found_degrees.append(degree)
        
        return found_degrees if found_degrees else None
    
    def _get_page_count(self):
        """Get number of pages in PDF"""
        try:
            with open(self.resume_path, 'rb') as fh:
                pages = list(PDFPage.get_pages(fh))
                return len(pages)
        except:
            return 1
    
    def get_extracted_data(self):
        """
        Main method to extract all data from resume
        Returns dict with: name, email, mobile_number, skills, degree, no_of_pages
        """
        return {
            'name': self._extract_name(),
            'email': self._extract_email(),
            'mobile_number': self._extract_phone(),
            'skills': self._extract_skills(),
            'degree': self._extract_degree(),
            'no_of_pages': self._get_page_count()
        }


# Backward compatibility alias
ResumeParser = CustomResumeParser
