import argparse
import sys
import os
import yaml

from db.postgresql_connector import PostgreSQLConnector
from db.query import get_voters_for_precinct


def load_config(filename):
    """loads the config yaml file"""
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    else:
        with open(os.path.realpath(filename)) as f:
            return yaml.load(f)


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

    db_session = PostgreSQLConnector().connect(engine_string=engine_string)
    voters = get_voters_for_precinct(db_session, args.get('precinct'))

