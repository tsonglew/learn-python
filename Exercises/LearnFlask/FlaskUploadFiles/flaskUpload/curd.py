import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

con = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

with con as cur:
    cur.execute
