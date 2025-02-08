
import json
import duckdb
import pandas as pd


import dlt
from dlt.common.pendulum import pendulum
from dlt.sources.helpers import requests
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)

from typing import Any, Optional


# ============= #
# API Utilities #
# ============= #

# Authentication #

def _wto_auth(r, key: int = 1):
    """Return the authentication function for the WTO API."""
    # Validate key choice
    token = 'WTO_PRIMARY_KEY' \
        if key == 1 else 'WTO_SECONDARY_KEY'\
        if key == 2 else None

    # If not valid raise a ValueError
    if not token:
        raise ValueError('Invalid API key. Must be 1 or 2.')
    
    # Assign the headers
    r.headers = {'Cache-Control': 'no-cache',
                 'Ocp-Apim-Subscription-Key': dlt.secrets[token]}
        
    return r

def _wto_headers(key: int):
    """Return the headers for the WTO API."""
    token = 'WTO_PRIMARY_KEY' \
        if key == 1 else 'WTO_SECONDARY_KEY'\
        if key == 2 else None

    if not token:
        raise ValueError('Invalid API key. Must be 1 or 2.')
 
    headers = {'Cache-Control': 'no-cache',
               'Ocp-Apim-Subscription-Key': dlt.secrets[token]}
    
    return headers

# ============== #
# WTO References #
# ============== #

# Reference Parameters

def get_reference_parameters(endpoint: str) -> dict:
    """Return a dictionary of default API reference parameters.
    """
    match endpoint:
        
        case '/topics':
            params = dict(lang=1)
        
        case '/frequencies':
            params = dict(lang=1)
        
        case '/periods':
            params = dict(lang=1)
        
        case '/units':
            params = dict(lang=1)
        
        case '/indicator_categories':
            params = dict(lang=1)
        
        case '/indicators':
            params = dict(i='all',t='all',pc='all',
                          tp='all',frq='all',lang=1)
        
        case '/territory/regions':
            params = dict(lang=1)
        
        case '/territory/groups':
            params = dict(lang=1)
        
        case '/reporters':
            params = dict(ig='all', reg='all', gp='all', lang=1)

        case '/partners':
            params = dict(ig='all', reg='all', gp='all', lang=1)

        case '/product_classifications':
            params = dict(lang=1)

        case '/products':
            params = dict(pc='all', lang=1)

        case '/years':
            params = dict()
        
        case '/value_flags':
            params = dict(lang=1)
        
        case _:
            raise ValueError(f'Invalid endpoint: {endpoint}')

    return params

# Extract Data From a Resource

def fetch_reference_data(endpoint: str, params: dict):
    # Get the endpoint url
    url = f'https://api.wto.org/timeseries/v1{endpoint}'

    try:
        # Send the GET request
        response = requests.get(url=url, params=params, auth=_wto_auth)

        # Check for errors
        response.raise_for_status()

        yield from response.json()

    except Exception as err:
        print(err)

# Load Reference Data to DuckDB

def dlt_wto_reference_loader(
        endpoint: str,
        params: dict = None,
        loader: callable = None
    ):
    """Load reference data from the WTO API into a DuckDB database.
    """
    # Get dataset name
    _endpoint = endpoint.replace('/','_')
    
    # Initialize a dlt pipeline to duckdb
    pipeline = dlt.pipeline(
        pipeline_name=f'{_endpoint}_pipeline',
        destination='duckdb',
        dataset_name=f'wto_reference_{_endpoint}'
    )

    # If no parameters, read default parameters
    if not any(params):
        params = get_reference_parameters(endpoint)
    
    # Get the source for a given endpoint
    if not callable(loader):
        loader = fetch_reference_data(endpoint, params)

    # Run the pipeline
    info = pipeline.run(loader)

    # Print the pipeline info
    print(info)


    
    

def main():
    params = dict(
        i='TP_A_0010', r='all',
        p='default', ps='default',
        pc='default', spc='false',
        fmt='json', mode='full',
        dec='default', off='0',
        max='500', head='H',
        lang='1', meta='false'
    )
    # Load reporting economies to duckdb
    dlt_wto_reference_loader('reporters', params=params)

if __name__ == '__main__':
    print()
    main()
    print()