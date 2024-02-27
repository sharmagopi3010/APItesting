import pytest

@pytest.fixture(scope="class")
def start_exec():
    print("JJJJJ")
    yield
    print ("I will execute last")

@pytest.fixture()
def dataload():
    print("fixture with data")
    return ["username", "password"]

@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param



@pytest.fixture(params=[("Chrome","user1"), ("Firefox","user2"), ("IE","user3")])
def crossBrowser1(request):
    return request.param