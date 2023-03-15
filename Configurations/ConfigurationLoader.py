from Configurations.Configuration import Configuration


def open_json(path: str):
    with open(path, 'r') as file:
        return file.read()


def load_configuration(path: str) -> Configuration:
    config_json = open_json(path)

    return Configuration.from_json(config_json)


