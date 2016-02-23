import os, json, ping, sendgrid
from datetime import datetime, timedelta
import sqlite3 as sqlite

class twctattler:
    def __init__(self, target):
        self.target = target
        self.db_setup()
        self.sendgrid_info = self.get_sendgrid_info()

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

    def get_sendgrid_info(self):
        with open(os.path.join(os.path.expanduser('~'),'.sendgrid')) as data_file:
            return json.load(data_file)

    def get_stats(self):
        query = 'SELECT * FROM Tattler_Results where date >= "{0}";'.format(str(datetime.utcnow()-timedelta(days=1)))
        self.cur.execute(query)
        return self.cur.fetchall()

    def calc_stats(self):
        stats = self.get_stats()
        failures = [date for tar,date,res,resp in stats if not bool(res)]
        success_rate = len([res for tar,date,res,resp in stats if bool(res)])
        output = ("Failures: {0}".format(failures),
                "Success: {0}% of {1} checks".format((float(success_rate)/float(len(stats)))*100,len(stats)))
        return output


    def send_stats(self):
        sg = sendgrid.SendGridClient(self.sendgrid_info['api-key'])
        message = sendgrid.Mail()
        message.set_from(self.sendgrid_info['email-from'])
        message.add_to(self.sendgrid_info['email-to'])
        message.set_subject('Tattler Stats')
        message.set_html("<html><body><p>Results from the last 24 hours</p><p>{0}</p><p>{1}</p></body></html>".format(*self.calc_stats()))
        status, msg = sg.send(message)
        print "Stats sent! {0}, {1}".format(status, msg)
