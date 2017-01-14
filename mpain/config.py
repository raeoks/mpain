import toml

CONFIG = {}


def load(config_path="config.yml"):
    with open(config_path) as config_file:
        global CONFIG
        CONFIG = toml.loads(config_file.read())
