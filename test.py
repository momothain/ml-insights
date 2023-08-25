import pytest
from models import Base, User, engine, Session

@pytest.fixture(scope='module')
def test_session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_add_user(test_session):
    user = User(username='test_user')
    test_session.add(user)
    test_session.commit()

    queried_user = test_session.query(User).filter_by(username='test_user').first()
    assert queried_user is not None
    assert queried_user.username == 'test_user'


### GENERIC EXAMPLES BELOW
    
# Parameterized Tests:
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_addition(a, b, expected):
    assert a + b == expected

# Fixtures:
# Fixtures are a powerful feature that allows you to set up and tear down preconditions for your tests.
# They can be modular and reused across multiple tests.
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

def test_length(sample_data):
    assert len(sample_data) == 4


# Skipping and Expecting Failures:
# pytest allows you to mark certain tests as skipped or expected to fail, which can be helpful during development.
@pytest.mark.skip(reason="Incomplete test")
def test_incomplete():
    ...

@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2
