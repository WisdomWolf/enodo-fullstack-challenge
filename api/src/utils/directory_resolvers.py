from pathlib import Path


def get_project_path():
    return Path(__file__).parents[3]


def get_db_uri(filename):
    project_path = get_project_path()
    db_path = project_path.joinpath('api/data').joinpath(filename)
    uri = f'sqlite:///{db_path}'
    return uri


def get_file_path(filename):
    project_path = get_project_path()
    file_path = project_path.joinpath('source_data').joinpath(filename)
    return file_path
