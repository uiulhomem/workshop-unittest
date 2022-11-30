def fatorial(x):
    if isinstance(x, float) or x < 0:
        msg = 'A operação fatorial só é definida para inteiros positivos.'
        raise ValueError(msg)
        
    fat = 1
    for i in range(1, x+1):
        fat *= i

    return fat
