from examples import numeric_types as num_types


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


if __name__ == "__main__":
    run_numeric_types_script()
