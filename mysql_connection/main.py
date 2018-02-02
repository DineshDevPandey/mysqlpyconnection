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

    def connect_existing_db(self):
        '''
        Get Connection
        '''
        db_conn = DbOperations()
        db_conn.db_connect(self.host, self.db_name)
        '''
        Show all databases
        '''
        db_conn.show_db()
        '''
        Show all tables in db
        '''
        db_conn.show_tables()
        '''
        Display data of table
        '''
        db_conn.show_data("vc_info")
        '''
        Close Connection
        '''
        db_conn.close_connection()


if __name__ == "__main__":
    '''
    Param1 : host name/IP
    Param2 : DB name
    '''
    db = MysqlDb("localhost", "rc_admin_test")
    '''
    Existing DB operations
    '''
    db.connect_existing_db()

