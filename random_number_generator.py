

def quick_picks(n:int):

    import random
    from variables import keno_combinations

    _sysrand = random.SystemRandom()
    numbers = _sysrand.sample(keno_combinations, n)
    print(numbers)
    print(numbers[0])

    return sorted(numbers)