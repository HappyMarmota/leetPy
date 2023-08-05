def reverse_int(i :int) -> int
    r = 0
    while i != 0:
        r = r * 10 + i % 10
        i = int(i / 10)
    return r