from dephell_licenses import licenses


def test_get_by_id():
    license = licenses.get_by_id('MIT')
    assert license.classifier == 'License :: OSI Approved :: MIT License'


def test_get_by_classifier():
    license = licenses.get_by_classifier('License :: OSI Approved :: MIT License')
    assert license.id == 'MIT'
