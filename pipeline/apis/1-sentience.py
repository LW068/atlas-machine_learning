#!/usr/bin/env python3
"""...sentience..."""
import requests


def sentientPlanets():
    """returns the list of home planets of all sentient species"""
    planets = []
    next_page = 'https://swapi.dev/api/species/'

    while next_page is not None:
        response = requests.get(next_page)
        if response.status_code == 200:
            result = response.json()
            for species in result['results']:
                # checking if species is sentient
                if species['classification'] in \
                        ('sentient', 'reptilian', 'mammal') or \
                        species['designation'] in \
                        ('sentient', 'reptilian', 'mammal'):

                    planet_url = species['homeworld']
                    if planet_url:
                        planet_response = requests.get(planet_url)
                        if planet_response.status_code == 200:
                            planet_name = planet_response.json()['name']
                            planets.append(planet_name)
            next_page = result['next']
        else:
            # If the API call was not successful then we break the loop
            break

    return planets
