import dlt
from dlt.sources.helpers import requests
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources




@dlt.source
def wto_quarterly_merchandise_imports(api_key: str = dlt.secrets.value):
    config: RESTAPIConfig = {
        "client": {
            'base_url': 'http://api.wto.org/timeseries/v1',
            'headers': {
                'Cache-Control': 'no-cache',
                'Ocp-Apim-Subscription-Key': api_key
            }
        },
        "resources": [
            {
                'endpoint': 'data',
            }
        ],
    }
    return rest_api_resources(config)


def wto_quarterly_merchandise_imports(
        endgoint: str, params: dict = None
    ):
    """Yields timeseries data from the WTO API."""
    # Specify the URL of the API endpoint
    url = ('https://api.wto.org/timeseries/v1/data' \
               '?i=ITS_MTV_QM&r=all&p=default&ps=default' \
               '&pc=default&spc=false&fmt=json&mode=full&' \
               'dec=default&off=100&max=3000&head=H&lang=1' \
               '&meta=false')

    # Make a request and check if it was successful
    response = requests.get(url, )
    response.raise_for_status()

    pipeline = dlt.pipeline(
        pipeline_name='wto_api',
        destination='duckdb',
        dataset_name='timeseries',
    )
    # The response contains a list
    load_info = pipeline.run(
        response.json(),
        table_name=endgoint,
        write_disposition="replace"  # <-- Add this line
    )

    print(load_info)



def main():
    wto_quarterly_merchandise_imports('ITS_MTV_QM', )



if __name__ == "__main__":
    main()