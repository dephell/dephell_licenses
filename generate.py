import json
import requests
from pathlib import Path
from textdistance import levenshtein
from tqdm import tqdm

url = 'https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json'
info = requests.get(url).json()['licenses']

url = 'https://pypi.org/pypi?%3Aaction=list_classifiers'
classifiers = requests.get(url).text.split('\n')

licenses = []
for classifier in tqdm([c for c in classifiers if c.strip().startswith('License :: ')]):
    classifier = classifier.strip()
    name = classifier.split('::')[-1].strip()
    best_license = info[0]
    best_distance = float('Inf')
    for license in info:
        d = levenshtein(name, license['name'] + ' ' + license['licenseId'])
        if d < best_distance:
            best_license = license
            best_distance = d
    licenses.append(dict(
        approved=best_license['isOsiApproved'],
        classifier=classifier,
        deprecated=best_license['isDeprecatedLicenseId'],
        id=best_license['licenseId'],
        links=best_license['seeAlso'],
        name=best_license['name'],
        url=best_license['detailsUrl'],
    ))

Path('dephell_licenses', 'licenses.json').write_text(json.dumps(licenses, sort_keys=True, indent=2))
