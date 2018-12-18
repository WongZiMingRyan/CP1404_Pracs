class ProgrammingLanguage:

    def __init__(self, typing="", dynamic="", reflection=True, year=0):
        self.typing = typing
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    """def is_dynamic(self):
        if self.dynamic.lower() == "dynamic":
            return True
        else:
            return False"""

    def __str__(self):
        return "test {}, {}, {}, {}".format(self.typing, self.dynamic, str(self.reflection), str(self.year))


def languages():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

