from packages.connect_to_db import ConnectToDatabase as cd

class FetchData:
    
    def __init__(self, conn, db_table : str) -> None:
        self.conn = conn
        self.db_table = db_table

    def _fetch_data(self):
        """ Check data availability in the DB """
        
        sample_db = 0
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM {self.db_table};")
            sample_db = cur.fetchall()
            conn.commit()
            print(f"Fetching Data from {str(self.db_table)}")
            return  sample_db
        
        except Exception as e:
            print(f"Error while fetching data: {str(e)}")
            conn.rollback()
            return 1
        
        cur.close()
        conn.close()

    def _show_results(self):
        """ Preview into the data from the DB """
        
        try:
            results = self._fetch_data()
            for record in results[:10]:     # Adjust results limit according to needs
                print(record)
                
        except Exception as e:
            print(f" Preview unavailable due to this error: {str(e)}")
            exit(1)