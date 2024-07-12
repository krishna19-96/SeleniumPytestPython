from configparser import ConfigParser


def get_config(section, key):
    config = ConfigParser()
    config.read('../ConfigurationData/config.ini')
    return config.get(section, key)


browser = get_config("basic info","browser")
print(browser)