from os import environ

pin_key, base_uri = map(
    lambda e: (lambda tier: environ[tier], lambda tier: 'http://{tier}.pin.net.au/1/'.format(tier=tier, val=e[1][0])
               )[e[0]](tier=e[1][0]),
    enumerate(zip((lambda tier: {'prod': ('PIN_SECRET_KEY', 'api')
                                 }.get(tier, ('PIN_TEST_SECRET_KEY', 'test-api'))
                   )(environ['PIN_TIER'])))
)
