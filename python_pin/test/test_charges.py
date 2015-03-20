from unittest import TestCase, main as unittest_main
from urlparse import urljoin

from python_pin.base import base_uri, pin_key
from python_pin.auth import HTTPKeyAuth

import requests


class TestCharges(TestCase):
    maxDiff = 2880

    def test_post(self):
        request = {
            'amount': 400,
            'description': 'test charge',
            'email': 'roland@pin.net.au',
            'currency': 'AUD',
            'ip_address': '203.192.1.172',
            'card': {
                'number': 5520000000000000,
                'expiry_month': '05',
                'expiry_year': 2016,
                'cvc': 123,
                'name': 'Roland Robot',
                'address_line1': '42 Sevenoaks St',
                'address_city': 'Lathlain',
                'address_postcode': 6454,
                'address_state': 'WA',
                'address_country': 'AU'
            }
        }

        response = {
            "response": {
                "token": "ch_lfUYEBK14zotCTykezJkfg",
                "success": True,
                "amount": 400,
                "currency": "USD",
                "description": "test charge",
                "email": "roland@pin.net.au",
                "ip_address": "203.192.1.172",
                "created_at": "2012-06-20T03:10:49Z",
                "status_message": "Success",
                "error_message": None,
                "card": {
                    "token": "card_pIQJKMs93GsCc9vLSLevbw",
                    "scheme": "master",
                    "display_number": "XXXX-XXXX-XXXX-0000",
                    "expiry_month": 6,
                    "expiry_year": 2020,
                    "name": "Roland Robot",
                    "address_line1": "42 Sevenoaks St",
                    "address_line2": None,
                    "address_city": "Lathlain",
                    "address_postcode": "6454",
                    "address_state": "WA",
                    "address_country": "Australia",
                    "primary": None
                },
                "captured": True,
                "authorisation_expired": False,
                "transfer": [],
                "amount_refunded": 0,
                "total_fees": 42,
                "merchant_entitlement": 358,
                "refund_pending": False,
                "settlement_currency": "AUD"
            }
        }

        self.assertEqual(
            requests.post(url=urljoin(base_uri, 'charges'), data=request, auth=HTTPKeyAuth(pin_key)).json(),
            response
        )


if __name__ == '__main__':
    unittest_main()
