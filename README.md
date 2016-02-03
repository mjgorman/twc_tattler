# twc_tattler
Monitor for keeping an eye on timewarner

# Setup
setup.py included for install and dependency management.

# Usage
The two installed scripts idealy would be run via a daemon managemnt such as supervisord. Could also run via cron if you want it less frequently.

twc-tattler - Script will run and ping google dns and record the results in sqlite db

twc-tattler-stats - Script will run and generate stats, email them via sendgrid (WIP)
