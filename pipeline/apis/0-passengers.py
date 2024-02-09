#!/usr/bin/env python3
"""...passengers..."""
import requests


def availableShips(passengerCount):
    """availableShips"""
    ships = []
    next_page = 'https://swapi.dev/api/starships/'

    while next_page is not None:
        response = requests.get(next_page)
        if response.status_code == 200:
            result = response.json()
            for ship in result['results']:
                psngrs = ship['passengers'].replace(',', '').lower()
                # Check if passenger count is a digit and greater or equal
                if psngrs not in ('unknown', 'n/a') and psngrs.isdigit():
                    if int(psngrs) >= passengerCount:
                        ships.append(ship['name'])
            next_page = result['next']
        else:
            # If the API call was not successful then we break the loop
            break

    return ships
