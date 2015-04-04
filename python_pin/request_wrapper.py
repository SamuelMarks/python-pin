from urlparse import urljoin
from json import dumps as jsonify

from requests.api import request

from python_pin.base import base_uri, pin_key
from python_pin.auth import HTTPKeyAuth

req = lambda path, data=None, method='GET': \
    request(method=method,
            url=urljoin(base_uri, path),
            data=data,  # jsonify(data) if data else data,
            auth=HTTPKeyAuth(pin_key)).json()
req.__doc__ = """Request wrapper
    @path - e.g.: '/charges'
    @data - e.g.: "{'foo': 'bar'}"
    @method - e.g.: 'PUT'
"""
