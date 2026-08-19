from check import status, pct

def test_status_zero_pass():
    assert status(0) == "PASS"

def test_status_zero_fail():
    assert status(5) == "FAIL"

def test_pct():
    assert pct(1, 10) == 10.0