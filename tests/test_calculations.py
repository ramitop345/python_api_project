import pytest
from  app.calculations import *

@pytest.mark.parametrize("num1, num2, expected", [(2,3,5),(0,0,0),(1,1,2)])
def test_add(num1, num2, expected):
    assert add(num1,num2) == expected


def test_add_without_params():
    assert add(3,4) == 7

#using fixtures
@pytest.fixture
def return_5():
    return 5

def test_use_fixture(return_5):
    assert return_5 == 5