import MySQLdb


class DbOperations:
    """
    contains all db operations
    """
    user = "root"
    password = "root123"
    db_conn = ''

    def db_connect(self, host, db_name):
        try:
            DbOperations.db_conn = MySQLdb.connect(host, DbOperations.user, DbOperations.password, db_name)
            print("\nConnected to DB :\n")
        except MySQLdb.Error:
            print("Db connection error :" % MySQLdb.Error)

    def show_db(self):
        cur = DbOperations.db_conn.cursor()
        cur.execute("show databases")
        print("\nDatabases : \n")
        for row in cur.fetchall():
            print(row[0])



    def show_tables(self):
        cur = DbOperations.db_conn.cursor()
        cur.execute("show tables")
        print("\nTables :\n")
        for row in cur.fetchall():
            print(row[0])

    def close_connection(self):
        DbOperations.db_conn.close()
        print("\nConnection cloased :\n")

    def show_data(self, table_name):
        cur = DbOperations.db_conn.cursor()
        select_query = "select * from " + table_name
        cur.execute(select_query)
        print("\nTable data :\n")
        for row in cur.fetchall():
            print(row)
