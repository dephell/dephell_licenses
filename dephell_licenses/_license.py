import attr
import requests
from cached_property import cached_property


@attr.s()
class License:
    id = attr.ib(type=str)
    classifier = attr.ib(type=str)
    name = attr.ib(type=str)

    approved = attr.ib(type=bool)
    deprecated = attr.ib(type=bool)

    links = attr.ib(type=tuple)
    url = attr.ib(type=str)

    @cached_property
    def _details(self):
        requests.get(self.url).json()

    @property
    def template(self):
        return self._details['standardLicenseTemplate']

    @property
    def comments(self):
        return self._details['licenseComments']
