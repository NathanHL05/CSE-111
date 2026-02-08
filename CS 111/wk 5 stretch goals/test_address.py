from address import extract_city, extract_state, extract_zipcode
import pytest


# number and street, city, state zipcode

def test_extract_city():
    city = extract_city("450sw 90th Ave, Portland, OR 97225")
    assert isinstance(city, str)

    assert extract_city("450sw 90th Ave, Portland, OR 97225") == "Portland"

def test_extract_state():
    assert extract_city("450sw 90th Ave, Portland, OR 97225") == "OR"


pytest.main(["-v", "--tb=line", "-rN", __file__])