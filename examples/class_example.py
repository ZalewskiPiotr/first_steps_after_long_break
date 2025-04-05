class MyFirstClass:
    # _name = "PiotrZET"
    # _age = 18
    # _skill = "power"
    global_count = 0

    def __init__(self, name: str, age: int, skill:str):
        self._name = name
        self._age = age
        self._skill = skill
        self._count = 1
        MyFirstClass.global_count += 1

    def __str__(self):
        return self._name

    def show_properties(self):
        print(f"The object properties: Name-{self._name}, Age-{self._age}, Skill-{self._skill}")