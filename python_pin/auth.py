from base64 import b64encode

from requests.auth import AuthBase


class HTTPKeyAuth(AuthBase):
    """Attaches HTTP Basic Authentication (with one key) to the given Request object."""

    def __init__(self, key):
        self.key = key

    def __call__(self, r):
        r.headers['Authorization'] = 'Basic ' + b64encode(self.key).encode('latin1').strip().decode('latin1')
        return r
