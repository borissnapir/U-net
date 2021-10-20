# Generic imports
import pytest
import os

# Local modules
from fixtures import environment

# test if environment variable exists
def test_environment_variables(environment):
    assert pytest.dark_calibration_file_path is not None

