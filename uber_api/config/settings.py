import yaml
import os

def get_config():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'config.yaml'), 'r') as stream:
        try:
            uber_config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return uber_config
