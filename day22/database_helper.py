import psycopg2


class UseDatabase:
    def __init__(self, config):
        self.configuration = config
    

    def __enter__(self):
        self.conn = psycopg2.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
        
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()