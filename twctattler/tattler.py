import os
import ping
from datetime import datetime
import sqlite3 as sqlite

class twctattler:
    def __init__(self, target):
        self.target = target
        self.db_setup()

    def db_setup(self):
        self.con = sqlite.connect(os.path.join(os.path.expanduser('~'),'tattler_results.db'))
        self.cur = self.con.cursor()
        with self.con:
            self.cur.execute("CREATE TABLE IF NOT EXISTS Tattler_Results(target TEXT, Date TEXT, Result INT, Response_time INT)")

    def ping_and_log(self):
        result = ping.quiet_ping(self.target)
        with self.con:
            query="INSERT INTO Tattler_Results VALUES('{0}','{1}', {2}, {3})".format(self.target, str(datetime.utcnow()), int(not result[0]), int(result[2]))
            self.cur.execute(query)
