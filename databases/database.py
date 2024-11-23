###########################################################################################
#
# Author: Daniel Tehan, Wenjie Tehan
#
# Date: Nov 3, 2024
#
#
#
########################################################################################### 
from langchain_community.utilities import SQLDatabase

class Database():
        
    def __init__(self, db_type, host, database, user, password, port, logmech):
        self.db_type = db_type
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.logmech = logmech

    def get_database(self):
        # Format: dialect+driver://username:password@host:port/database

        # Set dialect and driver based on the database
        if self.db_type == "mysql":
            # db = SQLDatabase.from_uri('mysql+mysqlconnector://<user>:<password>@<host>:<port>/<db name>')
            connstr = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.db_type == "mssql":
            # db = SQLDatabase.from_uri('mssql+pyodbc://<user>:<password>@<host>:<port>/<db name>?TrustServerCertificate=yes&driver=ODBC+Driver+18+for+SQL+Server')
            driver = 'ODBC+Driver+18+for+SQL+Server'
            connstr = f"mssql+pyodbc://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?TrustServerCertificate=yes&driver={driver}"
        elif self.db_type == "postgresql":
            # db = SQLDatabase.from_uri('postgresql+psycopg2://<user>:<password>@<host>:<port>/<schema name>')
            connstr = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.db_type == "db2":
            # db = SQLDatabase.from_uri('db2+ibm_db://<user>:<password>@<host>:<port>/<db name>')
            connstr = f"db2+ibm_db://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.db_type == "oracle": 
            # db = SQLDatabase.from_uri('oracle+oracledb://<user>:<password>@<hostname>:<port>')
            # or db = SQLDatabase.from_uri('oracle+oracledb://<user>:<password>@<dsn>'))
            connstr = f"oracle+oracledb://{self.user}:{self.password}@{self.host}"     
        elif self.db_type == "teradatasql": 
            connstr = f"teradatasql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?logmech={self.logmech}"   

        db = SQLDatabase.from_uri(connstr)
        
        return db
