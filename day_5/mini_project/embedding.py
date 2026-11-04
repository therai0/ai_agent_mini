
# class design to convert the text into vectors using open source model [all-MiniLM-L6-v2]
# chunking the document with the size of 600 and overlap size is 200
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Embdedding:
    def __init__(self, model="all-MiniLM-L6-v2", chunk_size=600, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model)

    def chunk_documents(self, documents):
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n", "\n", " ", ""],
            )
            chunks = splitter.split_documents(documents=documents)
            
            return chunks
        except Exception as e:
            print(e)

    def embed_chunks(self, chunks):
        try:
            text = [chunk.page_content for chunk in chunks]
            vectors = self.model.encode(text)
            return vectors
        except Exception as e:
            print(e)