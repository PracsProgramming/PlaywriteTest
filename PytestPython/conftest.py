import pytest


@pytest.fixture(scope="session")
def pre_work():
    print("I setup browser instance")
    return "Pass"

@pytest.fixture(scope="module")
def pre_work2():
    print("I setup module instance")

@pytest.fixture(scope="function")
def pre_work3():
    print("I setup function instance")
    yield
    print("tear down validation")