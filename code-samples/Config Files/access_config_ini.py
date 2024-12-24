"""
Code chunk demonstrating how to acces standalone config file
"""
import configparser
import os

class ConfigSingleton(type):
    """
    Singleton class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ConfigSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Configuration(metaclass=ConfigSingleton):
    """
    Configuration class
    """
    def __init__(self):
        config = configparser.ConfigParser()
        dir_name = os.path.dirname(__file__)
        config.read_file(open(os.path.join(dir_name, "config.ini"), "r"))
        self.settings = config._sections
        # Add new config variable for use in other files
        self.settings["section1"]["config33"] = "some value"


config_settings = Configuration().settings

print(f"Section 1 Config 1 value: {config_settings['section1']['config1']}")
print(f"Section 2 Config 1 value: {config_settings['section2']['config1']}")

# The config setting can be imported in other files using
# from config.configurations import config_settings
# and then the relevant config values accessed from it
