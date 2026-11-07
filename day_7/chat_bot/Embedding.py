
from langchain_community.document_loaders.json_loader import JSONLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from sentence_transformers import SentenceTransformer 
from constant import transformer_model

class Embedding:
    def __init__(self,chunk_size:int,chunk_overlap:int,model):
        self.model = SentenceTransformer(model)
        self.chunk_size=chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_doc(self,documents):
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size= self.chunk_size,
                chunk_overlap = self.chunk_overlap,
                separators = ["\n\n","\n"," ", ""]
            )
            chunks = splitter.split_documents(documents)
            return chunks
        except Exception as e:
            print(e)

    def embed_vector(self,chunks):
        try:
            texts = [chunk.page_content for chunk in chunks]
            vectors = self.model.encode(texts)
            return vectors
        except Exception as e:
            print(e)
        