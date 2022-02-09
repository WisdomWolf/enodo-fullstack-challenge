from os import environ
from pathlib import Path
import subprocess

from openpyxl import load_workbook
import pytest
import yaml

from utils.directory_resolvers import get_db_uri, get_file_path, get_project_path
from utils.data_loader import resolve_headers


@pytest.fixture
def headers(sample_data):
    return sample_data['headers']


def test_get_project_path():
    module_path = Path(__file__)
    assert module_path.is_relative_to(get_project_path())


def test_get_db_uri():
    environ['DATA_PATH'] = '/data'
    assert get_db_uri('real_estate.db') == 'sqlite:////data/real_estate.db'


def test_resolve_headers(headers):
    excel_file_path = get_file_path('Enodo_Skills_Assessment_Data_File.xlsx')
    wb = load_workbook(excel_file_path)
    ws = wb.worksheets[0]
    assert resolve_headers(ws) == headers

