def base62_encode(deci):
    symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(symbols)
    if deci == 0:
        return symbols[0]
    result = ''
    while deci > 0:
        result = symbols[deci % base] + result
        deci = deci // base
    return result

print(base62_encode(123142))