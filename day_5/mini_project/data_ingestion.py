from langchain_community.document_loaders import PyMuPDFLoader
import os 
def data_ingestion(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File not found error")
        loader = PyMuPDFLoader(path)
        return loader.load()
    except FileNotFoundError as e:
        print(e)