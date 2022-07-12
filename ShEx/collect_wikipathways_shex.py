# -*- coding: utf-8 -*-
"""collect_wikipathways_shex.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yq8Z92vNAAXD9ExlK1jcJnYIGfBl4_h9

This notebook was developed on google colab: https://colab.research.google.com/drive/1yq8Z92vNAAXD9ExlK1jcJnYIGfBl4_h9?usp=sharing
"""

from rdflib import Graph
import requests
from bs4 import BeautifulSoup, SoupStrainer
import zipfile
import io
from contextlib import closing
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE

def fetch_wprdf():
  temp = Graph()
  url = 'http://data.wikipathways.org/current/rdf'
  page = requests.get(url).text
  files = []
  for link in BeautifulSoup(page, "lxml", parse_only=SoupStrainer('a')):
      address = str(link).split("\"")
      if len(address) > 1:
          filename = address[1].replace("./", "/")
          if len(filename) > 1:
              if filename not in files:
                  if filename != "./":
                      files.append(url + filename)
  for file in set(files):
      if "rdf-authors" in file:  # get the most accurate file
          print(file)
          u = requests.get(file)
          with closing(u), zipfile.ZipFile(io.BytesIO(u.content)) as archive:
              for member in archive.infolist():
                  if "_" in str(member.filename):
                      continue
                  print("parsing: " + member.filename)
                  nt_content = archive.read(member)
                  temp.parse(data=nt_content, format="turtle")
          print("size: "+str(len(temp)))

      if "rdf-wp" in file:  # get the most accurate file
          print(file)
          u = requests.get(file)
          with closing(u), zipfile.ZipFile(io.BytesIO(u.content)) as archive:
              for member in archive.infolist():
                  nt_content = archive.read(member)
                  temp.parse(data=nt_content.decode(), format="turtle")
          print("size: "+str(len(temp)))
  return temp

wprdf = fetch_wprdf()

"""# Extract the Shape Expression
A shape expression is a formal description of a (subset of a) RDF file. 
"""


import pprint

q = "select ?class where { ?item rdf:type ?class }"
target_classes = []
x = wprdf.query(q)
for target_class in x:
  if str(target_class["class"]) not in target_classes:
    target_classes.append(str(target_class["class"]))

shex_target_file = "wikipathways.shex"

shaper = Shaper(target_classes=target_classes,
                rdflib_graph=wprdf,
                input_format=TURTLE,
                )  # Default rdf:type
            
shaper.shex_graph(output_file=shex_target_file)
