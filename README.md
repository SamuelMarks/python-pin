python-pin
==========

## Setup

Environment variable needs to be setup:

    PIN_TEST_SECRET_KEY
    PIN_SECRET_KEY
    PIN_TIER

`PIN_TIER` is set to `test` or `prod`.

## Dependency resolution

    pip install -r requirements.txt

## Test suite

I use [setuptools](https://pythonhosted.org/setuptools) and [unittest](https://docs.python.org/2/library/unittest.html):

    python setup.py test

## Example usage

    from python_pin.request_wrapper import req as pin_api

    
    pin_api('charges')  # GET is default method
    pin_api(method='POST', path='charges', data={'amount': 400,'currency': 'USD',
                                                 'description': 'test charge',
                                                 'email': 'roland@pin.net.au',
                                                 'ip_address': '203.192.1.172',
                                                 'card': {'number': 5520000000000000,
                                                          'expiry_month': '05',
                                                          'expiry_year': 2016,
                                                          'cvc': 123,
                                                          'name': 'Roland Robot',
                                                          'address_line1': '42 Sevenoaks St',
                                                          'address_line2': '',
                                                          'address_city': 'Lathlain',
                                                          'address_postcode': 6454,
                                                          'address_state': 'WA',
                                                          'address_country': 'AU'}
                                                 })

## Roadmap

Currently this API just exposes a simple wrapper over [python-requests](http://docs.python-requests.org).

If I get the chance, will: code-generate classes for a cleaner, more expressive, documented and code-completable interface.

## Known bugs

POST method on charges fails even when given exact same data payload as [example `curl` command](https://pin.net.au/docs/api/charges#post-charges).
