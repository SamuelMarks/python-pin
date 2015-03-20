from unittest import TestCase, main as unittest_main

from python_pin.request_wrapper import request_f


class TestAuth(TestCase):
    def test_auth(self):
        self.assertEqual(
            request_f('charges'),
            {u'count': 0, u'response': [],
             u'pagination': {u'count': 0, u'next': 2, u'current': 1, u'per_page': 25,
                             u'pages': 0, u'previous': None}}
        )


if __name__ == '__main__':
    unittest_main()
