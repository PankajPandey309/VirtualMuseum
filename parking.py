import sqlite3
from PIL import Image
from numpy import array

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        
        return conn
    except Error as e:
        print(e)

if __name__=='__main__':
    create_connection(r"C:\\sqlite\db\parking.db")
    
