# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    # This function tests the addition function
    assert add(1, 2) == 3
    assert add(1, -1) == 0
