import os
from src.my_module import get_database_from_config

def test_database_config():
    config_path = os.path.join(os.path.dirname(__file__), "test_config.json")
    db = get_database_from_config(config_path)
    print("CONFIG_USERNAME:", os.environ.get("CONFIG_USERNAME"))
    print("CONFIG_PASSWORD:", os.environ.get("CONFIG_PASSWORD"))
    print("DATABASE from config:", db)
    try:
        assert db == "misight_v15_dev"
        print("Assertion passed: database is misight_v15_dev")
    except AssertionError:
        print("Assertion failed: database is", db)
        raise