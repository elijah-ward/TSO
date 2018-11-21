import sys
from .classmodule import ExampleTsoClass
from .funcmodule import my_function


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = ExampleTsoClass('Some Text To Show')
    my_object.say_text()


if __name__ == '__main__':
    main()
