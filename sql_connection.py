import pyodbc
__cnx = None
def get_sql_connection():
    conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=SANJAY-DSK\MSSQLSERVER01;'
        r'DATABASE=grocerystore;'
        r'Trusted_Connection=yes;'
    )
    global __cnx
    if __cnx is None:
        __cnx = pyodbc.connect(conn_str)
    return __cnx