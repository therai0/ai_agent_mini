from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(path):
    try:
        loader = PyMuPDFLoader(path)
        return loader.load()
    except Exception as e:
        print(e)


