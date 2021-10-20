'''
This file collects fixtures that are potentially useful in several test modules
'''

# Generic stuff
import os
import pytest

# Cloud stuff
from google.cloud import storage

TEST_BUCKET_NAME = "gamaya_ds_test_data"

@pytest.fixture()
def environment():
    """ Get useful variables from the environment """
    pytest.dark_calibration_file_path = os.environ.get('DARK_CALIB_PATH', "/workspace/data/calib")

@pytest.fixture
def setup_test_gcp_bucket(scope="module"):
    """ Fixture to set up the test bucket acccess """
    storage_client = storage.Client()
    bucket = storage_client.bucket(TEST_BUCKET_NAME)
    yield bucket