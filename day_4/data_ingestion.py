""" 
Read the data from the file and return the document
"""
from langchain_community.document_loaders import PyMuPDFLoader 

class DataIngestion:
    def __init__(self,path):
        self.path = path 

    def ingest_data(self):
        try:
            loader = PyMuPDFLoader(file_path=self.path) 
            return loader.load()
        except Exception as e:
            print(e)

