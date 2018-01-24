FUNCTION_KEYWORD = 'def'
FUNCTION_START_INDEX = 4
CLASS_KEYWORD = 'class'
CLASS_START_INDEX = 6


class Name:
    def __init__(self, old_name):
        self.old_name = old_name


class FunctionName(Name):
    def __init__(self, old_name, new_name=None):
        super().__init__(old_name)
        self.new_name = new_name


class ClassName(Name):
    def __init__(self, old_name, new_name=None):
        super().__init__(old_name)
        self.new_name = new_name


def tab_counter(line):
    for char in line:
        if char != ' ':
            return line.index(char) // 4


def search_names(file_path, keyword, start_index, obj):
    names = set()

    with open(file_path) as ugly_file:
        for line in ugly_file.readlines():
            beginning_of_line = tab_counter(line) * 4

            if line.startswith(keyword, beginning_of_line):
                start_index = start_index + beginning_of_line
                final_index = line.index('(') if '(' in line else line.index(':')
                name = line[start_index:final_index]
                names.add(obj(name))

    return names
