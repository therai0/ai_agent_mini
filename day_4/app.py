


from data_ingestion import DataIngestion
from embedding import Embedding

file_path = "./day_4/data/deepmind.pdf"
if __name__== "__main__":
    di = DataIngestion(file_path)
    documents = di.ingest_data()
    embedding = Embedding()
    chunks = embedding.chunk_document(documents)
    print(chunks)
    vectors = embedding.embed_chunk(chunks)
    print(vectors)

    