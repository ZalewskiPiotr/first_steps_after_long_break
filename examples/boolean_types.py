def convert_to_boolean():
    print("bool(0) = {0}".format(bool(0)))  # False
    print("bool(1) = {0}".format(bool(1)))  # True
    print('bool("") = {0}'.format(bool("")))  # False (empty string)
    print('bool("hello") = {0}'.format(bool("hello")))  # True (non-empty string)
    print("bool([]) = {0}".format(bool([])))  # False (empty list)
    print("bool([1, 2]) = {0}".format(bool([1, 2])))  # True (non-empty list)

def show_boolean_values():
    x = True
    y = False
    print("Boolean values: {0}, {1}".format(x, y))