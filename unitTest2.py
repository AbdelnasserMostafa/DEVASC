import pytest


@pytest.fixture
def tools_lib():
    import tools

    return tools.Tools('admin')


def test_true_when_greater(tools_lib):
    assert tools_lib.is_greater(5, 4)


def test_user(tools_lib):
    assert tools_lib.user == 'admin'


def test_false_when_equal(tools_lib):
    assert not tools_lib.is_greater(5, 5)
