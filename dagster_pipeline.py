from dagster import job, op
from elastic_ops import index_sample_data

@op
def send_data_to_elasticsearch(context):
    result = index_sample_data()
    context.log.info(f"Indexed to ES: {result['_id']}")

@job
def elastic_job():
    send_data_to_elasticsearch()
