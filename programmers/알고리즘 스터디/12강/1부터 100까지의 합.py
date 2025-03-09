def recursive(x):
    if x == 1:
        return 1
    elif x > 1 and isinstance(x, int):
        return recursive(x-1) + x
    else:
        raise ValueError("ValueError")
print(recursive(100))