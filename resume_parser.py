import csv
import re
import spacy
import sys
from importlib import reload
reload(sys)
import pandas as pd
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import numpy as np
import urllib
from urllib.request import urlopen
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
#Function to extract name
def extract_name(string):
   # r1 = String(string,'utf-8')
    nlp = spacy.load('xx_ent_wiki_sm')

    doc = nlp(string)
    for ent in doc.ents:
        if(ent.label_ == 'PER'):
            print(ent.text)
            break
#Function to extract Phone Numbers
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
#Function to extract Email
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
resume_string = convert(r"C:\Users\Dell\Desktop\SAMPLE1.pdf")
resume_string1 = resume_string
resume_string = resume_string.replace(',',' ')
resume_string = resume_string.lower()

with open(r'C:\Users\Dell\Documents\resume-parser\techatt.csv') as f:
    reader = csv.reader(f)
    your_listatt = list(reader)
with open(r'C:\Users\Dell\Documents\resume-parser\techskill.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
with open(r'C:\Users\Dell\Documents\resume-parser\nontechnicalskills.csv') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)

s = set(your_list[0])
s1 = your_list
s2 = your_listatt
skillindex = []
skills = []
skillsatt = []
print('Candidate Name')
extract_name(resume_string1)
print('\n')
print('Phone Number is')
y = extract_phone_numbers(resume_string)
y1 = []
for i in range(len(y)):
    if(len(y[i])>9):
        y1.append(y[i])
print(y1)
print('\n')
print('Email id:')
print(extract_email_addresses(resume_string))
for word in resume_string.split(" "):
    if word in s:
        skills.append(word)
skills1 = list(set(skills))
print('\n')
print("Technical Skills")
print('\n')
np_a1 = np.array(your_list)
for i in range(len(skills1)):
    item_index = np.where(np_a1==skills1[i])
    skillindex.append(item_index[1][0])

nlen = len(skillindex)
for i in range(nlen):
    print(skills1[i])
    print(s2[0][skillindex[i]])
    print('\n')

s1 = set(your_list1[0])
nontechskills = []
for word in resume_string.split(" "):
    if word in s1:
        nontechskills.append(word)
nontechskills = set(nontechskills)
print('\n')

print("Non Technical Skills")
list5 = list(nontechskills)
print('\n')
for i in range(len(list5)):
    print(list5[i])
print('\n \n')
