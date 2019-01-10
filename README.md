# Telescope Schedule Optimizer (TSO)
## Observe freely :)


<p align="center">
<img align="center" src="https://github.com/elijah-ward/TSO/blob/master/resources/images/TSO.png" alt="TSO"/>
</p>

TSO is a scheduling tool written in Python for use by astronomical researchers in order to consider a wide variety of constraints and attempt to produce an optimal observation schedule.

## Getting Started

## Useful Tools

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
