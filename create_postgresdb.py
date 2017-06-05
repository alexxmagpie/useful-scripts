# -*- coding: utf-8 -*-

import psycopg2
import random
import string
import sys


db_name = raw_input("Enter new data base name: ")
username = raw_input("Enter username: ")
password = raw_input("Enter password (or left empty to generate random): ")

if password:
    confirm_password = raw_input("Confirm password: ")
    if password != confirm_password:
        sys.stdout('Passwords does not matches.')
        sys.exit()
else:
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))


conn = psycopg2.connect(dbname='postgres', user='postgres')
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE DATABASE %s;" % (db_name,))
cur.execute("CREATE USER %s WITH PASSWORD '%s';" % (username, password))
cur.execute("ALTER ROLE %s SET client_encoding TO 'utf8';" % (username,))
cur.execute("ALTER ROLE %s SET default_transaction_isolation TO 'read committed';" % (username,))
cur.execute("ALTER ROLE %s SET TIMEZONE TO 'UTC';" % (username,))
cur.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s;" % (db_name, username))

conn.close()

sys.stdout.write('Database %s created with %s password for %s user.\n' %
                 (db_name, password, username))

