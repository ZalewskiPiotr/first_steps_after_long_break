from examples.numeric_types import add_number, add_floats, show_variable_type, convert_float_to_int

def test_add_number():
    assert add_number(4,5) == 9
    assert add_number(14, 5) == 19

def test_add_floats():
    assert add_floats(12.3, 2.3) == 14.6 + 4.5 # 4.5 is the magic factor inside add_floats function

def test_show_variable_type():
    assert show_variable_type(2) == int
    assert show_variable_type(2.1) == float

def test_convert_float_to_int():
    assert convert_float_to_int(45.7) == 45