agenda={}
nomes=[]
def ad_contato():
    global agenda, nomes
    nome=input('Digite o nome: ')
    while nome in agenda:
        nome=input('Nome inválido\nDigite o nome: ')
    nomes.append(nome)
    agenda[nome]=[]
    tel1=input('Digite o 1º telefone: ')
    tel2=input('Digite o 2º telefone: ')
    agenda[nome].append(tel1)
    agenda[nome].append(tel2)
def rem_contato(nome):
    global agenda
    while nome not in agenda:
        nome=input('Contato não encontrado\nDigite o nome: ')
    agenda.pop(nome)
def pesquisa():
    global agenda
    while True:
        nome=input('Procure seu o contato: ')
        if agenda == {}:
            print('Agenda vazia')
            break
        elif nome not in agenda:
            print('Contato não encontrado')
        else:
            print(f'Nome: {nome}\nTelefones: {agenda[nome][0]},{agenda[nome][1]}')
            break
def carrega_contatos():
    global agenda, nomes
    if agenda == {}:
        pass
    else:
        with open('agenda2.txt','r') as arqagenda:
             for linha in arqagenda:
                  linha=arqagenda.readline().strip().split(',')
                  nomes.append(linha[0])
                  agenda[str(linha[0])]=[str(linha[1]),str(linha[2])]
                
def imprime_contatos():
    for nome in agenda:
        print(f'Nome: {nome}\nTelefones: {agenda[nome][0]},{agenda[nome][1]}')
                              
            
                              
while True:
    while True:
        try:
                    menu = int(input('\n[0] Cadastrar contato\n[1] Pesquisar contato \n[2] Exlcuir contato\n[3] Salvar\n[4] Carregar contatos\n[5] Todos os contatos\n[6] Sair\n'))
                    while menu != 0 and menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6: 
                        menu = int(input('\n[0] Cadastrar contato\n[1] Pesquisar contato \n[2] Exlcuir contato\n[3] Salvar\n[4] Carregar contatos\n[5] Sair\n'))
                    break
        except:
                    print('INVÁLIDO')
    if menu == 0:
            escolha = ad_contato()
    elif menu == 1:
            escolha = pesquisa()
    elif menu == 2:
            escolha = rem_contato(input('Qual contato deseja remover? '))
    elif menu == 3:
            for i in range(len(nomes)):
                with open('agenda2.txt','a') as arqagenda:
                    arqagenda.write('\n')
                    arqagenda.write(f'{nomes[i]},{agenda[nomes[i]][0]},{agenda[nomes[i]][1]}')
                    arqagenda.write('\n')
    elif menu==4:
             carrega_contatos()
    elif menu == 5:
             imprime_contatos()
    elif menu==6:
        break
        