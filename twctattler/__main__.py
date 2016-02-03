from datetime import datetime
from time import sleep
from twctattler.pinger import twctattler
import sys

def app():
    tattler = twctattler('8.8.8.8')
    tattler.ping_and_log()
def stats():
    print "STATS!"

if __name__ ==  '__main__':
    if sys.argv[1] == 'stats':
        stats()
    else:
        app()
