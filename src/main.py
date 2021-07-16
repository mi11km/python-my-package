#!/usr/bin/env python
import os
import mysql.connector as db


def main():
    mysql_connection_config = {
        'host': os.getenv('MYSQL_HOST', 'db'),
        'port': os.getenv('MYSQL_PORT', '3306'),
        'user': os.getenv('MYSQL_USER', 'worker'),
        'password': os.getenv('MYSQL_PASSWORD', 'dummy'),
        'database': os.getenv('MYSQL_DATABASE', 'python'),
    }

    conn = db.connect(**mysql_connection_config)
    conn.ping(reconnect=True)

    print(conn.is_connected())

    conn.close()


if __name__ == '__main__':
    main()
