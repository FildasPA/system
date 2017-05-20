import ConfigParser
import os.path


SECTION = 'Crisis'
CONFIG_FILE = 'local/sys.conf'


def write_config_file(filename, config):
    config.add_section(SECTION)
    config.set(SECTION, "no_response", "30")
    config.set(SECTION, "cpu", "90")
    config.set(SECTION, "ram", "100")
    config.set(SECTION, "disk", "95")
    config.write(open(filename, 'w'))


def read_config():
    """Read config file, or write one if there is none"""
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(CONFIG_FILE):
        write_config_file(CONFIG_FILE, config)
    config.read(CONFIG_FILE)
    if SECTION not in config.sections():
        write_config_file(CONFIG_FILE, config)
    return config


def check_crisis(info):
    """ description """
    config = read_config()
    crisis = {}
    for option in config.items(SECTION):
        if option[0] not in info:
            continue
        # print "{} : {}".format(option[0], option[1])
        if float(info[option[0]]) >= float(option[1]):
            crisis[option[0]] = info[option[0]]
        # value = info[option[0]]
    if crisis:
        print crisis
    else:
        print "no crisis"


def check_response():

if __name__ == "__main__":
    app.run()
