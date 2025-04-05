from examples import numeric_types as num_types
from examples import boolean_types
from examples import strings
from examples import lists
from examples import tuples
from examples import dictionary
from examples import functions
from examples import lambda_script
from examples import class_example
from examples.class_example import MyFirstClass


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

def run_tuples_list():
    tuples.show_tuple_list()
    tuples.convert_to_list()

def run_dictionary_script():
    dictionary.show_dictionary()
    dictionary.get_value("age")
    dictionary.get_value("skills")
    dictionary.show_keys()
    dictionary.add_item("gender", "male")

def run_functions_script():
    functions.show_kids_names("kid1", "kid2")

    # I want to check if the value of a variable changes after returning from a function. The function changes the
    # value of the variable
    example_name: str = "Piotr"
    functions.just_show_value(name = example_name)
    print(f"The name after returning from a function: {example_name}")

    functions.show_keywords_arguments(kid1 = "John", kid2 = "Ana", kid3 = "Marta")

    functions.show_default_parameter_value()
    functions.show_default_parameter_value("Piter")

def run_lambda_script():
    lambda_script.show_lambda(5, 8)

def run_class_example_script():
    person: class_example.MyFirstClass = MyFirstClass("Johny", 33, "Endurance")
    person.show_properties()
    person._name = "New Johny"
    print(person)

    person_1 = MyFirstClass("me", 11, "any")
    person._count = 23
    print(person_1._count)

    print('-------------------')
    print(person.global_count)
    print(person_1.global_count)
    person.global_count = 22
    print(person.global_count)
    print(person_1.global_count)


    del person

if __name__ == "__main__":
    run_numeric_types_script()
    run_boolean_types_script()
    run_strings_script()
    run_lists_script()
    run_tuples_list()
    run_dictionary_script()
    run_functions_script()
    run_lambda_script()
    run_class_example_script()