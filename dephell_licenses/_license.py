import re
import textwrap
from typing import Dict, Any, List

import attr
import requests

from ._cached_property import cached_property


# <<var;name="copyright";original="<year> <copyright holders>";match=".+">>
# <<var;name=organizationClause3;original=the copyright holder;match=.+>>
rex_var = re.compile(
    r'<<var;'
    r'name="?(?P<name>[a-zA-Z0-9]+)"?;'
    r'original="?(?P<original>.+?)"?;'
    r'match="?(?P<match>.+?)"?>>'   # noQA: C812
)
rex_junk = re.compile(r'<<.+?>>')


@attr.s()
class License:
    id = attr.ib(type=str)
    classifier = attr.ib(type=str)
    name = attr.ib(type=str)

    approved = attr.ib(type=bool)
    deprecated = attr.ib(type=bool)

    links = attr.ib(type=List[str])
    url = attr.ib(type=str)

    @cached_property
    def _details(self) -> Dict[str, Any]:
        return requests.get(self.url).json()

    @property
    def template(self) -> str:
        return self._details['standardLicenseTemplate']

    @property
    def comments(self) -> str:
        return self._details['licenseComments']

    @cached_property
    def vars(self) -> List[Dict[str, str]]:
        vars = []
        for match in rex_var.finditer(self.template):
            var = match.groupdict()
            var['text'] = match.group(0)
            vars.append(var)
        return vars

    def make_text(self, *, wrap: bool = True, **kwargs) -> str:
        text = self.template
        for var in self.vars:
            value = kwargs.get(var['name'], var['original'])
            text = text.replace(var['text'], value)
        text = rex_junk.sub('', text).strip()

        if wrap:
            wrapper = textwrap.TextWrapper(
                width=78,
                break_long_words=False,
                replace_whitespace=False,
            )
            text = '\n'.join(wrapper.fill(line) for line in text.splitlines())

        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')

        return text + '\n'
