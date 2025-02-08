
import duckdb

import dlt
from dlt.sources.helpers import requests


def extract_data_from_api(api_url: str, params: dict = None):
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    yield from response.json()

def load_data_to_duckdb(data, table_name):
    con = duckdb.connect(database=':memory:')
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM data")
    con.close()

def run_pipeline(api_url, params=None, table_name='api_data'):
    # Fetch data from API
    data = extract_data_from_api(api_url, params)

    # Initialize a dlt pipeline to duckdb
    pipeline = dlt.pipeline(
        pipeline_name=f'{table_name}_pipeline',
        destination='duckdb',
        dataset_name=f'{table_name}_dataset'
    )

    # Load data into DuckDB
    load_data_to_duckdb(data, table_name)

    # Run the pipeline
    info = pipeline.run(data)

    # Print the pipeline info
    print(info)

# Example usage
api_url = 'https://api.example.com/data'
params = {'param1': 'value1', 'param2': 'value2'}
run_pipeline(api_url, params, table_name='example_data')