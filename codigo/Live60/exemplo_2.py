while True:
    try:
        nome = input('Digite seu nome: ')
        print(f'Olá {nome}')
        1
    except KeyboardInterrupt:
        print('\nTudo Bemm já entendi, você não quer brincar')
        exit()
    except ZeroDivisionError:
        print('Você não sabe que não pode dividir por 0?')
