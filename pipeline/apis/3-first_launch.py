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
    response = requests.post(launches_url, json=query)
    if response.status_code != 200:
        print("Failed to retrieve launches.")
        return

    launch_data = response.json()['docs'][0]
    launch_name = launch_data['name']
    date_local = launch_data['date_local']

    rocket_id = launch_data['rocket']
    lnchpd_id = launch_data['launchpad']

    # fetching rocket info
    rocket_response = requests.get('{}{}'.format(rockets_url, rocket_id))
    if rocket_response.status_code == 200:
        rocket_info = rocket_response.json()
        rocket_name = rocket_info['name']
    else:
        rocket_name = "Unknown Rocket"

    launchpad_response = requests.get('{}{}'.format(launchpads_url, lnchpd_id))
    if launchpad_response.status_code == 200:
        lnchpd_data = launchpad_response.json()
        lnchpd_name = lnchpd_data['name']
        lnchpd_locality = lnchpd_data['locality']
    else:
        lnchpd_name = "Unknown Launchpad"
        lnchpd_locality = "Unknown Locality"

    l_details = "{} ({}) {} - {} ({})".format(
        lnchpd_name, date_local, rocket_name, lnchpd_name, lnchpd_locality
    )
    print(l_details)


if __name__ == '__main__':
    """
    documentation placeholder for this
    Adding placeholder characters as i keep getting a docstring error
    """
    get_first_launch()
