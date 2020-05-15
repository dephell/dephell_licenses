from dephell_licenses import licenses


def test_make_text():
    license = licenses.get_by_id('MIT')

    assert 'Copyright (c) <year> <copyright holders>' in license.make_text()
    assert 'beginOptional' not in license.make_text()
    assert license.make_text().strip().startswith('MIT License')

    assert 'MIT License 2018 Gram' in license.make_text(copyright='2018 Gram')
