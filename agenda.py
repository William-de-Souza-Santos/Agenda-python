from time import sleep
def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
    #while True:
        opcao = input('''
        ==========================================
                    AGENDA PESSOAL
        MENU:
        
        [1]CADASTRAR
        [2]LISTAR CONTATO
        [3]DELETAR CONTATO
        [4]BUSCAR CONTATO PELO NOME
        [5]SAIR 
        ==========================================
        ESCOLHA UMA OPÇÃO ACIMA:
        ''')
        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            listarContato()
        elif opcao == '3':
            deletarContato()
        elif opcao == '4':
            buscarContato()
        else:
            sair()
        sleep(2)
        voltarMenuPrincipal = input('Deseja voltar ao menu? [s/n]: ').lower()



def cadastrarContato():
    idContato = int(input('Escolha o Id do seu contato: '))
    nome = str(input('Digite o nome do seu contato: '))
    telefone = int(input('Telefone: '))
    email = str(input('Email: '))
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!!')
    except:
        print('ERRO na gravação do contato!')

def listarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()


def deletarContato():
    nomeDeletado = input('Digite o nome a ser deletado: ').lower()
    agenda = open('agenda.txt', 'r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!!!')
    listarContato()

    agenda.close()


def buscarContato():
    nome = input(f'Digite o nome procurado na lista: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)

    agenda.close()


def sair():
    print('Volte sempre...')
    exit()

def main():
    menu()

main()
