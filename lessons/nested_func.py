# Func can be nested

def pretty_print(arg):
    def print_stars():
        print('_' * 8)
        print('*' * 8)
    print_stars()
    print(arg)
    print_stars()

pretty_print("nya")