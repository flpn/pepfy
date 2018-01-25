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

    def pepfy_name(self):
        new_name = list(self.old_name)
        i = 0

        while True:
            try:
                if new_name[i].isupper():
                    new_name[i] = new_name[i].lower()

                    if 0 < i < len(new_name):
                        new_name.insert(i, '_')

                i += 1
            except IndexError:
                break

        return ''.join(new_name)


class ClassName(Name):
    def __init__(self, old_name, new_name=None):
        super().__init__(old_name)
        self.new_name = new_name

    def pepfy_name(self):
        new_name = list(self.old_name)
        i = 0

        while True:
            try:
                if i > 0 and self.old_name[i - 1] != '_' and self.old_name[i - 1].isupper():
                    new_name[i] = new_name[i].lower()
                elif i < len(new_name) - 1 and  new_name[i] == '_':
                    new_name[i + 1] = new_name[i + 1].upper()

                i += 1
            except IndexError:
                break

        new_name[0] = new_name[0].upper()

        return ''.join(new_name).replace('_', '')


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


if __name__ == '__main__':
    pass
