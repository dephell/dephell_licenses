import re
import attr
import requests
from cached_property import cached_property


# <<var;name="copyright";original="<year> <copyright holders>";match=".+">>
# <<var;name=organizationClause3;original=the copyright holder;match=.+>>
rex_var = re.compile(
    r'<<var;'
    r'name="?(?P<name>[a-zA-Z0-9]+)"?;'
    r'original="?(?P<original>.+?)"?;'
    r'match="?(?P<match>.+?)"?>>'
)
rex_junk = re.compile(r'<<.+?>>')


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
        return requests.get(self.url).json()

    @property
    def template(self):
        return self._details['standardLicenseTemplate']

    @property
    def comments(self):
        return self._details['licenseComments']

    @cached_property
    def vars(self):
        vars = []
        for match in rex_var.finditer(self.template):
            var = match.groupdict()
            var['text'] = match.group(0)
            vars.append(var)
        return vars

    def make_text(self, **kwargs) -> str:
        text = self.template
        for var in self.vars:
            value = kwargs.get(var['name'], var['original'])
            text = text.replace(var['text'], value)
        text = rex_junk.sub('', text)
        return text
