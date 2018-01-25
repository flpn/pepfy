# Pepfy
This project has the purpose to format Python code into the conventions of **PEP 8**, making things more readable and concise.

###### Example of usage:
```py
# main.py
from pepfy import pepfy_file


pepfy_file('MyFile.py')
```
Old file:

```py
# MyFile.py
class text_printer():
    def Print_Text(self, Text):
        print(Text)
def foo():
    return "foo"

def multipleFoo(NUMBER_OF_TIMES):
    return foo() * NUMBER_OF_TIMES

if __name__ == "__main__":
    tp=text_printer()
    if len(multiple_foo(42)) % 2 == 0:
        tp.Print_Text("Ohhhh yes!!!")
    else:
        tp.Print_Text("Oh no!")
```

New file:
```py
# my_file_pepfy.py
class TextPrinter:
    def print_text(self, text):
        print(text)
        

def foo():
    return 'foo'


def multiple_foo(number_of_times):
    return foo() * number_of_times


if __name__ == '__main__':
    tp = TextPrinter()
   
    if len(multiple_foo(42)) % 2 == 0:
        tp.print_text('Ohhhh yes!!!')
    else:
        tp.print_text('Oh no!')

```
