def operations_on_string(data: str):
    print(f"The base string from an user: {data}")

    print(f"The first character is: {data[0]}")
    print(f"The last character is: {data[-1]}")
    print(f"From index 3 to 17: {data[3:18]}")
    print(f"From index 0 to 17: {data[:18]}")
    print(f"From index 17 to the end: {data[17:]}")
    print(f"Last 5 characters: {data[-5:]}")
    print(f"Couple characters what are writing from the end: {data[18:5:-1]}")
    print(f"Reverse string: {data[::-1]}")

    print(f"Upper case string: {data.upper()}")
    print(f"Lower case string: {data.lower()}")

    print(f"Using 'split' function: {data.split()}")
    print(f"Another example of using 'split' function: {data.split('a')}")

    print(f"The length of a string: {len(data)}")

def change_string_to_asterix(data: str):
    new_data = "*" * len(data)
    new_data_1 = 100 * '+'
    print(f"Change a string to asterix: {new_data}")
    print(new_data_1)

def join_string(data: str, another_data: str):
    print(f"String1: {data}")
    print(f"String2: {another_data}")
    print(f"Joined string1 and string2: {data + ' ' + another_data}")

def check_substring(data: str, subdata: str):
    print("Check if '{0}' exists in '{1}': {2}".format(subdata, data, subdata in data))
