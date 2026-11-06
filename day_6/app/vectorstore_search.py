
import chromadb
import uuid
from sentence_transformers import SentenceTransformer
from constant import db_path,tenant,database,doc_path,transformer_model 
from embedding import Embedding 
from data_ingestion import load_documents 

client = chromadb.PersistentClient(path=db_path,tenant=tenant,database=database)
collection = client.get_or_create_collection(name="demo")

def vector_store(collection):
    try:
        doc = load_documents(path=doc_path)
        embedding = Embedding()
        chunks = embedding.chunk_doc(doc)
        vectors = embedding.embed_vector(chunks)
        texts = [chunk.page_content for chunk in chunks]
        ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
        metadatas = [chunk.metadata for chunk in chunks]
        collection.add(
            ids = ids,
            embeddings=vectors,
            documents=texts,
            metadatas=metadatas
        )
        print("successfully store")
    except Exception as e:
        print(e)


def vector_search(query,top_k=3):
    try:
        embeder = SentenceTransformer(transformer_model)
        vectors = embeder.encode(query)
        result = collection.query(
            query_embeddings=vectors,
            n_results=top_k
        )
        return result 
    except Exception as e:
        print(e)

