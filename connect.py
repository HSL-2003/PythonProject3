import psycopg2
from configparser import ConfigParser


def connect():

    conn = None
    try:

        params = {
            'host': 'localhost',
            'database': 'suppliers',
            'user': 'postgres',
            'password': 'Fptureset@2003'
        }


        print('Đang kết nối tới PostgreSQL database...')
        conn = psycopg2.connect(**params)


        cur = conn.cursor()


        print('PostgreSQL database version:')
        cur.execute('SELECT version()')


        db_version = cur.fetchone()
        print(db_version)


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Đã đóng kết nối database.')


if __name__ == '__main__':
    connect()