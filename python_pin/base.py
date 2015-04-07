from os import environ

pin_key, base_uri = (lambda up_tier, down_tier: (
    environ['PIN_{up_tier}_SECRET_KEY'.format(up_tier=up_tier)],
    'https://{tier}.pin.net.au/1/'.format(
        tier={'test': '{down_tier}api'.format(down_tier='test-'), 'prod': 'api'}[down_tier])
))(*(lambda tier: (tier.upper(), tier.lower()))(environ['PIN_TIER']))
