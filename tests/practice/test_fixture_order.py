import pytest

# fixtures documentation order example
order = []


@pytest.fixture(scope="session")
def s1():
    print("executing s1")
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    print("executing m1")
    order.append("m1")


@pytest.fixture
def f1(f3):
    print("executing f1")
    order.append("f1")


@pytest.fixture
def f3():
    print("executing f3")
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    print("executing a1")
    order.append("a1")


@pytest.fixture
def f2():
    print("executing f2")
    order.append("f2")


@pytest.mark.practice
def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]