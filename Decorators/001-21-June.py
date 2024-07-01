import time


def log_dectrator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken-" + str(end_time - start_time))

    return wrapper()

@log_dectrator
def log_function():
    time.sleep(5)

    print("Printing the log time taken")
