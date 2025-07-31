import pandas as pd
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

es = Elasticsearch(
    cloud_id=os.getenv("ELASTIC_CLOUD_ID"),
    basic_auth=(os.getenv("ES_USERNAME"), os.getenv("ES_PASSWORD"))
)

def read_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f" Successfully read {len(df)} rows from Excel.")
        return df.to_dict(orient='records')
    except Exception as e:
        print(f" Error reading Excel file: {e}")
        return []

def push_to_elasticsearch(index_name, data):
    if not es.indices.exists(index=index_name):
        try:
            es.indices.create(index=index_name)
            print(f" Created index: {index_name}")
        except Exception as e:
            print(f" Failed to create index '{index_name}': {e}")
            return

    for i, doc in enumerate(data):
        try:
            response = es.index(index=index_name, id=i+1, document=doc)
            print(f" Document {i+1} indexed: {response['result']}")
        except Exception as e:
            print(f" Failed to index document {i+1}: {e}")

if __name__ == "__main__":
    file_path = "data/product_list.xlsx"  
    data = read_excel_data(file_path)
    push_to_elasticsearch("product-list", data)
