import argparse
import sys
import os
import yaml
from geocode.google import GoogleGeocoder

from db.postgresql_connector import PostgreSQLConnector
from db.query import get_voters_for_district


def load_config(filename):
    """loads the config yaml file"""
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    else:
        with open(os.path.realpath(filename)) as f:
            return yaml.load(f)


def join_non_none(list_to_join, sep=" "):
    return " ".join([x for x in list_to_join if x])


def write_geocodes_to_text(geocoder, voters_mailing_addresses):
    with open('viz/geocoded_addresses.csv', 'w') as f:
        f.write("address_id,address,lat,long\n")
        for voter in voters_mailing_addresses:
            address_string = join_non_none(voter[:4])
            apt_numbers = join_non_none(voter[4], ";")
            lat, long = geocoder.get_lat_long_for_address(address_string)
            if lat and long:
                f.write("{0},{1},{2},{3}\n".format(address_string, lat, long, voter[5], apt_numbers))
    f.close()


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print('This script requires version 3.x of python. Please try running it with command `python3` instead')
        exit(8)

    parser = argparse.ArgumentParser(
        description='Extract Voter Addresses From National Voter File, use to generate Walk Lists for canvassers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-d', '--district', dest='district',
                        help='House District Key', default=779)
    parser.add_argument('-c', '--config', dest='config', help='location of configuration file')

    args = vars(parser.parse_args())

    config = load_config(args.get('config'))
    engine_string = config['PG_ENGINE_STRING']
    if not engine_string:
        print('Please set config variable PG_ENGINE_STRING to valid PostgreSQL connection')
        exit(8)

    google_geocoder = GoogleGeocoder(config['GOOGLE_GEOCODE_API_KEY'])

    db_session = PostgreSQLConnector().connect(engine_string=engine_string)
    voters_mailing_address = get_voters_for_district(db_session, args.get('precinct'))

    write_geocodes_to_text(google_geocoder, voters_mailing_address)
