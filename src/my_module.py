import json

def get_database_from_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config['database']