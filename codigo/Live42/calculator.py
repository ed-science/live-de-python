from numbers import Number


def soma(x, y):
    """AOR."""
    return x + y


def invert(x):
    """
    AOD - Delete o operador.
    AOR - Troca o operador
    """
    return -x


def sum_(*vals):
    """
    ASR - Troca o operador de atribuição.
    CRP - Troca as constantes
    """
    return sum(vals)


def is_number(val):
    """
    COD - Deletar operadores sozinhos (not)
    COI - Insere um operador lógico
    """
    return isinstance(val, Number)


def check_numbers(x, y):
    return bool(is_number(x) and is_number(y))
