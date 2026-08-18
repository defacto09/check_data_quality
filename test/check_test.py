from check import status

def test_status_zero_pass():
    assert status(0) == "PASS"

def test_status_zero_fail():
    assert status(5) == "FAIL"
