def decorator(func):
    def wrapper_around_func():
        print "Decorator calling func"
        func()
        print "Decorator called func"
    return wrapper_around_func


@decorator
def func():
    print "In the function"


func()
