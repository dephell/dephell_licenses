import json
import requests
import re
from pathlib import Path
from textdistance import hamming

url = 'https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json'
info = requests.get(url).json()['licenses']

url = 'https://pypi.org/pypi?%3Aaction=list_classifiers'
classifiers = requests.get(url).text.split('\n')


def get_by_name(name):
    best_license = info[0]
    best_distance = float('Inf')
    for license in info:
        d = hamming.normalized_distance(name, license['name'])
        if d < best_distance:
            best_license = license
            best_distance = d
    if best_distance < .90:
        return best_license


def get_by_fullname(name):
    best_license = info[0]
    best_distance = float('Inf')
    for license in info:
        d = hamming.normalized_distance(name, license['name'] + ' ' + license['licenseId'])
        if d < best_distance:
            best_license = license
            best_distance = d
    if best_distance < .90:
        return best_license


rex_clean = re.compile(r'[^a-zA-Z0-9]+')


def get_by_id(name):
    if '(' not in name:
        return
    name = name.split('(')[-1].split(')')[0]
    name = rex_clean.sub('', name)
    best_license = info[0]
    best_distance = float('Inf')
    for license in info:
        d = hamming.distance(name, rex_clean.sub('', license['licenseId']))
        if d < best_distance:
            best_license = license
            best_distance = d
    if best_distance <= 1:
        return best_license


licenses = []
for classifier in classifiers:
    classifier = classifier.strip()
    if not classifier.strip().startswith('License :: '):
        continue
    name = classifier.split('::')[-1].strip()

    best_license = get_by_id(name)
    if best_license is None:
        best_license = get_by_name(name)
    if best_license is None:
        best_license = get_by_fullname(name)
    if best_license is None:
        continue

    print(name, '|', best_license['licenseId'], '.', best_license['name'])
    if input('same? > ').strip():
        print('skipped')
        continue

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
