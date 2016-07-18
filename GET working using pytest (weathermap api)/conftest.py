import pytest

@pytest.fixture(scope="module") #fixture for generating baseurl
def baseurl():
    url= 'http://api.openweathermap.org/data/2.5/weather?'
    return url

@pytest.fixture(scope="module", params=['q=London,uk','q=goa,india','lat=35&lon=139'])
def urlparam(request):
   return request.param