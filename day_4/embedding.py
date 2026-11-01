
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


class Embedding:
    def __init__(self,model="all-MiniLM-L6-v2",chunk_size = 500,chunk_overlap=200):
        self.model = SentenceTransformer(model)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_document(self,documents):
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size = self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n","\n"," ",""],
                length_function=len
            )
            chunks = splitter.split_documents(documents)
            print(f"{len(documents)} chunks into {len(chunks)}")
            return chunks
        except Exception as e:
            print(e)

    def embed_chunk(self,chunks):
        try:
            text = [chunk.page_content for chunk in chunks ]
            print(f"Converting {len(text)} text in chunks")
            embedding = self.model.encode(text,show_progress_bar=True)
            print(f"Embedding shape:{embedding.shape}")
            return embedding
        except Exception as e:
            print(e)
