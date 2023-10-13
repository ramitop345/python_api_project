import pytest
from  app.calculations import *

@pytest.mark.parametrize("num1, num2, expected", [(2,3,5),(0,0,0),(1,1,2)])
def test_add(num1, num2, expected):
    assert add(num1,num2) == expected