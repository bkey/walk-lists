import argparse
import sys
import os
import yaml
from geocode.google import GoogleGeocoder

from db.postgresql_connector import PostgreSQLConnector
from db.query import get_voters_for_precinct


def load_config(filename):
    """loads the config yaml file"""
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    else:
        with open(os.path.realpath(filename)) as f:
            return yaml.load(f)


def write_geocodes_to_text(geocoder, voters_mailing_addresses):
    with open('viz/geocoded_addresses.csv', 'w') as f:
        f.write("address_id,address,lat,long\n")
        for voter in voters_mailing_addresses:
            lat, long = geocoder.get_lat_long_for_address(voter)
            if lat and long:
                f.write("{0},{1},{2},{3}\n".format(voter.mailing_address_id, voter.to_address_string(), lat, long))
    f.close()


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print('This script requires version 3.x of python. Please try running it with command `python3` instead')
        exit(8)

    parser = argparse.ArgumentParser(
        description='Extract Voter Addresses From National Voter File, use to generate Walk Lists for canvassers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-p', '--precinct', dest='precinct',
                        help='The precinct number for which to get addresses', default=5487)
    parser.add_argument('-c', '--config', dest='config', help='location of configuration file')

    args = vars(parser.parse_args())

    config = load_config(args.get('config'))
    engine_string = config['PG_ENGINE_STRING']
    if not engine_string:
        print('Please set config variable PG_ENGINE_STRING to valid PostgreSQL connection')
        exit(8)

    google_geocoder = GoogleGeocoder(config['GOOGLE_GEOCODE_API_KEY'])

    db_session = PostgreSQLConnector().connect(engine_string=engine_string)
    voters_mailing_address = get_voters_for_precinct(db_session, args.get('precinct'))

    write_geocodes_to_text(google_geocoder, voters_mailing_address)
