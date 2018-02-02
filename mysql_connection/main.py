from mysql_lib.mysql_operations import DbOperations


class MysqlDb:
    """
    Contains database related information
    """
    host = ''
    db_name = ''

    def __init__(self, host, db_name):
        self.host = host
        self.db_name = db_name

    def connect(self):
        db_conn = DbOperations()
        db_conn.db_connect(self.host, self.db_name)
        db_conn.show_db()
        db_conn.show_tables()
        db_conn.close_connection()


if __name__ == "__main__":
    db = MysqlDb("localhost", "rc_admin_test")
    db.connect()

