# Flask based Stripe Payments Website
Simple Stripe payment accepting implementation that can be used for other projects very easily. Built with Flask, Stripe API, and UWSGI


### THIS README WAS DESIGNED FOR RASPBERRY PI SERVERS! INSTRUCTIONS WILL LIKELY BE DIFFERENT FOR OTHER HOSTING METHODS!


## Stripe Setup
First, you will need to [make a Stripe Account](https://dashboard.stripe.com/login). You will need the secret and publishable keys in the "For Developers" section of the dashboard later.

Now, one-time payments should already be ready for products in `main.py`.

If you want subscriptions to work, you need to create a product. This can be done by going to the "Products" page, pressing "Add Product", and entering the required details. For price, this project includes 2, one for USD, and one for EUR. Then, under pricing, you will see an API IDs for each price.

Edit `main.py`, replacing the prices with the API IDs you got before:

`main.py line 30`

``` py
@app.route('/order-sub', methods=['POST'])
def order_sub():
    currency = request.args.get('currency')
    if currency == 'usd':
        price = USD API ID STRING
     
        payment = ['card']
    elif currency == 'eur':
        price = EUR API ID STRING
        payment = ['card']
    else: 
        price = USD API ID STRING
        payment = ['card']
```


## Website and Server Setup

### Port Forwarding (self-hosting only)
Port forwarding is required to ensure your server is visible online to everyone

#### Find your server's local ip
On Raspberry Pi, you can find this by typing `ip address` in your terminal. No matter the method, it should look like `192.168.*.*`

#### Forward your website
Go to your router configuration website. Refer to your router manual or online for how to do so. You should also be able to figure out where the port forwarding menu is, and add your local ip there. If you plan on using USWGI, your input port will be 5000. Use output port 80 for HTTP, and 443 for HTTPS. Set protocol to TCP if it's not that already. 

### Getting a domain
I highly recommend you get a domain, and preferably use Cloudflare DNS, to ensure your home IP isn't exposed when you self-host. You can get one at [Freenom](https://freenom.com) or [eu.org](https:/eu.org) for free!

There are many tutorials on how to configure Freenom with Cloudflare, so shouldn't be too difficult!

If you are self hosting, then in the DNS settings, create an `A` tag with the root domain of your choosing, and your home IP.

### Getting an SSL certificate 
Not required but highly recommended if you want to use HTTPS properly. First, get an SSL certificate and key. You can find many services to get one. Save these in your project directory. I saved mine as `server.crt` and `server.key`.


## Starting Your Server

### Use Python 3.9 or newer
#### It probably will work on older versions, but I have not tested it.

### `cd` to your project's directory

### Create and enter a virtual environment:
    python3 -m venv .
    . venv/bin/activate


    
### Installing Dependencies

#### Install OpenSSL (for HTTPS Support)
I am unsure whether this is required on other OSes or if it is at all, but it solved a problem I had with HTTPS.
On Raspberry Pi:

    sudo apt-get install libssl-dev

#### Install with `pip`
```
pip install flask
pip install stripe
pip install uwsgi
pip install python-dotenv
```
    
### Creating environment variables
In your project directory, create a file named `.env` and copy the code block below into it. Now go back to your Stripe dashboard, and copy the keys under the "For Developers" section as shown here:

    STRIPE_PUBLIC_KEY=Stripe Publishable Key
    STRIPE_SECRET_KEY=Stripe Secret Key


### Run the script
    uwsgi --master --https 0.0.0.0:8000,server.crt,server.key  -p 4 -w hello:app
replace `server.crt` with your certificate path and `server.key` with your key path.

`hello:app` runs `hello.py`, which contains dotenv setup before running `main.py`, where flask code is stored

if you want to run on http, replace `--https 0.0.0.0:8000,server.crt,server.key` with `--http 0.0.0.0:8000`
