


def pedido_cafe():
    total = 0  

    while True:
        print('Escolha seu café:')
        print(' [0] Cancelar pedido')
        print(' [1] Café coado - R$ 3,00')
        print(' [2] Café expresso - R$ 4,00')
        print(' [3] Capuccino - R$ 5,00')
        print(' [4] Chocolate - R$ 6,00')
        
        try:
            pedido = int(input('Digite o número da sua escolha: ')) 

            if pedido == 0:
                print('Pedido cancelado.')
                break  
            elif pedido == 1:
                print('Você escolheu um café coado')
                total += 3.00  
            elif pedido == 2:
                print('Você escolheu um café expresso')
                total += 4.00  
            elif pedido == 3:
                print('Você escolheu um capuccino')
                total += 5.00  
            elif pedido == 4:
                print('Você escolheu um chocolate')
                total += 6.00  
            else:
                print('Número incorreto. Por favor, escolha um número entre 0 e 4.')
                continue  
            repetir = input('Deseja fazer outro pedido? (s/n): ').lower()
            if repetir != 's':
                print(f'Obrigado! O total do seu pedido é R$ {total:.2f}.')
                break  

        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')
