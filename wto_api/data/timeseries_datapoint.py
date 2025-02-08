import dlt
from dlt.sources.helpers import requests
from dlt.sources.rest_api import (
    rest_api_source,
    rest_api_resources
)


# Resource Configuration

########### Python 3.2 #############
import urllib.request, json


def wto_timeseries_datapoint_loader(params: dict):
    """Return a list of datapoints for a given timeseries.
    """
    try:
        url = "https://api.wto.org/timeseries/v1/data"

        hdr = {
            # Request headers
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': dlt.secrets.wto_api_key
        }

        response = requests.get(url, params=params, auth=dlt.secrets.wto_api_key,)
        
        response.raise_for_status()

        yield from response.json()

    except Exception as e:
        print(e)
####################################


# Source Configuration
# See: https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api/basic#source-configuration

# # 
# 

# def get_client_config(
#         base_url: str,
#         headers: dict = None,
#         auth: str = dlt.secrets.wto_api_key,
#     ):
#     """Return 
#     """
#     pass




# config = {
#     "client": {
#         'base_url': str(),
#         'headers': {},
#         'auth': 
#         # ...
#     },
#     "resource_defaults": {
#         # ...
#     },
#     "resources": [
#         # ...
#     ],
# } 





def main():
    params = dict()

    wto_timeseries_datapoint_loader(params)

if __name__ == '__main__':
    print()
    main()
    print()
