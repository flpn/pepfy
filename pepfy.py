def tab_counter(line):
    for char in line:
        if char != ' ':
            return line.index(char) // 4


def pep_function_header(line):
    if line.startswith('def', (tab_counter(line) * 4)):
        l = list(line)
        excludes = {' ', '(', ')'}

        for i in range(len(l)):
            if l[i].isupper():
                l[i] = l[i].lower()

                if not l[i - 1] in excludes and not l[i + 1] in excludes:
                    l.insert(i, '_')

        return ''.join(l)
    else:
        return line


if __name__ == '__main__':
    with open('foo.py') as ugly_file:
        new_file = ''

        for line in ugly_file.readlines():
            new_file += pep_function_header(line)

        print(new_file)
