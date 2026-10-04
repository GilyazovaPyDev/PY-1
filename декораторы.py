import time


def time_run(func): # декоратор для измерения времени выполнения
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f'Функция {func.__name__} executed in {duration:.2f} seconds')
    return wrapper

def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'Функция {func.__name__} приняла {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} вернула {res}')
        return res
    return wrapper


def decor(func): #Декоратор, вложение одной функции в другую, замыкание
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

@decor
def null():
    print("null")

# @time_run
def etalon(n):
    print('START')
    time.sleep(n)

print(__name__)
if __name__ == '__main__':

    #print(__name__)
    null()
    # dec = decor(null)
    # dec()
    start = time.time()
    etalon(3)
    stop = time.time()
    print(stop)
    duration = stop - start
    print(duration)