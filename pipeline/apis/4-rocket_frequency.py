#!/usr/bin/env python3
"""script for rocket launch frequency"""

import requests

def get_launches_by_rocket():
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    launches_data = response.json()
    rocket_launches = {}

    for launch in launches_data:
        rocket_name = launch['rocket']['rocket_name']
        if rocket_name in rocket_launches:
            rocket_launches[rocket_name] += 1
        else:
            rocket_launches[rocket_name] = 1

    # sortign by number of launches descending, then alphabetically
    sorted_rockets = sorted(rocket_launches.items(), key=lambda x: (-x[1], x[0]))

    for rocket in sorted_rockets:
        print(f"{rocket[0]}: {rocket[1]}")

if __name__ == '__main__':
    get_launches_by_rocket()