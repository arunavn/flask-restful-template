import os
import json


class ApplicationConfig:
    def __init__(self, config_path: str) -> None:
        self.environment: str = os.environ.get('ENVIRONMENT', '')  # get env from the environment variable, else set to dev
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        self.global_config: dict = config_data['global']
        self.env_config: dict = config_data[self.environment]
        
    def get_app_name(self) -> str:
        return self.global_config['app_name']

    def get_school_name(self) -> str:
        return self.env_config.get('school_name')
