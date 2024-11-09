###########################################################################################
#
# Author: Daniel Tehan
#
# Date: Nov 3, 2024
#
#
#
###########################################################################################

from configparser import ConfigParser


def read_db_credentials(filepath):
    config = ConfigParser()
    config.read(filepath)

    db_type = config.get('Server', 'DatabaseType')
    host = config.get('Server', 'Host')
    database = config.get('Server', 'Database')
    user = config.get('Server', 'User')
    password = config.get('Server', 'Password')
    port = config.get('Server', 'port')
    logmech = config.get('Server', 'logmech')

    return db_type, host, database, user, password, port, logmech


def write_db_credentials(filepath, db_type, host, database, user, password, port, logmech):
    config = ConfigParser()

    config['Server'] = {'DatabaseType': db_type, 'Host': host, 'Database': database,
                        'User': user, 'Password': password, 'Port': port, 'Logmech': logmech}

    with open(filepath, 'w') as configfile:
        config.write(configfile)
