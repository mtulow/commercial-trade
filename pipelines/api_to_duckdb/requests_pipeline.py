"""The Requests Pipeline Template provides a simple starting point for a dlt pipeline with the requests library"""

# mypy: disable-error-code="no-untyped-def,arg-type"

from typing import Iterator, Any

import dlt

from dlt.sources.helpers import requests
from dlt.sources.rest_api import (
    RESTAPIConfig,
    AuthConfigBase,
    check_connection,
    rest_api_resources,
    rest_api_source,
)
from dlt.sources import TDataItems


YEAR = 2022
MONTH = 10
BASE_PATH = "https://api.chess.com/pub/player"


@dlt.resource(primary_key="player_id")
def players():
    """Load player profiles from the chess api."""
    for player_name in ["magnuscarlsen", "rpragchess"]:
        path = f"{BASE_PATH}/{player_name}"
        response = requests.get(path)
        response.raise_for_status()
        yield response.json()


# this resource takes data from players and returns games for the configured
@dlt.transformer(data_from=players, write_disposition="append")
def players_games(player: Any) -> Iterator[TDataItems]:
    """Load all games for each player in october 2022"""
    player_name = player["username"]
    path = f"{BASE_PATH}/{player_name}/games/{YEAR:04d}/{MONTH:02d}"
    response = requests.get(path)
    response.raise_for_status()
    yield response.json()["games"]


@dlt.source(name="chess")
def chess():
    """A source function groups all resources into one schema."""
    return players(), players_games()


def load_chess_data() -> None:
    # specify the pipeline name, destination and dataset name when configuring pipeline,
    # otherwise the defaults will be used that are derived from the current script name
    p = dlt.pipeline(
        pipeline_name="chess",
        destination='duckdb',
        dataset_name="chess_data",
    )

    load_info = p.run(chess())

    # pretty print the information on data that was loaded
    print(load_info)  # noqa: T201

def get_topics_params(lang: int = 1):
    return dict(lang=lang)

def get_frequencies_params(lang: int = 1):
    return dict(lang=lang)

def get_periods_params(lang: int = 1):
    return dict(lang=lang)

def get_units_params(lang: int = 1):
    return dict(lang=lang)

def get_indicator_categories_params(lang: int = 1):
    return dict(lang=lang)

def get_indicators_params(indicator: str = None,
                          indicator_name: str = None,
                          topics: list[str] = [],
                          product_classifications: str | list[str] = [],
                          trade_partner: str = 'all',
                          lang: int = 1):
    # Default indicator is all
    indicator = indicator or 'all'

    # Default topic is all
    topics = ','.join(topics) if any(topics) else 'all'

    # Default product classifications is all
    if not product_classifications:
        product_classifications = 'n'
    if product_classifications != 'all':    # all
        # None
        
    elif isinstance(product_classifications, list) and len(product_classifications) > 0:

        product_classifications = product_classifications[0]
    if product_classifications is None or product_classifications == 'all':
        product_classifications = str(product_classifications).lower()
    elif any()
    else:
        product_classifications = ','.join(product_classifications)



    product_classifications = ','.join(product_classifications) if any(product_classifications) else str(product_classifications)
    if product_classifications is None:
        product_classifications = []
    if any(product_classifications):
        product_classifications = ','.join(product_classifications)
    else:
    product_classifications = ','.join(product_classifications) if any(product_classifications) else 'all'



    params = dict(i=indicator,
                  name=indicator_name)


def get_wto_endpoint_params(endpoint: str) -> dict:
    # references

    match endpoint:
        case 'references':
            params = get_topics_params()
        case 'frequencies':
            params = get_frequencies_params()
        case 'periods':
            par
        case _:
            params = {}
    return params
    




def fetch_wto_endpoint(endpoint: str, params: dict | None = None):
    # Get the API endpoint URL
    url = f'http://api.wto.org/timeseries/v1/{endpoint}'
    # Get the endpoint parameters
    params = read

def ingest_topics() -> None:
    pipeline = dlt.pipeline(
        pipeline_name='topics_pipeline',
        destination='duckdb',
        dataset_name='wto_reference_topics'
    )

    pipeline.run()

if __name__ == "__main__":
    load_chess_data()
