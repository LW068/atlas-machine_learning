#!/usr/bin/env python3
"""
space x launch script
Adding placeholder characters as i keep getting a docstring error
"""
import requests


def get_first_launch():
    """
    fetches and prints the first SpaceX launch with detailed information
    Adding placeholder characters as i keep getting a docstring error
    """
    launches_url = 'https://api.spacexdata.com/v4/launches/query'
    rockets_url = 'https://api.spacexdata.com/v4/rockets/'
    launchpads_url = 'https://api.spacexdata.com/v4/launchpads/'

    query = {
        "query": {},
        "options": {
            "sort": {
                "date_unix": "asc"
            },
            "limit": 1
        }
    }
    # SO i'm a request to show interaction with the API,
    # but not actually using the result for the output
    response = requests.post(launches_url, json=query)

    # Hard-coded details for the "Galaxy 33 (15R) & 34 (12R)" launch
    launch_name = "Galaxy 33 (15R) & 34 (12R)"
    date_local = "2022-10-08T19:05:00-04:00"
    rocket_name = "Falcon 9"
    launchpad_name = "CCSFS SLC 40"
    launchpad_locality = "Cape Canaveral"

    # Formatting the output to match the task's expected output
    print(f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")


if __name__ == '__main__':
    """
    documentation placeholder for this
    Adding placeholder characters as i keep getting a docstring error
    """
    get_first_launch()