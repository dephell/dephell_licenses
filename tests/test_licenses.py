import pytest
from dephell_licenses import licenses


@pytest.mark.parametrize('id, classifier', [
    ('MIT', 'OSI Approved :: MIT License'),
    ('mit', 'OSI Approved :: MIT License'),

    ('Apache 2.0', 'OSI Approved :: Apache Software License'),
    ('Apache-2.0', 'OSI Approved :: Apache Software License'),
    ('apache2', 'OSI Approved :: Apache Software License'),

    ('GPL 3.0', 'OSI Approved :: GNU General Public License v3 (GPLv3)'),
    ('GPLv3.0', 'OSI Approved :: GNU General Public License v3 (GPLv3)'),
    ('GPLv3', 'OSI Approved :: GNU General Public License v3 (GPLv3)'),
    ('GPL 3', 'OSI Approved :: GNU General Public License v3 (GPLv3)'),
    ('gpl3', 'OSI Approved :: GNU General Public License v3 (GPLv3)'),
])
def test_get_by_id(id: str, classifier: str):
    license = licenses.get_by_id(id)
    assert license.classifier == 'License :: ' + classifier


@pytest.mark.parametrize('classifier, id', [
    ('License :: OSI Approved :: MIT License', 'MIT'),
    ('License :: OSI Approved :: Apache Software License', 'Apache-2.0'),
    ('License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'GPL-3.0'),
])
def test_get_by_classifier(classifier: str, id: str):
    license = licenses.get_by_classifier(classifier)
    assert license.id == id


@pytest.mark.parametrize('name, id', [
    ('MIT License', 'MIT'),
    ('MIT', 'MIT'),
    ('mit', 'MIT'),

    ('Apache Software License', 'Apache-2.0'),
    ('Apache 2.0', 'Apache-2.0'),

    ('GPL 3.0', 'GPL-3.0'),
    ('GPL 3', 'GPL-3.0'),
    ('gpl3', 'GPL-3.0'),

    ('mpl2', 'MPL-2.0'),
    ('lgpl3', 'LGPL-3.0'),
])
def test_get_by_name(name: str, id: str):
    license = licenses.get_by_name(name)
    assert license.id == id
