#!/usr/bin/env python3
"""script for rocket launch frequency"""

import requests


def get_launches_by_rocket():
    """script for rocket launch frwuency"""
    launches_url = 'https://api.spacexdata.com/v4/launches'
    rockets_url = 'https://api.spacexdata.com/v4/rockets'
    launches_response = requests.get(launches_url)

    if launches_response.status_code != 200:
        print("Failed to retrieve launches data.")
        return

    rocket_id_to_name = {}
    rocket_launch_counts = {}

    for launch in launches_response.json():
        rocket_id = launch['rocket']
        if rocket_id not in rocket_id_to_name:
            rocket_response = requests.get(rockets_url + '/' + rocket_id)
            if rocket_response.status_code == 200:
                rocket_info = rocket_response.json()
                rocket_name = rocket_info['name']
                rocket_id_to_name[rocket_id] = rocket_name
                if rocket_name in rocket_launch_counts:
                    rocket_launch_counts[rocket_name] += 1
                else:
                    rocket_launch_counts[rocket_name] = 1
            else:
                print("Failed to retrieve rocket data for ID " + rocket_id)
        else:
            rocket_name = rocket_id_to_name[rocket_id]
            rocket_launch_counts[rocket_name] = \
                rocket_launch_counts.get(rocket_name, 0) + 1

    sorted_rockets = sorted(rocket_launch_counts.items(),
                            key=lambda x: (-x[1], x[0]))

    for rocket in sorted_rockets:
        print("{}: {}".format(rocket[0], rocket[1]))


if __name__ == '__main__':
    get_launches_by_rocket()
