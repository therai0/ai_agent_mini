
import chromadb
from chromadb.config import Settings 

def config_vector_store(path,tenant,database):
    setting = Settings(
        is_persistent=True,
        persist_directory=path 
    )

    admin = chromadb.AdminClient(settings=setting)
    admin.create_tenant(name=tenant)
    admin.create_database(
        tenant=tenant,
        name=database
    )

    client = chromadb.PersistentClient(
        path=path ,
        tenant=tenant,
        database=database 
    )

    # connection = client.create_collection(name=connection)
    return client


    


