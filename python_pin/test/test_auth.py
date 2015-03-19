from unittest import TestCase, main as unittest_main
from urlparse import urljoin

from python_pin.base import base_uri, pin_key
from python_pin.auth import HTTPKeyAuth

import requests


class TestAuth(TestCase):
    def test_auth(self):
        self.assertEqual(
            requests.get(urljoin(base_uri, 'charges'), auth=HTTPKeyAuth(pin_key)).json(),
            {u'count': 0, u'response': [],
             u'pagination': {u'count': 0, u'next': 2, u'current': 1, u'per_page': 25,
                             u'pages': 0, u'previous': None}}
        )


if __name__ == '__main__':
    unittest_main()
