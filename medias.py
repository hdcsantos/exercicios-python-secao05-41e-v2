def geometrica(x, y, z):
    raiz = x * y * z
    raiz_c = raiz ** (1/3)
    return round(raiz_c)


def ponderada(x, y, z):
    return (x + (2 * y) + (3 * z)) / 6


def harmonica(x, y, z):
    return 1 / ((1 / x) + (1 / y) + (1 / z))


def aritimetica(x, y, z):
    return (x + y + z) / 3
