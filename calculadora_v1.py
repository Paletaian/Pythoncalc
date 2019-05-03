loop1 = 0
while loop1 < 1:
    print("\n******************* Python Calculator *******************")
    loop2 = 0
    while loop2 < 1:
        print('\n')
        print('Adição - 1')
        print('Subtração - 2')
        print('Multiplicação - 3')
        print('Divisão - 4')
        print('\n')
        NumberAction = input('Escolha sua operação: ')
        if NumberAction == '1' or NumberAction == '2' or NumberAction == '3' or NumberAction == '4':
            loop2 = 1
        else:
            print('Código invalido!')
    print('\n')
    loop4 = 0
    while loop4 == 0:
    	n3 = input('Número inicial: ')
    	if '.' in n3:
        	n1 = float(n3)
        	loop4 = 1
    	elif ',' in n3:
            print('Favor utilizar pontos para demarcar o início das casas decimais.')
            print('\n')
    	else:
    		n1 = int(n3)
    		loop4 = 1
    loop5 = 0
    while loop5 == 0:
    	n4 = input('Número final: ')    
    	if '.' in n4:
        	n2 = float(n4)
        	loop5 = 1
    	elif ',' in n4:
            print('Favor utilizar pontos para demarcar o início das casas decimais.')
            print('\n')
    	else:
        	n2 = int(n4)
        	loop5 = 1
    n10 = str(n1)
    n20 = str(n2)
    print('\n')    
    if int(NumberAction) == 1:     
        print(str(n1), '+', str(n2), '=', str(n1 + n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s + %s = %s\n' %(str(n1), str(n2), str(n1 + n2)
    elif int(NumberAction) == 2:
        print(str(n1), '-', str(n2), '=', str(n1 - n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s - %s = %s\n' %(str(n1), str(n2), str(n1 - n2))
    elif int(NumberAction) == 3:
        print(str(n1), '*', str(n2), '=', str(n1 * n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s * %s = %s\n' %(str(n1), str(n2), str(n1 * n2))
    else:
        print(str(n1), ':', str(n2), '=', str(n1 / n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s : %s = %s\n' %(str(n1), str(n2), str(n1 / n2))
    print('\n')      
    restart = input('Continuar usando a calculadora (s/n): ')    
    print('\n')    
    if restart.lower() == 's':        
        pass    
    else:        
        loop1 = 1
print('Obrigado por usar!')