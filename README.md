# Telescope Schedule Optimizer (TSO)

<p align="center">
<img align="center" src="https://github.com/elijah-ward/TSO/blob/master/resources/images/TSO.png" alt="TSO"/>
</p>

TSO is a scheduling tool written in Python for use by astronomical researchers in order to consider a wide variety of constraints and attempt to produce an optimal observation schedule.

[Github Repository](https://github.com/elijah-ward/TSO)

## Getting Started

### Installation
The main entrypoint into TSO is through the `tsocli` sub-module.
The details can be found in the [README of the submodule.](./src/tso/tsocli/README.md)

To install the cli tool just execute the following
1. `pip install -e .` (install the project)
2. `tsocli -h` start learning/using the entrypoint

## Using the TSO CLI

The TSO Commandline Interface largely operates as a pipe-and-filter system where the goal is to take in ObservingBlocks and Configuration as input and produce the desired output of a schedule that meets all of the supplied constraints.

During this process the following steps occur:

1) Input is **imported** from the database in the form of ObservingBlocks based on **filters** that are provided from the commandline arguments provided by the user.
2) ObservingBlocks are **transformed** into an internal model that makes the data more easily consumable by the scheduling modules.
3) A Scheduler object is instantiated based on the runtime configuration provided by the user (the default is `tso_config.json` in your current directory, but an alternate path may be supplied)
4) Global constraints are initialized based upon the configuration under `global_constraints` in the configuration file. These are applied to every block in this scheduling run.
5) Output is exported to various formats based on the arguments supplied by the user. Some options include to export to CSV or a table in your browser.

A basic command would look something like this:
```bash
tsocli schedule --max-observation-priority 300  --start-date-time "2019-03-01 19:00" --end-date-time "2019-03-30 19:00" --export-to-file --export-to-browser
```

This command would:

1) Import ObservingBlocks from the CFHT data model that have a maximum priority of 300 (assuming that a lower priority value indicates a higher priority i.e. 1st, 2nd, 3rd priority)
2) Schedule the blocks to times after `2019-03-01 19:00` and before `2019-03-30 19:00`
3) Export the output table to CSV and to the user's browser

For further examples, see the following details about configuration and commandline arguments.

### Configuration

During the execution of the TSO CLI, a well-formed configuration file is necessary. An example is included in this repo as `tso_config.json`. The user can optionally supply a path to their own config file, relative to their current working directory using the `--config-file <PATH TO FILE>` CLI argument. A configuration file is required and if one is not supplied, the system defaults to `tso_config.json` in the current working directory.

In the current state, the necessary configuration file looks like this:

```
{
    "telescope": {
        "slew_rate": 0.8,
        "read_out": 20,
        "filters": {
            "transitions": {
                "default": 30,
                "filter": [
                    {
                        "from": "B",
                        "to": "G",
                        "duration": 10
                    },
                    {
                        "from": "B",
                        "to": "R",
                        "duration": 10
                    },
                    {
                        "from": "G",
                        "to": "B",
                        "duration": 10
                    },
                    {
                        "from": "R",
                        "to": "B",
                        "duration": 10
                    }
                ]
            }
        }
    },
    "db": {
            "HOST": "127.0.0.1",
            "PORT": "3306",
            "DB": "tso",
            "USER": "tsouser",
            "PASSWORD": "password"
    },
    "global_constraints": {
        "AirmassConstraint": {
            "max": 3,
            "boolean_constraint": "False"
        },
        "AtNightConstraint.twilight_civil": null
    }
}
```

#### telescope

This section contains the values for certain configurations that are specific to your telescope.

`slew_rate`: Also known as dithering, this is the rate that your telescope moves between targets. (degrees/second)
`filter`: This object specifies the transitions between the filters of your telescope. If a block requests the use of a filter that causes a transition that does not exist here, the default time will be assumed.

#### db

This section contains the connection information for the database to be used to source observing blocks.

`HOST`: The servername that your database is running on.
`PORT`: The port that your database is exposed on.
`DB`: The name of the database to be used.
`USER`: The username of the account with sufficient **read** access to import data.
`PASSWORD`: The password of the account with sufficient **read** access to import data.

#### global_constraints

This section of the configuration allows users to enable and disable the global constraints they wish to be applied for scheduling runs. This object is parsed dynamically within the system as follows; Membership of a given `Constraint` as a key within the object enables the constraint to be used in the scheduling run. Removing it and its child objects causes the constraint to be disabled. Within the child object of each `Constraint` key, there are a set of key-value pairs. These are to set the parameters during the instantiation of that particular constraint.

The currently supported constraints are `AirmassConstraint`, `AtNightConstraint` and a custom `WeatherConstraint`. As the system evolves, more global constraints will be supported over time.

