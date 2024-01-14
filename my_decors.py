from time import time

def timer(func):
    def wrapper(*args):
        now=time()
        result=func(*args)
        print(f'Function executed in {time()-now} s')
        return result
    return wrapper
        
    