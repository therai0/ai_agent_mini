""" 
Implement the vector store using chroma db
"""
import uuid
import chromadb  
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# function to read the pdf file from the particular file path and return the document
def data_ingestion(file_path):
    try:
        loader = PyMuPDFLoader(file_path=file_path)
        return loader.load() 
    except Exception as e:
        print(e)


# class design to convert the text into vectors using open source model [all-MiniLM-L6-v2]
# chunking the document with the size of 600 and overlap size is 200
class Embdedding:
    def __init__(self,model,chunk_size=600,chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model)

    def chunk_documents(self,documents):
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size = self.chunk_size,
                chunk_overlap = self.chunk_overlap,
                separators=["\n\n","\n"," ",""],
            ) 
            chunks = splitter.split_documents(documents=documents)
            return chunks
        except Exception as e:
            print(e)


    def embed_chunks(self,chunks):
        try:
            text = [chunk.page_content for chunk in chunks]
            vectors = self.model.encode(text)
            return vectors
        except Exception as e:
            print(e)



# function to add the data into collection 
def vector_store(chunks,vectors):
    try:
        client = chromadb.Client()
        collection = client.create_collection("demo")
        metadata = [chunk.metadata for chunk in chunks]
        text = [chunk.page_content for chunk in chunks]
        ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
        vectors = vectors
        collection.add(
            ids=ids,
            embeddings=vectors,
            metadatas=metadata,
            documents=text
        )
        
    except Exception as e:
        print(e)

    

if __name__ == "__main__":
    path = "./day_5/data/version_4.pdf"
    model = "all-MiniLM-L6-v2"
    document = data_ingestion(path)
    embed_doc = Embdedding(model=model)
    chunks = embed_doc.chunk_documents(document)
    vectors = embed_doc.embed_chunks(chunks=chunks)

    print(len(vectors[0]))
