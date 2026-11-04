from sentence_transformers import SentenceTransformer
import chromadb

database_path = "./day_5/mini_project/chroma"
tenant = "report_app"
database = "reportapp_db"

client = chromadb.PersistentClient(path=database_path,tenant=tenant,database=database)
collection= client.get_collection(name="report_tb")

def search_vector(query,top_k:int,collection,model="all-MiniLM-L6-v2"):
    embedding = SentenceTransformer(model)
    vectors = embedding.encode(query).tolist()
    result = collection.query(
        query_embeddings= vectors,
        n_results=top_k
    )
    print(result["documents"])
    

search_vector("Who is Barsha Dangi",3,collection)


