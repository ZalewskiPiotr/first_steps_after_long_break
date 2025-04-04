from examples import numeric_types as num_types
from examples import boolean_types
from examples import strings
from examples import lists
from examples.lists import show_length, delete_element


def run_numeric_types_script():
    print("-------------------------------- START run_numeric_types_script -------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")

    print()
    print(f"Result of adding two numbers 34 + 56 = {num_types.add_number(34, 56)}")
    print(f"Result of adding two floating numbers and a magic factor 34.5 + 22.1 + magic factor = "
        f"{num_types.add_floats(34.5, 22.1)}")

    print()
    print(f"Convert 56.7 to int is: {num_types.convert_float_to_int(56.7)}")

    print()
    print(f"The type of 56 is: {num_types.show_variable_type(56)}")
    print(f"The type of 'text' is: {num_types.show_variable_type('text')}")
    print(f"The type of 12.2 is: {num_types.show_variable_type(12.2)}")
    bool_variable: bool = False
    print(f"The type of True is: {num_types.show_variable_type(bool_variable)}")

    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("--------------------------------- STOP run_numeric_types_script -------------------------------------------")

def run_boolean_types_script():
    print("***********************************************************************************************************")
    print("-------------------------------- START run_boolean_types_script -------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    boolean_types.convert_to_boolean()
    boolean_types.show_boolean_values()
    print("-----------------------------------------------------------------------------------------------------------")
    print("--------------------------------- STOP run_boolean_types_script -------------------------------------------")

def run_strings_script():
    print("***********************************************************************************************************")
    print("-------------------------------- START run_strings_script -------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    example_sentence: str = "It is a cool sentence for make examples how to use 'strings' in Python"
    strings.operations_on_string(example_sentence)
    strings.change_string_to_asterix(example_sentence)

    strings.join_string(example_sentence, "An another sentence")
    strings.check_substring("It is long string", "long")
    strings.check_substring("It is long string", "nolong")

    strings.replace_string("This is OLD string", "OLD", "NEW")
    print("-----------------------------------------------------------------------------------------------------------")
    print("--------------------------------- STOP run_strings_script -------------------------------------------")

def run_lists_script():
    lists.show_list()
    lists.add_value("fifty five")
    lists.show_length()
    lists.delete_element('two')
    lists.replace_element('four', 'NEW FOUR')
    lists.insert_value()
    lists.extend_list(['ext_1', 'ext_2', 'ext_3'])

if __name__ == "__main__":
    run_numeric_types_script()
    run_boolean_types_script()
    run_strings_script()
    run_lists_script()