import pytest
from datetime import datetime
import json
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")

@pytest.fixture
def load_test_data():
  json_file_path=os.path.join(os.path.dirname(__file__),"data","test_data.json")
  with open(json_file_path) as json_file:
      data=json.load(json_file)
      return data