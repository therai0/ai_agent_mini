from data_ingestion import data_ingestion
from embedding import Embdedding
from config import config_vector_store
import uuid
import chromadb

file_path = "./day_5/mini_project/data/barsha.pdf"
database_path = "./day_5/mini_project/chroma"
tenant = "report_app"
database = "reportapp_db"


documents = data_ingestion(file_path)

embedding = Embdedding()
chunks = embedding.chunk_documents(documents=documents)

vectors = embedding.embed_chunks(chunks=chunks)


# connection = config_vector_store(
#     path=database_path, tenant=tenant, database=database, connection=connection
# )

client = chromadb.PersistentClient(
    path=database_path,
    tenant=tenant,
    database=database
)
connection  = client.create_collection(name="report_tb")

def save_vector(chunks, connection,vectors):
    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
    documents = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    connection.add(ids=ids, embeddings=vectors,documents=documents, metadatas=metadatas)


save_vector(chunks, connection,vectors)
print("data save successfully")

