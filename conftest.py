__author__ = 'BackOffice-3'


import pytest

@pytest.fixture
def base_url():
    url = 'https://sj.teambookapp.com/api/users?per_page=1000'
    return url
