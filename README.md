# Flask based Stripe Payments Website
Simple Stripe payment accepting implementation that can be used for other projects very easily. Built with Flask, Stripe API, and UWSGI


## Starting off

### Getting a domain
I highly recommend you get a domain, and preferably use Cloudflare DNS, to ensure your home IP isn't exposed. You can get one at [Freenom](https://freenom.com) for free!

There are many tutorials on how to configure this with Cloudflare, so shouldn't be too difficult!


## How to start a server

### Install Python 3.9 or newer, may not work on older versions

### `cd` to project directory

### Create and enter a virtual environment:
    python3 -m venv .
    . venv/bin/activate
    
    
### Install Dependencies:
    pip install flask
    pip install stripe
    pip install uwsgi
    pip install python-dotenv
