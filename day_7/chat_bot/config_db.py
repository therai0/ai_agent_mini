from chromadb.config import Settings
import chromadb 

from constant import tenant,database,db_path 


def config_chromdb():
    try:
        settings = Settings(
            is_persistent=True,
            persist_directory=db_path
        )

        admin = chromadb.AdminClient(settings=settings)
        admin.create_tenant(name=tenant)
        admin.create_database(tenant=tenant,name=database)

        print("database and tenant creat scussesfully")
    except Exception as e:
        print(e)


config_chromdb()







