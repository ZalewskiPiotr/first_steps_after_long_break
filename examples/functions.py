def just_show_value(name: str):
    print(f"The original name is: {name}")
    name = "new name"
    print(f"The new name is: {name}")

def show_kids_names(*kids: str):
    for name in kids:
        print(f"The name of a kid is: {name}")

def show_keywords_arguments(**kids):
    print(f"I got dictionary: {kids}")

def show_default_parameter_value(name = "killer"):
    print(f"The name is: {name}")