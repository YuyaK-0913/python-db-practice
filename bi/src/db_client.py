import os
from abc import ABC, abstractmethod

import mysql.connector
from logger import configure_logger

logger = configure_logger(__name__)


class AbstractDBClient(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_connection(self):
        raise NotImplementedError


class MySQLClient(AbstractDBClient):
    def __init__(self):
        self.__mysql_user = os.getenv("MYSQL_USER")
        self.__mysql_password = os.getenv("MYSQL_PASSWORD")
        self.__mysql_port = int(os.getenv("MYSQL_PORT", 3306))
        self.__mysql_dbname = os.getenv("MYSQL_DATABASE")
        self.__mysql_host = os.getenv("MYSQL_HOST")
        self.__connection_string = {
            'host': self.__mysql_host,
            'port': self.__mysql_port,
            'database': self.__mysql_dbname,
            'user': self.__mysql_user,
            'password': self.__mysql_password
        }

    def get_connection(self):
        return mysql.connector.connect(**self.__connection_string)
    

# debug
if __name__ == "__main__":
    client = MySQLClient()
    try:
        conn = client.get_connection()
        if conn.is_connected():
            logger.info("Connection to MySQL verified.")
            conn.close()
            print("Connection to MySQL verified.")
    except Exception as e:
        logger.error("Failed to connect to MySQL.", exc_info=e)