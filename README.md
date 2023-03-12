# Flask based Stripe Payments Website
Simple Stripe payment accepting implementation that can be used for other projects very easily. Built with Flask, Stripe API, and UWSGI


## Starting off

### Port Forwarding (self-hosting only)
Port forwarding is required to ensure your server is visible online to everyone

#### Find your server's local ip
On Raspberry Pi, you can find this by typing `ip address` in your terminal. No matter the method, it should look like `192.168.*.*`


#### Forward your website
Go to your router configuration website. Refer to your router manual or online for how to do so. You should also be able to figure out where the port forwarding menu is, and add your local ip there. If you plan on using USWGI, your input port will be 5000. Use output port 80 for HTTP, and 443 for HTTPS. Set protocol to TCP if it's not that already. 

### Getting a domain
I highly recommend you get a domain, and preferably use Cloudflare DNS, to ensure your home IP isn't exposed when you self-host. You can get one at [Freenom](https://freenom.com) for free!

There are many tutorials on how to configure this with Cloudflare, so shouldn't be too difficult!

### Getting an SSL certificate 
Not required but highly recommended if you want to use Https properly. First, get an SSL certificate and key. You can find many services to get one. Save these in your project directory. I saved mine as `server.crt` and `server.key`.


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
