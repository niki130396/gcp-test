from fastapi import FastAPI
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("./gcp-service-account-keys.json")
client = bigquery.Client(credentials=credentials)

dataset = client.get_dataset("dataset")
table_id = f"{client.project}.{dataset.dataset_id}.students_table"


app = FastAPI()


@app.get("/people")
def get_people():
    query = f"""
        SELECT *
        FROM {table_id}
    """

    query_job = client.query(query)

    return {
        "people":
            [
                {
                    "name": row[0],
                    "age": row[1]
                } for row in query_job
            ]
    }
