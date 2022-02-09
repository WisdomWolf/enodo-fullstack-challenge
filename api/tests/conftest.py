from pathlib import Path

import pytest
import yaml


@pytest.fixture
def sample_data(shared_datadir):
    file_path = Path(shared_datadir).joinpath('sample_data.yaml')
    with open(file_path) as f:
        sample_data = yaml.safe_load(f)
    return sample_data
