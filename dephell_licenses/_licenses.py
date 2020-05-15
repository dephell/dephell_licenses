import json
import re
from pathlib import Path
from typing import Tuple, Dict, Iterator, Optional

from ._cached_property import cached_property
from ._license import License


rex_clean = re.compile(r'[^a-zA-Z0-9]+')


class Licenses:
    @cached_property
    def all(self) -> Tuple[License, ...]:
        path = Path(__file__).parent / 'licenses.json'
        licenses = json.loads(path.read_text(encoding='utf-8'))
        return tuple(License(**license) for license in reversed(licenses))

    # indices

    @cached_property
    def _reverse_index_classifier(self) -> Dict[str, License]:
        return {license.classifier: license for license in self.all}

    @cached_property
    def _reverse_index_id(self) -> Dict[str, License]:
        return {license.id: license for license in self.all}

    @cached_property
    def _reverse_index_cleaned_id(self) -> Dict[str, License]:
        return {self._clean_id(license.id): license for license in self.all}

    @cached_property
    def _reverse_index_cleaned_name(self) -> Dict[str, License]:
        result = dict()
        for license in self.all:
            name = license.classifier.split(' :: ')[-1]
            result[self._clean_name(name)] = license
        for license in self.all:
            result[self._clean_name(license.name)] = license
        return result

    # getters

    def get_by_classifier(self, classifier: str) -> Optional[License]:
        return self._reverse_index_classifier.get(classifier)

    def get_by_id(self, license_id: str) -> Optional[License]:
        license = self._reverse_index_id.get(license_id)
        if license is not None:
            return license
        return self._reverse_index_cleaned_id.get(self._clean_id(license_id))

    def get_by_name(self, name: str) -> Optional[License]:
        license = self._reverse_index_cleaned_name.get(self._clean_name(name))
        if license is not None:
            return license
        license = self.get_by_id(name)
        if license is not None:
            return license
        return None

    # private methods

    @staticmethod
    def _clean_id(license_id: str) -> str:
        return rex_clean.sub('', license_id.replace('.0', '')).replace('v', '').lower()

    @classmethod
    def _clean_name(cls, license_name: str) -> str:
        return cls._clean_id(license_name).replace('license', '').strip()

    # magic methods

    def __iter__(self) -> Iterator[License]:
        yield from self.all

    def __repr__(self) -> str:
        return '{}()'.format(type(self).__name__)
