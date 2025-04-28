# conftest.py

import pytest
from config.settings import Config

def pytest_configure(config):
    config._metadata['Environment'] = Config.BASE_URL
    config._metadata['Timeout (s)'] = Config.TIMEOUT

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Optional: Clean up some unwanted default metadata
    metadata.pop('Python', None)
    metadata.pop('Platform', None)
    metadata.pop('Packages', None)
    metadata.pop('Plugins', None)
