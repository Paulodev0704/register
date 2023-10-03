import os


entrar = input("Deseja entrar em cadastro de funcionarios [S]im ou [N]ão: ")
entrar_ms = entrar.upper()

lista = []
cont = 0
while entrar_ms == "S":
    nome = input("Digite seu nome (Se desejar parar  com o cadastro de nomes aperte a tecla ENTER):")
    tam_nome = len(nome)
    if tam_nome > 3:
        idade = int(input("Digite sua idade: "))
    else:
        break
    if  idade >0 and idade <=150:
        salario = int(input("Digite seu salario: "))
    else:
        print("Digite uma iddade real de 0 a 150 anos") 
    if salario > 0:
        sexo = input("Digite seu sexo [M]asculino ou [F]eminino: ")
        sexo_ms = sexo.upper()
    else:
        print("Seu salario obrigatoriamente tem que ser maior que 0")
    if sexo_ms == "F":
        sexo_final = "Feminino"
    elif sexo_ms == "M":
        sexo_final = "Masculino"    
    if sexo_ms == "F" or sexo_ms == "M":
        estado_civil = input("Digite seu estado civil [S]olteiro, [C]asado, [V]iuvo, [D]ivorciado: ")
        estado_civil_ms = estado_civil.upper()
    else:
        print("Somente sexo Feminino ou Masculino")    
    for i in range(1):
        lista.append(nome)
        lista.append(idade)
        lista.append(salario)
        lista.append(sexo_final)
        lista.append(estado_civil_ms)
        lista.append("|||")
        os.system("cls")
    if estado_civil_ms == "S" or estado_civil_ms == "C" or estado_civil_ms == "V" or estado_civil_ms == "D":
        if estado_civil_ms == "S":
            estado_civil_final = "Solteiro"
        elif estado_civil_ms == "C":
            estado_civil_final = "Casado"
        elif estado_civil_ms == "V":
            estado_civil_final = "Viuvo"
        elif estado_civil_ms == "D":
            estado_civil_final = "Divorciado"
            
                            
        else:
            print("Somente um dos quatro valores")
    
if entrar_ms == "N":
    consulta_lista = input("Se deseja acessar a lista de registros digite [R]egistros: ")
    consulta_lista_ms = consulta_lista.upper()
    if consulta_lista_ms == "R":
        print(lista)
    else:
        print("Fim do programa.")
elif nome == "":
    consulta_lista = input("Se deseja acessar a lista de registros digite [R]egistros se nao tecle enter: ")
    consulta_lista_ms = consulta_lista.upper()
    if consulta_lista_ms == "R":
        print(lista)
    else:
        print("Fim do programa.")