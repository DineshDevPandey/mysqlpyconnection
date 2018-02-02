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
            print("Connected to DB :\n\n")
        except MySQLdb.Error:
            print("Db connection error :" % MySQLdb.Error)

    def show_db(self):
        cur = DbOperations.db_conn.cursor()
        cur.execute("show databases")
        print("Databases : \n\n")
        for row in cur.fetchall():
            print(row[0])

        DbOperations.db_conn.close()
