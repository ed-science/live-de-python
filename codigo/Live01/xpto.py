def eh_par(val: int) -> bool:
    """
    Função que verifica se numero é par.

    Arg:
        - val: Valor de entrada do tipo inteiro
    """
    return val % 2 == 0 if isinstance(val, (int, float)) else False
