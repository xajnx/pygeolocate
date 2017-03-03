#!/usr/bin/env python3

import requests

base_url='https://maps.googleapis.com/maps/api/geocode/json?'

def geo2add(geo):
    my_coord = {'latlng': geo, 'sensor':'true'}

    response = requests.get(base_url, params = my_coord)
    results = response.json()['results']
    x_add = results[0]['formatted_address']

    print("Approximate address: ",x_add)

def add2geo(add):
    get_tag = {'address': add, 'language':'en'}

    response = requests.get(base_url, params = get_tag)
    results = response.json()['results']
    addy= results[0]['geometry']['location']

    print("Approximate geotag: ",addy['lat'],addy['lng'])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='''PyLocate: Address and geotag lookup script''')
    parser.add_argument("-g", "--geo", dest="geo", type=geo2add,
                        help="enter lat,lng to lookup. seperate fields with commas.")
    parser.add_argument("-a", "--addy", dest="add", type=add2geo,
                        help="enter address. seperate fields with commas.")


    args = parser.parse_args()
