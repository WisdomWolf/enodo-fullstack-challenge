# Run Challenge Server
From a terminal execute `run_enodo_example_server.sh`.  It should create the necessary docker containers and open a web browser pointed at the site.

### Run Tests
From a terminal CD to project root and execute `PYTHONPATH=src pytest`

### Troubleshooting
- [docker-compose](https://docs.docker.com/compose/install/) needs to be installed  
- If for some reason it doesn't open a brower you can access the site (once both api and ui docker containers are running) at http://localhost:8080
- Running tests requires dev dependencies to be installed.  Run the following in a virtual environment to install the necessary packages:
```shell
pip install -U pip
pip install pipenv
pipenv install --dev
```