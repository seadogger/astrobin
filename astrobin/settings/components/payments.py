import os

SUPPORTED_CURRENCIES = ['USD', 'EUR', 'GBP', 'CAD', 'AUD', 'CHF', 'CNY']
TRANSFERWISE_API_TOKEN = os.environ.get('TRANSFERWISE_API_TOKEN')

if DEBUG or TESTING:
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_TEST_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_TEST_KEY')
    STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET_TEST')

    STRIPE_PRODUCT_LITE = os.environ.get('STRIPE_PRODUCT_LITE_TEST')
    STRIPE_PRODUCT_PREMIUM = os.environ.get('STRIPE_PRODUCT_PREMIUM_TEST')
    STRIPE_PRODUCT_ULTIMATE = os.environ.get('STRIPE_PRODUCT_ULTIMATE_TEST')
else:
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_LIVE_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_LIVE_KEY')
    STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET_LIVE')

    STRIPE_PRODUCT_LITE = os.environ.get('STRIPE_PRODUCT_LITE_LIVE')
    STRIPE_PRODUCT_PREMIUM = os.environ.get('STRIPE_PRODUCT_PREMIUM_LIVE')
    STRIPE_PRODUCT_ULTIMATE = os.environ.get('STRIPE_PRODUCT_ULTIMATE_LIVE')
