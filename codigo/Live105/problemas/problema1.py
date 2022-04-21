def maior(x, y):
    '''problema 1.'''
    return y if x < y else x


def é_vogal(letra):
    '''problema 2.'''
    vogais = 'a e i o u'.split()
    if letra.lower() in vogais:
        return 'vogal'
    return 'consoante'
