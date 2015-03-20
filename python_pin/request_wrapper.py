from urlparse import urljoin

from requests.api import request

from python_pin.base import base_uri, pin_key
from python_pin.auth import HTTPKeyAuth

request_f = lambda path, data=None, method='GET': \
    request(method=method, url=urljoin(base_uri, path), data=data, auth=HTTPKeyAuth(pin_key)).json()
request_f.__doc__ = """Request wrapper
    @path - e.g.: '/charges'
    @data - e.g.: "{'foo': 'bar'}"
    @method - e.g.: 'PUT'
"""
