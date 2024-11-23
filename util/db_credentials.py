###########################################################################################
#
# Author: Wenjie Tehan
#
# Date: Nov 3, 2024
#
#
#
###########################################################################################

import getpass
import os
from configparser import ConfigParser
from util.dbconfig import write_db_credentials
from util.dbconfig import read_db_credentials
from util.helper import get_dbconfig_file_path


def get_credentials():

    filepath = get_dbconfig_file_path()
    print("Credentials filepath: ", filepath)

    if os.path.exists(filepath):
        db_type, host_name, db_name, user_name, password, port, logmech = read_db_credentials(
            filepath)
    else:
        db_type = input(
            "Enter the database type (db2/mssql/mysql/oracle/postgresql/teradatasql): ").lower()
        db_name = input("Enter the database or schema name: ")
        host_name = input("Enter the host name: ")
        port = input("Enter the port number: ")
        user_name = input("Enter the user name: ")
        logmech = input("Enter Login Mechansim: ")
        password = getpass.getpass("Enter the password: ")

        write_db_credentials(filepath, db_type, host_name,
                             db_name, user_name, password, port, logmech)

    return db_type, db_name, host_name, port, user_name, password, logmech
