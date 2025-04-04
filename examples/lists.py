my_list: list = ['one', 'two', 'three', 'four' , 'five', 'one']
my_second_list: list = [1, 4, False, 'aaaaa']
new_list = list(('apple', 'banana')) # make the list using a constructor

def show_list():
    print(f"This is an original list: {my_list}")

def add_value(new_value: str):
    my_list.append(new_value)
    print(f"This is a list with added value '{new_value}': {my_list}")

def insert_value():
    my_list.insert(2, "aaaaaaaaaaaaaahhhaaaa")
    print(f"After inserting a one new element list look like this: {my_list}")

def show_length():
    print(f"The length of the list is: {len(my_list)}")

def delete_element(element: str):
    my_list.remove(element)
    print(f"The element '{element}' was deleted from list: {my_list}")

def replace_element(old_element: str, new_element: str):
    index_old_element = my_list.index(old_element)
    my_list[index_old_element] = new_element
    print(f"The element '{old_element}' was replaced by a new one '{new_element}'. The list looks like this: {my_list}")

def extend_list(new_list: list):
    my_list.extend(new_list)
    print(f"This is extended list: {my_list}")