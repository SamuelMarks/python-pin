from unittest import TestCase, main as unittest_main

from python_pin.request_wrapper import req


class TestAuth(TestCase):
    def test_auth(self):
        self.assertEqual(
            req('charges'),
            {'count': 0, 'response': [],
             'pagination': {'count': 0, 'next': 2, 'current': 1, 'per_page': 25,
                            'pages': 0, 'previous': None}}
        )


if __name__ == '__main__':
    unittest_main()
