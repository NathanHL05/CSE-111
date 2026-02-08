from circuitAnalysis import get_current, get_total_voltage, get_parallel_res, series_res
import pytest

def test_get_current():
    #divided by zero error already accounted for in main code and will not be tested here
    assert get_current(12, 2) == 6
    assert get_current(0,5) == 0
    assert get_current(9.6, 3.2) == pytest.approx(3.0, 0.01)
    assert get_current(-10,2) == -5

def test_get_total_voltage():
    assert get_total_voltage(2, 5) == 10
    assert get_total_voltage(0, 100) == 0
    assert get_total_voltage(3.5, 2) == 7.0
    assert get_total_voltage(-4, 3) == -12

def test_get_parallel_res():
    #divided by zero error already accounted for in main code and will not be tested here
    assert get_parallel_res([10, 10]) == 5.0
    assert get_parallel_res([5, 10, 15]) == pytest.approx(2.727, 0.01)
    assert get_parallel_res([100, 200, 300, 400]) == 48
    assert get_parallel_res([50]) == 50.0
    assert get_parallel_res([1, 1, 1, 1, 1]) == 0.2

pytest.main(["-v", "--tb=line", "-rN", __file__])