## Walk List Generator

The goal of this project is to take data from the [National Voter File](https://github.com/national-voter-file/national-voter-file) and generate walk lists for canvassers

### Running

``python3 main.py --config <config file location> --precinct <precinct number>``

The config file should be a YAML file that contains the database connection string and Google API Key.

``
PG_ENGINE_STRING: "postgres://<User>:<Password>@<Host>:<Port>/<Database>"
GOOGLE_GEOCODE_API_KEY: <Key>
``