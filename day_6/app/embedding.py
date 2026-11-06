from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter 



from data_ingestion import load_documents

class Embedding:
    def __init__(self,chunk_size=500,chunk_overlap=200,model="all-MiniLM-L6-v2"):
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




