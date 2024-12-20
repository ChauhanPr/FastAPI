import pytest

def test_equal_or_not_equal():
    assert 3 == 3
    assert 3!=1

def test_is_instance():
    assert isinstance('this is a string',str)
    assert not isinstance('10',int)

def test_boolean():
    validate=True
    assert validate is True
    assert ('hello' == 'world') is False

def test_type():
    assert type('Hello' is str)
    assert type('world' is not int)

def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10

def test_list():
    num_list=[1,2,3,4,5]
    any_list=[False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)

class student:
    def __init__(self,fn:str, ln:str, major:str, years:int):
        self.fn=fn
        self.ln=ln
        self.major=major
        self.year=years


@pytest.fixture
def default_employee():
    return student('Preeti','Chauhan','Computer Science',3)


def test_person_initialization(default_employee):
   # p = student('Preeti','Chauhan','Computer Science',3)
    assert default_employee.fn == 'Preeti', 'First name should be Preeti'
    assert default_employee.ln == 'Chauhan','Last name shoud be Chauhan'
    assert default_employee.major == 'Computer Science'
    assert default_employee.year == 3

