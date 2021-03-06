from planning_poker import parse_votes, generate_fibonacci, check_for_break
import pytest

def test_parse_votes():
    test_strings = ["1 2 3 5", "1 2 3 5  ", "1  2 3 5", "    1    2   3      5   ", "1 a 2 3 d 5"]
    expected = [[1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5]]
    for i, string_in in enumerate(test_strings):
        actual_out = parse_votes(string_in)
        assert actual_out == expected[i]

def test_generate_fibonacci():
    inputs = [5, 6, 1, 2]
    expected = [[0, 1, 2, 3, 5], [0, 1, 2, 3, 5, 8], [0], [0, 1]]
    for i, in_val in enumerate(inputs):
        actual_out = generate_fibonacci(in_val)
        assert actual_out == expected[i]

    # Test an exception with 0 and negative values
    for i in range(-5, 1, 1):
        with pytest.raises(Exception) as excinfo:
            actual_out = generate_fibonacci(i)
        assert "Cannot take 0 or negative value for length" in str(excinfo.value)

def test_check_for_break():
    inputs = [[1, 3, 5], [1, 8, 13], [1, 3, 8], [1, 3, 9], [4, 21], [6, 21], [5, 22], [5, 20]]
    expected_out = [False, True, True, True, True, False, True, False]
    for i, in_val in enumerate(inputs):
        assert check_for_break(in_val) == expected_out[i]