
answer = 0

while answer != 5:
    if answer == 0:
        print(f'\nBem vindo a sua calculadora integrada, ofereçemos todas as modalidades\n'
        'de calcúlos possíveis.')
        print('Responda com as seguintes respostas:\n'
            '1 - Para soma (+)\n' 
            '2 - Para subtração (-)\n'
            '3 - Para divisão (/)\n'
            '4 - Para multiplição (* ou x)\n'
            '5 - Para fechar o programa\n')
        answer = int(input(f'R: '))

    while answer == 1:
        
        Quest1 = int(input(f'\nQual o primeiro número para soma?\n\nR: '))
        Quest2 = int(input(f'\nQual o segundo número para soma?\n\nR: '))
        print(f'\nO calculo total é de: {Quest1 + Quest2}')
        
        answersubmen = str(input(f'\nDeseja continuar os cálculos? (s/n)\nR: '))
        if answersubmen == 's':
            answer = 1
        elif answersubmen == 'n':
            answermen = str(input(f'\nDeseja voltar para o menu inicial? (s/n)\nR: '))
            if answermen == 's':
                answer = 0
            else:
                print(f'\nPrograma encerrado, obrigado por utiliza-lo :)\n')
                answer = 5
    
    while answer == 2:
        
        Quest1 = int(input(f'\nQual o primeiro número para a subtração?\n\nR: '))
        Quest2 = int(input(f'\nQual o segundo número para subtração?\n\nR: '))
        print(f'\nO calculo toral é de: {Quest1 - Quest2}')
        
        answersubmen = str(input(f'\nDeseja continuar os cálculos? (s/n)\nR: '))
        if answersubmen == 's':
            answer = 2
        elif answersubmen == 'n':
            answermen = str(input(f'\nDeseja voltar ao menu inicial? (s/n)\nR: '))
            if answermen == 's':
                answer = 0
            else:
                print(f'\nPrograma encerrado, obrigado por utiliza-lo :)\n')
                answer = 5
    
    while answer == 3:
        
        Quest1 = int(input(f'\nQual o primeiro número para a divisão?\n\nR: '))
        Quest2 = int(input(f'\nQual o segundo número para a divisão?\n\nR: '))
        print(f'O resutado da divisão foi: {Quest1 / Quest2}')
        
        answersubmen = str(input(f'\nDeseja continuar com os cálculos? (s/n)\nR: '))
        if answersubmen == 's':
            answer = 3
        elif answersubmen == 'n':
            answermen = str(input(f'\nDeseja voltar ao menu inicia? (s/n)\nR: '))
            if answermen == 's':
                answer = 0
            elif answermen == 'n':
                print(f'\nPrograma encerrado, obrigado por utiliza-lo :)\n')
                answer = 5
    
    while answer == 4:
        
        Quest1 = int(input(f'\nQual o primeiro número para a multiplicação?\n\nR: '))
        Quest2 = int(input(f'\nQual o segundo número para a multiplicação?\n\nR: '))
        print(f'O resultado da multiplocação foi: {Quest1 * Quest2}')
        
        answersubmen = str(input(f'\nDeseja continuar com os cálculos? (s/n)\nR: '))
        if answersubmen == 's':
            answer = 4
        elif answersubmen == 'n':
            answermen = str(input(f'Deseja voltar ao menu inicial? (s/n)\nR: '))
            if answermen == 's':
                answer = 0
            elif answermen == 'n':
                print(f'\nPrograma encerrado, obrigado por utiliza-lo :)\n')
                answer = 5
    
    if answer == 5:
        print(f'\nPrograma encerrado, obrigado por utiliza-lo :)\n')
    
    if answer > 5 or answer < 0:
        print(f'\nNão entendi, tente novamente.\n')
        answer = 0
