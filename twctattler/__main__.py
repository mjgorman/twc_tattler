from datetime import datetime
from time import sleep
from twctattler.tattler import twctattler
import sys

def app():
    tattler = twctattler('8.8.8.8')
    tattler.ping_and_log()
def stats():
    tattler = twctattler('8.8.8.8')
    tattler.send_stats()

if __name__ ==  '__main__':
    if sys.argv[1] == 'stats':
        stats()
    else:
        app()
