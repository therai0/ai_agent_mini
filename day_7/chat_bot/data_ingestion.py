"""
Read the data from the json data
"""

import os
import json
from langchain_community.document_loaders.json_loader import JSONLoader


def load_data(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File doesn't exist")

        loader = JSONLoader(
            path,
            jq_schema=".[].content",
            text_content=False,
            metadata_func= lambda record,metadata: {
                **metadata,
                "topics":list(record.keys())
            }
        )
        return loader.load()
    except Exception as e:
        print(e)


