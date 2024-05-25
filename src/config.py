"""
Loads the application configuration from a JSON file.
"""
import os
import json


class ApplicationConfig:
    """Applicatiom configuration
    """
    def __init__(self, config_path: str) -> None:
        self.environment: str = os.environ.get('ENVIRONMENT', '')
        # get env from the environment variable, else set to dev
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        self.global_config: dict = config_data['global']
        self.env_config: dict = config_data[self.environment]

    def get_app_name(self) -> str:
        """Returns the app name from global config
        Returns:
            str: app_name from config
        """
        return self.global_config['app_name']

    def get_school_name(self) -> str:
        """Return the school name from environment config
        Returns:
            str: school_name from config
        """
        return self.env_config.get('school_name')
