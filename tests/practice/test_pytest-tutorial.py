import pytest
import logging

smtpserver = "mail.python.org"
LOGGER = logging.getLogger(__name__)


@pytest.mark.practice
def test_ehlo(smtp_connection):
    LOGGER.info(smtp_connection)
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    # assert 0  # for demo purposes


@pytest.mark.practice
def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes


@pytest.mark.practice
def test_show_helo(smtp_connection):
    assert 0, smtp_connection.helo()


def compute_expensive_image():
    print("computing image...")
    return []


def f():
    raise SystemExit(1)


def add(a, b):
    return a + b


def get_max_value(my_list):
    return max(my_list)


@pytest.mark.xfail(strict=False)
def test_max():
    get_max = get_max_value([2, 5, 6, 7, 8])
    assert get_max == 9


@pytest.mark.practice
class TestClass:

    LOGGER = logging.getLogger(__name__)

    def test_my_test_1(self):
        self.LOGGER.info("Running practice test 1")
        with pytest.raises(SystemExit):
            f()

    def test_add(self):
        self.LOGGER.info("Running practice test 2")
        assert 5 == add(3, 2)
        assert 4 == add(-2, 6)

    # content of test_tmpdir.py
    @pytest.mark.xfail(strict=False)
    def test_needs_files(self, tmpdir):
        print(tmpdir)
        p = tmpdir.mkdir("sub").join("hello.txt")
        p.write("content")
        assert p.read() == "content"
        assert len(tmpdir.listdir()) == 1
        assert 0
