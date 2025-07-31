from dagster import op, job

def read_excel_data(file_path):
   
    pass

def push_to_elasticsearch(index, data):
   
    pass

@op
def get_excel_data():
    return read_excel_data("product_list.xlsx")

@op
def send_data_to_elasticsearch(data):
    push_to_elasticsearch("product-list", data)

@job
def excel_to_elasticsearch_job():
    send_data_to_elasticsearch(get_excel_data())
