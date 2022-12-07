
import json
import os
from typing import Union


DEFAULT_CACHE_DIR = '~/.cache'


def get_config_dir() -> str:
    return os.path.join(
        os.path.expanduser(os.path.join(DEFAULT_CACHE_DIR, 'lnrun')), 'config.json'
    )


def load_config() -> dict:
    config_path = get_config_dir()
    data = None
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            data = None
    if data is None:
        data = {}
    return data


def write_config(data: dict) -> None:
    config_path = get_config_dir()

    if not os.path.exists(os.path.dirname(config_path)):
        os.makedirs(os.path.dirname(config_path))

    json_object = json.dumps(data, indent=4)
    with open(config_path, 'w') as outfile:
        outfile.write(json_object)


def get_token() -> Union[str, None]:
    config = load_config()
    if 'line_token' in config:
        return config['line_token']
    return None


def is_token_setted() -> bool:
    return 'line_token' in load_config()


trues = ['1', 'true', 'yes', 'on']


def get_config(key: str) -> bool:
    config = load_config()
    if key in config:
        value: str = config[key]
        if len(value) > 0:
            value = value.lower()
            return value in trues
    return False


def get_config_value(key: str) -> str:
    config = load_config()
    if key in config:
        return config[key]
    return None
