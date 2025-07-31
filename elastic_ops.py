from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv() 

def get_es_client():
    es = Elasticsearch(
        os.getenv("ES_HOST"),
        basic_auth=(os.getenv("ES_USERNAME"), os.getenv("ES_PASSWORD")),
        request_timeout=30,
        verify_certs=True
    )
    return es

def index_sample_data():
    es = get_es_client()
    doc = {"message": "Hello from Dagster!", "status": "success"}
    response = es.index(index="dagster-demo", document=doc)
    return response
