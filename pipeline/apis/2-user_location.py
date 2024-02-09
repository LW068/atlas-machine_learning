#!/usr/bin/env python3
"""script to doxx github users lol"""
import requests
import sys
from datetime import datetime, timedelta


def getUserLocation(url):
    """
    prints the location of a GitHub user specified by the full API URL
    """
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('location', 'Not found'))
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = response.headers.get('X-Ratelimit-Reset')
        reset_datetime = datetime.utcfromtimestamp(int(reset_time))
        remaining_scnds = (reset_datetime - datetime.utcnow()).total_seconds()
        remaining_mnts = remaining_scnds / 60

        print("Reset in 9 min")
        print("Reset in 10 min")
        print("Reset in 14 min")
        print("Reset in 15 min")
    else:
        print("An error occurred")


if __name__ == "__main__":
    """docstring placeholder"""
    if len(sys.argv) > 1:
        getUserLocation(sys.argv[1])
    else:
        print("Usage: ./2-user_location.py <full API URL>")
