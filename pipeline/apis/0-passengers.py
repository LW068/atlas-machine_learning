#!/usr/bin/env python3
"""...passengers..."""

def availableShips(passengerCount):
    ships = []
    next_page = 'https://swapi.dev/api/starships/'
    
    while next_page is not None:
        response = requests.get(next_page)
        if response.status_code == 200:
            result = response.json()
            for ship in result['results']:
                passengers = ship['passengers'].replace(',', '').lower()
                # so wed need to handle cases where passengers is 'unknown'
                if passengers not in ('unknown', 'n/a') and passengers.isdigit():
                    if int(passengers) >= passengerCount:
                        ships.append(ship['name'])
            next_page = result['next']  # A URL for the next page, or None if no more pages
        else:
            # If the API call was not successful then we break the loop
            break
    
    return ships