#!/usr/bin/env python3
"""space x launch script"""
import requests


def get_first_launch():
    """fetches and prints the first SpaceX launch with detailed information"""
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
    launchpad_id = launch_data['launchpad']

    # fetching rocket info
    rocket_response = requests.get(f'{rockets_url}{rocket_id}')
    if rocket_response.status_code == 200:
        rocket_info = rocket_response.json()
        rocket_name = rocket_info['name']
    else:
        rocket_name = "Unknown Rocket"

    launchpad_response = requests.get(f'{launchpads_url}{launchpad_id}')
    if launchpad_response.status_code == 200:
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data['name']
        launchpad_locality = launchpad_data['locality']
    else:
        launchpad_name = "Unknown Launchpad"
        launchpad_locality = "Unknown Locality"

    launch_details = (
        f"{launch_name} ({date_local}) {rocket_name} - "
        f"{launchpad_name} ({launchpad_locality})"
    )
    print(launch_details)


if __name__ == '__main__':
    """documentation placeholder for this"""
    get_first_launch()
