from calc_logic import calculate

def test_add():
    result = calculate(12, 5, "+")
    assert result == 17

def test_divide():
    assert calculate(12,5, "/") == 2.4

test_add()
test_divide()
print("All tests passed!")