from math_operations import add

class TestMathOperations:
  def test_add_positive(self):
    assert add(2, 3)==5
  def test_add_zeros(self):
    assert add(0, 0)==0