#### Commandline Arguments

```
"--config-file",
default="tso_config.json",
help="The local path to your runtime config file (See the included tso_config.json for an example of format)"
```
```
"--start-date-time",
default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
help="The date time to begin the scheduling. Must be UTC. format - YYYY-MM-DD HH:mm"
```
```
"--end-date-time",
default=(datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M"),
help="The date time to end the scheduling. Must be UTC. format - YYYY-MM-DD HH:mm"
```
```
"--max-program-priority",
default=MAX_SIZE,
help="The maximum program priority to query against (1 is highest priority)"
```
```
"--max-observation-priority",
default=MAX_SIZE,
help="The maximum block priority to query against (1 is highest priority)"
```
```
"--max-remaining-observing-chances",
default=MAX_SIZE,
help="Include only those blocks whose remaining observing chances is less than this value"
```
```
"--observation-duration-min",
default=0,
help="Include only those blocks whose duration is greater than or equal to this"
```
```
"--observation-duration-max",
default=MAX_SIZE,
help="Include only those blocks whose duration is less than or equal to this"
```
```
"--no-weather-constraints",
help="Whether weather should be imported for this schedule",
action="store_true"
```
```
"--export-to-file",
help="Whether to export to a file or not",
action='store_true'
```
```
"--export-to-browser",
help="Display schedule in browser",
action='store_true'
```

## Future Work

The following features do not exist within the current iteration of the TSO CLI but should be considered high priority for future development:

- Block-level constraints (constraints that uniquely apply to a single ObservingBlock)
- Creation of additional custom constraints to satisfy all constraint requirements existing within the CFHT/MSE data model
- Conversion to consume GRPC messages using protobuf instead importing input data from DB
- Hands-on integration with CFHT/MSE to synchronize the data model
- Leverage Astropy to export the output schedule table to a wider variety of formats (perhaps one that can be directly consumed by the telescope)

## Developer Documentation

### Useful Tools

- `conda` - https://conda.io/miniconda.html (useful in managing multiple python environments)
- `docker` - https://docs.docker.com/install (useful for running interfacing services or databases in a lightweight fashion)
- `docker-compose` - https://docs.docker.com/compose/install (useful for organizing docker containers with a more efficient workflow)

### Conda

In this repository there is an `environment.yml` file that contains information about the dependencies required by this project. It also specifies `tso` as the name of the environment.

#### Creating a New Environment in Conda From an `environment.yml` File

```
conda env create -f environment.yml
```

#### Switching Environments Created Using Conda

**MacOS/Linux**
```
source activate tso
```
**Windows**
```
activate tso
```

### Docker

If you'd like to work against a lightweight instance of the database or do some rapid iteration on test data sets, Docker can be of use to you while working on this project.
<br>
Docker can be installed [here](https://docs.docker.com/install) and docker-compose can be installed [here](https://docs.docker.com/compose/install).

#### Standing up a local MySQL database using Docker

From the root of the project execute the following:
```
docker-compose up --build -d
```
This executes docker-compose which will read the `docker-compose.yml` file and stand up docker containers with the images defined there. The `--build` flag tells it to always build a new image (in case of changes). `-d` tells it to run in "detached" mode (or else it will take over your prompt to display the container logs).

#### Applying Database Migrations

From the root of the project:
1. `cd db`
2. `./maintain_db migrate`

This will run a container with a tool called [Flyway](https://flywaydb.org/) within. It will run the scripts within the `db/migrations` directory (likely just the schema). It will also run any scripts in the `db/sample-data` where we will house scripts that insert test data.

#### Generate test data

There are two ways for generating test TSO data.
_A python script supports these methods._

**[generate_test_data.py](./db/generate_test_data.py)**
Methodology
from root of project
1. Using `generate_test_data.py sql n` -- Connecting directly to DB through python and executing statements
2. Using `generate_test_data.py file n` -- Outputting a file locally to be used with flyway/Docker....other methods.

In both of the above, n is an integer to dictate the number of observation blocks created.

#### Cleaning the database

Sometimes it can be useful to start from a fresh database (most useful to pick up changes you have made to test data, for example). Since we are not working with a production database, we need not worry about wiping our local database clean and starting over.

From the root of the project:
1. `cd db`
2. `./maintain_db clean`


You can now apply migrations again against a clean database.

## Maintainers

- [Sebastian Lopez](https://github.com/se95lopez)
- [Gustavo Andres Murcia](https://github.com/GAUNSD)
- [Kirk Vander Ploeg](https://github.com/Kirk-V)
- [Elijah Ward](https://github.com/elijah-ward)

## Credits

<div>Icons made by <a href="https://www.flaticon.com/authors/eleonor-wang" title="Eleonor Wang">Eleonor Wang</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
