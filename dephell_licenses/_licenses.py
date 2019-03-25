import json
from pathlib import Path
from cached_property import cached_property

from ._license import License


class Licenses:
    @cached_property
    def all(self):
        path = Path(__file__).parent / 'licenses.json'
        licenses = json.loads(path.read_text(encoding='utf-8'))
        return tuple(License(**license) for license in licenses)

    def get_by_classifier(self, name):
        for license in self.all:
            if license.classifier == name:
                return license

    def get_by_id(self, name):
        for license in self.all:
            if license.id == name:
                return license

    def get_by_name(self, name):
        for license in self.all:
            if license.name == name:
                return license
        for license in self.all:
            if license.classifier.split(' :: ')[-1] == name:
                return license
