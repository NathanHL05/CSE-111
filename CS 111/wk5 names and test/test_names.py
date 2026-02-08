from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    name = make_full_name("john", "doe")
    assert isinstance(name, str)

    assert make_full_name("","") == ";"
    assert make_full_name("john", "") == ";john"
    assert make_full_name("","doe") == "doe;"
    assert make_full_name("john", "d-oe") == "d-oe;john"
    assert make_full_name("Xiphactinus","Lovegood") == "Lovegood;Xiphactinus"
def test_extract_family_name():
    last = extract_family_name("larson;nathan")
    assert isinstance(last, str)

    assert extract_family_name("lar-son;nathan") == "lar-son"
    assert extract_family_name("Xiphactinus; Lovegood") == "Xiphactinus"
    assert extract_family_name(";nathan") == ""



def test_extract_given_name():
    first = extract_given_name("larson;nathan")
    assert isinstance(first, str)

    assert extract_given_name("larson;nat-han") == "nat-han"
    assert extract_given_name("Xiphactinus;Lovegood") == "Lovegood"
    assert extract_given_name(";nathan") == "nathan"    

pytest.main(["-v", "--tb=line", "-rN", __file__])