# twc_tattler 
[![Build Status](https://travis-ci.org/mjgorman/twc_tattler.svg?branch=master)](https://travis-ci.org/mjgorman/twc_tattler)

Monitor for keeping an eye on timewarner

# Setup
setup.py included for install and dependency management.
create a .sendgrid file in your user's homedir:
```
{
"api-key": "YOURAPIKEY",
"email-to": "to email",
"email-from": "from email"
}
```

# Usage
The two installed scripts idealy would be run via a daemon managemnt such as supervisord. Could also run via cron if you want it less frequently.

twc-tattler - Script will run and ping google dns and record the results in sqlite db

twc-tattler-stats - Script will run and generate stats, email them via sendgrid
