import os
from src.my_module import get_database_from_config

def test_database_config():
    config_path = os.path.join(os.path.dirname(__file__), "test_config.json")
    db = get_database_from_config(config_path)
    assert db == "misight_v15_dev"