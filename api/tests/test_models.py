import subprocess

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.real_estate import RealEstateProperty
from utils.directory_resolvers import get_db_uri, get_project_path

import logging

logger = logging.getLogger()

@pytest.fixture
def setup_database():
    try:
        project_path = get_project_path()
        script_path = project_path.joinpath('api/initialize-database.sh')
        result = subprocess.run(['bash', f'{script_path}'])
        assert result.returncode == 0
    except Exception:  # We want to halt if anything goes wrong at this step
        logger.exception('oh noes!')
        pytest.exit('Exiting because database init failed')


@pytest.fixture
def session_creator():
    db_uri = get_db_uri('real_estate.db')
    engine = create_engine(db_uri)
    return sessionmaker(engine)


@pytest.fixture
def model_data(sample_data):
    return sample_data['models']


@pytest.mark.usefixtures('setup_database')
def test_one_model(session_creator, model_data):
    with session_creator() as session:
        estate_one = session.query(
            RealEstateProperty
        ).filter(
            RealEstateProperty.property_id == 1
        ).one_or_none()

        assert estate_one.serialize() == model_data['estate_one']
