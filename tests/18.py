
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)



def count(f):
    """调用次数"""
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def memo(f):
    """记录下以前的调用记录，提高效率"""
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized


def count_frames(f):
    """计算最大的frames数目"""
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.open_count, counted.max_count)
        result =  f(n)
        counted.open_count -= 1
        return result
    counted.max_count = 0
    counted.open_count = 0
    return counted





    
        