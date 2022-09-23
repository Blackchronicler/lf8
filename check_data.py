# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc
from io import StringIO
import pandas as pd
from connect_to_db import ConnectToDatabase
from load_db import conn, database_tables

def _sampling_db():
    """ Check data availability in the DB """
    
    sample_db= 0
    cur = conn.cursor()
    try:
        for table in database_tables:
            cur.execute(f"SELECT COUNT(*) FROM {table};")
        conn.commit()
        sample_db = cur.fetchall()
        return  sample_db
    
    except Exception as e:
        print(f"Error while fetching data: {str(e)}")
        conn.rollback()
    
    cur.close()