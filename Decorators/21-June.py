# Dectorators : is a powerful and flexible that allow you to modifiy the behaviour  of the function or method without
#chamging the actual code
# they are essential function that takes function as a argument 


def my_decorator(func):
    def wrapper():
        print("Starting ........")
        func()
        print("Ending....")

    return wrapper()

@my_decorator
def say_hello():
    print("HELLOs")
