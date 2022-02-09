from os import getenv
from pathlib import Path


def get_project_path():
    return Path(__file__).parents[3]


def get_db_uri(filename):
    """
    Resolves database uri either from env variable or based on directory walk
    :param filename: The filename for sqlite database ie `real_estate.db`
    :type filename: str
    :return:
    """
    if path := getenv('DATA_PATH'):
        data_path = Path(path)
    else:
        project_path = get_project_path()
        data_path = project_path.joinpath('api/data')
    db_path = data_path.joinpath(filename)
    uri = f'sqlite:///{db_path}'
    return uri


def get_file_path(filename):
    project_path = get_project_path()
    file_path = project_path.joinpath('source_data').joinpath(filename)
    return file_path
