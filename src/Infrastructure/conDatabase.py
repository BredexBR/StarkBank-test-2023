import psycopg2

class conDatabase:
    def conDatabase():
        try:
            conn = psycopg2.connect(
            database="database",
            host="host",       
            user="usuario",
            password="senha",
            port="porta"
            )
            return conn
        
        except psycopg2.Error as e:
            print(f"An error occurred while trying to connect to the database: {e}")
            return "erro"
    
    def closeDatabase(conn):
        conn.close()