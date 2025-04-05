my_dict: dict = {
    "name": "piotr",
    "age": 18,
    "skills": ["Python", "C#", "PHP"]
}

def show_dictionary():
    print(f"This is a dictionary: {my_dict}")

def get_value(key: str):
    value = my_dict.get(key)
    print(f"This is value for key '{key}': {value}. the type of thew value is {type(value)}")

def show_keys():
    key_list = my_dict.keys()
    key_string = ""
    for one_key in key_list:
        key_string += one_key + ','
    print(f"The list of all keys in the dictionary: {key_string}")

def add_item(key: str, value: str):
    my_dict[key] = value
    print(f"This is a dictionary after adding a new element: {my_dict}")