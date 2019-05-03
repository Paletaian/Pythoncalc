# Inicia o loop para var. restart.
loop1 = 0
while loop1 < 1:
	
	# Cabeçalho.
    print("\n******************* Python Calculator *******************")
    
    # Inicia loop2 para evitar números fora do sumário.
    loop2 = 0
    while loop2 < 1:
    	
    	# Sumário
        print('\n')
        print('Adição - 1')
        print('Subtração - 2')
        print('Multiplicação - 3')
        print('Divisão - 4')
        print('\n')
        
        # Var. Para escolha da operação.
        NumberAction = input('Escolha sua operação: ')
        
        # Utilizando loop2, impede códigos inválidos.
        if NumberAction == '1' or NumberAction == '2' or NumberAction == '3' or NumberAction == '4':
            loop2 = 1
        else:
            print('Código invalido!')
            
    print('\n')
    
    # Inicia loop4 para evitar vírgulas nos números.
    loop4 = 0
    while loop4 == 0:
    
    	# Input para primeiro número a ser + - * :
    	n3 = input('Número inicial: ')
    	
    	# Verifica o tipo do número, e o transforma neste, para impedir erros.
    	if '.' in n3:
        	n1 = float(n3)
        	loop4 = 1
        	
        # Verifica se existe vírgula no número.
    	elif ',' in n3:
            print('Favor utilizar pontos para demarcar o início das casas decimais.')
            print('\n')
            
        # Se nenhuma das outras condições forem cumpridas, n3 se torna int.
    	else:
    		n1 = int(n3)
    		loop4 = 1
    	
	# Aqui temos o mesmo sistema acima.	
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
        	
    print('\n') 
       
    # Se a operação escolhida for +
    if int(NumberAction) == 1:  
        print(str(n1), '+', str(n2), '=', str(n1 + n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s + %s = %s\n' %(str(n1), str(n2), str(n1 + n2)
    
    # Se a operação escolhida for -
    elif int(NumberAction) == 2:
        print(str(n1), '-', str(n2), '=', str(n1 - n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s - %s = %s\n' %(str(n1), str(n2), str(n1 - n2))
            
	# Se a operação escolhida for *
    elif int(NumberAction) == 3:
        print(str(n1), '*', str(n2), '=', str(n1 * n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s * %s = %s\n' %(str(n1), str(n2), str(n1 * n2))
            
    # Se a operação escolhida for :
    else:
        print(str(n1), ':', str(n2), '=', str(n1 / n2))
        with open('datacalc.txt', 'a') as arq:
            arq.write('%s : %s = %s\n' %(str(n1), str(n2), str(n1 / n2))
            
    print('\n')   
    
    # Var. motivo do loop1
    restart = input('Continuar usando a calculadora (s/n): ')   
     
    print('\n')  
    
    # Volta ao início do código.
    if restart.lower() == 's':        
        pass  
          
    # Encerra o loop1
    else:  
        loop1 = 1
        
print('Obrigado por usar!')