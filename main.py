import os

import stripe
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

secret_key = os.environ['STRIPE_SECRET_KEY']

public_key = os.environ['STRIPE_PUBLIC_KEY']

app.config['STRIPE_PUBLIC_KEY'] = public_key
app.config['STRIPE_SECRET_KEY'] = secret_key
stripe.api_key = app.config['STRIPE_SECRET_KEY']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/order-sub', methods=['POST'])
def order_sub():
    currency = request.args.get('currency')
    if currency == 'usd':
        price = 'price_1JilnGFWGfLspjFTFhB6w1yh'

        payment = ['card']
    elif currency == 'eur':
        price = 'price_1JiowEFWGfLspjFTFcbfJLuO'
        payment = ['card']
    else:
        price = 'price_1JilnGFWGfLspjFTFhB6w1yh'
        payment = ['card']
    try:
        checkout_session = stripe.checkout.Session.create(

            line_items=[{  # TODO: replace this with the `price` of the product you want to sell
                'price': price, 'quantity': 1, }, ], payment_method_types=payment, mode='subscription',
            success_url=url_for('thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('choosemethod', _external=True) + '?url=order-sub', )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)


@app.route('/normal-edition', methods=['POST'])
def normal_edition():
    currency = request.args.get('currency')
    if currency == 'usd':
        price = 100
        payment = ['card']
    elif currency == 'eur':
        price = 86
        payment = ['card', 'ideal', 'sepa_debit']
    else:
        price = 100
        payment = ['card']
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price_data': {'currency': currency,  # 'product': 'prod_exampleid123',

                                        # delete the product_data index if using product id
                                        'product_data': {'name': '1 Time File',
                                                         "description": "preview of the true power you can get by paying for our subscription",
                                                         "images": [
                                                             "https://files.stripe.com/links/MDB8YWNjdF8xSmlsa0dGV0dmTHNwakZUfGZsX3Rlc3RfV3hBOUttaVhOTmxEb3dXdlVTclZ0VDJy00Nh9VuO3e"], },
                                        'unit_amount': price, }, 'quantity': 1, }], payment_method_types=payment,
            mode='payment',
            success_url=url_for('thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('choosemethod', _external=True) + '?url=normal-edition', )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)


@app.route('/choosemethod')
def choosemethod():
    url = request.args.get('url')
    return render_template('choosemethod.html', url=url)


context = ('server.crt', 'server.key')
if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context=context)
